START PROGRAM

LOOP FOREVER

    DISPLAY MENU
        1 → Chunk file
        2 → Merge file
        3 → Exit

    GET USER CHOICE

    IF choice == 1
        CALL chunkFile()

    IF choice == 2
        CALL mergeFile()

    IF choice == 3
        BREAK LOOP

END LOOP

END PROGRAM

FUNCTION chunkFile()

    ask user for file name
    ask user for chunk size

    extract base file name

    create directory for chunks

    open metadata file

    WHILE file not finished
        read chunk
        write chunk file
        record chunk name in metadata
    END WHILE

END FUNCTION

FUNCTION mergeFile()

    ask user for metadata file

    read metadata

    create reconstructed file

    FOR each chunk in metadata
        read chunk
        append to output file
    END FOR

END FUNCTION