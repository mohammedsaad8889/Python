def mario(number):
    number=int(number)
    for i in range(1,number+1):
        
        print((" ")*(number-i)+("*")*(i))
    

def mario_list(number):
    number = int(number)
    result = []
    for i in range(1, number + 1):
        line = (" ")*(number - i) + ("*")*i
        result.append(line)
    return result

    

number=input()
print(mario_list(number))