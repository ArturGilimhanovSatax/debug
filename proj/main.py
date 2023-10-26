#1111111111111111111111111111
try:
    a = int(input())
    b = int(input())
    if a < 0 or b < 0:
        raise Exception('Введите положительные числа')
    print(a/b)
except ValueError as ve:
    print('Введите числа', ve)
except Exception as e:
    print(e)


print('Конец кода')

#22222222222222222222222222222
import random

sum = 0
for i in range(10):
    print(i)
    sum += random.randint(0, 10)
print(sum)

def sum2(x, y):
    print(x + y)

#333333333333333333333333333333
def pos_or_neg(x):

	try:

		if x > 0:
			return 'positive'
		elif x < 0:
			return 'negative'
		else:
			return 'zero'
	except:
		return('Error')