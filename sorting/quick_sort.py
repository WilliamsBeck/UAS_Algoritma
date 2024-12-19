class QuickSort:
    def run(self, arr):
        if len(arr) <= 1:   # Jika array memiliki 1 elemen atau kurang, array sudah terurut
            return arr
        
        # Pilih elemen pertama sebagai pivot
        pivot = arr[0]
        
        # 'less' berisi elemen-elemen yang nilainya kurang dari atau sama dengan pivot
        less = [x for x in arr[1:] if x <= pivot]
        
        # elemen-elemen yang nilainya lebih besar dari pivot
        greater = [x for x in arr[1:] if x > pivot]
        
        # Urutkan bagian 'less' dan 'greater' secara rekursif, lalu gabungkan dengan pivot
        return self.run(less) + [pivot] + self.run(greater)
