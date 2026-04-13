def decimal_to_binary(n):       ## bikin fungsi buat ubah angka desimal ke biner
    if n == 0:                  ## kalau angkanya udah 0, berhenti di sini
        return 0                ## hasil akhirnya 0
    
    return n % 2 + 10 * decimal_to_binary(n // 2)       ## ambil sisa bagi 2 terus susun jadi angka biner pakai rekursi

print(decimal_to_binary(10))        ## contoh jalanin fungsi buat angka 10