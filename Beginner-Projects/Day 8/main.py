alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cipher =  """,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88   """
print(cipher)
def decode(msg, shift):
    cipher_list = []  # 1. Create a new empty list
    for letter in msg:
        if letter in alphabet:
            # 2. Use modulo (%) to wrap around if shift goes past 'z'
            ind = alphabet.index(letter)
            ind_sh = (ind - shift) % 26
            cipher_list.append(alphabet[ind_sh])
        else:
            # 3. Keep spaces or symbols as they are
            cipher_list.append(letter)

    print(f"Here's the decoded result:{"".join(cipher_list)}")


def encode(msg, shift):
    cipher_list = []  # 1. Create a new empty list
    for letter in msg:
        if letter in alphabet:
            # 2. Use modulo (%) to wrap around if shift goes past 'z'
            ind = alphabet.index(letter)
            ind_sh = (ind + shift) % 26
            cipher_list.append(alphabet[ind_sh])
        else:
            # 3. Keep spaces or symbols as they are
            cipher_list.append(letter)

    print(f"Here's the encoded result:{"".join(cipher_list)}")
yes = True
while yes:
    en_or_dc = input("Type 'encode' to encrypt, type 'decode' to decrypt:").lower()
    msg = input("Type your message:").lower()
    shift = int(input("Type the shift number:"))
    if en_or_dc == "encode":
        encode(msg,shift)
    elif en_or_dc == "decode":
        decode(msg,shift)
    else:
        print("Please enter valid answer!!")
        continue
    another = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if another == "yes":
        continue
    elif another == "no":
        print("Goodbye")
        yes = False
