# open a file in read mode
with open("input.txt", 'r') as infile:  # open() returns a file object
                                        # with() will automatically close the file when block is exited
    content = infile.read() # read in one go
    for line in infile:     # read line by line
        print(line.strip()) # strip() to remove leading/trailing whitespace

# write to a file
with open("output.txt", 'w') as outfile:   # creates new file if it doesn't exist, or overwrites existing file if it does exist
    outfile.write("Hello world!\n")        # write() does not add a newline character at the end, so we need to add it ourselves
