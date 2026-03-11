open output file (reconstructed.txt)

chunk_number = 1

loop
    build chunk file name
    try opening chunk file

    if file does not exist
        break loop

    read chunk contents
    append to reconstructed file

    close chunk file
    chunk_number++
end loop

close reconstructed file