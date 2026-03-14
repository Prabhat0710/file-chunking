#include <iostream>
#include <fstream>
#include <vector>
#include <filesystem>

namespace fs = std::filesystem;
using namespace std;

void chunkFile()
{
    string fileName;
    cout << "Enter file name (inside files folder): ";
    cin >> fileName;

    int chunkSize;
    cout << "Enter chunk size (bytes): ";
    cin >> chunkSize;

    // build full input path automatically
    string inputPath = "../files/" + fileName;

    ifstream file(inputPath, ios::binary);

    if (!file)
    {
        cout << "Error: file not found in files folder\n";
        return;
    }

    // remove extension
    string baseName = fileName;
    size_t dot = baseName.find_last_of('.');

    if (dot != string::npos)
        baseName = baseName.substr(0, dot);

    // create chunk directory
    string chunkDir = "../chunks_folder/" + baseName;
    fs::create_directories(chunkDir);

    // create metadata file
    string metaPath = chunkDir + "/" + baseName + ".meta";
    ofstream metaFile(metaPath);

    metaFile << "original_file " << fileName << endl;
    metaFile << "chunk_size " << chunkSize << endl;

    int chunkNumber = 1;

    vector<char> buffer(chunkSize);

    while (file.read(buffer.data(), chunkSize) || file.gcount() > 0)
    {
        string chunkName = baseName + "_" + to_string(chunkNumber) + ".chunk";

        string chunkPath = chunkDir + "/" + chunkName;

        ofstream chunkFile(chunkPath, ios::binary);

        chunkFile.write(buffer.data(), file.gcount());

        chunkFile.close();

        // record chunk in metadata
        metaFile << chunkName << endl;

        chunkNumber++;
    }

    file.close();
    metaFile.close();

    cout << "File chunked successfully\n";
}

int main(){

    chunkFile();
    return 0;
}