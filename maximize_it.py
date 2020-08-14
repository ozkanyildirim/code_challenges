credentials = input('Enter K and M values: ').split()
lists  = []
crd = list(map(int,credentials))
for i in range(crd[0]):
    lst = input('input list values: ').split()
    lst_i = list(map(int,lst))
    lists.append(lst_i[1:])
from itertools import product
kartezyen = list(product(*lists))    
def func(nums):
    return sum(x*x for x in nums) % crd[1]
print(max(list(map(func, kartezyen))))
