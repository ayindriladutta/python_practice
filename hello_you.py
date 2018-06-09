#Ask user name
name = input("what is your name?: ")


#Ask user age
age = input("how old u r?: ")

#Ask user city
city = input("what city do u live in?: ")

#Ask user what they enjoy
love = input("what do u love doing?: ")

#create output text
string = "Your name is {} and you are {} years old.You live in {} and you love {}."
output =string.format(name,age,city,love)

#print output to screen
print(output)
