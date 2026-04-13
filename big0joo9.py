def allFib(n):
    for i in range(n):                         # looping dari 0 sampai n-1
        print(str(i)+":, " + str(fib(i)))      # tampilkan indeks + hasil fibonacci

def fib(n):
    if n <= 0:            # kalau n <= 0, hasilnya 0
        return 0          # base case
    elif n == 1:          # kalau n = 1, hasilnya 1
        return 1          # base case
    return fib(n-1) + fib(n-2)  # hitung fibonacci pakai rekursi

allFib(4)                 # jalanin fungsi sampai n = 4