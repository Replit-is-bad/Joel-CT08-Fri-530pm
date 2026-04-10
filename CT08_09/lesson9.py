import os
import time
 
notepath = os.path.join(os.getcwd(), 'Null.txt')

if os.path.exists(notepath):
    with open("Null.txt", "r") as file:
        content = file.read()
        print("FILE FOUND")
else:
    print('NOT FOUND')

print("Cleaning up the code...")
time.sleep(2)
print()

cleaned = ""

for char in content:
    if char.isalpha():
        cleaned += char.lower()
    elif char == " ":
        cleaned += char

print(cleaned)

print()
print("DECODING...")
time.sleep(2)
print()

Secret = ""
Secret += cleaned[0]
for i in range(len(cleaned)):
    if cleaned[i] == " ":
        Secret += cleaned[i + 1]
print(Secret)

print()
print("ENCRYPTING...")
print()
time.sleep(1)


encrypted = ""
for i in range(len(Secret)):
    encrypted = Secret[::-1]

file = open('hidden_message.txt', 'w')
file.write(encrypted)
file.close()

time.sleep(1)
print("SUCSESSFULLY ENCRYPTED")

