def parse_metrics(data):

    job = data["jobs"][0]

    read = job["read"]
    write = job["write"]

    throughput_mib = (read["bw"] + write["bw"]) / 1024
    iops = read["iops"] + write["iops"]

    p95_latency_ms = read["clat_ns"]["percentile"]["95.000000"] / 1e6
    p99_latency_ms = read["clat_ns"]["percentile"]["99.000000"] / 1e6

    return {
        "throughput_mib": throughput_mib,
        "iops": iops,
        "p95_latency_ms": p95_latency_ms,
        "p99_latency_ms": p99_latency_ms
    }