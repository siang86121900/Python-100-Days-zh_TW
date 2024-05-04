"""
英製單位英寸和公製單位厘米互換

Version: 0.1
Author: 駱昊
Date: 2018-02-28
"""

value = float(input('請輸入長度: '))
unit = input('請輸入單位: ')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
    print('請輸入有效的單位')
