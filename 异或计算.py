def xor(a,b):
    c =[]
    for i in range(len(a)):
        c.append(str(int(a[i])^int(b[i])))
    return ''.join(c)


a = '100101'
b = '000000'
result = xor(a,b)
print(result)