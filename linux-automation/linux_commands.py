
import subprocess

print("================================")
print("    LINUX AUTOMATION TOOLKIT")
print("================================")

# 1. Check server uptime
print("\n1. SERVER UPTIME")

subprocess.run(["uptime"])

# 2. Check memory usage
print("\n2. MEMORY USAGE")

subprocess.run(["free", "-h"])

# 3. Check disk space
print("\n3. DISK USAGE")

subprocess.run(["df", "-h"])

# 4. Check logged-in user
print("\n4. CURRENT USER")

subprocess.run(["whoami"])

# 5. Check hostname
print("\n5. SERVER HOSTNAME")

subprocess.run(["hostname"])

# 6. Check running processes
print("\n6. RUNNING PROCESSES")

subprocess.run(["ps", "aux"])

print("\n================================")
print("AUTOMATION COMPLETED")
print("================================")
