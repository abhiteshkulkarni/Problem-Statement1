import psutil
import datetime as dt

CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 80

def log_message(msg):
    with open("system_health_log", "a") as f:
        f.write(f"{dt.dt.now()} - {msg}\n")
    print(msg)

cpu = psutil.cpu_percent()
memory = psutil.VM().percent
disk = psutil.disk_usage("/").percent

if cpu > CPU_THRESHOLD:
    log_message("High CPU Usage: {cpu}%")
if memory > MEM_THRESHOLD:
    print("High Memory Usage:{memory}%")
if disk > DISK_THRESHOLD:
    print("High Disk Usage: {disk}%")
log_message(f"System Health Check Completed - CPU: {cpu}%, MEM: {memory}%, DISK: {disk}%")



