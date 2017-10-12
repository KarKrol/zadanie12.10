def check( toCheck, n):
    b = 0
    e = len(toCheck) - 1
    toCheck = quickSort(toCheck)
    while b != e:
        if toCheck[e] > n or toCheck[e] + toCheck[b] > n:
            e -= 1
        if toCheck[e] + toCheck[b] < n:
            b += 1
        if toCheck[e] + toCheck[b] == n:
            return True
    return False

def quickSort(tabl):
    tab = tabl[:]
    mniejsze = []
    rowne = []
    wieksze = []
    if len(tab) > 1:
        pivot = tab[0]
        for x in tab:
            if x < pivot:
                mniejsze.append(x)
            if x == pivot:
                rowne.append(x)
            if x > pivot:
                wieksze.append(x)
        return quickSort(mniejsze)+rowne+quickSort(wieksze)
    else:
        return tab


print check([1,2,3,5,4,3,6,7,10,4,2], 4)
print check([1,2,3,5,4,3,6,7,10,4,2], 30)
print check([1,2,3,5,4,3,6,7,10,4,2], 10)
