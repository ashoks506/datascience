# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 10:31:12 2018

@author: asatharla
"""
#https://www.programiz.com/python-programming/matrix
#Create a matrix in python
# a is 2-D matrix with integers
a = [['Roy',80,75,85,90,95],
     ['John',75,80,75,85,100],
     ['Dave',80,80,80,90,95]]

#b is a nested list but not a matrix
b= [['Roy',80,75,85,90,95],
    ['John',75,80,75],
    ['Dave',80,80,80,90,95]]

#Create a dynamic matrix using for loop in python

n = 3
m = 4
a1 = [0] * n
for i in range(n):
    a1[i] = [i] * m
print(a1)

#Create a matrix using numpy in pyhton

from numpy import * 

x = range(16)

x = reshape(x,(4,4)) 

print(x) 


#Accessing elements of the matrix in python by using list index
# a is 2-D matrix with integers
a = [['Roy',80,75,85,90,95],
     ['John',75,80,75,85,100],
     ['Dave',80,80,80,90,95]]

print(a[0])

print(a[0][1])

print(a[1][2])

#Accessing elements of the matrix in python by using negative list index

a = [['Roy',80,75,85,90,95],
     ['John',75,80,75,85,100],
     ['Dave',80,80,80,90,95]]
	
print(a[-1]) 
	
print(a[-1][-2]) 

print(a[-2][-3]) 

#Slicing a matrix in python using colon(:)  and numpy
a = array([['Roy',80,75,85,90,95],
           ['John',75,80,75,85,100],
           ['Dave',80,80,80,90,95]])
print(a[:3,[0,1]])

#Change elements of a matrix in python
a = [['Roy',80,75,85,90,95],
     ['John',75,80,75,85,100],
     ['Dave',80,80,80,90,95]]

b=a[0]
print(b)

b[1]=75
print(b)

a[2]=['Sam',82,79,88,97,99]
print(a)

a[0][4]=95
print(a)


#Adding a new row in the matrix in python using append()

a = array([['Roy',80,75,85,90,95],
	       ['John',75,80,75,85,100],
	       ['Dave',80,80,80,90,95]])

a= append(a,[['Sam',82,79,88,97,99]],0)
#here 0 is axis that represents the dimensions where 0 stands for row and 1 stands for column

print(a)


#Add a new column in the matrix for economics marks using insert()
a = array([['Roy',80,75,85,90,95],
      ['John',75,80,75,85,100],
      ['Dave',80,80,80,90,95]]) 

a= insert(a,[6],[[73],[80],[85]],axis=1) 
#here axis represents the dimensions where 0 stands for row and 1 stands for column 

print(a) 


# Add a row in the matrix in python using +
a=[['Roy',80,75,85,90,95],
    ['John',75,80,75,85,100],
    ['Dave',80,80,80,90,95]]

a= a+ [['Sam',82,79,88,97,99]]

print(a)

#Delete a row of a matrix in python using delete from numpy
a = array([['Roy',80,75,85,90,95],
      ['John',75,80,75,85,100],
      ['Dave',80,80,80,90,95]])

a= delete(a,[1],0)

print(a)






