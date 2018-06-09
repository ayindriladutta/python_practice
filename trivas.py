known_users=["Alice","Bob","Claire","Dan","Emma","Fred","Georgie","harry"]

print(len(known_users))

while True:
    name = input("what is your name?").strip().capitalize()
    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("would u like to remove ur name (y/n)").lower()
        if remove == "y":
            known_users.remove(name) #remove() delete only the first instance of
                                        #dublicate element from list 
        elif remove == "n":
            print("no problem")
            
    else:
        print("hmm i don't think i know {}".format(name))
        add_me = input("would u like  to be added (y/n)").strip().lower()
        if add_me =="y":
            known_users.append(name)
        elif add_me== "n":
            print("no worries")
        
