# File Chunking System (C++)

A modular C++ application that splits large files into smaller chunks and reliably reconstructs them using structured metadata.

---

## 🚀 Features

- Fixed-size file chunking
- Reliable file reconstruction
- Structured metadata system
- Missing chunk detection
- Automatic directory management
- Modular architecture (src/include)

---

## 📁 Project Structure

<img width="692" height="506" alt="image" src="https://github.com/user-attachments/assets/00732d65-e256-4155-8e70-5ea96951b457" />



---

## ⚙️ How It Works

### 1. Chunking

- User provides full file path
- File is split into fixed-size chunks
- Chunks are stored in: data/chunks/<filename>/
- A metadata file is created describing:
- file name
- file size
- chunk size
- total chunks
- chunk list

---

### 2. Merging

- Reads metadata file
- Validates:
- total chunks
- existence of all chunk files
- Reconstructs original file into: data/merged/

---

## 🧠 Metadata Format

- Example:
- file_name=data.txt
- file_size=1024
- chunk_size=100
- total_chunks=11
 
- chunks:
- data_1.chunk
- data_2.chunk
- data_3.chunk

---

## 🛠️ Build Instructions

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

⚠️ Current Limitations
Only fixed-size chunking implemented
No checksum/hash validation yet
Metadata integrity not verified

---

🧠 Learning Goals
This project explores:
File I/O in C++
Binary data handling
Filesystem operations
Modular software design
Real-world system structuring

---

👤 Author
Prabhat
