def check_string(test):
    
    balance = 0 
    for char in test:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0:
            print("NO")
            return
        if balance == 0:
            print("YES")
        else:
            print("NO")


check_string("()")
check_string("(()())")
check_string("(()(()")
check_string(")(")
check_string("")