# Mock Server Setup – Low Cost Demonstration

## Hardware (used prices)

| Component | Recommendation | Cost (USD) |
|-----------|----------------|------------|
| GPU | NVIDIA RTX 3060 (12 GB) | $200-300 |
| CPU | Xeon E5 or Ryzen 5 | $50-100 |
| RAM | 16 GB DDR4 | $30 |
| Storage | 256 GB SSD | $20 |
| **Total** | | **$300-450** |

## Software

1. Install Ubuntu 22.04 or 24.04
2. Install Python 3.10+
3. Clone the repo: `git clone https://github.com/khan-amit/encom-shorte`
4. Run: `python3 PARALLEL_TEST.py`

## Scaling

The pre‑filter can be deployed on multiple nodes with a job dispatcher. Each node processes independent chunks of candidates.

## Cost to Test

A $400 mock server can demonstrate 97% energy savings before committing to a full data center deployment.
