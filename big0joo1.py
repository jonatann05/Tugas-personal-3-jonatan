def foo(array):     ## bikin fungsi yang nerima input berupa list/array
    sum = 0         ## siapin variabel buat nampung hasil penjumlahan
    product = 1     ## siapin variabel buat nampung hasil perkalian
    
    for i in array:     ## looping tiap angka di dalam array
        sum += i        ## tambahin semua angka ke total sum
    
    for i in array:         ## looping lagi buat perkalian
        product *= i            ## kaliin semua angka ke product
    
    print("Sum = "+str(sum)+", Product = "+str(product))            ## tampilkan hasil jumlah & kali

ar1 = [1,2,3,4]         ## bikin array
foo(ar1)                ## panggil fungsi dengan array