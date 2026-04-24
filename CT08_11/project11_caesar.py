import os

def caesar_shift_enter(char,key,mode):
    ascii_value = ord(char) # Character -> Number
    ascii_value -= 32 

    if mode.lower() == "e":
        ascii_value += key
    elif mode.lower() == "d":
        ascii_value -= key
    else:
        return None

    ascii_value %= 95 # Remainder 
    ascii_value += 32
    char = chr(ascii_value)
    return char

def ceasar_shift_sentence(sentence,key,mode):
    encrypted_sentence = ""
    for char in sentence:
        encrypted_sentence += caesar_shift_enter(char,key,mode)
    return encrypted_sentence

def ceasar_shift_file(input_file, output_file, key, mode):
    notepath = os.path.join(os.getcwd()), input_file
    with open(input_file,"r") as file:
        content = file.read()
    encrypted_file = ceasar_shift_sentence(content,key,mode)

    if encrypted_file:
        with open(input_file,"w") as file:
            file.write(encrypted_file)
    else:
        print("File Was INVALID")



# sentence = input("GIVE ME SENTENCE! ")
# mode = input("Input a mode (E = encrypt D = decrypt): ")
# encrypted_sentence = ceasar_shift_sentence(sentence, 5, mode)
# if encrypted_sentence != "":
#     print(encrypted_sentence)
# decrypted_sentence = ceasar_shift_sentence(encrypted_sentence,5,"d")
# if decrypted_sentence:
#     print(f"Decryped : {decrypted_sentence}")

ceasar_shift_file("default.txt","encryped.txt",8,"e")