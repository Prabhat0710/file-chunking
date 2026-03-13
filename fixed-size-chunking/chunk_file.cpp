#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

//an infiinte loop for the program 
//give user 2 option chunking or merging
//if chunking, provide file path, file shoujld be there
//if merging, then ask for file name and if a folder with file name is found inside the  chunks_folder then start assembling the file
int main(){
    string inputFile = "input.txt";//make this path dynamic
    // string inputFile = "../files/input.txt";//make this path dynamic

    int chunkSize = 4;//take chunks size from user

    //opens the user specfied file and puts it in the file variable
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
        string outFile = "chunk_" + to_string(chunkNumber) + ".txt";//this nameing will be dyanamic and tthe prefix will be the name of the file openeed
        ofstream chunkFile(outFile, ios::binary);//the chunk extension should be dynamic
        chunkFile.write(buffer.data(), file.gcount());
        chunkFile.close();
        chunkNumber++;
    }
    //whenever a new file is chunked createcx a new folder inside the chunks folder and dynamically add a folder inside that foler with files's name and all chunks of thatt file should be placed inside that folder
    file.close();
    cout << "File chunks successfully created." << endl;
    return 0;
}
