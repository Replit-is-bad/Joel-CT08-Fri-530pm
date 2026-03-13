import os                   # import os
filepath = os.getcwd()      # get the file path

# join the file path to get the full path
fullpath = os.path.join(filepath, 'file.txt')

# check existence of a file
if os.path.exists(fullpath):
    print('yess')
else:
    print('no')

# add to the .txt file
file = open('manual_output.txt', 'w') # w = write is replacing things in that file. a = append is to add without replacing
file.write('Manual Write example')
file.close()

# copy
file = open('manual_output.txt', 'r') # r = read is to copy into a var
content = file.read
file.close()

# 'with' keyword
# easier to open and close file
with open('manual_output.txt', 'w') as file:
    file.write('sup')

# writelines
# using a list we can turn it into diff lines 
lines = ['Line 1\n', 'Line 2\n','Line 1\n']
with open('output.txt', 'w') as file:
    file.writelines(lines)

#readlines and .strip
# .strip helps remove extra spacing between lines
with open('output.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print('line:' , line.strip())