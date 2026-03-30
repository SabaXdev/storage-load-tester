OLTP_WORKLOAD = {
    "name": "oltp",

    # Random read/write pattern typical for databases
    "rw": "randrw",
    "rwmixread": 70,   # 70% reads, 30% writes

    # small database pages
    "bs": "4k",

    # concurrency parameters
    "iodepth": 32,
    "numjobs": 4,

    "size": "256M",

    "direct": 1,

    "runtime": 30,
    "time_based": 1,

    # when group_reporting=1, fio aggregates results across all jobs into the first job entry
    "group_reporting": 1
}

STREAM_WORKLOAD = {
    "name": "stream",

    # sequential reading like backup or video streaming
    "rw": "read",

    # large blocks for throughput
    "bs": "1M",

    "iodepth": 32,
    "numjobs": 1,

    "size": "2G",

    "direct": 1,

    "runtime": 30,
    "time_based": 1,

    "group_reporting": 1
}
