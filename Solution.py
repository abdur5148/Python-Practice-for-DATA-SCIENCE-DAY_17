dict1 = {}
var = input("Enter String : ")
for i in var.split():
    dict1[i] = dict1.get(i, 0)+1
for j in sorted(dict1):
    print("{} : {}" .format(j, dict1[j]))
