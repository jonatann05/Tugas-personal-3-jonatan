def printUnorderedPairs(array):         ## bikin fungsi buat nampilin pasangan tanpa ada yang keulang
    for i in range(0,len(array)):       ## looping indeks pertama dari 0 sampai akhir array
        for j in range(i+1,len(array)): ## looping indeks kedua, mulai dari setelah i biar nggak double
            print(str(array[i]) + "," + str(array[j]))  ## tampilkan pasangan elemen

array = [1, 2, 3]       ## bikin array
printUnorderedPairs(array)   ## panggil fungsi