class InsertionSort:
    def run(self, arr):
        for i in range(1, len(arr)):   # Mulai iterasi dari elemen kedua hingga akhir array
            key = arr[i]    # Simpan elemen saat ini sebagai 'key'
            
            # Bandingkan elemen sebelumnya dengan 'key' dan geser elemen lebih besar ke kanan
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            
            # Tempatkan 'key' di posisi yang benar
            arr[j + 1] = key
        
        return arr
