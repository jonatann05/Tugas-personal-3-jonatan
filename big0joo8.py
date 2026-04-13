def factorial(n):
    if n < 0:                 # kalau n negatif, nggak valid buat faktorial
        return -1             # kasih tanda error
    elif n == 0:              # base case: 0! itu 1
        return 1              # balikin 1
    else:
        return n * factorial(n-1)  # hitung faktorial pakai rekursi

print(factorial(3))           # coba jalanin fungsi