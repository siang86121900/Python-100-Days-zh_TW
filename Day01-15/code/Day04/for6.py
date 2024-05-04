"""
列印各種三角形圖案

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
Author: 駱昊
Date: 2018-03-01
"""

row = int(input('請輸入行數: '))
for i in range(row):
    for j in range(i + 1):
        print('*', end='')
    print()
print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()
print()

for i in range(row):
    for j in range(row - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()
print()

for i in range(row, 0, -1): 
    for j in range(i):
        print('*', end='')
    print()
print()

for i in range(row):
    for j in range(row):
        if j < i:
            print(' ', end='')
        else:
            print('*', end='')
    print()
print()

for i in range(row, 0, -1):  # 倒數迴圈，從 row 開始倒數到 1
    for j in range(row - i):  # 輸出空白，隨著行數減少而增加空白數量
        print(' ', end='')
    for j in range(2 * i - 1):  # 輸出星號，每行星號數量隨著行數減少而減少
        print('*', end='')
    print()
print()


for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()