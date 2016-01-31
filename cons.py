import sys
from utils import fasta

samples = fasta.read_samples(sys.stdin)
length = len(samples[0]['sequence'])
profile_matrix = {
    'A': [0] * length,
    'C': [0] * length,
    'G': [0] * length,
    'T': [0] * length
}

for sample in samples:
    dna = sample['sequence']
    for idx, nt in enumerate(dna):
        profile_matrix[nt][idx] += 1
consensus = [(' ', 0)] * length

for key in profile_matrix:
    for i in xrange(length):
        if profile_matrix[key][i] > consensus[i][1]:
            consensus[i] = (key, profile_matrix[key][i])

print ''.join([nt[0] for nt in consensus])
for key in profile_matrix:
    print key + ':',
    for i in xrange(length):
        print profile_matrix[key][i],
    print
