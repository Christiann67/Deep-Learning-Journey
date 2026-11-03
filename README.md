# Deep Learning & Systems Engineering Prep

Repositori portofolio implementasi algoritma dan komputasi dasar neural network dari nol tanpa *third-party libraries*.

## 1. Pure Neural Compute (`neural_network/`)
* **Layer Formula:** $\text{Output} = \text{ReLU}(X \cdot W + b)$
* **Multiply-Accumulate (MAC):** Operasi dot product $X \cdot W$ diakumulasikan secara sekuensial.
* **Kompleksitas Algoritmik:** Perkalian matriks serial berorde $\mathcal{O}(N^3)$ waktu dan $\mathcal{O}(M \times N)$ memori.

## 2. Hardware Rationale: CPU vs GPU (SIMT)
* **CPU Bottleneck:** Sifat serial latensi rendah CPU membuat eksekusi loop bersarang lambat saat matriks membesar ($N \ge 2048$).
* **Akselerasi SIMT:** Operasi MAC antar-elemen bersifat independen sehingga dapat diparalelkan di ribuan core thread GPU secara simultan.
