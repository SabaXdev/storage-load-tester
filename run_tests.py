from src.runner import run_fio
from src.parser import parse_metrics
from src.report import print_report
from src.workloads import OLTP_WORKLOAD

data = run_fio(OLTP_WORKLOAD)

metrics = parse_metrics(data)

print_report("OLTP", metrics)