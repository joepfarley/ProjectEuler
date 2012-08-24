#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       lcm.py
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




def lcm(x,y):
	gcf=0
	lcm=0
	if x>y:
		dividend=x
		divisor=y
	else:
		dividend=y
		divisor=x
	def find_gcf(dividend,divisor):
		reminder=-1
		while reminder !=0:
			qoutient=dividend/divisor
			reminder=dividend%divisor
			if reminder !=0:
				dividend=divisor
				divisor=reminder
		gcf=divisor
		return divisor

	def find_lcm(x,y,gcf):
		lcm=(x*y)/gcf
		return lcm

	gcf=find_gcf(dividend,divisor)
	lcm=find_lcm(x,y,gcf)		
	return lcm
	
def lcmFactorial(x):
	b=x
	for i in range(x,1,-1):
		print lcm(b,i)
		b=lcm(b,i)
	print b
	return b

lcmFactorial(10)

