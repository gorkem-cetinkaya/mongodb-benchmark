import json
from faker import Faker
import time

fake = Faker()

def generate_docs(n):
 
    docs = []
    for _ in range(n):
        doc = {}
        for i in range(10):
            if i % 2 == 0:
                doc[f"field{i}"] = fake.random_int(0, 1_000_000)
            else:
                doc[f"field{i}"] = fake.word()
        docs.append(doc)
    return docs

if __name__ == "__main__":
    sizes = [1_000, 10_000, 100_000, 1_000_000, 10_000_000]

    for n in sizes:
        print(f"\nÜretiliyor: {n:,} kayıt…")
        start = time.perf_counter()
        docs = generate_docs(n)
        filename = f"data_{n}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(docs, f, ensure_ascii=False)
        elapsed = time.perf_counter() - start
        print(f"→ {filename} oluşturuldu: {n:,} belge, süre: {elapsed:.2f} sn")
