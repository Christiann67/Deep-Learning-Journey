def is_palindrome(s: str) -> bool:
    """Mengecek valid palindrome dengan optimasi memori O(1) Two Pointers.

    Kompleksitas Waktu  : O(N) - Memindai string satu kali lintasan.
    Kompleksitas Ruang  : O(1) Auxiliary Space - Tanpa string penampung baru.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # Lewati karakter non-alfanumerik di sisi kiri
        while left < right and not s[left].isalnum():
            left += 1

        # Lewati karakter non-alfanumerik di sisi kanan
        while left < right and not s[right].isalnum():
            right -= 1

        # Bandingkan karakter dalam huruf kecil (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False

        # Geser kedua pointer ke dalam jika karakter cocok
        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    # Test Cases
    test_1 = "A man, a plan, a canal: Panama"
    test_2 = "race a car"

    print(f"Test 1 ('{test_1}'): {is_palindrome(test_1)}")  # True
    print(f"Test 2 ('{test_2}'): {is_palindrome(test_2)}")  # False

    assert is_palindrome(test_1) is True
    assert is_palindrome(test_2) is False
    print("Semua pengujian Palindrome O(1) lolos!")
