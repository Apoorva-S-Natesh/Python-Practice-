#Caesar used to send his messgaes in an encrypted format. With each alphabet moved by a certain number or shift.The code tries to fo the same.
#The code was a practice for defining functions which takes input, nested while and if.
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP""" """"  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""" """" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

#defining Caesar Method
def caesar(plain_text, shift_amount, choice):
    cipher_text = ""
    
    #if the shift number is grater than 26 then number has to be reset so that the loop doesnt break and we dont get out of index error. 
    if shift_amount > 26:
        shift_amount %= 26
        
    #if the character isnt an alphabet then it has to be retained. example: Meet me at 3.(including the spaces)
    for char in plain_text:
        if char in alphabet:
            #getting the index of the character in text using list.index()
            position = alphabet.index(char)
            if direction == "encode":
                new_position = position + shift_amount
                #if the position index is more than 25 then to avoid out of index error. example: if the shift is 5 and the alphabet is y whose index is 24 
                #i.e 24+5=29 which when sutracted by 26 gives the correct position which is character at index 3 in alphabet list which is d.
                if new_position > 25:
                    cipher_text += alphabet[new_position - 26]
                else:
                    cipher_text += alphabet[new_position]
            else:
                new_position = position - shift_amount
                if new_position < 0:
                    cipher_text += alphabet[new_position + 26]
                else:
                    cipher_text += alphabet[new_position]
        #adding characters that are not alphabets to the final string
        else:
            cipher_text += char
    print(f"The {direction}d text is {cipher_text}")

#If the user wants to contine the process of encodig and decodning
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #giving keyword arguments to Caesar
    caesar(plain_text=text, shift_amount=shift, choice=direction)

    result = input("Do you wan to go again? Type \'Y\' or \'N\'").upper()
    if result == "N":
        should_continue = False

print("Thank you :) We should send more secret coded messages:P ")
