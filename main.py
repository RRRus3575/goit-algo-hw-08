import heapq

def min_cost_to_connect_cables(cable_lengths):
    heapq.heapify(cable_lengths)
    
    total_cost = 0
    connection_order = []
    
    while len(cable_lengths) > 1:
        first_min = heapq.heappop(cable_lengths)
        second_min = heapq.heappop(cable_lengths)
        
        cost = first_min + second_min
        
        total_cost += cost
        
        heapq.heappush(cable_lengths, cost)

        connection_order.append((first_min, second_min))

        print(f"Об'єднано кабелі довжиною {first_min} і {second_min}, витрати: {cost}")
        print(f"Стан купи після об'єднання: {cable_lengths}")
    

    return total_cost, connection_order

cable_lengths = [4, 3, 2, 6]
min_cost, order = min_cost_to_connect_cables(cable_lengths)

print(f"\nМінімальні витрати на з'єднання кабелів: {min_cost}")
print("Порядок з'єднання:")
for first, second in order:
    print(f"Об'єднано кабелі довжиною {first} і {second}")
