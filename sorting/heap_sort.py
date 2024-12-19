import heapq

class HeapSort:
    def run(self, arr):
        # Mengubah array menjadi heap (struktur data berbasis heap)
        heapq.heapify(arr)
        
        # Keluarkan elemen-elemen dari heap satu per satu dan tambahkan ke  heapq.heappop() 
        return [heapq.heappop(arr) for _ in range(len(arr))]
