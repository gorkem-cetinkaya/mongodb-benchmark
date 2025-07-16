import json, time
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["benchmark"]
collection = db["test_collection"]

def clear_collection():
    collection.drop()

def benchmark_insert(n, batch_size=1000):
    with open(f"data_{n}.json", "r", encoding="utf-8") as f:
        docs = json.load(f)
    clear_collection()
    start = time.perf_counter()
    for i in range(0, len(docs), batch_size):
        collection.insert_many(docs[i:i+batch_size])
    return time.perf_counter() - start

def benchmark_update(n):
    with open(f"data_{n}.json", "r", encoding="utf-8") as f:
        docs = json.load(f)
    clear_collection()
    collection.insert_many(docs)
    start = time.perf_counter()
    collection.update_many({}, {"$inc": {"field0": 1}})
    return time.perf_counter() - start

def benchmark_delete(n):
    with open(f"data_{n}.json", "r", encoding="utf-8") as f:
        docs = json.load(f)
    clear_collection()
    collection.insert_many(docs)
    start = time.perf_counter()
    collection.delete_many({})
    return time.perf_counter() - start

def main():
    sizes = [1_000, 10_000, 100_000, 1_000_000, 10_000_000]
    results = {"insert": [], "update": [], "delete": []}

    print("=== INSERT Benchmark Başlıyor ===")
    for n in sizes:
        t = benchmark_insert(n)
        print(f"Insert {n:,} belge: {t:.2f} sn")
        results["insert"].append({"count": n, "time": t})

    print("\n=== UPDATE Benchmark Başlıyor ===")
    for n in sizes:
        t = benchmark_update(n)
        print(f"Update {n:,} belge: {t:.2f} sn")
        results["update"].append({"count": n, "time": t})

    print("\n=== DELETE Benchmark Başlıyor ===")
    for n in sizes:
        t = benchmark_delete(n)
        print(f"Delete {n:,} belge: {t:.2f} sn")
        results["delete"].append({"count": n, "time": t})

    with open("benchmark_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("\nSonuçlar benchmark_results.json dosyasına kaydedildi.")

if __name__ == "__main__":
    main()
