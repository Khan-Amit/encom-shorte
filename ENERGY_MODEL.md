# Energy Savings Model – encom-shorte

## Formula

Where:
- `E_total` = total data center energy
- `P_filter` = energy of pre‑filter (negligible, <0.1% of total)
- `R` = rejection rate (99%)
- `H_base` = hashing/inference energy without filter
- `C_reduced` = cooling energy after heat reduction (90% less)

## Example: 39 MW Data Center

| Component | Without Filter | With encom-shorte |
|-----------|----------------|-------------------|
| Hashing/Compute | 30 MW | 0.3 MW |
| Cooling | 9 MW | 0.9 MW |
| Pre‑filter | 0 MW | 0.01 MW |
| **Total** | **39 MW** | **1.21 MW** |

## Annual Cost (at $0.10/kWh)

- Without filter: 39 MW × 8760 h × $0.10 = **$34.16 million**
- With encom-shorte: 1.21 MW × 8760 h × $0.10 = **$1.06 million**
- **Savings: $33.1 million per year (97%)**

## ROI

A $400 mock server pays for itself in:
$400 / ($33,100,000 / year) ≈ **0.000012 years ≈ 3 hours**
