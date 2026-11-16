
import subprocess

def run_command(command, description):

    print(f"\nChecking {description}...")

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
            timeout=10
        )

        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print("Command failed:", e.stderr)

    except subprocess.TimeoutExpired:
        print("Command timed out!")

    except FileNotFoundError:
        print("Command not found!")

# Server health checks

run_command(["uptime"], "Server Uptime")

run_command(["free", "-h"], "Memory Usage")

run_command(["df", "-h"], "Disk Usage")

run_command(["hostname"], "Hostname")

run_command(["whoami"], "Current User")

print("\nSERVER HEALTH CHECK COMPLETED")
