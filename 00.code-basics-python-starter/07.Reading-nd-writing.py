####################### Topics ###############################
# 1.Create a new file and write to it.
# 2.Reading file line by line.
# 3.File open modes.
# 4.with statement.
#############################################################

# mind it to give 2 slace rather than one slace.
# f = open("D:\\Workspace\\pratice@Python\\funny.txt", "a")
# f.write('I love Python')
# f.write('\n I love AWS')  # \n create anew line and add the item.

# f.close()
# close will free up all the operation /os associate with this file.
# write will override all the data so we use append for this.

# READ files line by line and calculate word count and then write this to the new file with wc.----------
f = open("D:\\Workspace\\pratice@Python\\funny.txt", "r")
f_out = open("D:\\Workspace\\pratice@Python\\funny_out.txt", "w")
# print(f.read())
for line in f:
    tokens = line.split(' ')
    f_out.write(line + 'word count: ' + str(len(tokens)))
    # print(len(tokens))  # its done the word count.
    # print(line)
f.close()
f_out.close()


##### if we are not explicitly close our open file we can use by with statement.#########

with open("D:\\Workspace\\pratice@Python\\funny.txt", 'r') as f1:
    print(f1.read())
print(f1.closed)


# :~:text=To%20check%20if%20a%20file%20exists%20in%20Python%20use%20the,number%20of%20uses%20in%20Python.
https: // careerkarma.com/blog/python-check-if-file-exists/
