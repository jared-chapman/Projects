def reverse(original):
    reversed = ""
    count=1
    for i in original:
        reversed += original[len(original)-count]
        count += 1
    return reversed

def easyReverse(original):
    return original[::-1]



print(easyReverse("Hello"))
