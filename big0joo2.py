def printPairs(array):          ## bikin fungsi buat nampilin semua pasangan angka di array
    for i in array:             ## looping pertama buat ambil tiap elemen
        for j in array:         ## looping kedua buat dipasangkan sama elemen lain
            print(str(i)+","+str(j))  ## tampilkan semua kombinasi pasangan

array = [1, 2, 3]               ## bikin array sederhana
printPairs(array)               ## jalankan fungsi