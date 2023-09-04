"""////////////////////////////////////////////////////////////////////////////
/решение системы линейных уравнений методом гауса с выбором главных элементов/
/////////////////////////////////////////////////////////////////////////////"""


from configparser import RawConfigParser
from re import search
from tokenize import Double
import numpy 
value = 0 



n = int(input('введите размерность матрицы'))
input_massiv_a = numpy.zeros((n,n)) #матрица коэфицентов
input_massiv_b = numpy.zeros((n)) #массив свободных членов
input_massiv_x = numpy.zeros((n)) #массив иксов
input_massiv_v = numpy.zeros((n)) # массив ответов
input_massiv_c = numpy.zeros((n,n)) #матрица коэфицентов копия
input_massiv_z = numpy.zeros([n]) #массив свободных членов копия
split = []
columcell = -1
rewcell = -1
gog = 0
Filename = str('coefficients.txt') # файл с коэфицентами 

"""////////////////////////////////////////////////////////////////////////////
//////////////////////функция считывания матрицы коэфицентов//////////////////
/////////////////////////////////////////////////////////////////////////////"""


def MatrixReader(Filename): 
    Filename = open(Filename, "r")
    for i in range(n):
        s = Filename.readline()
        spli = s.split(" ")
        for  j in range (n):
            input_massiv_a [i,j] = numpy.double(spli[j])
            input_massiv_c [i,j] = numpy.double(spli[j])
        # создаём копию для проверки ответа
        input_massiv_b[i] = numpy.double(spli[n])
        input_massiv_z[i] = numpy.double(spli[n])

    print(input_massiv_b) 
    Filename.close

"""////////////////////////////////////////////////////////////////////////////
///////////////функция осуществляет поиск максимального элимента//////////////
/////////////////////////////////////////////////////////////////////////////"""

def SearchMax(input_massiv_a): 
    global index
    cell = 0
    for i in range(value, n):
        for j in range(value, n):
          if (abs(input_massiv_a[i,j]) > cell):
                cell = abs(input_massiv_a[i,j])
                rewcell = i
                columcell = j
    index = numpy.array([rewcell,columcell])
    
"""////////////////////////////////////////////////////////////////////////////
////////////////////функция меняет столбцы местами////////////////////////////
/////////////////////////////////////////////////////////////////////////////"""

def columc(input_massiv_a):
    input_massiv_a[:,[index[1],gog]] = input_massiv_a[:,[gog,index[1]]]
    r = input_massiv_x[gog]
    input_massiv_x[gog] = input_massiv_x[index[1]]
    input_massiv_x[index[1]] = r
    

    
"""////////////////////////////////////////////////////////////////////////////
////////////////////////функция меняет местами строки/////////////////////////
/////////////////////////////////////////////////////////////////////////////"""
    
def Row(input_massiv_a): 
    input_massiv_a[[index[0],gog]] = input_massiv_a[[gog,index[0]]]
    input_massiv_b[[index[0],gog]] = input_massiv_b[[gog,index[0]]]
    
    
"""////////////////////////////////////////////////////////////////////////////
////////////////////////функция меняет первый элемент на 1////////////////////
/////////////////////////////////////////////////////////////////////////////"""
    
def One(input_massiv_a,input_massiv_b):
    num = input_massiv_a[gog,gog]
    for i in range(n):
        input_massiv_a[gog,i]= input_massiv_a[gog,i] / num 
    input_massiv_b[gog] = input_massiv_b[gog] / num
        
"""////////////////////////////////////////////////////////////////////////////
////////////////////////функция меняет элементы под 1 на 0////////////////////
/////////////////////////////////////////////////////////////////////////////"""

def zero(input_massiv_a,input_massiv_b):
    for i in range(gog + 1,n):
        num = input_massiv_a[i,gog]
        for j in range(n):
            input_massiv_a[i,j]= input_massiv_a[i,j] / num - input_massiv_a[gog,j]
        input_massiv_b[i] = input_massiv_b[i] / num - input_massiv_b[gog]
    
"""////////////////////////////////////////////////////////////////////////////
/////////////функция осуществляет обратный ход для вычисления x///////////////
/////////////////////////////////////////////////////////////////////////////"""

def revers(input_massiv_a):
    for i in range (n-1,-1,-1):
        sum = input_massiv_b[i]
        for j in range(i+1,n):
            sum = sum - input_massiv_a[i,j] * input_massiv_v[j]
        input_massiv_v[i] = sum/input_massiv_a[i,i]

"""////////////////////////////////////////////////////////////////////////////
/////////////функция осуществляет проверку найденных значений/////////////////
/////////////////////////////////////////////////////////////////////////////"""

def CheckAnsver(input_massiv_a): 
    print("проверка ответа")
    for i in range(n):
                sum = 0
                for j in range(n):
                    sum = sum + input_massiv_c[i,j] * input_massiv_v[j]
                sum = round(sum,2)
                    
                print( sum, '=', input_massiv_z[i])
    print(" ")
        

if __name__ == "__main__": 
    MatrixReader(Filename)
    print('Исходная матрица')
    print(input_massiv_a)
    print('массив свободных членов')
    print(input_massiv_b)
    for i in range(n):
        input_massiv_x[i] =i+1
    for gog in range (n):
        print('итерация', gog + 1)
        SearchMax(input_massiv_a)
        Row(input_massiv_a)
        columc(input_massiv_a)
        One(input_massiv_a,input_massiv_b)
        zero(input_massiv_a,input_massiv_b)
        print(input_massiv_a)
        print('массив свободных членов')
        print(input_massiv_b)
        revers(input_massiv_a)
        
       
    
    for i in range(n):
        j = i
        while ((j<n-1) and (input_massiv_x[j]!= i+1)):
            j=j+1
        if (j != i):
            tem = input_massiv_x[i]
            temp = input_massiv_v[i]
            input_massiv_x[i] = input_massiv_x[j]
            input_massiv_v[i] = input_massiv_v[j]
            input_massiv_x[j] = tem
            input_massiv_v[j] = temp
        print("x" , input_massiv_x[i],  "=", round(input_massiv_v[i],1))
    CheckAnsver(input_massiv_a)
    









       


