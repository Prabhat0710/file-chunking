#include <iostream>
#include <fstream>
#include <vector>
#include <filesystem>
#include <limits>

namespace fs = std::filesystem;
using namespace std;

void chunkFile()
{
    string filePath;
    cout << "Enter full file path: ";
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    getline(cin, filePath);

    // Check if file exists
    if (!fs::exists(filePath))
    {
        cout << "Error: File not found\n";
        return;
    }

    int chunkSize;
    cout << "Enter chunk size (bytes): ";
    cin >> chunkSize;

    // Extract file name from path
    string fileName = fs::path(filePath).filename().string();

    // Remove extension to create base name
    string baseName = fileName;
    size_t dot = baseName.find_last_of('.');
    if (dot != string::npos)
        baseName = baseName.substr(0, dot);

    // Create local folders if they do not exist
    fs::create_directories("files");
    fs::create_directories("chunks_folder");

    // Copy original file into files/ directory
    string localCopy = "files/" + fileName;
    fs::copy_file(filePath, localCopy, fs::copy_options::overwrite_existing);

    cout << "Checking file: " << filePath << endl;
    // Open copied file for reading
    ifstream file(localCopy, ios::binary);

    if (!file)
    {
        cout << "Error opening copied file\n";
        return;
    }

    // Create folder for chunks
    string chunkDir = "chunks_folder/" + baseName;
    fs::create_directories(chunkDir);

    // Create metadata file
    string metaPath = chunkDir + "/" + baseName + ".meta";
    ofstream metaFile(metaPath);

    metaFile << "original_file " << fileName << endl;
    metaFile << "chunk_size " << chunkSize << endl;

    int chunkNumber = 1;

    // Buffer used to temporarily hold chunk data
    vector<char> buffer(chunkSize);

    while (file.read(buffer.data(), chunkSize) || file.gcount() > 0)
    {
        string chunkName = baseName + "_" + to_string(chunkNumber) + ".chunk";
        string chunkPath = chunkDir + "/" + chunkName;

        ofstream chunkFile(chunkPath, ios::binary);

        chunkFile.write(buffer.data(), file.gcount());
        chunkFile.close();

        // Record chunk name inside metadata
        metaFile << chunkName << endl;

        chunkNumber++;
    }

    file.close();
    metaFile.close();

    cout << "File chunked successfully\n";
}

void mergeFile()
{
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

    while (metaFile >> chunkName)
    {
        string chunkPath = "chunks_folder/" + baseName + "/" + chunkName;

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

    cout << "File merged successfully\n";
}

int main()
{
    int choice;

    while (true)
    {
        cout << "\n----- File Chunking System -----\n";
        cout << "1. Chunk File\n";
        cout << "2. Merge File\n";
        cout << "3. Exit\n";
        cout << "Enter choice: ";

        cin >> choice;

        if (choice == 1)
        {
            chunkFile();
        }
        else if (choice == 2)
        {
            mergeFile();
        }
        else if (choice == 3)
        {
            cout << "Exiting program\n";
            break;
        }
        else
        {
            cout << "Invalid choice\n";
        }
    }

    return 0;
}