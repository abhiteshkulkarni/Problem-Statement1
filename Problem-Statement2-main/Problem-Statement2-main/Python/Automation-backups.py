import os
import shutil
import datetime as dt

src = "/home/ubuntu/data"
dst = "/home/ubuntu/backup"

timestamp = dt.dt.now().strftime("%Y%m%d_%H%M%S")
backup_path = os.path.join(dst, f"backup_{timestamp}")

try:
    shutil.copytree(src,backup_path)
    print(f"Backup successful ! files copied to {backup_path}")
except Exception as e:
    print(f"Backup Failed: {e}")
    
