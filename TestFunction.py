# Import ทั้งหมดทุกฟังก์ชั่นใน module
import Number
# Import บาง Module
from Number import calculate
# Import แบบเรียกทุกฟังก์ชั่นโดยคำสั่ง from
from Number import  *
# Import และตั้งชื่อนามแฝง
from Number import calculate as cal
from Number import number as num

# ทดสอบ import module ที่มากับ Python
import this
import os
import math


#print(number.factorial(5))
#print(number.fibonacci(100))

#print(calculate.plus(5,8))


print(cal.plus(8, 9))
print(num.factorial(5))
print(num.fibonacci(100))
print(os.cpu_count())
print(math.log10(10))


