OLTP_WORKLOAD = {
    "name": "oltp",
    "rw": "randrw",     #tells fio what kind of operations to perform.
    "bs": "4k",         # size of each operation
    "iodepth": 32,  #How many IO operations can be in a flight at the same time per job
    "numjobs": 4,
    "size": "256M",
    "direct": 1     #when you want real disk performance. bypass RAM speed
}

STREAM_WORKLOAD = {
    "name": "stream",
    "rw": "read",
    "bs": "1M",
    "iodepth": 16,
    "numjobs": 4,
    "size": "2G",
    "direct": 1
}

# Total concurency = numjobs x iodepth