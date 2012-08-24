#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       untitled.py
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
#       
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.


'''
from math import sqrt

def sq(x):return x*x

def checkPyth(a,b,c):
	if sq(a)+sq(b)==sq(int(c)):
		return True
	else:
		return False

def pythCount(butt):
	a=1
	b=1
	c=1
	while c<butt:
		if a+b+c == butt:
			#print a,b,c,a*b*c,checkPyth(a,b,c)
			#raw_input()
			if checkPyth(a,b,c)==True:
				print a,b,c,a*b*c,checkPyth(a,b,c)
				return a,b,c,a*b*c,checkPyth(a,b,c)
				exit()
			else:
				a=a+1
		else:
			a=a+1
			if a==butt:
				b=b+1
				a=1
				if b==butt:
					c=c+1
					a=1
					b=1
				

pythCount(100)












''' Junk code for now. I'll paste the data in later. 
def main():
	
	return 0

if __name__ == '__main__':
	main()
'''























