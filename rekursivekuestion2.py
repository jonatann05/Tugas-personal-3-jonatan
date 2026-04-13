def power(x, n):         ## bikin fungsi buat hitung pangkat
    if n == 0:           ## kalau pangkatnya 0, stop di sini
        return 1         ## hasilnya selalu 1 kalau n = 0
    return x * power(x, n - 1)      ## kaliin x terus secara rekursif sampai n habis

print(power(2, 4))      ## contoh hasil 2 pangkat 4