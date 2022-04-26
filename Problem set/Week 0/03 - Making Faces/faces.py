#Ask for user's input
text = input("")
#Replaces :) and :( with emojis 
print(text.strip().replace(':)', '🙂').replace(':(', '🙁'))