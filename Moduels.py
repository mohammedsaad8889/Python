#d1
def count_number_of_vowels(name):
    name=str(name)
    vowels="aeiouAEIOU"
    count=0
    for i in name:   
        if i in vowels :
            count+=1
    return count 

def  locations_of_i(name):
    name=str(name)
    for i in range(1,len(name)): 
        if name[i]=="i" or name[i]=="I" : 
            return i

def  multiplication_table (number):
    number=int(number)
    for i in range(1,number+1) :  # 1 2 3 4 
        for j in range(1,i+1) :   # 1          
            print(f"{i}x{j}={i*j}") 

#d2
def get_user_email_info():
    while True:
        name = input("Enter your name: ")
        strname = name.strip()
        
        if strname == "":
            print("Name is empty. Please try again.")
            continue
        elif any(char.isdigit() for char in strname):
            print("Name should not contain numbers. Try again.")
            continue
        else:
            break

    while True:
        email = input("Enter your email: ").strip()
        
        try:
            username = email.split("@")[0]
            dom = email.split("@")[1].split(".")[0]
            tld = email.split("@")[1].split(".")[1]

            if username.isalpha() and dom.isalpha() and tld.isalpha():
                break
            else:
                print("Invalid email. Enter a valid email address.")
        except IndexError:
            print("Invalid email format. Please try again.")

    return strname, email

def generate_multiplication_lists(n):
    result = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, i + 1):
            row.append(i * j)
        result.append(row)
    return result

def get_sorted_numbers(n):
    n=int(input("Enter nuumber of numbers that u want Sort:"))
    arr = []
    for x in range(n):
        z = int(input(f"Enter number {x+1}: "))
        arr.append(z)
    arr.sort(reverse=True)
    return arr

#d3
def find_user_and_pass(user,listed):
    listed=[{"name":"mohamed", "pass":"123"},{"name":"ahmed", "pass":"1234"},{"name":"omar", "pass":"12345"}]
    for a in range(len(listed)):
        x=list(listed[a].values())
        if user == x[0] :
            password=input("Enter Your pass : ")
            if password == x[1] :
                print(True)
            else:
                 print(False)           
#d4
def get_user_email_info_by_try_and_exept():
    while True:
        try:
            name = input("Enter your name: ").strip()
            if not name:
                raise ValueError("Name is empty.")
            if any(char.isdigit() for char in name):
                raise ValueError("Name should not contain numbers.")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            email = input("Enter your email: ").strip()
            username, domain = email.split("@")
            dom, tld = domain.split(".")

            if not (username.isalpha() and dom.isalpha() and tld.isalpha()):
                raise ValueError("Email parts must be alphabetic.")
            break
        except ValueError as e:
            print(f"Invalid email: {e}")
        except IndexError:
            print("Invalid email format. Please try again.")

    return name, email

# Usage

print(())






