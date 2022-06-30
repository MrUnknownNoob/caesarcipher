import string

print('''

  ____  _____  _____   ____  _____  ____      ____  _____  ____   _   _  _____  ____  
 /  __||  _  ||  ___| / ___||  _  ||  _ \    /  __||_   _||  _ \ | | | ||  ___||  _ \ 
|  /   | | | || |___ | |__  | | | || |_| |  |  /     | |  | |_| || | | || |___ | |_| |
| |    | |_| ||  ___| \__ \ | |_| ||    /   | |      | |  |  __/ | |_| ||  ___||    / 
| |    |  _  || |        | ||  _  || |\ \   | |      | |  | |    |  _  || |    | |\ \ 
|  \__ | | | || |___  ___| || | | || | | |  |  \__  _| |_ | |    | | | || |___ | | | |
 \____||_| |_||_____||____/ |_| |_||_| |_|   \____||_____||_|    |_| |_||_____||_| |_|

 ****** Tool Name ::Caesar Cipher ******
       Why This tool :: This tool Is Made for Entrypted and Decrypted Caesar Cipher
       Contact with Me : https://github.com/mrwnknown
    ** Donot try to Copy This. All right Reserved By MR.UNKOWN 

01. Only Entrypted [windows]
02. Entrypted and Decrypted Both [windows]

''')



select = int(input("Choose a Number:"))

if(select == 1):
    text = str(input("Enter Your Message::"))
    shift = int(input("Enter your difference::"))

    alphabet = string.ascii_lowercase
    shifted =  alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted)

    encrypted = text.translate(table)
    print(encrypted)


if(select == 2):
    print('''
    01. For Encrpyted
    02. For Decrpted
    03. EXIT
    ''')

    whattodo = int(input("Choose a Option::"))
    #alphabet = string.ascii_lowercase + string.ascii_lowercase
    #sentence = list(input("ENter your Text :").lower())
    #1shiftnumber = int(input("Enter the Shift Number from 1 to 25:"))

    endpro = False
    while not endpro:
        if (whattodo == 1):
            alphabet = string.ascii_lowercase + string.ascii_lowercase
            sentence = list(input("ENter your Text :").lower())
            shiftnumber = int(input("Enter the Shift Number from 1 to 25:"))

            for i in range (len(sentence)):
                if sentence[i] == ' ':
                    sentence[i] = ' '
                else:
                    newletter = alphabet.index(sentence[i]) + shiftnumber
                    sentence[i] = alphabet[newletter]
            print("Your Decrpted Message is :", ''.join(map(str,sentence)))
            endpro = True

        elif(whattodo == 2):
            alphabet = string.ascii_lowercase + string.ascii_lowercase
            sentence = list(input("ENter your Text :").lower())
            shiftnumber = int(input("Enter the Shift Number from 1 to 25:"))

            for i in range(len(sentence)):
                if sentence[i] == ' ':
                    sentence[i] = ' '
                else:
                    newletter = alphabet.index(sentence[i]) - shiftnumber
                    sentence[i] = alphabet[newletter]
            print("Your Encrpted Message is :",''.join(map(str,sentence)))
            endpro = True

        elif(whattodo == 3):
            print('''IF InValid Entry
            01. Try Again
            02. Quit
            ''')
            decide = int(input("Choose A Number:"))
            if (decide == 1):
                print("Run Again the Programme")
                break
            elif(decide == 2):
                endpro = True
                break
            else:
                print("ERROR!!!")
                break
        else:
            print("ERROR!!!")


        
        

   