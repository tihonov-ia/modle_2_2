first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second and first == third:
    print( 3, '- три числа равны между собой')
elif first == second or first == third or second == third:
    print(2, '- два числа равны между собой')
else:
    print(int(not(1)), '- не обнаружено равных между собой чисел')