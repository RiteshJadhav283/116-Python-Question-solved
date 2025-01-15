def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))

matrix=[]
for i in range(rows):
    row = list(map(int, input(f"Enter row {i+1} (space separated): ").split()))
    matrix.append(row)

transposed_matrix=transpose_matrix(matrix)

print("\nOriginal Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)