import pytest

from proj.first import neg
from proj.first import chet
from proj.first import cnt
from proj.first import lst


#ЗАДАНИЕ 1 ПРОВЕРКА
def test_neg_p():
	assert neg(10) == 'Число не отрицательно'

def test_neg_n():
	assert neg(-10) == 'Число отрицательно'

def test_neg_z():
	assert neg(0) == 'Число не отрицательно'

def test_str():
	with pytest.raises(TypeError):
		neg('asfasfsdf')



#ЗАДАНИЕ 2 ПРОВЕРКА
def test_chet_true():
	assert chet(6) == 'Число четное'

def test_chet_false():
	assert chet(9) == 'Число не четное'



#ЗАДАНИЕ 3 ПРОВЕРКА
def test_cnt_check():
	assert cnt(3642) == 4