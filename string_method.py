x = "hello".count("l")
print(x)
x = "Ayindrila Dutta"
print(x.upper())
print(x) #strings are immutable
x = x.lower()
print(x)
print(x.title())
print(x.isupper())
print(x.islower())
print("Andy".isalpha())
print("Andy ".isalpha())
print("123".isdigit())
print("andy123".isalnum())

#.count() .upper() .lower() .title() .capatalize()
#.isalpha() .isdigit() .isalnum()
#.islower() .isupper() .istitle()

print(x.index("dutta"))    #methods used to find the position of sub string
print(x.find("dutta"))     #these methods are case sensitive

y = "0000000000happybirthday0000000000"
print(y.strip("0"))
print(y.lstrip("0"))

name = input("what is your name?: ")
print(name)
print(len(name))  #counts the letter with the space


name = input("what is your name?: ").strip()
print(name)
print(len(name))


