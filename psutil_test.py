import psutil
from pathlib import Path
import datetime

def date(format="%Y%m%d"):
    return datetime.datetime.utcnow().strftime(format)

def make_output_dir() -> Path:
    today = date("%Y%m%d")
    output_dir = Path(".") / f"results_{today}"
    output_dir.mkdir(exist_ok=True)
    return output_dir

if __name__ == "__main__":
    make_output_dir()
