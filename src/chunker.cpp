#include <iostream>
#include <fstream>
#include <vector>
#include <filesystem>

#include "chunker.h"

namespace fs = std::filesystem;
using namespace std;

void chunkFile()
{
    string filePath;

    cout << "Enter full file path: ";
    getline(cin >> ws, filePath);  // supports spaces in path

    // Check if file exists
    if (!fs::exists(filePath))
    {
        cout << "Error: File not found\n";
        return;
    }

    int chunkSize;
    cout << "Enter chunk size (bytes): ";
    cin >> chunkSize;

    if (chunkSize <= 0)
    {
        cout << "Invalid chunk size\n";
        return;
    }

    // Extract file name (example: data.txt)
    string fileName = fs::path(filePath).filename().string();

    // Remove extension → base name (data.txt → data)
    string baseName = fileName.substr(0, fileName.find_last_of('.'));

    // Define fixed directories
    fs::path baseDir = "data";
    fs::path chunksDir = baseDir / "chunks";

    // Create directories if not exist
    fs::create_directories(chunksDir);

    // Create folder for this file's chunks
    fs::path fileChunkDir = chunksDir / baseName;
    fs::create_directories(fileChunkDir);

    // Open original file
    ifstream file(filePath, ios::binary);

    // Create metadata file
    fs::path metaPath = fileChunkDir / (baseName + ".meta");
    ofstream metaFile(metaPath);

    metaFile << "original_file " << fileName << endl;
    metaFile << "chunk_size " << chunkSize << endl;

    int chunkNumber = 1;

    // Buffer to store chunk data temporarily
    vector<char> buffer(chunkSize);

    // Read file chunk by chunk
    while (file.read(buffer.data(), chunkSize) || file.gcount() > 0)
    {
        // Create chunk file name
        string chunkName = baseName + "_" + to_string(chunkNumber) + ".chunk";

        // Full path for chunk file
        fs::path chunkPath = fileChunkDir / chunkName;

        // Write chunk to file
        ofstream chunkFile(chunkPath, ios::binary);
        chunkFile.write(buffer.data(), file.gcount());
        chunkFile.close();

        // Store chunk name in metadata
        metaFile << chunkName << endl;

        chunkNumber++;
    }

    file.close();
    metaFile.close();

    cout << "File chunked successfully\n";
}