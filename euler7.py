#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       euler7.py
#       
#       Copyright 2012 joe farely <joe@demiplane>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       


"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?


first step:
Check if number is prime 
	check by calulating 1 to square root of number
"""
from math import sqrt
from math import fabs


def isPrime(number):
	if number==2:return "prime"
	if number % 2==0:return "not prime"
	for i in range(3,int(sqrt(number)+1),2):
		if number % i==0:
			#print number,"is divisible by ",i
			return "not prime"	
	return "prime"
	
	
def listPrime(number): #number should end up being 10001
	prime=[]
	for i in range(2,number+1):
		if isPrime(i)=="prime":
			prime.append(i)
	return prime


def primesToNumber(number):
	i=2
	p=0
	while p != number:
		if isPrime(i)=="prime":
			p=p+1
			print p,i
		else:
			pass
		i=i+1
			


