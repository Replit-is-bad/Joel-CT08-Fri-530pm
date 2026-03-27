import os

filepath = os.getcwd()
sherlock_path = os.path.join(filepath, "sherlock.txt")

if os .path.exists(sherlock_path):
    with open("sherlock.txt", "r") as file:
        content = file.read()
        print(f"Total Characters : {len(content)}")

    counta = 0
    counte = 0
    counti = 0
    counto = 0
    countu = 0
    for char in content:
        if char.lower() == "a":
         counta += 1
        elif char.lower() == "e":
         counte += 1
        elif char.lower() == "i":
         counti += 1
        elif char.lower() == "o":
         counto += 1
        elif char.lower() == "u":
         countu += 1
    print(f" a = {counta}")
    print(f" e = {counte}")
    print(f" i = {counti}")
    print(f" o = {counto}")
    print(f" u = {countu}")
    total = counta + countu + counte + counti + counto
    print(f" total vowels = {total}")

    percentage = total / len(content) * 100
    percentage = round(percentage , 2)
    print(f"Percent of vowels in 'sherlock.txt' : {percentage}%")

    with open('SAVE.txt', 'w')as file:
        file.write(f" total characters = {len(content)}")
        file.write(f"\n total vowels = {total}")
        file.write("\n")
        file.write(f"\n a = {counta}")
        file.write(f"\n e = {counte}")
        file.write(f"\n i = {counti}")
        file.write(f"\n o = {counto}")
        file.write(f"\n u = {countu}")
        file.write(f"\n a = {counta}")
        file.write(f"\n Percent of vowels in 'sherlock.txt' : {percentage}%")
else:
    print('NOT FOUND')