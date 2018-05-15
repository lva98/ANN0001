#!/usr/local/bin/python
# coding: latin-1
# -*- coding: utf-8 -*-
import math
import sys

def funcaoA(flag, x):
	if flag:
		return -math.atan(x-1)

	return x + math.atan(x-1)


def funcaoB(flag, x):
	e = math.exp(1)
	if flag:
		return (((e**x)*(x**(5.0/3.0)))/9.0)**(1.0/2.0)
	return 9 * (x ** (1/3)) - e**x

def funcaoC(flag, x):
	e = math.exp(1)
	if flag:
		return (math.log(6.0*math.log(x,e),e))/math.log(2,e)
	return 2**x - 6.0*math.log(x,e)


def funcaoIteracao(func, x_ite):
	print('{:^9}|{:^16}|{:^16}|{:^16}|{:^16}|'.format('iteracao', 'x', 'Eabs', 'Erel', 'f(x)'))

	i = 0

	while True:
		_x   = func(1, x_ite)
		fx   = func(0, _x)
		eabs = abs(_x - x_ite)
		erel = abs(_x - x_ite)/abs(_x)
		print('{:^9}|{:^16.12f}|{:^16.10f}|{:^16.12f}|{:^16.12f}|'.format(i, _x, eabs, erel, fx))

		if(eabs < 10**-10):
			break

		x_ite = _x
		i     = i + 1

	print('Obs.: Eabs refere-se ao erro absoluto relativo')

def main(argv):
	arg = sys.argv

	if(len(arg) != 3 and len(arg) != 2):
		print("Duvidas? Use \"Help\" como passagem de parametro")
	else:
		if(arg[1] == 'a'):
			print('f(x) = x + arctg(x - 1)')
			funcaoIteracao(funcaoA, 2)
		elif(arg[1] == 'b'):
			print('f(x) = 9*(x ** 1/3) - e ** x')
			if(not(float(argv[2]) > 0 and float(argv[2]) <= 1)):
				print('f(x) nao converge para ponto inicial solicitado')
				exit()
			funcaoIteracao(funcaoB, float(argv[2]))
		elif(arg[1] == 'c'):
			print('f(x) = 2**x - 6*ln(x)')
			if(not(float(argv[2]) > 0)):
				print('f(x) nao converge para ponto inicial solicitado')
				exit()
			funcaoIteracao(funcaoC, float(argv[2]))
		else:
			print('Implementacao trabalho pratico de Analise Numerica ANN0001-BCC/2018.1\n')
			print('Primeiro argumento:')
			print('Escolha a funcao para anlise (a, b, c)')
			print('    (a) f(x) = x + arctg(x - 1), converge para -infinito,+infinito')
			print('    (b) f(x) = 9*(x ^ 1/3) - e ** x, converge para x > 0 e x <= 1')
			print('    (c) f(x) = 2^x - 6*ln(x), converge para x > 0')
			print('\nSegundo argumento:')
			print('Ponto inicial da iteracao, devera ser um valor dentro dos limites de convergencia')
			print('\nExemplos de execucao')
			print('python ann.py a 0')
			print('python ann.py b 1')

	return 0


if __name__ == "__main__":
    main(sys.argv)

#https://drive.google.com/file/d/1nJjc1eSr-nAPyrYNiMBXuMkAT8fh65Nm/view
