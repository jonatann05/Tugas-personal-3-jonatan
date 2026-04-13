def reverse(array):
    if not array:                 # cek dulu apakah array kosong atau nggak
        return array              # kalau kosong, ya langsung balik aja

    for i in range(len(array)//2):  # jalanin loop sampai tengah array aja
        other = len(array) - i - 1  # cari posisi lawan dari belakang
        array[i], array[other] = array[other], array[i]  # tuker elemen depan sama belakang

    return array                  # balikin array yang udah dibalik

arrayA = [1,2,3,4,5]              # bikin array
print(reverse(arrayA))            # panggil fungsi dan print hasilnya