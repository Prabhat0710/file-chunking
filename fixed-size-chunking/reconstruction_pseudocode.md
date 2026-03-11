input: number_of_chunks

open output file "reconstructed.txt"

for each chunk from 1 to number_of_chunks
    open chunk_i.txt
    read bytes
    append bytes to reconstructed.txt
    close chunk_i.txt
end loop

close reconstructed.txt