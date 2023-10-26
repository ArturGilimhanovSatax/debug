#ЗАДАНИЕ 1
def neg(x):
	if x < 0:
		return 'Число отрицательно'
	else:
		return 'Число не отрицательно'


#ЗАДАНИЕ 2
def chet(n):
	if n % 2 == 0:
		return 'Число четное'
	elif n % 2 == 1:
		return 'Число не четное'


#ЗАДАНИЕ 3
def cnt(c):
	return len(str(c))


#ЗАДАНИЕ 4
def sumA(numList):
    sumB = 0
    for i in numList:
        sumB = sumB + i
    return sumB

print(sumA([1, 2, 3, 4, 5]))