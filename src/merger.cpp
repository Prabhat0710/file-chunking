#include <iostream>
#include <fstream>
#include <vector>
#include <filesystem>

#include "merger.h"

namespace fs = std::filesystem;
using namespace std;

void mergeFile()
{
    string baseName;

    cout << "Enter base file name (without extension): ";
    cin >> baseName;

    fs::path baseDir = "data";
    fs::path chunksDir = baseDir / "chunks";
    fs::path mergedDir = baseDir / "merged";

    fs::create_directories(mergedDir);

    fs::path fileChunkDir = chunksDir / baseName;
    fs::path metaPath = fileChunkDir / (baseName + ".meta");

    if (!fs::exists(metaPath))
    {
        cout << "Error: Metadata file not found\n";
        return;
    }

    ifstream metaFile(metaPath);

    string line;
    string fileName;
    int chunkSize = 0;
    int totalChunks = 0;

    // Read metadata header
    getline(metaFile, line); // file_name=...
    fileName = line.substr(line.find("=") + 1);

    getline(metaFile, line); // file_size=...

    getline(metaFile, line); // chunk_size=...
    chunkSize = stoi(line.substr(line.find("=") + 1));

    getline(metaFile, line); // total_chunks=...
    totalChunks = stoi(line.substr(line.find("=") + 1));

    getline(metaFile, line); // "chunks:"

    vector<string> chunkNames;
    string chunkName;

    while (getline(metaFile, chunkName))
    {
        if (!chunkName.empty())
            chunkNames.push_back(chunkName);
    }

    // ✅ Validate chunk count
    if (chunkNames.size() != totalChunks)
    {
        cout << "Error: Metadata mismatch (missing chunks)\n";
        return;
    }

    fs::path outputPath = mergedDir / (baseName + "_merged.txt");
    ofstream outputFile(outputPath, ios::binary);

    for (const auto& name : chunkNames)
    {
        fs::path chunkPath = fileChunkDir / name;

        if (!fs::exists(chunkPath))
        {
            cout << "Error: Missing chunk " << name << endl;
            cout << "Merge aborted\n";
            return;
        }

        ifstream chunkFile(chunkPath, ios::binary);
        vector<char> buffer(chunkSize);

        while (chunkFile.read(buffer.data(), chunkSize) || chunkFile.gcount() > 0)
        {
            outputFile.write(buffer.data(), chunkFile.gcount());
        }

        chunkFile.close();
    }

    outputFile.close();
    metaFile.close();

    cout << "File merged successfully\n";
}