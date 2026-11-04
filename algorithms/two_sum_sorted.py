from typing import List


def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    """Menyelesaikan Two Sum II (Input Array Is Sorted) menggunakan teknik Two Pointers.

    Kompleksitas Waktu: O(N) - Memindai array paling banyak satu kali lintasan.
    Kompleksitas Ruang: O(1) Auxiliary Space - Tanpa alokasi struktur data hash map.

    Args:
        numbers: List bilangan bulat yang sudah terurut menaik (1-indexed).
        target: Target nilai penjumlahan dua angka.

    Returns:
        List berisi dua indeks (1-based) dari angka yang menghasilkan target.
    """
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            # Mengembalikan indeks dalam format 1-based indexing
            return [left + 1, right + 1]
        elif current_sum > target:
            # Nilai terlalu besar, geser pointer kanan ke arah angka yang lebih kecil
            right -= 1
        else:
            # Nilai terlalu kecil, geser pointer kiri ke arah angka yang lebih besar
            left += 1

    return []


if __name__ == "__main__":
    # Test Case 1: Latihan pertama (Target mengecilkan nilai via pointer kanan)
    test_1 = [2, 7, 11, 15]
    target_1 = 9
    result_1 = two_sum_sorted(test_1, target_1)
    print(f"Test 1 Output: {result_1}")
    assert result_1 == [1, 2], f"Expected [1, 2], got {result_1}"

    # Test Case 2: Latihan kedua (Target membesarkan nilai via pointer kiri)
    test_2 = [1, 3, 4, 8, 12]
    target_2 = 15
    result_2 = two_sum_sorted(test_2, target_2)
    print(f"Test 2 Output: {result_2}")
    assert result_2 == [2, 5], f"Expected [2, 5], got {result_2}"

    print("Semua skenario Two Pointers lolos verifikasi!")
