
students = {}   #empty dictionary
students ={"Andy":25,"thusar":24, "praveen":27,"abc":10,"xyz":55}
print(students["praveen"])  #how to look up a key
print(students["Andy"])
students["Andy"]=26
print(students["Andy"])

print(students.keys())    #get the list of keys using dictionar key()
del students["thusar"]
print(students.keys())
print(students.values())
#print(students["thusar"])

#dict_keys are not indexed
#convert dict_keys into list

student=list(students.keys())
print(student)

print(student[1])

age=list(students.values())
print(age)
 
