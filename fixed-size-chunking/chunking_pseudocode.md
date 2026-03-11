input: file_path, chunk_size

open the file in binary mode

chunk_number = 1

while not end_of_file
    read chunk_size bytes from file
    create new file named chunk_<chunk_number>
    write the bytes into that chunk file
    chunk_number = chunk_number + 1
end while

close the file
