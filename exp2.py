import time

# -------------------------------
# Naive String Matching
# -------------------------------
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            matches.append(i)

    return matches


# -------------------------------
# KMP Algorithm
# -------------------------------
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)

    matches = []
    i = 0
    j = 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            matches.append(i - j)
            j = lps[j - 1]

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches


# -------------------------------
# Rabin-Karp Algorithm
# -------------------------------
def rabin_karp(text, pattern, q=101):
    d = 256
    n = len(text)
    m = len(pattern)

    h = pow(d, m - 1) % q
    p = 0
    t = 0

    matches = []

    # Initial hash values
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Slide the pattern
    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                matches.append(i)

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q

    return matches


# -------------------------------
# Main Program
# -------------------------------
text = "ABABDABACDABABCABABABABCABAB"
pattern = "ABABCABAB"

# Naive
start = time.perf_counter()
result1 = naive_search(text, pattern)
end = time.perf_counter()
print("Naive Search:")
print("Matches found at:", result1)
print("Execution Time:", end - start, "seconds\n")

# Rabin-Karp
start = time.perf_counter()
result2 = rabin_karp(text, pattern)
end = time.perf_counter()
print("Rabin-Karp Search:")
print("Matches found at:", result2)
print("Execution Time:", end - start, "seconds\n")

# KMP
start = time.perf_counter()
result3 = kmp_search(text, pattern)
end = time.perf_counter()
print("KMP Search:")
print("Matches found at:", result3)
print("Execution Time:", end - start, "seconds")
