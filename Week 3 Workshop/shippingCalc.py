
cost = []
items = []
all_items = []

total = int
total = 0


numitems = int(input('Enter the number of items you will be calculating'))


for i in range(0, numitems, 1):
    items.append(i)
    items[i] = int(input('please enter how much each item is (from start to finish)'))
    total = items[i] + total

print(items)
print('Your total shipping cost is', total)



#all_items.append('1')
#items.append('hello')
#items.append('world')
#all_items.append(items)

#print(all_items[1][0])