# ЗАДАНИЕ 1
date = '2025-12-31'

# Разделяем date на год, месяц и день, а также задаем split на -
y, m, d = date.split('-')

# Меняем местами ymd на dmy
date_tuple = (d, m, y)
print(date_tuple)






# ЗАДАНИЕ 2
numbers = ['1', '2', '3', '4', '5']

# Создаем переменную str, в которой суммируются все числа в списке (перед этим создаем переменную num в int чтобы мы могли делать математические вычисления с числами в списке)
nums_sum = sum(int(num) for num in numbers)
print(nums_sum)






# ЗАДАНИЕ 3
nums = [1, 2, 3, 4, 5, 6]

# Делим длинну nums на пополам т.е. 1,2,3|4,5,6
half = len(nums) // 2

# Делим nums на две части - one и two
one_half = nums[:half]
two_half = nums[half:]

# Сумма чисел первой половины и сумма чисел второй половины
sum_one_half = sum(one_half)
sum_two_half = sum(two_half)

# Деление первого числа на второе
res = sum_one_half / sum_two_half
print(res)






# Задание 4
dct1 = {
  'a': 1,
  'b': 2,
}
dct2 = {
  'c': 3,
  'd': 4,
}

# Создаем dct3 и объединяем два словаря в один - dct3
dct3 = {}
dct3.update(dct1)
dct3.update(dct2)
print(dct3)






#Задание 5
dct = {
  1: {
    1: 11,
    2: 12,
    3: 13,
  },
  2: {
    1: 21,
    2: 22,
    3: 23,
  },
  3: {
    1: 24,
    2: 25,
    3: 26,
  },
}

s = 0

for dct1 in dct.values():
  for values in dct1.values():
    s += values

print(s)