# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("enter lower range value")
lowr = int(input())
print("enter upper range value")
upr = int(input())
if upr<lowr:
    print("invalid input")
else:
    print("Even numbers between",lowr,"-",upr,"are")
    for i in range(lowr,upr+1,1):
        if(i%2==0):
            print("even",i)
    print("odd numbers between", lowr, "-", upr, "are")
    for i in range(lowr,upr+1,1):
        if (i % 2 != 0):
            print("odd", i)
