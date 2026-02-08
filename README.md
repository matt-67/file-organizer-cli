# 🧹 File Organizer CLI

A powerful, lightweight Python utility designed to clean up your messy directories in seconds. It automatically categorizes files into meaningful folders based on their extensions.

## ✨ Key Features

- **Smart Categorization**: Groups files into Images, Videos, Documents, Audio, Archives, Programming, and Data.
- **Safety First (Dry Run)**: Use the `--dry-run` flag to see what happens before making any changes.
- **Duplicate Protection**: Automatically renames files (e.g., `image_1.png`) if a file with the same name already exists in the destination.
- **"Others" Fallback**: Any unrecognized file types are safely moved to an `Others` folder instead of being left in the root.
- **Zero Dependencies**: Built entirely using Python's standard library.

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Installation
1. Clone the repository:

   git clone https://github.com/matt-67/file-organizer-cli.git
   cd file-organizer-cli

2. Run the script directly! No `pip install` required.

## 🛠 Usage

To organize a specific folder (e.g., your Downloads):

python organizer.py ~/Downloads

### Preview Changes
It is highly recommended to run a preview before moving files:

python organizer.py ~/Downloads --dry-run

## 📂 Supported Categories

| Category | Extensions |
| :--- | :--- |
| **Images** | .jpg, .jpeg, .png, .gif, .webp, .svg, .bmp, .tiff |
| **Videos** | .mp4, .mov, .avi, .mkv, .wmv |
| **Documents** | .pdf, .docx, .txt, .pptx, .xlsx, .rtf |
| **Audio** | .mp3, .wav, .aac, .flac, .m4a |
| **Archives** | .zip, .rar, .tar, .gz, .7z |
| **Programming**| .py, .js, .html, .css, .cpp, .java, .sh |
| **Data** | .json, .csv, .xml, .sql, .yaml |
| **Others** | Any extension not listed above |

## 🤝 Contributing

Contributions are welcome! 
1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---
Created by matt