#include <iostream>

#include "../include/chunker.h"
#include "../include/merger.h"

using namespace std;

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
            cout << "Exiting...\n";
            break;
        }
        else
        {
            cout << "Invalid choice\n";
        }
    }

    return 0;
}