# Fixed Size Chunking

Fixed-size chunking splits a file into pieces of equal size.

Example:

File:
ABCDEFGHIJKL

Chunk size: 4

Chunks:
ABCD
EFGH
IJKL

Algorithm idea:
1. Open the file
2. Read N bytes
3. Save the chunk
4. Repeat until file ends

Advantages:
- Simple
- Fast
- Easy to implement
- pridictability

Disadvantages:
- Small changes shift all chunks
- Poor deduplication    
