# 🧹 File Organizer CLI

A powerful, lightweight Python utility designed to clean up your messy directories in seconds. It automatically categorizes files into meaningful folders based on their extensions.

## ✨ Key Features

- **Smart Categorization**: Groups files into Images, Videos, Documents, Audio, Archives, Programming, and Data.
- **Safety First (Dry Run)**: Use the `--dry-run` flag to see what happens before making any changes.
- **Duplicate Protection**: Automatically renames files (e.g., `image_1.png`) if a file with the same name already exists in the destination.
- **"Others" Fallback**: Any unrecognized file types are safely moved to an `Others` folder instead of being left in the root.
- **Beginner Friendly**: Simple codebase, easy to extend with your own file types.

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed.

### Installation
1. Clone the repository:

   git clone https://github.com/matt-67/file-organizer-cli.git
   cd file-organizer-cli

2. No external dependencies required! Just standard Python libraries.

## 🛠 Usage

To organize a folder (e.g., your Downloads):

python organizer.py ~/Downloads

### Preview Changes
Always a good idea before running on important folders:

python organizer.py ~/Downloads --dry-run

## 📂 Supported Categories

| Category | Extensions |
| :--- | :--- |
| **Images** | .jpg, .png, .gif, .webp, .svg, .bmp, .tiff |
| **Videos** | .mp4, .mov, .avi, .mkv, .wmv |
| **Documents** | .pdf, .docx, .txt, .pptx, .xlsx, .rtf |
| **Audio** | .mp3, .wav, .aac, .flac, .m4a |
| **Archives** | .zip, .rar, .tar, .gz, .7z |
| **Programming**| .py, .js, .html, .css, .cpp, .java, .sh |
| **Data** | .json, .csv, .xml, .sql, .yaml |

## 🤝 Contributing

Contributions are welcome! 
1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---
Created by **Eyuel Engida** via **EyuX-Lite**.
