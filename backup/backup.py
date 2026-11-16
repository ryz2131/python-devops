import os
import shutil
from datetime import datetime

# Define source directory
source_dir = os.path.expanduser("~/python-devops/backup/source")

# Define backup location
backup_dir = os.path.expanduser("~/python-devops/backup/backups")

# Generate timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Create unique backup folder
backup_path = os.path.join(
    backup_dir,
    f"backup_{timestamp}"
)

print("================================")
print("      AUTOMATED BACKUP SYSTEM")
print("================================")

# Check source directory
if not os.path.exists(source_dir):

    print("ERROR: Source directory does not exist!")

else:

    # Create backup directory if missing
    os.makedirs(backup_dir, exist_ok=True)

    # Copy source directory
    try:

        shutil.copytree(source_dir, backup_path)

        print("Backup completed successfully!")

        print("Source:", source_dir)

        print("Backup:", backup_path)

        print("Time:", datetime.now())

    except Exception as e:

        print("Backup failed:", e)

print("================================")
