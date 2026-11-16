import argparse
import csv
from datetime import datetime, timedelta
from pathlib import Path

import psutil


CPU_THRESHOLD = 85
MEMORY_THRESHOLD = 85
DISK_THRESHOLD = 90


def get_system_health(disk_path):
    """Collect current system health information."""

    cpu_usage = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory()

    disk = psutil.disk_usage(disk_path)

    boot_time = datetime.fromtimestamp(
        psutil.boot_time()
    )

    uptime = datetime.now() - boot_time

    return {
        "timestamp": datetime.now().isoformat(
            timespec="seconds"
        ),
        "cpu_percent": cpu_usage,
        "memory_percent": memory.percent,
        "disk_percent": disk.percent,
        "uptime": str(
            timedelta(seconds=int(uptime.total_seconds()))
        ),
    }


def check_alerts(health):
    """Identify resources exceeding their thresholds."""

    alerts = []

    if health["cpu_percent"] >= CPU_THRESHOLD:
        alerts.append(
            f"High CPU usage: {health['cpu_percent']}%"
        )

    if health["memory_percent"] >= MEMORY_THRESHOLD:
        alerts.append(
            f"High memory usage: {health['memory_percent']}%"
        )

    if health["disk_percent"] >= DISK_THRESHOLD:
        alerts.append(
            f"High disk usage: {health['disk_percent']}%"
        )

    return alerts


def save_csv(health, filename):
    """Append system health information to a CSV file."""

    path = Path(filename).expanduser()

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    file_exists = path.exists() and path.stat().st_size > 0

    with path.open(
        "a",
        newline="",
        encoding="utf-8",
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=list(health.keys()),
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow(health)


def display_report(health, alerts):
    """Display a readable terminal report."""

    print("\nLINUX SYSTEM HEALTH REPORT")
    print("=" * 45)

    print(f"Timestamp: {health['timestamp']}")
    print(f"CPU Usage: {health['cpu_percent']}%")
    print(f"Memory Usage: {health['memory_percent']}%")
    print(f"Disk Usage: {health['disk_percent']}%")
    print(f"System Uptime: {health['uptime']}")

    print("\nSYSTEM STATUS")
    print("-" * 45)

    if alerts:
        print("WARNING: Resource thresholds exceeded")

        for alert in alerts:
            print(f"[ALERT] {alert}")

    else:
        print("OK: All monitored resources are below thresholds")


def main():
    parser = argparse.ArgumentParser(
        description="Monitor Linux system health."
    )

    parser.add_argument(
        "--disk",
        default="/",
        help="Filesystem path to monitor (default: /)",
    )

    parser.add_argument(
        "--output",
        default="reports/system_health.csv",
        help="CSV report filename",
    )

    args = parser.parse_args()

    try:
        health = get_system_health(args.disk)

        alerts = check_alerts(health)

        display_report(health, alerts)

        save_csv(health, args.output)

        print(f"\nReport saved to: {args.output}")

    except (OSError, ValueError) as error:
        parser.exit(
            1,
            f"Monitoring failed: {error}\n",
        )


if __name__ == "__main__":
    main()
