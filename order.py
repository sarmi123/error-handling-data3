#we are using open(), built in functionality from python to open files
def open_and_print(file_to_open):
    try: #tries to run a block of code
        file =open ("order.txt", 'r')
        file_line_list =file.readlines()

        for line in file_line_list:
            print(line.rstrip('\n'))

        file.close()

    except FileNotFoundError as errmsg: #if it fails it runs this block of code
        print("Hi:) File could not be open")
        print(errmsg)
open_and_print('order.txt')