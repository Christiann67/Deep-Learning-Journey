from dense_layer import dense_forward

if __name__ == "__main__":
  # Simulasi input [3, 2]
  # Neuron 1: W1 = [2, 1], bias = -4
  # Neuron 2: W2 = [1, -2], bias = 2
  x = [3, 2]
  weights = [[2, 1], [1, -2]]
  biases = [-4, 2]

  output = dense_forward(x, weights, biases)

  print("=== Test Forward Pass ===")
  print(f"Output: {output}")

  assert output == [4, 1], f"Expected [4, 1], got {output}"
  print("Status: Passed (100% Match)!")
