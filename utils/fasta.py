def read_samples(hdl):
    contents = hdl.read()
    matches = contents[1:].split('>')
    samples = []
    for match in matches:
        sample = match.split('\n')
        samples.append({
            'id': sample[0],
            'sequence': ''.join(sample[1:])
        })
    return samples
