class MergeSort:
    def run(self, arr):
        # Kasus dasar: jika array memiliki 1 elemen atau kurang, array sudah terurut
        if len(arr) <= 1:
            return arr
        
        # Tentukan titik tengah untuk membagi array menjadi dua bagian
        mid = len(arr) // 2
        
        # Urutkan bagian kiri dan kanan secara rekursif
        left = self.run(arr[:mid])
        right = self.run(arr[mid:])
        
        # Gabungkan bagian kiri dan kanan yang sudah terurut
        return self.merge(left, right)
    
    def merge(self, left, right):
        # Gabungkan dua array terurut menjadi satu array terurut
        result = []
        
        # Selama kedua array (left dan right) tidak kosong
        while left and right:
            # Pilih elemen terkecil dari kedua array dan tambahkan ke hasil
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        
        # Tambahkan sisa elemen dari salah satu array yang belum diproses
        result.extend(left or right)
        return result
