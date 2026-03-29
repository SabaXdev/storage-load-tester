def print_report(name, metrics):

    print("\n====== TEST REPORT ======")
    print(f"Workload: {name}")

    print(f"Throughput: {metrics['throughput_mib']:.2f} MiB/s")
    print(f"IOPS: {metrics['iops']:.2f}")

    print("Latency:")
    print(f"P95: {metrics['p95_latency_ms']:.2f} ms")
    print(f"P99: {metrics['p99_latency_ms']:.2f} ms")