list_1=['red','blue','pink','yellow','white','green']
print("colors of list one:",list_1)
list_2=['brown','grey','pink','red','orange','white']

print("colors of list two:"list_2)
print("colors from colors_list 1 not contained in color list 2:")
for color in list_1:
    if color in list_2:
        continue
    else:
        print(color)
