list1 = list(map(int, input("List 1: ").split()))
list2 = list(map(int, input("List 2: ").split()))

print("Same length:", len(list1) == len(list2))
print("Same sum:", sum(list1) == sum(list2))
print("Common elements:", bool(set(list1) & set(list2)))
