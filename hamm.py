"""
Given two strings s and t of equal length, the Hamming distance between s
and t, denoted dH(s,t), is the number of corresponding symbols that differ
in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
"""

s = raw_input()
t = raw_input()

ct = 0

for i, ch in enumerate(s):
    if ch != t[i]:
        ct += 1

print ct
