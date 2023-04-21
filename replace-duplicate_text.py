# importing all required libraries

import os
from sys import exit as exit
os.system("clear")

# banner
banner="""\033[1;31m   
TOOL NAME 

▀█▀ █▀▀ ▀▄▀ ▀█▀   █▀█ █▀▀ █▀█ █░░ ▄▀█ █▀▀ █▀▀
░█░ ██▄ █░█ ░█░   █▀▄ ██▄ █▀▀ █▄▄ █▀█ █▄▄ ██▄

ABOUT THIS TOOL ---> THIS IS ONE OF THE BEST TOOL FOR ADDING ANY CHARACTER, SYMBOLS, NUMBERS OR REPLACING YOUR TEXT INSTANTLY IN A SECONDS. NO WORRIES HOW MANY OF LINES YOU WANT TO ADD YOUR NEW TEXT OR REPLACE WITH NEW TEXT IT READS ALL THE LINES AND ADD OR REPLACE YOUR TEXT. 


AUTHOR NAME


░█████╗░███╗░░██╗██╗░░░██╗░██████╗██╗░░██╗
██╔══██╗████╗░██║██║░░░██║██╔════╝██║░░██║
███████║██╔██╗██║██║░░░██║╚█████╗░███████║
██╔══██║██║╚████║██║░░░██║░╚═══██╗██╔══██║
██║░░██║██║░╚███║╚██████╔╝██████╔╝██║░░██║
╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═════╝░╚═╝░░╚═╝

\033[1;32m☠️🔥 DON'T CONSIDER MY KINDNESS AS MY WEAKNESS 
BCOZ THE BEAST IS ON ME IS SLEEPING💫☠️ 🔰🖤

                \033[1;31m        ANUSH 💫🤟☠️👿

\033[1;93m ✧ ▬▭▬ ▬▭▬ ✦✧✦ ▬▭▬ ▬▭▬ ✧ ̶̶̶̶  «̶ ̶̶̶ ̶ «̶ ̶̶̶ ✩̣̣̣̣̣ͯ┄•͙✧⃝•͙┄✩ͯ•͙͙✧⃝•͙͙✩ͯ   ̶ ̶ ̶»̶ ̶̶̶ ̶ »̶ ̶̶̶  ✦✧✦ ▬▭▬ 
\033[1;32m ⇨AUTHOR    : ANUSH PATHAK
\033[1;32m ⇨FACEBOOK  : anush.pathak.104
\033[1;32m ⇨TOOL NAME   : TEXT REPLACE
\
\033[1;93m ✧ ▬▭▬ ▬▭▬ ✦✧✦ ▬▭▬ ▬▭▬ ✧ ̶̶̶̶  «̶ ̶̶̶ ̶ «̶ ̶̶̶ ✩̣̣̣̣̣ͯ┄•͙✧⃝•͙┄✩ͯ•͙͙✧⃝•͙͙✩ͯ   ̶ ̶ ̶»̶ ̶̶̶ ̶ »̶ ̶̶̶  ✦✧✦ ▬▭▬ """

def main():
    os.system("clear")
    print(banner) 
    print(" \033[1;92m[1] START TOOL  ")
    print(" \033[1;92m[2] FACEBOOK PROFILE ")
    print(" \033[1;92m[3] GO TO GITHUB PROFILE  ")
    print (" \033[1;92m[0] EXIT") 
    print (' \033[1;93m✧ ▬▭▬ ▬▭▬ ✦✧✦ ▬▭▬ ▬▭▬ ✧ ̶̶̶̶  «̶ ̶̶̶ ̶ «̶ ̶̶̶ ✩̣̣̣̣̣ͯ┄•͙✧⃝•͙┄✩ͯ•͙͙✧⃝•͙͙✩ͯ   ̶ ̶ ̶»̶ ̶̶̶ ̶ »̶ ̶̶̶  ✦✧✦ ▬▭▬ ') 
    key = input(" [*] \033[1;32mC H O O S E : ")
    print (' \033[1;93m✧ ▬▭▬ ▬▭▬ ✦✧✦ ▬▭▬ ▬▭▬ ✧ ̶̶̶̶  «̶ ̶̶̶ ̶ «̶ ̶̶̶ ✩̣̣̣̣̣ͯ┄•͙✧⃝•͙┄✩ͯ•͙͙✧⃝•͙͙✩ͯ   ̶ ̶ ̶»̶ ̶̶̶ ̶ »̶ ̶̶̶  ✦✧✦ ▬▭▬')
    if key in [""]:
        print (" [!] INCORRECT OPTION")
        exit()
    elif key in ["1", "01"]:
        Text()
    elif key in ["2",  "02"]:
        os.system("https://www.facebook.com/anush.pathak.104")
    elif key in ["3", "03"]:
        os.system("https://github.com/anushpathak09")

    else:
        print("INVALID OPTION")


def Text(): 
    # Prompt the user for input and output file names
    input_file = input("Enter input file name: ")
    output_file = input("Enter output file name: ")

# Prompt the user for the text to replace duplicates of
    duplicate_text = input("Enter text to replace duplicates of: ")
    new_text = input("Enter Your New Replacing text")

# Open the input file for reading
    with open(input_file, 'r') as infile:
    # Read all lines from the input file
        lines = infile.readlines()

# Create a set to keep track of which lines have already been modified
    modified_lines = set()

# Open the output file for writing
    with open(output_file, 'w') as outfile:
    # Loop over all lines in the input file
        for i, line in enumerate(lines):
        # Check if this line contains the duplicate text and has not already been modified
            if duplicate_text in line and i not in modified_lines:
            # Replace all instances of the duplicate text with an empty string
                new_line = line.replace(duplicate_text, new_text)

            # Write the modified line to the output file
                outfile.write(new_line)

            # Mark this line as modified
                modified_lines.add(i)
            else:
                # Write the unmodified line to the output file
                outfile.write(line)

# Print a message indicating that the program has finished
print("File processing complete!")


           
main()