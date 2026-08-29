from pathlib import Path
import subprocess

LEVELS= {"INFO","WARNING","ERROR"}

file_path=r"C:\Users\tanishka\OneDrive\Documents\work\python-for-devops\day2\app.log"

def read_log_file(path):
    return Path(file_path).read_text(encoding="utf-8")


def count_log_levels(text):
    counter={"INFO":0,"WARNING":0,"ERROR":0}
    for line in text.splitlines():
        tokens=line.split()
        for level in LEVELS:
            if level in tokens:
                counter[level]+=1
    return counter

def show_docker_containers():
    return subprocess.run(
        ["docker","ps","-a"],
        capture_output=True,
        text=True)