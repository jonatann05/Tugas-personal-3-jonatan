def powersOf2(n):
    # print("n:"+str(n))          # debug: lihat nilai n
    if n < 1:                    # kalau n kurang dari 1, stop
        return 0                 # balikin 0
    elif n == 1:                 # base case: kalau n = 1
        print(1)                 # tampilkan 1
        return 1                 # balikin 1
    else:
        prev = powersOf2(int(n/2))   # panggil lagi dengan n dibagi 2
        # print("prev:"+str(prev))   # debug hasil sebelumnya
        print(prev)                  # tampilkan hasil sebelumnya
        curr = prev*2                # kali 2 buat nilai berikutnya
        print(curr)                 # tampilkan hasil sekarang
        return curr                 # balikin hasil sekarang

powersOf2(50)                      # coba jalanin fungsi