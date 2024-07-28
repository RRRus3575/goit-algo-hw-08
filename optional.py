import heapq

def merge_k_lists(lists):
    min_heap = []
    
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))  
    
    merged_list = []
    
    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(val)
        
        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(min_heap, next_tuple)
    
    return merged_list


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
