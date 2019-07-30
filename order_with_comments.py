# we are using open(), built in functionality from python to open files
try:  # tries to run a block of code
    file = open("order.txt", 'r')
    file_line_list = file.readlines()
    # print(file)
    # print type((file_line_list))
    for line in file_line_list:
        print(line.rstrip('\n'))

    file.close()  # if you dont close it you can cause a look in the file- like trying to delete a file whilst it is open elsewhere.


except FileNotFoundError as errmsg:  # if it fails it runs this block of code
    print("Hi:) File could not be open")
    print(errmsg)  # captured error message in line 5
    # print("PANIC ERROR OCCURRED ")
    raise  # sends the default error and stops the code