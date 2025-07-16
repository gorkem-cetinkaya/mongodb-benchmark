# batch_benchmark.py

import json
import time
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["benchmark"]
coll = db["test_collection"]

def load_docs(n):
    return json.load(open(f"data_{n}.json", encoding="utf-8"))

def benchmark_insert_batch(n, batch_size):
    docs = load_docs(n)
    coll.drop()
    start = time.perf_counter()
    for i in range(0, len(docs), batch_size):
        coll.insert_many(docs[i:i+batch_size])
    return time.perf_counter() - start

if __name__ == "__main__":
    n = 100_000 
    batch_sizes = [100, 1_000, 5_000, 10_000]
    results = []

    for bs in batch_sizes:
        t = benchmark_insert_batch(n, bs)
        ops_per_s = n / t
        print(f"Batch size {bs}: {t:.2f} sn, throughput: {ops_per_s:.0f} ops/s")
        results.append({
            "batch_size": bs,
            "time_sec": round(t, 4),
            "throughput_ops_per_s": round(ops_per_s)
        })

    with open("batch_benchmark_results.json", "w", encoding="utf-8") as f:
        json.dump({
            "record_count": n,
            "results": results
        }, f, ensure_ascii=False, indent=2)

    print("\nSonuçlar batch_benchmark_results.json dosyasına kaydedildi.")
