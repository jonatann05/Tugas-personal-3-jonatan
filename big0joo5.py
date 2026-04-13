def printUnorderedPairs(arrayA, arrayB):            ## bikin fungsi buat nampilin pasangan dari 2 array
    for i in range(len(arrayA)):                    ## looping indeks arrayA
        for j in range(len(arrayB)):                ## looping indeks arrayB
            for k in range(0,100000):               ## looping tambahan biar ngeprint berkali-kali (super banyak)
                print(str(arrayA[i]) + "," + str(arrayB[j]))                ## tampilkan pasangan elemen berulang

arrayA = [1,2,3]        ## array pertama
arrayB = [4,5]          ## array kedua

printUnorderedPairs(arrayA, arrayB)     ## jalankan fungsi