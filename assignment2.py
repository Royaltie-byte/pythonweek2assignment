"""Create an empty list called my_list.
Append the following elements to my_list: 10, 20, 30, 40.
Insert the value 15 at the second position in the list.
Extend my_list with another list: [50, 60, 70].
Remove the last element from my_list.
Sort my_list in ascending order.
Find and print the index of the value 30 in my_list."""
my_list=[]
numbers=[10, 20, 30, 40]
for number in numbers:
    my_list.append(number)
my_list.insert(1,15)
my_list.extend([50, 60, 70])

del my_list[-1]

my_list.sort()

print(f"The index of the value 30 in my list is : {my_list.index(30)}")

