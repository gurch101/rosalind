def transcribe(dna):
    rna = []
    for nt in dna:
        if nt == 'T':
            rna.append('U')
        else:
            rna.append(nt)
    return ''.join(rna)
