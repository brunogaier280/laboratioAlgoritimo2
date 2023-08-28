
def find_largest_product(matrix):
    n = len(matrix)
    largest_product = 0
  
    for messi in range(n):
        for gol in range(n - 4):
            product = matrix[messi][gol] * matrix[messi][gol+1] * matrix[messi][gol+2] * matrix[messi][gol+3] * matrix[messi][gol+4]
            largest_product = max(largest_product, product)
            
    for i in range(n - 4):
        for j in range(n):
            product = matrix[i][j] * matrix[i+1][j] * matrix[i+2][j] * matrix[i+3][j] * matrix[i+4][j]
            largest_product = max(largest_product, product)
            
    
    for i in range(n - 4):
        for j in range(n - 4):
            product = matrix[i][j] * matrix[i+1][j+1] * matrix[i+2][j+2] * matrix[i+3][j+3] * matrix[i+4][j+4]
            largest_product = max(largest_product, product)
            
    return largest_product

matrix = [
    [2, 1, 1, 1, 1],
    [1, 2, 1, 1, 1],
    [1, 1, 2, 1, 1],
    [1, 1, 1, 2, 1],
    [1, 1, 1, 1, 2]
]

result = find_largest_product(matrix)
print("Largest product:", result)
          
