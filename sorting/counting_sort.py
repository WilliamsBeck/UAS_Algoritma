class CountingSort:
    def run(self, arr):
        # Temukan nilai maksimum 
        max_val = max(arr)
        
        # Inisialisasi array count dengan ukuran max_val + 1
        count = [0] * (max_val + 1)
        
        # Hitung frekuensi kemunculan setiap elemen 
        for num in arr:
            count[num] += 1
        
        # Bangun array yang sudah terurut berdasarkan frekuensi
        sorted_arr = []
        for i, c in enumerate(count):
            # Tambahkan elemen 'i' sebanyak 'c' kali 
            sorted_arr.extend([i] * c)
        
        return sorted_arr
