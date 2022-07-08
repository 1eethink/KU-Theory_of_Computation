#!/usr/bin/python3

import os
import sys
import re

###########################################
# Your regex pattern runs in this function!
# Return the matching result as a string
###########################################


def regex_play(str, prob_idx):
    if prob_idx == '1':
        print("==problem1==")
        p = re.compile('^http[s]?\:\/\/www[.]((facebook)|(instagram)|(cyworld)|(twitter))[.]com\/[a-zA-Z]*$', re.IGNORECASE)
        m = p.match(str)
        if m:
            result = m.group()
        else:
            result = ""
    elif prob_idx =='2':
        print("==problem2==")
        p = re.compile('(^[a-zA-Z][a-zA-Z0-9\_\.]*\@[a-z]+(([.]ac[.]kr)|([.]com)|([.]net)|([.]co[.]kr))$)|(^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])([.]([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3}$)|(^[0-9]{4}(\-[0-9]{4}){3}$)')
        m = p.match(str)
        if m:
            result = m.group()
        else:
            result = ""
    elif prob_idx =='3':
        print("==problem3==")
        p = re.compile('(?!.*(.)\\1\\1.*)(?!.*(\\s).*)((^([\\W\_]{10,})$)|(^([a-zA-Z]{10,})$)|(^(?=.*[a-zA-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}$)|(^(?=.*[a-zA-Z])(?=.*[\\W\_])[a-zA-Z\\W\_]{8,}$)|(^(?=.*[0-9])(?=.*[\\W\_])[0-9\\W\_]{8,}$)|(^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[\\W\_])[a-zA-Z0-9\\W\_]{8,}$))')

        # ('(?!.*(.)\\1\\1.*)(?!.*(\\s).*)((^([\\W\_]{10,})$)|(^([a-zA-Z]{10,})$)|(^(?=.*[a-zA-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}$)|(^(?=.*[a-zA-Z])(?=.*[\\W\_])[a-zA-Z\\W\_]{8,}$)|(^(?=.*[0-9])(?=.*[\\W\_])[0-9\\W\_]{8,}$)|(^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[\\W\_])[a-zA-Z0-9\\W\_]{8,}$))')
        # ('(?!.*(.)\\1\\1.*)((^([\~\`\!\@\#\$\%\^\&\*\(\)\-\_\+\=\{\}\[\]\|\\\/\:\;\"\'\<\>\,\.\?]{10,})$)|(^([a-zA-Z]{10,})$)|(^(?=.*[a-zA-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}$)|(^(?=.*[a-zA-Z])(?=.*[\~\`\!\@\#\$\%\^\&\*\(\)\-\_\+\=\{\}\[\]\|\\\/\:\;\"\'\<\>\,\.\?])[a-zA-Z\~\`\!\@\#\$\%\^\&\*\(\)\-\_\+\=\{\}\[\]\|\\\/\:\;\"\'\<\>\,\.\?]{8,}$)|(^(?=.*[0-9])(?=.*[\~\`\!\@\#\$\%\^\&\*\(\)\-\_\+\=\{\}\[\]\|\\\/\:\;\"\'\<\>\,\.\?])[0-9\~\`\!\@\#\$\%\^\&\*\(\)\-\_\+\=\{\}\[\]\|\\\/\:\;\"\'\<\>\,\.\?]{8,}$)|(^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[\~\`\!\@\#\$\%\^\&\*\(\)\-\_\+\=\{\}\[\]\|\\\/\:\;\"\'\<\>\,\.\?])[a-zA-Z0-9\~\`\!\@\#\$\%\^\&\*\(\)\-\_\+\=\{\}\[\]\|\\\/\:\;\"\'\<\>\,\.\?]{8,}$))')


        m = p.match(str)
        if m:
            result = m.group()
        else:
            result = ""
    else:
        print("[ERROR] WRONG PROBLEM NUMBER")
        exit(1)

    return result

def main(file, prob_idx):
    result  = []
    # open problem file 
    try:
        with open(file, 'r') as f: 
            data = f.read()
    except FileNotFoundError as e:
        print("[ERROR] FILE NOT FOUND!")
    split_data = data.splitlines()

    #Run the regex_play function line by line
    for line in split_data:
        result.append(regex_play(line,prob_idx))
    result = list(filter(None, result))
    w_data = '\n'.join(result)
    
    try:
        with open('output_'+prob_idx+'.txt', 'w', -1, "utf-8") as file: 
            file.write(w_data)
            file.close()
    except FileNotFoundError as e:
        print("[ERROR] FILE NOT FOUND!")
    print(w_data)
    

if __name__ == '__main__':
    if(not sys.argv[1]):
    	print("""USAGE: python3 "FILE NAME" "problem NUMBER" """)
    if(not sys.argv[2]):
        print("""USAGE: python3 "FILE NAME" "problem NUMBER" """)
    file = sys.argv[1]
    prob_idx = sys.argv[2]
    main(file, prob_idx)