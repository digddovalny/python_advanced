inp_val = -1
MIN_INP = 0
MAX_INP = 100000

count = 0

while not (MIN_INP <= inp_val <= MAX_INP):
    inp_val = int(input(f"Введите число для проверки в диапазоне от {MIN_INP} до {MAX_INP}: "))

for i in range(2, inp_val // 2 + 1):
    if (inp_val % i == 0):
        count += 1
if count <= 0:
    print("Число простое")
else:
    print("Число составное")
