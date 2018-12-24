print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print('Üdvözöllek az egyszerû számológépben!                                              Ver. 1.0')
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print(
    'Help: Eloszor add meg, hogy mit szeretnel(Osszeadas, Kivonas, Szorzas, Osztas, Hatvanyozas ) \n majd add meg a tagokat(Ha nincs tobb tag,akkor irj 0 -t! ')
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print('')

All = input('Osszeadas(1), Kivonas(2), Szorzas(3), Osztas(4), Hatvanyozas(5): ')
All2 = 0

print('')
num1 = int(input('Add meg az elsõ tagot: '))
num2 = int(input('Add meg a második tagot: '))
print('')

if All == "1":
    All2 = int(num1) + int(num2)
    print(num1, '+', num2, '=', All2)

if All == "2":
    All2 = int(num1) - int(num2)
    print(num1, '-', num2, '=', All2)

if All == "3":
    All2 = int(num1) * int(num2)
    print(num1, '*', num2, '=', All2)

if All == "4":
    All2 = int(num1) / int(num2)
    print(num1, '/', num2, '=', All2)

if All == "5":
    All2 = int(num1) ** int(num2)
    print(num1, '**', num2, '=', All2)

print('')
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

nothing = input('')