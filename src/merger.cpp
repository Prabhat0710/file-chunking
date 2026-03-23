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

    // Define directories
    fs::path baseDir = "data";
    fs::path chunksDir = baseDir / "chunks";
    fs::path mergedDir = baseDir / "merged";

    // Create merged folder if not exists
    fs::create_directories(mergedDir);

    // Path to chunk folder of this file
    fs::path fileChunkDir = chunksDir / baseName;

    // Metadata file path
    fs::path metaPath = fileChunkDir / (baseName + ".meta");

    if (!fs::exists(metaPath))
    {
        cout << "Error: Metadata file not found\n";
        return;
    }

    ifstream metaFile(metaPath);

    string label, originalFile;
    int chunkSize;

    // Read metadata header
    metaFile >> label >> originalFile;
    metaFile >> label >> chunkSize;

    // Output file path
    fs::path outputPath = mergedDir / (baseName + "_merged.txt");

    ofstream outputFile(outputPath, ios::binary);

    string chunkName;

    // Read chunk names from metadata
    while (metaFile >> chunkName)
    {
        fs::path chunkPath = fileChunkDir / chunkName;

        // Check if chunk exists
        if (!fs::exists(chunkPath))
        {
            cout << "Error: Missing chunk " << chunkName << endl;
            cout << "Merge aborted\n";
            return;
        }

        ifstream chunkFile(chunkPath, ios::binary);

        vector<char> buffer(chunkSize);

        // Read chunk and write to output
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