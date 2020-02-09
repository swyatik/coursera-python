def list_int_str(list_int):
    y = []
    for i in list_int:
        y.append(str(i))
    return y

x = [1,2,3,4,5,6,7,8,9]

y = list_int_str(x)

print('type x[1]:', type(x[1]))
print('type y[1]:', type(y[1]))
