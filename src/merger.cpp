#include <iostream>
#include <fstream>
#include <vector>
#include <filesystem>

#include "merger.h"

namespace fs = std::filesystem;
using namespace std;

void mergeFile(){
    string baseName;
    cout << "Enter base file name to merge: ";
    cin >> baseName;

    string metaPath = "chunks_folder/" + baseName + "/" + baseName + ".meta";
    cout << "Looking for metadata at: " << metaPath << endl;
    ifstream metaFile(metaPath);

    if (!metaFile)
    {
        cout << "Metadata file not found\n";
        return;
    }

    string label;
    string originalFile;
    int chunkSize;

    // Read metadata header
    metaFile >> label >> originalFile;
    metaFile >> label >> chunkSize;

    // Create folder for merged output
    fs::create_directories("merged_folder");

    string outputPath = "merged_folder/" + originalFile;

    ofstream outputFile(outputPath, ios::binary);
 
    string chunkName;

    while(metaFile >> chunkName){
        string chunkPath = "chunks_folder/" + baseName + "/" + chunkName;

        if(!fs::exists(chunkPath))
        {
            cout << "Error: Missing chunk " << chunkName << endl;
            cout << "Merge aborted\n";
            return;
        }

        ifstream chunkFile(chunkPath, ios::binary);

        vector<char> buffer(chunkSize);

        while(chunkFile.read(buffer.data(), chunkSize) || chunkFile.gcount() > 0)
        {
            outputFile.write(buffer.data(), chunkFile.gcount());
        }

        chunkFile.close();
    }

    cout << "File merged successfully";
}