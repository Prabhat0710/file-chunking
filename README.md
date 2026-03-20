# File Chunking System (C++)

A modular C++ project that splits large files into smaller chunks and reconstructs them reliably.

---

## 🚀 Features
- Fixed-size file chunking
- File reconstruction from chunks
- Metadata-based validation
- Automatic folder management
- Cross-platform file handling using C++17 filesystem
- Modular architecture (`src/` and `include/`)

---

## 📁 Project Structure
file-chunking/
│
├── src/
│ ├── main.cpp # Menu-driven interface
│ ├── chunker.cpp # Chunking logic
│ └── merger.cpp # Reconstruction logic
│
├── include/
│ ├── chunker.h
│ └── merger.h
│
├── files/ # Input files
├── chunks_folder/ # Generated chunks
├── merged_folder/ # Reconstructed files
│
├── README.md
├── pseudocode.md
├── explanation.md
└── .gitignore


---

## ⚙️ How It Works

### 1. Chunking
- User provides full file path
- File is split into fixed-size chunks
- Chunks are stored in:
- A metadata file is created to track chunk order

---

### 2. Merging
- Program reads metadata file
- Validates all chunks exist
- Reconstructs original file in:

---

## 🛠️ Compilation
```bash
g++ -std=c++17 -Iinclude src/main.cpp src/chunker.cpp src/merger.cpp -o chunker

---

▶️ Run
./chunker

---

🧪 Example Usage
1. Chunk File
Enter full file path: D:\data\file.txt
Enter chunk size: 1024

2. Merge File
Enter base file name: file

---

🧠 Learning Goals
This project explores:
File I/O in C++
Binary data handling
Filesystem operations
Modular software design
Real-world system structuring


📌 Author
Prabhat