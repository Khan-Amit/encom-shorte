from multiprocessing import Pool
from prefilter import EncomShorte

def scan_chunk(start, end):
    es = EncomShorte()
    count = 0
    for n in range(start, end):
        if es.is_ripe(1231006505, n):
            count += 1
    return count

if __name__ == "__main__":
    print("Scanning 1 million nonces with 4 threads...")
    with Pool(4) as p:
        results = p.starmap(scan_chunk, [(0, 250000), (250000, 500000), (500000, 750000), (750000, 1000000)])
    total = sum(results)
    print(f"Total ripe candidates: {total}")
