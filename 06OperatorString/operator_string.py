# Operatot Precedence 

a = 12
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
print(a - b / b + a)  # Python follows BODMAS kind of rule 

#Strings and Slicing 

parrot = "Norwegian Blue"

print (parrot)

print(parrot[3])
print(parrot[-1])  # Python Starts counting the character backward from -1 indexing 

# Slicing general format...
# var[start:end:step] or #print(parrot[START:STOP:STEP])
print(parrot[0:6])  #Norweg
# Python doesn't include the end index in the slicing like "UPTO BUT NOT INCLUDING"

print(parrot[:6])  #Norweg
print(parrot[6:])  #ian Blue
print(parrot[6:-1])  #ian Blu
print(parrot[6:-2])  #ing Bl
print(parrot[6:-2:2])  #inB
print(parrot[::2])  # Every second character i.e NreinBu
print(parrot[::-1])  # Reverse the string
print(parrot[::-2])  # Printing in Reverse & every second character i.e  el agwo
print(parrot[:]) # Norwegian Blue
print(parrot[-4:12]) # Bl
print(parrot[-4:-2]) # Bl