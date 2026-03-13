#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

//make merging as a separate functionality in the program and in the program loop ask user if they want to merge any chunks
int main(){
    string outFileName = "reconstructedFile.txt";
    int chunkNumber = 1;
    int chunkSize = 4;

    ofstream outputFile(outFileName, ios::binary);

    if (!outputFile) {
        cout << "Error creating output file" << endl;
        return 1;
    }

    vector<char> buffer(chunkSize);
    
    while(true){
        string chunkName = "chunk_" + to_string(chunkNumber) + ".txt";
        ifstream chunkFile(chunkName, ios::binary);
        if(!chunkFile){
            break;
        }
        while(chunkFile.read(buffer.data(), chunkSize) || chunkFile.gcount() > 0){
            outputFile.write(buffer.data(), chunkFile.gcount());
        }

        chunkFile.close();
        chunkNumber++;
    }

    outputFile.close();
    cout << "File successfully Reconstructed." <<  endl;

    return 0;
}