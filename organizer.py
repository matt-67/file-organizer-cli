import os
import shutil
import argparse

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp", ".tiff"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx", ".rtf"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".m4a"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Programming": [".py", ".js", ".html", ".css", ".cpp", ".java", ".sh"],
    "Data": [".json", ".csv", ".xml", ".sql", ".yaml", ".yml"],
}


def _get_category_for_extension(ext):
    for folder, extensions in FILE_TYPES.items():
        if ext.lower() in extensions:
            return folder
    return "Others"


def _unique_destination_path(target_folder, filename):
    base, ext = os.path.splitext(filename)
    candidate = os.path.join(target_folder, filename)
    if not os.path.exists(candidate):
        return candidate

    counter = 1
    while True:
        new_name = f"{base}_{counter}{ext}"
        candidate = os.path.join(target_folder, new_name)
        if not os.path.exists(candidate):
            return candidate
        counter += 1


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

        folder = _get_category_for_extension(ext)
        target_folder = os.path.join(folder_path, folder)

        if dry_run:
            target_path = _unique_destination_path(target_folder, file)
            planned_name = os.path.basename(target_path)
            if planned_name != file:
                print(f"[DRY RUN] Would move: {file} → {folder}/{planned_name} (renamed)")
            else:
                print(f"[DRY RUN] Would move: {file} → {folder}/")
        else:
            os.makedirs(target_folder, exist_ok=True)
            target_path = _unique_destination_path(target_folder, file)
            final_name = os.path.basename(target_path)
            shutil.move(file_path, target_path)
            if final_name != file:
                print(f"Moved: {file} → {folder}/{final_name} (renamed)")
            else:
                print(f"Moved: {file} → {folder}/")

        moved_files += 1

    print(f"\nFinished. Processed {moved_files} files.")


def main():
    parser = argparse.ArgumentParser(description="Organize files in a folder by type.")
    parser.add_argument("path", help="Path to the folder")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without moving files")

    args = parser.parse_args()
    organize(args.path, args.dry_run)


if __name__ == "__main__":
    main()
