
"""
Sadece kenarlari bilinen ucgenin alani hesaplama yontemi >> 

a, b ve c ucgenin kenar uzunluklari ve s 
ucgenin cevre uzunluğunun yarisi olmak uzere;

Alan = √(s(s-a)(s-b)(s-c)) formuluyle hesaplanir.

"""

print('Method for calculating the area of a triangle with only known sides')

from math import sqrt

while True:
        try:
                a = float(input("birinci kenar: "))
                b = float(input("ikinci kenar: "))
                c = float(input("ucuncu kenar: "))

                if (a < b+c) and (b < a+c) and (c < b+a):

                        s = (a + b + c) * 0.5 
                        alan_ucgen = sqrt(s * (s-a) * (s-b) * (s-c))
                        alan_ucgen = float(alan_ucgen)

                        cevre_ucgen = a+b+c
                        print(f'sekilin cevresi: {cevre_ucgen}\nSeklin alani: {alan_ucgen}')
                        break
        except ValueError:
                print('It is not a triangle. Try again!')
print('*** ' *10)

# bir ileriki asamada kordinatlari verilen veya sadece kenarlari verilen bir n kenarli ic bukey veya dis bukey bir cismin alanini bulmaya calisacagiz
# arayuz ile tercih menusu olusturulacak (kenar mi yoksa kordinat mi diye.)