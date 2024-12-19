class SelectionSort:
    def run(self, arr):
        for i in range(len(arr)):  # Iterasi melalui setiap elemen dalam array
            min_idx = i
            
            # Cari elemen terkecil
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            # Tukar elemen terkecil dengan elemen pada indeks
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        return arr
