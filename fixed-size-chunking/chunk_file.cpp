#include <iostream>
#include <fstream>
#include <vector>
#include <filesytem>

namespace fs = std::filesystem
using namespace std;

void chunkFile(){
    string inputFile;
    cout << "Enter file name : ";
    cin >> inputFile;

    int chunkSize;
    cout << "Enter chunkSize (bytes) : ";
    cin >> chunkSize;

    ifstream file(inputFile, ios::binary);

    if(!file){
        cout << "Error opening file\n";
        return;
    }

    string baseName = inputFile;

    size_t dot = baseName.find_last_of('.');
    if(dot != string::npos){
        baseName = baseName.substr(0, dot);
    }

    fs::create_directories("chunk_folder/"+ baseName);

    string metaPath = "chunks_folder/" + baseName + "/" + baseNamee + ".neta";
    ofstream metafile(metaPath);

    metaFile << "original_file " << inputFile << endl;
    metaFile << "chunk_size " << chunkSize << endl;

    int chunkNumber = 1;
    vector<char> buffer(chunkSize);

    while(file.read(buffer.data(), chunkSize) || file.gcount() > 0){
        string chunkName = baseName + "_" + to_string(chunkNumber) + ".chunk";
        string chunkPath = "chunks_folder/" + baseName + "/" + chunkNumber;

        of stream chunkFile(chunkPath , ios::binary);
        chunkFile.write(buffer.data(), file.gcount());
        chunkFile.close();

        metaFile << chunkName << endl;

        chunkNumber++
    }

    file.close();
    metaFile.close();

    cout << "File chunked successfully\n";
}

int main(){
    chunkFile();
    return 0;
}
