# Storage Load Testing Research

## 1. fio Tool Overview
**fio (Flexible I/O Tester)** is a widely used tool to generate synthetic storage workloads. It allows fine-grained control over:

- Read/write patterns (`rw`)
- Block size (`bs`)
- Concurrency (`numjobs`, `iodepth`)
- Cache bypass (`direct`)
- Runtime and data size
- Output formats (JSON, stdout)

fio helps simulate real-world workloads like OLTP databases or media streaming.

---

## 2. Workload Simulation

### OLTP Database Workload
- Characteristics: Many small random reads/writes, high IOPS, low latency requirement
- Recommended fio parameters:

| Parameter       | Value                 | Reason |
|-----------------|---------------------|--------|
| rw              | randrw              | Simulates random reads/writes typical for OLTP |
| bs              | 4k                  | Small blocks as in database transactions |
| iodepth         | 32                  | Multiple in-flight I/Os for concurrency |
| numjobs         | 4–8                 | Multiple worker threads to simulate multiple clients |
| direct          | 1                   | Bypass OS cache for realistic device-level performance |
| runtime         | 30–300 sec          | Test duration |
| time_based      | 1                   | Run based on time, not total data size |

---

### Streaming Video Service
- Characteristics: Sequential large reads, high throughput
- Recommended fio parameters:

| Parameter       | Value                 | Reason |
|-----------------|---------------------|--------|
| rw              | read                | Sequential reads to simulate video streaming |
| bs              | 1M                  | Large block sizes for throughput |
| iodepth         | 32                  | Higher queue depth for continuous streaming |
| numjobs         | 1                   | Single process sufficient for single stream simulation |
| direct          | 1                   | Avoid OS caching to measure actual disk/network throughput |
| runtime         | 30–120 sec          | Sufficient for throughput measurement |
| time_based      | 1                   | Time-based test rather than data-size-based |

---

## 3. fio Parameter Explanation

- **iodepth**: Number of I/O requests in flight per thread.  
  Higher iodepth → more parallelism, can increase device utilization, may increase tail latency.

- **numjobs**: Number of parallel threads or processes generating I/O.  
  Higher numjobs → simulates more concurrent clients or workload threads.

- **direct=1**: Skip Linux's page cache and go straight to the raw device. Without it, you're testing RAM speed, not disk speed
  Ensures results measure **device performance**, not just OS caching.

---

## 4. iperf3 Overview (Network Testing)
**iperf3** is a tool to measure network throughput and performance between two hosts.

- Metrics to include in reports:
  - **Throughput (Mbps/Gbps)**: Network data transfer rate
  - **Retransmissions**: Indicates packet loss or network congestion
  - **Jitter**: Variation in packet timing
  - **TCP RTT / Window Size**: Affects max achievable throughput

- Purpose: Detect if **network is the primary bottleneck** when testing remote storage.

---

## References
- [fio official documentation](https://fio.readthedocs.io/)
- [iperf3 official documentation](https://iperf.fr/)