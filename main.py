import array as arr

order = input("Crescent or decrescent order? ").lower()
numbers = 5
list = arr.array('i',[])

def addToList(newNumber):
    length = len(list)
    
    if length == 0:
        list.append(newNumber)
        
        return 0
    
    for key,number in enumerate(list):
        length = len(list)
        
        if order == "crescent":
            if newNumber < number:
                list.insert(key,newNumber)
                
                return key
            else:
                if key == length - 1:
                    list.append(newNumber)
                    
                    return key + 1
        elif order == "decrescent":
            if newNumber > number:
                list.insert(key,newNumber)
                
                return key
            else:
                if key == length - 1:
                    list.append(newNumber)
                    
                    return key + 1

for num in range(numbers):
    key = addToList(int(input())) + 1
    numberPostfix = "th"
    
    if key == 1:
        numberPostfix = "st"
    elif key == 2:
        numberPostfix = "nd"
    elif key == 3:
        numberPostfix = "rd"
    
    print(f"Added number to {str(key)}{numberPostfix} position.")

print(list)