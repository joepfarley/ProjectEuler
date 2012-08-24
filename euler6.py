#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       Sums and Squares.py
#       
#       Copyright 2012 Joe Farley <admin@joepfarley.com>
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
#       

"""
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten 
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one
 hundred natural numbers and the square of the sum.
 
 Let's define the steps
 
 easy stuff
	Create list 
	put in variable 
	sum up list 
	square it
 
 hard stuff
	square all the numbers between 1 and 100
	add them together
"""
from math import pow

def main(naturalNumber):
	
	def getList():
		li = []
		for i in range(1,naturalNumber+1):li.append(i)
		#print li
		return li
	
	def sumList():
		SUM = sum(getList())
		print SUM, "= sum of numbers."
		return SUM
		
	def squareSum():
		square = pow(sumList(),2)
		print square,"= square of sum."
		return square
		
	def squareEach():
		x=0
		for i in range(1,naturalNumber+1):
			x=x+pow(i,2)
			#print i,"squared =",pow(i,2),"total",x
		print x, "= sum of squares"
		return x
	
	return squareSum()-squareEach()

if __name__ == '__main__':
	x=input("Please enter a number to run the calculation: ")
	print main(x), "= square of sums minus sum of squares."

