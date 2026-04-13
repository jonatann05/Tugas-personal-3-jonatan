def gcd(a, b):      ## bikin fungsi buat cari FPB (Greatest Common Divisor)
    if b == 0:      ## kalau b udah 0, berarti ketemu hasil akhirnya
        return a    ## a itu jadi FPB-nya
    
    return gcd(b, a % b)        ## pakai cara rekursif (algoritma Euclid) sampai b = 0

print(gcd(8, 12))       ## contoh jalanin fungsi buat cari FPB 8 dan 12