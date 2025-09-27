from copy import deepcopy

numbers=[7, 2, 5]
numbers.append(4)
numbers.insert(1,10)
numbers.extend([1, 1, 1])
numbers.remove(7)
pop1=numbers.pop()
numbers.sort()
numbers.reverse()
print(numbers.count(2))
print(numbers.index(1))
a1=numbers.copy()
a2=deepcopy(numbers)
numbers.clear()
print(numbers, a1, a2, pop1)