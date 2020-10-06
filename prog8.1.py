#!/usr/bin/python3

'''
Program:        Really Lame File Processor
Version:        8.1.1
Author:         Logan Kessler
Date:           10-02-2020
Description:    Basic CSV file creator
'''

import os   # used to interface with OS

def file_prompt():
    lock =  True    # used 'lock' and loop for extreame case where file exists
    path = ''       # our 'directory' on OS to save file in
    full_path = ''  # file handle of 'directory' and 'file name' 
    while lock:
        io = input('Please enter directory where to save a file\n-->>> ')
        if os.path.isdir(io):
            path = io
        elif os.path.isdir(io) == False:
            os.makedirs(io) # create directories on OS recursively
            path = io

        io = input('Please enter file name\n-->>> ')
        full_path = path + io
        lock = False

        # sanity check if file exists already
        if os.path.isfile(full_path):
            lock = True
            print('File Exists!')

    return full_path

def file_contents():
    # using a Dictionary for expandability
    u_dict = {}

    # loop can be added for more 'items', if necessary
    io = input('Please enter your name: ')
    u_dict['name'] = io
    io = input('Please enter your address: ')
    u_dict['address'] = io
    io = input('Please enter your phone number: ')
    u_dict['phone'] = io

    return u_dict

def create_file(fp, udict):
    # concat Dictionary values to a CSV
    f_input = str(udict['name']) + ',' + str(udict['address']) + ',' + str(udict['phone'])

    # open path and file 'fp' as file handle 'fh' for writing
    with open(fp, 'w') as fh:
        fh.write(f_input)
        print('Writing to file complete!\n')

def file_print(fp):
    # open path and file 'fp' as file handle 'fh' for reading then printing
    with open(fp, 'r') as fh:
        f_out = fh.read()
        print('Printing File...\n')
        print(f_out)

def main():
    # welcome message is standard now
    print('Welcome to LK\'s Really Lame File Processor!\n')

    # variables used to pass and set through functions
    file_path = ''
    contents = ''

    # prompt user for OS directory to save in and file name
    file_path = file_prompt()
    # prompt user for CSV values
    contents = file_contents()
    # creates 'file_path' directory and file to OS and writes 'contents' to file
    create_file(file_path, contents)
    # prints 'file_path' to STDOUT for user to see
    file_print(file_path)

    # print exit message
    print('\nThank you, for using LK\'s Really Lame File Processor!')

###############
# Run Program #
###############
main()
