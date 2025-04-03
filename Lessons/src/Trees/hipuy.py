import sys

class MaxHeap:
    def __init__(self):
        self.heap = [None]
        self.heap_size = 0

    def insert(self, value):
        self.heap.append(value)
        self.heap_size += 1
        current_index = self.heap_size
        while current_index > 1 and self.heap[current_index] > self.heap[current_index // 2]:
            self.heap[current_index], self.heap[current_index // 2] = self.heap[current_index // 2], self.heap[current_index]
            current_index = current_index // 2

    def extract_max(self):
        if self.heap_size == 0:
            return None 
        max_value = self.heap[1]
        if self.heap_size > 1:
            self.heap[1] = self.heap.pop()
            self.heap_size -= 1
            current_index = 1
            while True:
                left_child_index = 2 * current_index
                right_child_index = 2 * current_index + 1
                larger_child_index = -1
                if left_child_index <= self.heap_size:
                    if right_child_index <= self.heap_size:
                        if self.heap[left_child_index] >= self.heap[right_child_index]:
                            larger_child_index = left_child_index
                        else:
                            larger_child_index = right_child_index
                    else:
                        larger_child_index = left_child_index
                else:
                    break
                if larger_child_index != -1 and self.heap[current_index] < self.heap[larger_child_index]:
                    self.heap[current_index], self.heap[larger_child_index] = self.heap[larger_child_index], self.heap[current_index]
                    current_index = larger_child_index
                else:
                    break
        else:
            self.heap.pop() 
            self.heap_size -= 1
        return max_value
def main():
    n = int(sys.stdin.readline())
    heap = MaxHeap()
    output_values = []
    for _ in range(n):
        command = sys.stdin.readline().split()
        operation_type = int(command[0])
        if operation_type == 0:
            value_to_insert = int(command[1])
            heap.insert(value_to_insert)
        elif operation_type == 1:
            extracted_value = heap.extract_max()
            output_values.append(str(extracted_value))
            
    print("\n".join(output_values))

if __name__ == "__main__":
    main()