# New journal app 

from datetime import datetime
from os.path import *
from os import environ
from pathlib import *
from sys import *

__version__   = '1.0.0'
__author__    = 'duncan.hardy'

# The inevitable refactor to a class 
# def init():
#     home = get_home_directory()
#     check_entry_write_dir_exists(home)
#     return home

def journal(): 

    home = get_home_directory()
    filepath = check_entry_write_dir_exists(home)

    welcome()

    entries = []

    # add date time and author to top of entry file
    entries.append(f'{datetime.now()} {__version__} {__author__}\n')
    running = True 
    try:
        while running:
            entry = input(f'{datetime.now()} Journal Entry: ')
            if len(entry):
                entries.append(entry + '\n')
            else: 
                running = False

        # only write out files that have more entries than 
        # just the time stamp and author value
        if (len(entries[0]) > 1):
            file_prefix = format_timestamp(str(datetime.now()))
            with open(f"{filepath}/{file_prefix}_journal.txt", 'w') as outfile:
                outfile.writelines(entries)
    
    except KeyboardInterrupt:
        print("Good bye!")


def welcome(): 
    welcome_message = "Welcome to your Journal!"
    print(welcome_message)


# probably has a built in function to do this but...
def format_timestamp(in_timestamp):
    chars = [' ', ':', '-', '.']
    for char in chars:
        in_timestamp = in_timestamp.replace(char, '')
    
    return in_timestamp


def get_home_directory():
        username = environ['USERNAME']
        home = expanduser(f"~{username}")
        return home

def check_entry_write_dir_exists(home_directory):
    write_path = Path(f'{home_directory}/Journal')
    if (not write_path.exists()):
        write_path.mkdir()
        print("Write directory does not exist!")
        print(f"Created {write_path}")
        return write_path
    else:
        print(f"{write_path} already exists!")
        return write_path
    
if __name__ == '__main__': 
    journal()