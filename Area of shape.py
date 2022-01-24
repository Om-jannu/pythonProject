
print("Area of the given shape")
print("enter whose area to be calculated")
print("1.circle")
print("2.rectangle")
print("3.triangle")
ch = int(input())
if ch < 1 or ch > 3:
    print("invalid input")
else:
    if ch == 1:
        print("enter radius of circle")
        rad = float(input())
        area = 3.14 * (rad ** 2)
        print(area)
    elif ch == 2:
        print("enter length of rectangle")
        len = float(input())
        print("enter length of rectangle")
        bre = float(input())
        area = len * bre
        print(area)
    elif ch == 3:
        print("enter height of triangle")
        hei = float(input())
        print("enter baselength of triangle")
        bas = float(input())
        area = (hei * bas) / 2
        print(area
