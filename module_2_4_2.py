# ДЗ moodule_2_4 Цикл for.
# =================================
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # 1-й список
print(numbers)
primes = []  # 2-й список простые числа
not_primes = []  # 3-й список не простые числа
#for i in range(2, len(numbers) + 1):
for i in numbers[1:]:
    is_prime = True
    for j in range(2, (i)):  # Делители для чисел первого цикла
        a = i % j
        if a == 0:
            is_prime = False
    if is_prime == True:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)
