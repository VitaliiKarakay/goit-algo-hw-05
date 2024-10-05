from boyer_moore import boyer_moore_search
from knuth_morris_pratt import knuth_morris_pratt
from rabin_karp import rabin_karp
from utils import detect_encoding, measure_time, find_fastest

encoding1 = detect_encoding('стаття 1.txt')
encoding2 = detect_encoding('стаття 2.txt')

with open('стаття 1.txt', 'r', encoding=encoding1) as file1:
    text1 = file1.read()

with open('стаття 2.txt', 'r', encoding=encoding2) as file2:
    text2 = file2.read()

existing_substring = "серед"
non_existing_substring = "hello world!"

results1 = {
    'Boyer-Moore': measure_time(boyer_moore_search, text1, existing_substring),
    'KMP': measure_time(knuth_morris_pratt, text1, existing_substring),
    'Rabin-Karp': measure_time(rabin_karp, text1, existing_substring),
}

results2 = {
    'Boyer-Moore': measure_time(boyer_moore_search, text1, non_existing_substring),
    'KMP': measure_time(knuth_morris_pratt, text1, non_existing_substring),
    'Rabin-Karp': measure_time(rabin_karp, text1, non_existing_substring),
}

results3 = {
    'Boyer-Moore': measure_time(boyer_moore_search, text2, existing_substring),
    'KMP': measure_time(knuth_morris_pratt, text2, existing_substring),
    'Rabin-Karp': measure_time(rabin_karp, text2, existing_substring),
}

results4 = {
    'Boyer-Moore': measure_time(boyer_moore_search, text2, non_existing_substring),
    'KMP': measure_time(knuth_morris_pratt, text2, non_existing_substring),
    'Rabin-Karp': measure_time(rabin_karp, text2, non_existing_substring),
}

print("Час виконання для статті 1:")
print(results1)
print("Час виконання для статті 1 (вигаданий):")
print(results2)
print("Час виконання для статті 2:")
print(results3)
print("Час виконання для статті 2 (вигаданий):")
print(results4)

fastest_existing1 = find_fastest(results1)
fastest_non_existing1 = find_fastest(results2)
fastest_existing2 = find_fastest(results3)
fastest_non_existing2 = find_fastest(results4)

print(f"Найшвидший алгоритм для статті 1 (існуючий): {fastest_existing1}")
print(f"Найшвидший алгоритм для статті 1 (вигаданий): {fastest_non_existing1}")
print(f"Найшвидший алгоритм для статті 2 (існуючий): {fastest_existing2}")
print(f"Найшвидший алгоритм для статті 2 (вигаданий): {fastest_non_existing2}")