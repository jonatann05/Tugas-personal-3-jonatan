def printUnorderedPairs(arrayA, arrayB):        ## bikin fungsi buat nampilin pasangan dari 2 array
    for i in range(len(arrayA)):                ## looping indeks arrayA
        for j in range(len(arrayB)):            ## looping indeks arrayB
            if arrayA[i] < arrayB[j]:           ## cek kalau elemen A lebih kecil dari elemen B
                print(str(arrayA[i]) + "," + str(arrayB[j]))            ## tampilkan pasangan yang lolos syarat

arrayA = [1,2,3,4,5]        ## array pertama
arrayB = [2,6,7,8]         ## array kedua

printUnorderedPairs(arrayA, arrayB)         ## jalanin fungsi