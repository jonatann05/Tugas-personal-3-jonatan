def sum_of_digits(n):    ## bikin fungsi buat jumlahin semua digit angka
    if n == 0:    ## kalau angkanya udah 0, berhenti (base case)
        return 0        ## balikin 0 karena udah nggak ada angka lagi
    
    return n % 10 + sum_of_digits(n // 10)  ## ambil digit terakhir, terus tambahin hasil dari sisa angkanya (rekursif)

print(sum_of_digits(9))  ## contoh jalanin fungsi