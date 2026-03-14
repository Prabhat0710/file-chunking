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

void mergeFile(){
    string baseName;

    cout << "Enter base file name to merge : ";
    cin >> baseName;

    string metaPath = "../chunks_folder/" + baseName + "/" + baseName + ".meta";

    ifstream metaFile(metaPath);

    if(!metaFile){
        cout << "Error: metadata file not found\n";
        return;
    }

    string label;
    string originalFiles;
    int chunkSize;

    metaFile >> label >> originalFiles;
    metaFile >> label >> chunkSize;

    fs::create_directories("../merged_folder");
    string outputPath = "../merged_folder/" + originalFiles;
    ofstream outputFile(outputPath, ios::binary);
    string chunkName;

    while(metaFile >> chunkName){
        string chunkPath = "../chunks_folder/" + baseName + "/" + chunkName;

        ifstream chunkFile(chunkPath, ios::binary);

        if (!chunkFile)
        {
            cout << "Error opening chunk: " << chunkName << endl;
            return;
        }

        vector<char> buffer(chunkSize);

        while (chunkFile.read(buffer.data(), chunkSize) || chunkFile.gcount() > 0)
        {
            outputFile.write(buffer.data(), chunkFile.gcount());
        }

        chunkFile.close();
    }

    outputFile.close();
    metaFile.close();

    cout << "File reconstructed successfully\n";
}

int main(){
    int choice;
    while(true){
        cout << "\n----- File Chunking System -----\n";
        cout << "1. Chunk File\n";
        cout << "2. Merge File\n";
        cout << "3. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        if (choice == 1){
            chunkFile();
        }
        else if (choice == 2){
            mergeFile();
        }
        else if (choice == 3){
            break;
        }
        else{
            cout << "Invalid choice\n";
        }
    }

    return 0;
}