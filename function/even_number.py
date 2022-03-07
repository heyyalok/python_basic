# to print even number form list
def iseven(j):
    enum =[]
    for num in j:
        if num%2==0:
            enum.append(num)
    return enum
iseven([1,2,3,4,56,7,8])
