import shutil
import datetime
import os

# Define correct directories
source_dir = r"C:\Users\Omen\Desktop\GOSHHFArb Crypto"  # Update this to match your actual project folder
backup_dir = r"C:\Users\Omen\Desktop\GOSHHFArb Crypto\CPRecall"  # Ensure CPRecall is used for recall storage

# Generate timestamped backup file
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_path = os.path.join(backup_dir, f"GOSHHFArb_backup_{timestamp}.zip")

# Create compressed archive backup
shutil.make_archive(backup_path.replace('.zip', ''), 'zip', source_dir)
print(f"🚀 Backup created successfully: {backup_path}")