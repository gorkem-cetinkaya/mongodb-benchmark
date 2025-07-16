# MongoDB Benchmark

Bu repoda, MongoDB üzerinde farklı CRUD ve batch insert senaryolarının benchmark kodları ve sonuçları bulunur.

## İçindekiler
- `generate_data.py`: Veri üretim script’i  
- `benchmark.py`: Insert / Update / Delete testleri  
- `batch_benchmark.py`: Farklı batch size testleri  
- `benchmark_results.json`, `batch_benchmark_results.json`: JSON sonuçları  
- `REPORT.md`: Detaylı rapor ve grafikler

## Kurulum

1. Repoyu klonlayın:
   ```bash
   git clone https://github.com/gorkem-cetinkaya/mongodb-benchmark.git
   cd mongodb-benchmark

2. Python sanal ortamı oluşturun ve aktifleştirin:
   python3 -m venv bm-env
   source bm-env/bin/activate  # macOS/Linux
   .\bm-env\Scripts\activate  # Windows
   
3. Gerekli paketleri yükleyin:
   pip install pymongo faker

## Kullanım

1) Veri Üretimi
python generate_data.py
1 000 – 10 000 000 arası data_{n}.json dosyaları üretir.

2. CRUD Benchmark
   python benchmark.py
Tüm ölçümleri benchmark_results.json dosyasına yazar.

3. Batch Size Benchmark
   python batch_benchmark.py
Farklı batch boyutları için sonuçları batch_benchmark_results.json dosyasına yazar.

## Sonuçları Görüntüleme

JSON dosyalarını pandas, jq veya MongoDB Compass ile inceleyebilirsiniz.
Detaylı rapor ve grafikler için: REPORT.md



