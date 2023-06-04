# New journal app 

from datetime import datetime
import os, os.path, pathlib, json 

__version__   = '1.0.1'

# The inevitable refactor to a class 
# def init():
#     home = get_home_directory()
#     check_entry_write_dir_exists(home)
#     return home

def journal(): 

    # TODO: wrap in function 
    home = get_home_directory()
    filepath = check_entry_write_dir_exists(home)
    setup_dir = pathlib.Path(f'{home}/Journal/Setup') 

    if not check_for_config(setup_dir):    
        journal_config = set_config()
        write_config(setup_dir, journal_config)
    else: 
        journal_config = read_config(setup_dir)

    welcome()

    entries = []

    # add date time and author to top of entry file
    entries.append(f"{datetime.now()} {__version__} {journal_config['author']}\n")
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

            # Update the config file meta data
            journal_config['last_entry'] = (str(datetime.now()))
            journal_config['total_entries'] += 1
            
            with open(f"{filepath}/{file_prefix}_journal.txt", 'w') as outfile:
                outfile.writelines(entries)
            
            # set last entry and total entries values 
            write_config(setup_dir, journal_config)
    
    except KeyboardInterrupt:
        print("Good bye!")

def check_for_config(in_path): 

    if not in_path.exists():
        in_path.mkdir()
        return False
    
    return True

def set_config():
    journal_config = {}

    print("No config file detected, performing some initial setup...")
    
    journal_config['author'] = input("Who is the author of this journal?")
    journal_config['subject'] = input("Is there a particular subject that you're writing about?")
    journal_config['version'] = __version__
    journal_config['first_entry'] = str(datetime.now())
    journal_config['last_entry'] = ''
    journal_config['total_entries'] = 0

    return journal_config

def write_config(in_path, in_config_data):

    with open(f'{in_path}/setup.config', 'w') as config_file: 
        json.dump(in_config_data, config_file)

def read_config(in_path):
    with open(f'{in_path}/setup.config', 'r') as config_file: 
        config_data = json.load(config_file)

    return config_data

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
    username = os.environ['USERNAME']
    home = os.path.expanduser(f"~{username}")
    return home

def check_entry_write_dir_exists(home_directory):
    write_path = pathlib.Path(f'{home_directory}/Journal/Entries')
    if not write_path.exists():
        write_path.mkdir()
        print("Write directory does not exist!")
        print(f"Created {write_path}.")
        return write_path
    else:
        print(f"{write_path} already exists!")
        return write_path
    
if __name__ == '__main__': 
    journal()