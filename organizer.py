import os
import shutil
import argparse

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"]
}


def organize(folder_path, dry_run=False):
    if not os.path.isdir(folder_path):
        print("❌ Invalid folder path")
        return

    moved_files = 0

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(file)

        for folder, extensions in FILE_TYPES.items():
            if ext.lower() in extensions:
                target_folder = os.path.join(folder_path, folder)
                target_path = os.path.join(target_folder, file)

                if dry_run:
                    print(f"[DRY RUN] Would move: {file} → {folder}/")
                else:
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, target_path)
                    print(f"Moved: {file} → {folder}/")

                moved_files += 1
                break

    print(f"\nFinished. Processed {moved_files} files.")


def main():
    parser = argparse.ArgumentParser(description="Organize files in a folder by type.")
    parser.add_argument("path", help="Path to the folder")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without moving files")

    args = parser.parse_args()
    organize(args.path, args.dry_run)


if __name__ == "__main__":
    main()
