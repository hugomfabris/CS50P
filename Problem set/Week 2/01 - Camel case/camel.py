#Ask for user's input
camel = input("CamelCase: ")
#Turn into a list
camel_list = list(camel)
#Iterate through each letter of the list, turning every upper case element lower case and inserting an underline before it
for i in range(len(camel_list)):
    if camel_list[i].isupper():
        camel_list[i] = '_' + camel_list[i].lower()
#Now we turn our list into a string again to reach our result
snake_case = ''.join(camel_list)
print(snake_case)