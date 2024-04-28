def read_vectors_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        vectors = [Vector(line.split()) for line in lines]
    return vectors

def find_max_dimension_min_length(vectors):
    max_dimension_vector = max(vectors, key=lambda vec: (vec.dimension(), -vec.length()))
    return max_dimension_vector

def find_max_length_min_dimension(vectors):
    max_length_vector = max(vectors, key=lambda vec: (vec.length(), -vec.dimension()))
    return max_length_vector

def average_length(vectors):
    total_length = sum(vec.length() for vec in vectors)
    return total_length / len(vectors)

def count_vectors_above_average_length(vectors):
    avg_length = average_length(vectors)
    return sum(vec.length() > avg_length for vec in vectors)

def max_component_vector(vectors):
    return max(vectors, key=lambda vec: (vec.max_component(), -vec.min_component()))

def min_component_vector(vectors):
    return min(vectors, key=lambda vec: (vec.min_component(), -vec.max_component()))

# Приклад використання:
file_path = "your_file.txt"  # Замініть на шлях до вашого файлу
vectors = read_vectors_from_file(file_path)

result1 = find_max_dimension_min_length(vectors)
result2 = find_max_length_min_dimension(vectors)
result3 = average_length(vectors)
result4 = count_vectors_above_average_length(vectors)
result5 = max_component_vector(vectors)
result6 = min_component_vector(vectors)

print("Той з найбільшою розмірністю та найменшою довжиною:", result1)
print("Той з найбільшою довжиною та найменшою розмірністю:", result2)
print("Середня довжина вектора:", result3)
print("Кількість векторів з довжиною більше за середню:", result4)
print("Вектор з максимальною найбільшою компонентою та мінімальною найменшою:", result5)
print("Вектор з мінімальною найменшою компонентою та максимальною найбільшою:", result6)