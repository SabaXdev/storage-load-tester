import subprocess
import json

def run_fio(workload):

    cmd = ["fio"]

    for key, value in workload.items():
        cmd.append(f"--{key}={value}")

    cmd.append("--ioengine=libaio")
    cmd.append("--output-format=json")

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"fio command failed: {result.stderr}")

    return json.loads(result.stdout)
