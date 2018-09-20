```python
'''
Title: Comparing Spectra with the Spectral Convolution
URL: http://rosalind.info/problems/conv/

Given: Two multisets of positive real numbers S1 and S2.
The size of each multiset is at most 200.

Return: The largest multiplicity of S1⊖S2, as well as
the absolute value of the number x maximizing (S1⊖S2)(x)
(you may return any such value if multiple solutions exist).
'''

from collections import Counter

with open('rosalind_conv.txt') as infile:
    s1 = [float(i) for i in infile.readline().split()]
    s2 = [float(i) for i in infile.readline().split()]


def Minkowski_diff(s1, s2):
    return Counter([round(i - j, 5) for i in s1 for j in s2]).most_common(1)

print(Minkowski_diff(s1, s2))

```





