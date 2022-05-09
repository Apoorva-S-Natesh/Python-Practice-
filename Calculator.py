#Calculator
#add
def add(n1,n2):
    return n1 + n2
#sutract
def subtract(n1,n2):
    return n1-n2
   
#mutliply
def multiply(n1,n2):
    """Multiplies firt number with second number and returns the product"""
    return n1*n2
#divide
def divide(n1,n2):
    """Divides first number by second number and returns the quotient"""
    return n1 / n2

#Creating a dictionary which has the symbols as the key and corresponding functions as the value
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
from art import logo
def calculator():
    print(logo)
    num1= float(input("What\'s the First number? :"))
    for operator in operations:
        print(operator)
    continue_operation='y'
    while continue_operation=='y':
        operation_symbol=input("Which operation do you want to do : ")
        num2= float(input("What\'s the Second number? :")) 
        answer=(operations[operation_symbol](num1,num2))
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_operation=input(f"""type 'y' to continue calculating with {answer} \n type 'n' to exit \n type 'new' to start a new calultion :""")
        if continue_operation=='y':
            num1=answer
        elif continue_operation=='n':
            print("thank you")
            break
        elif continue_operation=="new":
            calculator()
         
calculator()
