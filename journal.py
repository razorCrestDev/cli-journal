# New journal app 

from datetime import datetime

__version__   = '1.0.0'
__author__    = 'duncan.hardy'

#TODO: change this
__filepath__ = 'C:/Users/dunca/Projects/Personal/Journal/entries/'

def welcome(): 
    welcome_message = "Welcome to your Journal!"
    print(welcome_message)

def journal(): 

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
        if (len(entries) > 1):
            file_prefix = format_timestamp(str(datetime.now()))
            with open(f"{__filepath__}{file_prefix}_journal.txt", 'w') as outfile:
                outfile.writelines(entries)
    
    except KeyboardInterrupt:
        print("Good bye!")


# probably has a built in function to do this but...
def format_timestamp(in_timestamp):
    chars = [' ', ':', '-', '.']
    for char in chars:
        in_timestamp = in_timestamp.replace(char, '')
    
    return in_timestamp


if __name__ == '__main__': 
    journal()