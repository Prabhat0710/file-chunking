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
    getline(cin >> ws, filePath);

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

    // Extract file name
    string fileName = fs::path(filePath).filename().string();

    // Remove extension → base name
    string baseName = fileName.substr(0, fileName.find_last_of('.'));

    // Define directories
    fs::path baseDir = "data";
    fs::path chunksDir = baseDir / "chunks";

    fs::create_directories(chunksDir);

    fs::path fileChunkDir = chunksDir / baseName;
    fs::create_directories(fileChunkDir);

    ifstream file(filePath, ios::binary);

    // Get file size
    file.seekg(0, ios::end);
    size_t fileSize = file.tellg();
    file.seekg(0);

    // Metadata file
    fs::path metaPath = fileChunkDir / (baseName + ".meta");
    ofstream metaFile(metaPath);

    // Write metadata header
    metaFile << "file_name=" << fileName << endl;
    metaFile << "file_size=" << fileSize << endl;
    metaFile << "chunk_size=" << chunkSize << endl;

    vector<string> chunkNames;

    int chunkNumber = 1;
    vector<char> buffer(chunkSize);

    while (file.read(buffer.data(), chunkSize) || file.gcount() > 0)
    {
        string chunkName = baseName + "_" + to_string(chunkNumber) + ".chunk";

        fs::path chunkPath = fileChunkDir / chunkName;

        ofstream chunkFile(chunkPath, ios::binary);
        chunkFile.write(buffer.data(), file.gcount());
        chunkFile.close();

        chunkNames.push_back(chunkName);
        chunkNumber++;
    }

    int totalChunks = chunkNames.size();

    // Write remaining metadata
    metaFile << "total_chunks=" << totalChunks << endl;
    metaFile << "chunks:" << endl;

    for (const auto& name : chunkNames)
    {
        metaFile << name << endl;
    }

    file.close();
    metaFile.close();

    cout << "File chunked successfully\n";
}