import psutil

# CPU Usage
cpu = psutil.cpu_percent(interval=1)

# RAM Usage
ram = psutil.virtual_memory().percent

# Disk Usage
disk = psutil.disk_usage('/').percent

print("===== SERVER MONITORING =====")

print("CPU Usage:", cpu, "%")
print("RAM Usage:", ram, "%")
print("Disk Usage:", disk, "%")

if cpu > 80:
    print("WARNING: High CPU Usage!")

if ram > 80:
    print("WARNING: High RAM Usage!")

if disk > 80:
    print("WARNING: High Disk Usage!")

print("=============================")
