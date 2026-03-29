import subprocess
import json

def run_fio(workload):

    cmd = [
        "fio",
        f"--name={workload['name']}",
        f"--rw={workload['rw']}",
        f"--bs={workload['bs']}",
        f"--iodepth={workload['iodepth']}",
        f"--numjobs={workload['numjobs']}",
        f"--size={workload['size']}",
        f"--direct={workload['direct']}",
        "--ioengine=libaio",
        "--output-format=json"
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"fio command failed: {result.stderr}")

    return json.loads(result.stdout)