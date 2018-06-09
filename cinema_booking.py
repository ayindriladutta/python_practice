flims ={
    "Sanju":[20,5],
    "Padmabati":[18,7],
    "Antman":[3,6],
    "Tarzan":[10,5]
    }
while True:
    choice= input("which movie u want to watch?").strip().title()

    if choice in flims:
        #pass
        age = int(input("how old are you?:").strip())

        #check user age
        
        if age >=flims[choice][0]:
            #check engouh seats
            num_seats = flims[choice][1]
            if num_seats>0:
                print("enjoy the flime")
                flims[choice][1]=num_seats-1
            else:
                print("we are sold out")
        else:
            print("you are too young to watch the flim")
    else:
        print("we dont have the flime")
        
    

