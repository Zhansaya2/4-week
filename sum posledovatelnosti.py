def sump():
    n = int(input())
    global sum
    if n != 0:
        sum += n
        sump()
    return sum


sum = 0
print(sump())
print('')
