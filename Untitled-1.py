def ask_password():
    for i in range(0, 3):
        s = input()
        if s == 'password':
            print('можно.')
            break 
        else:
            print("не подходит")          

ask_password()  
    
# def quarter(x, y):
#     if x > 0 and y > 0:
#         print('1')
#     if x > 0 and y < 0:
#         print('4')
#     if x < 0 and y > 0:
#         print('2')
#     if x < 0 and y < 0:
#         print('3')

# quarter(100,-100)