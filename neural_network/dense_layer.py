def relu(z: float) -> float:
  """Fungsi Aktivasi ReLu: max(0, z)"""
  return max(0.0, z)


def dense_layer(
  X: list[float], W_matrix: list[list[float]]. B: list[float]
) -> list[float]:
  """Menghitung output 1 layer penuh (Dense/Fully Connected Layer) berbasis Pure Python.
  - X         : Vektor input [Panjang input]
  - W_matrix  : Matriks bobot [jumlah neuron x panjang input]
  - B         : Vektor bias [jumlah neuron]
  """
  output_layer = []

  # Iterasi setiap neuron (setiap baris bobot W dan bias b) menggunakan zip()
  for W_neuron, b in zip(W_matrix, B):
    # 1. Hitung Dot Product untuk neuron ini
    dot_product = sum(x * w for x, w in zip(X, W_neuron))

    # 2. Tambahkan Bias (b)
    z = dot_product + b

    # 3. Saring dengan ReLU lalu simpan hasilnya
    output_layer.append(relu(z))

  return output_layer


# --- Uji Coba Sesuai Hitungan Kita Kemarin ---
if __name__ == "__main__":
  input_data = [5.0, 2.0, 1.0, 4.0]

  # Matriks bobot 3 neuron
  matriks_bobot = [
      [1.0, 0.0, -1.0, 2.0],  # Bobot Neuron 1
      [0.0, 2.0, 1.0, -1.0],  # Bobot Neuron 2
      [-1.0, 1.0, 0.0, 1.0],  # Bobot Neuron 3
  ]

  # Bias 3 neuron
  vektor_bias = [-3.0, 1.0, -2.0]

  hasil = dense_layer(input_data, matriks_bobot, vektor_bias)
  print(f"Output Layer: {hasil}")
  # Ekspektasi Output: [9.0, 2.0, 0.0]
