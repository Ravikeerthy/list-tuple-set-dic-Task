# List
task_list = [10,20,30,40,50,60,70,80]


for index, value in enumerate(task_list):
    print(f"Index {index} : Value: {value}")

# Tuple

task_tuple1 = (1,2,3,4,5,6,7,8,9)
task_tuple2 = ('a', 'b', 'c','d', 'e', 'f', 'g')

for num, char in zip(task_tuple1, task_tuple2):
    print(f"Tuple-1:{num}, Tuple-2:{char}")

iter_tuple = iter(task_tuple1)
while True:
    try:
        print(next(iter_tuple))
    except StopIteration:
        break


# Set

task_set = {10,20,30,40,50,60,70}

squared_Set = {x ** 2 for x in task_set}
print("Squared Set: ", squared_Set)

task_set_list = list(task_set)
i=0
while i<len(task_set_list):
    print((lambda x: x*2)(task_set_list[i]))
    i+=1


# Dictionary

task_dict = {'a':5, 'b':10, 'c': 8 ,'d': 5}

for key, value in task_dict.items():
    print(f"Key: {key}, Values: {value}")

sorted_dict = dict(sorted(task_dict.items(), key=lambda item: item[1]))
print("Sorted Dictionary: ", sorted_dict)

keys_list = list(task_dict.keys())
i=0
while i< len(keys_list):
    key = keys_list[i]
    print(f"key:{key}, value: {task_dict[key]}")
    i+=1


