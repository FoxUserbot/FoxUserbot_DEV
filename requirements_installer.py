import subprocess
import sys

def install_library(name):
    requirements = ["install"]
    for i in name.split():
        requirements.append(i)
    
    print(requirements)
    subprocess.run([sys.executable, "-m", "uv", "pip"] + requirements + ["--system"], check=True)
