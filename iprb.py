HH, Hh, hh = map(float, raw_input().split())
total = HH + Hh + hh

prob = (
    HH / total * (HH - 1) / (total - 1) +
    HH / total * Hh / (total - 1) +
    Hh / total * HH / (total - 1) +
    0.75 * (Hh / total * (Hh - 1) / (total - 1)) +
    HH / total * hh / (total - 1) +
    hh / total * HH / (total - 1) +
    0.5 * (Hh / total * hh / (total - 1)) +
    0.5 * (hh / total * Hh / (total - 1))
)

print prob


