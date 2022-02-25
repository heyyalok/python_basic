#A
for row1 in range (4):
    for col1 in range (4):
        if (row1 == 0 or row1 == 2) or (col1 ==0 or col1 ==3):
            print('#',end=(''))
        else:
            print(' ',end=(''))
    print()
