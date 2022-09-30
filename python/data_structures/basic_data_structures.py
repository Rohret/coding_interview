
# list, often use to mimic a stack or a queue

stack = []
stack.append(1)
stack.append(2)

queue = []
queue.append(1)
queue.append(2)

pop_elem = stack.pop()
queue_elem = queue.pop(0)

print(pop_elem)
print(queue_elem)
# list comprehension, instead of making loops and other things..
# newlist = [expression for item in iterable if condition == True]

lst = [1,2,3,4,5,6,7,8]

even_lst = [x for x in lst if x % 2 == 0]

sqr_lst = [x ** 2 for x in lst]

print(sqr_lst)
print(even_lst)



# set, can be used to get the intersection or union

arr1 = [1,2,3,4,5]
arr2 = [5,6,7,8,9]

set1 = set(arr1)
set2 = set(arr2)

intersection = set1 & set2
intersection1 = set.intersection(set1,set2)
union = set.union(set1,set2)

print(intersection,intersection1, union)

# dict, often used for hashtable. Time to look up a valie for a key is O(1) 

ages = dict()

ages["Adam"] = 24
ages["Erik"] = 19

for key,value in ages.items():
    print(key,value)







