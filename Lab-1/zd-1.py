numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

numb = numbers

numb[4] = 0

summ = sum(numb)
lenn = len(numb)
aver = summ/lenn

numbers[4] = aver

print("Измененный список:", numbers)
