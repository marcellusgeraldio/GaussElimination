# Nama = Marcellus Geraldio Florenta
# NIM  = 2702262816

import numpy as np

def gauss_elimination(augmented_matrix):
    num_rows, num_cols = augmented_matrix.shape

    # Langkah eliminasi Gauss
    for pivot_row in range(num_rows):
        # Mencari pivot (elemen diagonal) non zero
        
        pivot_index = pivot_row
        while pivot_index < num_rows and augmented_matrix[pivot_index, pivot_row] == 0:
            pivot_index += 1
        
        # Jika tidak ada pivot non zero
        if pivot_index == num_rows:
            return "Sistem tidak konsisten"

        # Menukar baris jika pivot tidak berada di pivot row
        if pivot_index != pivot_row:
            augmented_matrix[[pivot_row, pivot_index]] = augmented_matrix[[pivot_index, pivot_row]]

        # Normalisasi baris pivot (membuat elemen diagonal menjadi 1)
        pivot_value = augmented_matrix[pivot_row, pivot_row]
        augmented_matrix[pivot_row] /= pivot_value

        # Melakukan eliminasi elemen di bawah pivot
        for row in range(pivot_row + 1, num_rows):
            multiplier = augmented_matrix[row, pivot_row]
            augmented_matrix[row] -= multiplier * augmented_matrix[pivot_row]

    # Mencari solusi variabel menggunakan substitusi mundur
    solutions = np.zeros(num_cols - 1)
    for i in range(num_rows - 1, -1, -1):
        solutions[i] = augmented_matrix[i, -1]
        for j in range(i + 1, num_cols - 1):
            solutions[i] -= augmented_matrix[i, j] * solutions[j]

    return solutions

def main():
    # Input matriks augmented
    print("Masukkan matriks augmented:")
    augmented_matrix = []
    equation = list(map(float, input().split()))
    num_variables = len(equation) - 1
    augmented_matrix.append(equation)

    # Input koefisien matriks augmented
    for _ in range(num_variables - 1):
        equation = list(map(float, input().split()))
        # Mengecek jumlah koefisien yang tepat
        if len(equation) != num_variables + 1:
            print("Error!! Masukkan jumlah koefisien yang tepat")
            return
        augmented_matrix.append(equation)

    augmented_matrix = np.array(augmented_matrix)

    # Memanggil fungsi gauss elimination
    solutions = gauss_elimination(augmented_matrix)

    # Output solusi
    if isinstance(solutions, str):
        print(solutions)
    else:
        for i in range(num_variables):
            print(f"Solusi untuk x{i + 1} =", solutions[i])

if __name__ == "__main__":
    main()
