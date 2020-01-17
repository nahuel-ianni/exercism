def slices(series, length):
    if length > len(series) or length < 1:
        raise ValueError("The length of the subset cannot be computed.")

    return [series[i:i + length] for i in range(len(series)) if i + length <= len(series)]
