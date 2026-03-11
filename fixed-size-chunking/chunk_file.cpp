#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main(){
    string inputFile = "input.txt";
    int chunkSize = 4;

    ifstream file(inputFile, ios::binary);

    if(!file){
        cout << "Error opening file" << endl;
        return 1;
    }

    int chunkNumber = 1;
    vector<char> buffer(chunkSize);

    while(file.read(buffer.data(), chunkSize) || file.gcount() > 0){
        string outFile = "chunk_" + to_string(chunkNumber) + ".txt";
        ofstream chunkFile(outFile, ios::binary);
        chunkFile.write(buffer.data(), file.gcount());
        chunkFile.close();
        chunkNumber++;
    }

    file.close();
    cout << "File chunks successfully created." << endl;
    return 0;
}