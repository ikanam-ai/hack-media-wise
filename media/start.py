import subprocess
import os


def main() -> None:
    cmd = ["poetry", "run", "streamlit", "run", "media_wise/main.py", "--server.port", 
           os.environ.get("STREAMLIT_PORT", "7464")]
    subprocess.run(cmd)
