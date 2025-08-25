try:
    while True:

        op1=float(input("Enter first number :"))
        op2=float(input("Enter second number :"))
        operator=input("Enter operator :")

        
        if operator == "+":
            result = op1 + op2
            
            

        elif operator == "-":
            result = op1 - op2
            

        elif operator == "*":
            result = op1 * op2
            

        elif operator == "/":
            if op2 == 0:
                print("No any number divide by zero")
            continue
            result=op1 / op2
        else:
            print("plz Enter valid operator")
            continue
            

        print(f"result={result}")

             


            

except ValueError:
        print("value error")


 

 





