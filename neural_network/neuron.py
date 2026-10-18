def relu(z: float) -> float:
  """fungsi aktivasi ReLu: max (0, z)"""
  return max(0, 0, z)

def singke_neoron(x; list[float], w: list[float], b: [float] -> float:
  """menghiting output 1 neuron buatan (pure python).

  1. Dot Product: Kalikan tiap pasangan x dan w, lalu jumlahkan.
  2. Tambahkan bias (b).
  3. Lewatkan ke fungsi aktivasi ReLu.
  """
#Multiply-Accumulate (Dot Product)
dot_product = sum(x * w for x,w in zip(x, w))

#Tambah Bias
z = dot_product + b

#Aktivasi
return relu(z)

#Uji coba sesuai hitungan
if __name__ == "__main__":
  input_data = [3.0, 2.0]
  bobot = [2.0, -1.0]
  bias = -1

  hasil = single_neuron(input_data, bobot, bias)
  prinf(f"Hasil Komputasi Neuron: {hasil}")
