from typing import List, Union

Vector = List[Union[int, float]]
Matrix = List[Vector]


def relu(z: Union[int, float]) -> Union[int, float]:
  """Rectified Linear Unit Activation: f(z) = max(0, z)"""
  return max(0, z)


def pure_matmul(matrix_a: Matrix, matrix_b: Matrix) -> Matrix:
  """Perkalian dua matriks 2D tanpa library eksternal.

  Kompleksitas Waktu: O(M * K * N) -> O(N^3) untuk matriks persegi.
  Kompleksitas Memori: O(M * N)
  """
  rows_a, cols_a = len(matrix_a), len(matrix_a[0])
  rows_b, cols_b = len(matrix_b), len(matrix_b[0])

  if cols_a != rows_b:
    raise ValueError(
        f"Dimensi tidak valid untuk perkalian: {cols_a} != {rows_b}"
    )

  transposed_b = list(zip(*matrix_b))

  result: Matrix = []
  for row in matrix_a:
    new_row: Vector = []
    for col in transposed_b:
      mac_sum = sum(x * y for x, y in zip(row, col))
      new_row.append(mac_sum)
    result.append(new_row)

  return result


def dense_forward(x: Vector, weights: Matrix, biases: Vector) -> Vector:
  """Forward pass 1 layer: ReLU(X * W + b)"""
  matrix_x: Matrix = [x]
  z_matrix = pure_matmul(matrix_x, weights)
  z_vector = z_matrix[0]

  return [relu(z + b) for z, b in zip(z_vector, biases)]
