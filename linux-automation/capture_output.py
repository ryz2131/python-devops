
import subprocess

result = subprocess.run(
    ["df", "-h"],
    capture_output=True,
    text=True
)

print("DISK INFORMATION")
print(result.stdout)

print("RETURN CODE:", result.returncode)

if result.returncode == 0:
    print("Command executed successfully")
else:
    print("Command failed")
    print(result.stderr)
