def searchIndex(self, pattern: str, str_in: str) -> int:
    if not pattern:
        return 0 if not str_in else -1


# A*b*c
    parts = [p for p in pattern.split("*") if p]

    if not parts:
        return 0

    start_search_idx = 0
    result_idx = -1

    for i, part in enumerate(parts):
        found_at = str_in.find(part, start_search_idx)

        if found_at == -1:
            return -1
        if i == 0:
            result_idx = found_at

        start_search_idx = found_at + len(part)
    if pattern.startswith('*'):
        return 0
    else:
        return result_idx


# def kmp_search(text, pattern):
#     """
#     Finds the starting index of 'pattern' in 'text' using the KMP algorithm.
#     Returns the start index if found, otherwise returns -1.
#     """
#
#     # Edge case: If pattern is empty, technically it starts at index 0
#     if not pattern:
#         return 0
#
#     # Edge case: If text is empty or shorter than pattern, it's impossible to match
#     if not text or len(pattern) > len(text):
#         return -1
#
#     n = len(text)
#     m = len(pattern)
#
#     # Step 1: Preprocess the pattern to calculate the LPS array.
#     # LPS[i] stores the length of the longest proper prefix of pattern[0...i]
#     # that is also a suffix of pattern[0...i].
#     lps = compute_lps(pattern)
#
#     i = 0  # index for text
#     j = 0  # index for pattern
#
#     while i < n:
#         # If characters match, move both pointers forward
#         if pattern[j] == text[i]:
#             i += 1
#             j += 1
#
#         # Check if we have found the complete pattern
#         if j == m:
#             # Match found! Return the starting index.
#             # To continue searching for more occurrences, we would set j = lps[j-1] here.
#             return i - j
#
#         # Mismatch after j matches
#         elif i < n and pattern[j] != text[i]:
#             # Do not match lps[0..lps[j-1]] characters, because they will match anyway.
#             if j != 0:
#                 # Fall back to the previous longest prefix match
#                 j = lps[j - 1]
#             else:
#                 # If j is 0, we can't fall back; just move the text pointer
#                 i += 1
#
#     # Pattern was not found in text
#     return -1
#
#
# def compute_lps(pattern):
#     """
#     Computes the Longest Prefix Suffix (LPS) array for the KMP algorithm.
#     """
#     m = len(pattern)
#     lps = [0] * m
#
#     # length of the previous longest prefix suffix
#     length = 0
#
#     # the loop calculates lps[i] for i = 1 to m-1
#     i = 1
#
#     while i < m:
#         if pattern[i] == pattern[length]:
#             # If characters match, extend the current prefix length
#             length += 1
#             lps[i] = length
#             i += 1
#         else:
#             # If characters don't match
#             if length != 0:
#                 # Fall back to the previous length in the LPS array.
#                 # We do NOT increment i here. We check pattern[i] against
#                 # the character at the new 'length' index.
#                 length = lps[length - 1]
#             else:
#                 # If length is 0, we can't fall back anymore.
#                 # So lps[i] is 0 and we move to the next character.
#                 lps[i] = 0
#                 i += 1
#
#     return lps
#
#
# # --- Example Usage ---
# if __name__ == "__main__":
#     text_str = "ABABDABACDABABCABAB"
#     pat_str = "ABABCABAB"
#
#     result = kmp_search(text_str, pat_str)
#
#     if result != -1:
#         print(f"Pattern found at index: {result}")
#     else:
#         print("Pattern not found")
