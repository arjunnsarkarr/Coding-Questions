def generate_pascals_triangle(num_rows):
    if num_rows < 2 or num_rows > 30:
        raise ValueError("Number of rows must be between 2 and 30.")
    
    triangle = []
    for i in range(num_rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    max_width = len(" ".join(map(str, triangle[-1])))
    
    for row in triangle:
        row_str = " ".join(map(str, row))
        print(row_str.center(max_width))

# Example usage:
num_rows = 6 
generate_pascals_triangle(num_rows)
