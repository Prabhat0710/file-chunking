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
    // We used vector instead of arrays because arrays are dynamic
    // vector<char> will tell computer to store 1 byte of data in vector
    // buffer(chunkSize) creates a beffer container of 4 cells each of 1 byte in memory 
    
    while(file.read(buffer.data(), chunkSize) || file.gcount() > 0){ 
        // file.read(buffer.data(), chunkSize) this tells to read 4 bytes from the file and store it in buffer
        // buffer.data() will give the first address of beffer cell
        // file.gcount() if last chunk contains less than chunkSize of bytes it will handle that
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
