def Pal(a):
    if a[::-1]==a[::1]:
        return "palindrome"
    else:
        return "no"
string=input("input any string which u want to check weather it is palindrome or not: ")
Pal(string)
