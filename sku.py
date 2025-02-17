#!  python3
#   20250217 - v1.1
#   SKU - Cole a página do ML, o programa irá filtrar os SKUs em ordem crescente.

import re

text = """
PASTE_HERE
"""

pattern = r'(\d+)\s+unidade[s]?\s+SKU:\s+(\d{8})'

matches = re.findall(pattern, text)

results = []
for match in matches:
    quantity, sku = match
    total = int(quantity)  # Unidade | Unidades
    sku_nozero = str(int(sku))  # SKU
    results.append(f"({total}) -{sku_nozero}")

results.sort()

for value in results:
    print(value)
