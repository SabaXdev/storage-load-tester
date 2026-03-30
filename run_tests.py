import threading
import os
import json
from src.runner import run_fio
from src.parser import parse_metrics
from src.report import print_report
from src.workloads import OLTP_WORKLOAD, STREAM_WORKLOAD


def save_results(results, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        json.dump(results, f, indent=4)


def run_workload(workload):
    print(f"Starting workload: {workload['name']}")

    data = run_fio(workload)

    save_results(data, f"results/{workload['name']}.json")

    metrics = parse_metrics(data)

    print_report(workload["name"], metrics)


if __name__ == "__main__":    
    t1 = threading.Thread(target=run_workload, args=(OLTP_WORKLOAD,))
    t2 = threading.Thread(target=run_workload, args=(STREAM_WORKLOAD,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
