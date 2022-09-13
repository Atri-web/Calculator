# Calculator program
user_input = input("What operation do you want to do? add, subtract, multiply or divide? ")

x = input(f'What is the first number you want to {user_input}? ')
y = input(f'What is the second number you want to {user_input}? ')

#function which adds, subtracts, multiplies, and divides
def operation_function(user_input, x, y):
    if(user_input.lower() == "add" or user_input.upper() == "Add"):
      return(int(x) + int(y))

    elif(user_input.lower() == "subtract" or user_input.upper() == "Subtract"):
       return(int(x) - int(y))

    elif(user_input.lower() == "multiply" or user_input.upper() == "Multiply"):
        return(int(x) * int(y))

    elif(user_input.lower() == "divide" or user_input.upper() == "Divide"):
        divide_total = int(x) % int(y)
        if(divide_total == 0):
            return(int(int(x) / int(y)))
        else:
            return(int(x) / int(y))

#prints out the output
print(operation_function(user_input, x, y))

