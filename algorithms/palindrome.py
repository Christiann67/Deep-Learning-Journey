def is_palindrome(kata: str) -> bool:
  """Mengecek apakah suatu kata sama jika dibaca terbalik.
  Kompleksitas: 0(N) waktu, 0(N) memori
  """
  return kata == kata[::-1]

if __name__ == "__main__":
  test_kata = ["katak", "malam", "radar", "mobil", "nvidia"]
  for k in test_kata:
    print(f"apakah '{k}' palidrome? {is_palidrome(k)}")
