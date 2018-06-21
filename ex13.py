"""

打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

Version: 0.1
Author: chary
Date: 2018-06-20

"""


row = int (input('请输入行数:'))
for i in range (row):
	for j in range(i+1):
		print ('*',end='')
	print ()

for i in range (row):
	for k in range(row):
		if k<row -i -1:
			print (' ',end='')
		else:
			print('*', end='')
	print ()


for i in range (row):
	for m in range(row-i-1):
			print (' ',end='')
	for m in range(2*i+1):
			print('*', end='')
	print ()
