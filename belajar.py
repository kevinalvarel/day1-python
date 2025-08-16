# LOGIKA PYTHON DASAR TANPA LIBRARY

# 1. FUNGSI MATEMATIKA DASAR
def faktorial(n):
    """Menghitung faktorial dari bilangan n"""
    if n <= 1:
        return 1
    else:
        return n * faktorial(n - 1)

def fibonacci(n):
    """Menghasilkan deret fibonacci hingga bilangan ke-n"""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def is_prima(n):
    """Mengecek apakah bilangan n adalah bilangan prima"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 2. SORTING ALGORITHMS
def bubble_sort(arr):
    """Mengurutkan array menggunakan bubble sort"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    """Mengurutkan array menggunakan selection sort"""
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 3. SEARCHING ALGORITHMS
def linear_search(arr, x):
    """Mencari elemen x dalam array menggunakan linear search"""
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary_search(arr, x):
    """Mencari elemen x dalam array terurut menggunakan binary search"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 4. MANIPULASI STRING
def reverse_string(s):
    """Membalik string tanpa menggunakan [::-1]"""
    result = ""
    for char in s:
        result = char + result
    return result

def is_palindrome(s):
    """Mengecek apakah string adalah palindrome"""
    s = s.lower().replace(" ", "")
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def count_words(text):
    """Menghitung jumlah kata dalam teks"""
    words = text.split()
    return len(words)

# 5. STRUKTUR DATA SEDERHANA
class Stack:
    """Implementasi Stack (LIFO)"""
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

class Queue:
    """Implementasi Queue (FIFO)"""
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# 6. VALIDASI DATA
def is_email_valid(email):
    """Validasi email sederhana"""
    if "@" not in email or "." not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    local, domain = parts
    if len(local) == 0 or len(domain) == 0:
        return False
    if "." not in domain:
        return False
    return True

def is_phone_valid(phone):
    """Validasi nomor telepon sederhana (hanya angka)"""
    return phone.isdigit() and len(phone) >= 10

# 7. KONVERSI BILANGAN
def decimal_to_binary(n):
    """Konversi decimal ke binary"""
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

def binary_to_decimal(binary):
    """Konversi binary ke decimal"""
    decimal = 0
    power = 0
    for digit in reversed(binary):
        if digit == '1':
            decimal += 2 ** power
        power += 1
    return decimal

# 8. FUNGSI UTILITAS
def find_max_min(arr):
    """Mencari nilai maksimum dan minimum dalam array"""
    if not arr:
        return None, None
    max_val = min_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val, min_val

def calculate_average(arr):
    """Menghitung rata-rata dari array"""
    if not arr:
        return 0
    return sum(arr) / len(arr)

def remove_duplicates(arr):
    """Menghapus duplikat dari array"""
    unique = []
    for item in arr:
        if item not in unique:
            unique.append(item)
    return unique

# CONTOH PENGGUNAAN
if __name__ == "__main__":
    print("=== CONTOH PENGGUNAAN LOGIKA PYTHON ===\n")
    
    # Test matematika
    print(f"Faktorial 5: {faktorial(5)}")
    print(f"Fibonacci 10: {fibonacci(10)}")
    print(f"17 adalah prima: {is_prima(17)}")
    
    # Test sorting
    data = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nData asli: {data}")
    print(f"Bubble sort: {bubble_sort(data.copy())}")
    print(f"Selection sort: {selection_sort(data.copy())}")
    
    # Test searching
    sorted_data = [11, 12, 22, 25, 34, 64, 90]
    print(f"\nMencari 25 dalam {sorted_data}")
    print(f"Linear search: index {linear_search(sorted_data, 25)}")
    print(f"Binary search: index {binary_search(sorted_data, 25)}")
    
    # Test string
    text = "Kasur Rusak"
    print(f"\nTeks: '{text}'")
    print(f"Reverse: '{reverse_string(text)}'")
    print(f"Palindrome: {is_palindrome(text)}")
    
    # Test stack
    print("\n=== TEST STACK ===")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Pop: {stack.pop()}")
    print(f"Peek: {stack.peek()}")
    
    # Test konversi
    print(f"\nDecimal 10 ke binary: {decimal_to_binary(10)}")
    print(f"Binary '1010' ke decimal: {binary_to_decimal('1010')}")
    
    # Test utilitas
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    max_val, min_val = find_max_min(numbers)
    print(f"\nArray: {numbers}")
    print(f"Max: {max_val}, Min: {min_val}")
    print(f"Rata-rata: {calculate_average(numbers)}")
    print(f"Tanpa duplikat: {remove_duplicates(numbers)}")