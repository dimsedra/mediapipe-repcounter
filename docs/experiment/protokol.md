# Protokol Pengambilan Data Squat

**Tujuan:** mengukur akurasi sistem menghitung repetisi squat pada berbagai
situasi (arah kamera, jarak, cahaya, baju, kedalaman squat).

**Total:** 14 video per atlet × 4 atlet = **56 video** (1 take per kondisi).

---

## A. Yang perlu disiapkan

| Alat | Keperluan |
|------|-----------|
| Kamera/laptop dengan webcam | min 720p, ≥24 fps |
| Tripod | biar kamera tidak goyang |
| Meteran | ukur jarak 1 m dan 2 m |
| Lampu tambahan (opsional) | untuk kondisi redup dan backlit |
| Baju longgar | 1 stel (kaus kebesaran/hoodie) |
| Baju pas badan | 1 stel (kaos + legging/celana training) |
| 4 atlet (A1, A2, A3, A4) | bergantian jadi atlet dan operator |
| 2–3 orang tim | 1 atlet, 1 operator kamera, 1 pencatat nama file |

---

## B. Setting baseline (patokan)

Semua kondisi berangkat dari sini:

| Faktor | Nilai baseline | Cara ngatur |
|--------|---------------|-------------|
| Arah kamera | **Serong 45°** | Badan setengah menghadap kamera |
| Jarak | **2 meter** | ~3 langkah besar dari kamera |
| Cahaya | **Normal** | Lampu ruangan menyala biasa |
| Baju | **Pas badan** | Kaos + legging/celana training |
| Kedalaman squat | **Penuh** | Turun sampai paha di bawah sejajar |
| Tempo | **Normal** | Tidak cepat, tidak lambat |
| Jumlah rep | **10 rep** | Hitung 1–10 |

### Cara setel kamera

1. **Tinggi kamera** = setinggi pinggang–dada atlet
2. **Ukur jarak** pakai meteran dari kamera ke tempat atlet berdiri
3. **Cek framing:** atlet lakukan 1 squat pelan — seluruh badan (kepala–kaki)
   harus masuk layar dari berdiri sampai posisi squat paling bawah
4. **Posisi atlet:**
   - **Serong (baseline):** badan ~45° ke kamera
   - **Depan:** badan menghadap lurus ke kamera
   - **Samping:** badan menyamping 90° ke kamera

> Kalau atlet bergeser selama rekaman, **hentikan dan ulangi**.

---

## C. Tiga sub-eksperimen

Data dikelompokkan ke 3 sub-eksperimen. Masing-masing **fully balanced**
(jumlah data tiap variasi sama). Analisis dilakukan **per sub-eksperimen**.

### Sub-1: Arah kamera × Jarak (24 video)

Semua di: cahaya=normal, baju=pas, kedalaman=penuh.

| Kode file | Arah kamera | Jarak |
|-----------|-------------|-------|
| `front-1m` | depan | 1 m |
| `front-2m` | depan | 2 m |
| `diag-1m` | serong | 1 m |
| `base` | serong | 2 m |
| `side-1m` | samping | 1 m |
| `side-2m` | samping | 2 m |

Tiap kode × 4 atlet × 1 take = **24 video. Balance: 4 video per sel.**

### Sub-2: Cahaya × Baju (20 video)

Semua di: serong, 2 m, kedalaman=penuh.
Catatan: `base` (normal + pas) sudah di Sub-1, tidak perlu diulang.

| Kode file | Cahaya | Baju |
|-----------|--------|------|
| `dim` | redup | pas |
| `backlit` | backlit | pas |
| `loose` | normal | longgar |
| `dim-loose` | redup | longgar |
| `backlit-loose` | backlit | longgar |

Tiap kode × 4 atlet × 1 take = **20 video. Balance: 4 video per sel.**

### Sub-3: Kedalaman (8 video)

Semua di: serong, 2 m, normal, pas.
Catatan: `penuh` (base) sudah di Sub-1, tidak perlu diulang.

| Kode file | Kedalaman | Keterangan |
|-----------|-----------|------------|
| `parallel` | parallel (~90–100°) | Sejajar lantai |
| `partial` | partial (>100°) | Setengah, tidak sampai sejajar |

Tiap kode × 4 atlet × 1 take = **8 video. Balance: 4 video per level.**

### Kontrol kelelahan (4 video)

| Kode file | Keterangan |
|-----------|------------|
| `base-end` | Baseline di akhir sesi (sama seperti `base`) |

Rekam di paling akhir. Bandingkan hasilnya dengan `base` dari Sub-1.
Kalau error base-end lebih besar, atlet sudah lelah.

### Ringkasan per atlet (14 video)

| No | Kode | Sub | Yang diubah dari baseline |
|----|------|-----|---------------------------|
| 1 | `front-1m` | 1 | arah=depan, jarak=1m |
| 2 | `front-2m` | 1 | arah=depan |
| 3 | `diag-1m` | 1 | jarak=1m |
| 4 | `base` | 1 | — (baseline) |
| 5 | `side-1m` | 1 | arah=samping, jarak=1m |
| 6 | `side-2m` | 1 | arah=samping |
| 7 | `dim` | 2 | cahaya=redup |
| 8 | `backlit` | 2 | cahaya=backlit |
| 9 | `loose` | 2 | baju=longgar |
| 10 | `dim-loose` | 2 | cahaya=redup, baju=longgar |
| 11 | `backlit-loose` | 2 | cahaya=backlit, baju=longgar |
| 12 | `parallel` | 3 | kedalaman=parallel |
| 13 | `partial` | 3 | kedalaman=partial |
| 14 | `base-end` | K | baseline di akhir |

---

## D. Aturan penamaan file

Format: `{atlet}_{kode}_t1.mp4`

Contoh:
- `A1_base_t1.mp4` — A1, baseline
- `A2_side-2m_t1.mp4` — A2, samping 2 m
- `A3_dim-loose_t1.mp4` — A3, redup + longgar

Aturan:
- Huruf kecil semua
- Pakai tanda `-` (strip) untuk kode bertingkat: `dim-loose`, `backlit-loose`
- Nama file **harus sama persis** dengan yang ada di `label_template.csv`

---

## E. Urutan rekaman

Agar tidak bias karena kelelahan, urutan diacak per atlet:

| Atlet | Urutan |
|-------|--------|
| **A1** | base → side-1m → front-2m → parallel → dim → loose → diag-1m → dim-loose → partial → side-2m → backlit → front-1m → backlit-loose → **base-end** |
| **A2** | base → dim → front-2m → backlit-loose → side-1m → partial → loose → front-1m → parallel → diag-1m → side-2m → dim-loose → backlit → **base-end** |
| **A3** | base → side-2m → diag-1m → backlit → parallel → front-2m → dim-loose → loose → front-1m → backlit-loose → side-1m → dim → partial → **base-end** |
| **A4** | base → parallel → backlit → side-1m → diag-1m → front-2m → dim-loose → backlit-loose → front-1m → side-2m → loose → dim → partial → **base-end** |

---

## F. Checklist

**Sebelum rekam:**
- [ ] Kamera di tripod, tidak goyang
- [ ] Arah kamera & jarak sesuai kondisi
- [ ] Faktor lain masih seperti baseline? (mis. pas `dim` — pastikan arah=serong, jarak=2m, baju=pas, squat=penuh)
- [ ] Seluruh badan masuk layar
- [ ] Nama file sudah benar

**Saat rekam:**
- [ ] Hitung 10 rep dengan suara keras (1…2…3…)
- [ ] Atlet jangan bergeser
- [ ] Kalau salah → ulang

**Setelah rekam:**
- [ ] Rename file kalau belum
- [ ] Taruh di folder `videos/`

> **Kalau rep bukan 10:** catat jumlah aslinya. Nanti diisi di kolom `rep_asli`.

---

## G. Proses video

Semua 56 video sudah di folder `videos/`:

```bash
python scripts/batch.py --workers 4
```

Hasil: **`dataset.csv`** — satu baris per video. Kolom penting:

| Kolom | Arti |
|-------|------|
| `status` | `ok`=sukses, `uncalibrated`=gagal kalibrasi, `no_pose`=tak terdeteksi, `error`=rusak |
| `total_reps` | Jumlah rep yang dihitung sistem |
| `full_reps` | Rep dengan sudut < 90° |
| `partial_reps` | Rep dengan sudut ~90–100° |

> Buang baris `status ≠ ok` sebelum hitung akurasi.

---

## H. Analisis — 3 sheet

| Sheet | Isi | File |
|-------|-----|------|
| **A — Label** | Data kondisi tiap video | `docs/experiment/label_template.csv` |
| **B — Hasil** | Output sistem | `dataset.csv` (hasil batch) atau `docs/experiment/hasil_template.csv` |
| **C — Analisis** | Gabungan A+B + hitungan error | Buat sendiri |

### Cara buat Sheet C

Gabung Sheet A dan Sheet B by kolom `video` (VLOOKUP/XLOOKUP). Tambah:

| Kolom | Rumus |
|-------|-------|
| `selisih` | `=total_reps - rep_asli` |
| `error` | `=ABS(selisih)` |
| `benar` | `=IF(total_reps = rep_asli, 1, 0)` |

Hasil contoh:
```
video           sub_eks  arah_kamera  rep_asli  total_reps  error  benar
A1_base_t1      1        serong       10        10          0      1
A2_side-2m_t1   1        samping      10        6           4      0
A3_dim_t1       2        serong       10        9           1      0
```

### Analisis per sub-eks — jangan dicampur!

Filter dulu `sub_eks`-nya. Analisis masing-masing secara terpisah.

---

## I. Sub-1: Viewpoint & Jarak

**Data:** `sub_eks == 1` (24 video). Balance: 4 video per sel.

**Faktor konstan:** cahaya=normal, baju=pas, kedalaman=penuh.

### Efek arah kamera (agregasi dari kedua jarak)

| Arah kamera | Rata-rata error | % benar | Jumlah video |
|-------------|----------------|---------|-------------|
| depan | | | 8 |
| serong | | | 8 |
| samping | | | 8 |

### Efek jarak (agregasi dari ketiga arah)

| Jarak | Rata-rata error | % benar | Jumlah video |
|-------|----------------|---------|-------------|
| 1 m | | | 12 |
| 2 m | | | 12 |

### Interaksi arah × jarak (tabel 3×2)

| Arah kamera | 1 m | 2 m |
|-------------|-----|-----|
| depan | error=…, %benar=… | error=…, %benar=… |
| serong | error=…, %benar=… | error=…, %benar=… |
| samping | error=…, %benar=… | error=…, %benar=… |

---

## J. Sub-2: Cahaya & Baju

**Data:** `sub_eks == 2` (20 video). Balance: 4 video per sel.

**Faktor konstan:** serong, 2 m, penuh.

### Efek cahaya (agregasi dari kedua baju)

| Cahaya | Rata-rata error | % benar | Jumlah video |
|--------|----------------|---------|-------------|
| normal | (ambil dari `base` Sub-1) | | 4 |
| redup | | | 8 |
| backlit | | | 8 |

### Efek baju (agregasi dari ketiga cahaya)

| Baju | Rata-rata error | % benar | Jumlah video |
|------|----------------|---------|-------------|
| pas | (ambil dari `base` Sub-1) | | 4 |
| longgar | | | 12 |

### Interaksi cahaya × baju (tabel 3×2)

| Cahaya | pas | longgar |
|--------|-----|---------|
| normal | error=… (dari `base` Sub-1) | error=… |
| redup | error=… | error=… |
| backlit | error=… | error=… |

---

## K. Sub-3: Kedalaman

**Data:** `sub_eks == 3` (8 video). Balance: 4 video per level.

**Faktor konstan:** serong, 2 m, normal, pas.

| Kedalaman | Rata-rata error | % benar | Rata-rata full_reps | Jumlah video |
|-----------|----------------|---------|--------------------|-------------|
| penuh | (dari `base` Sub-1) | | | 4 |
| parallel | | | | 4 |
| partial | | | | 4 |

**Yang perlu diperhatikan:**
- **Partial** — seharusnya sistem **tidak menghitung** rep (tidak mencapai parallel)
- **Parallel** — harus terhitung, tapi `full_reps` kecil (hanya sampai parallel)
- **Penuh** — `full_reps` besar (di bawah parallel)

---

## L. Kontrol kelelahan

**Data:** `sub_eks == K` (4 video).

Bandingkan `base` (Sub-1) vs `base-end` tiap atlet.

| Atlet | Error base | Error base-end | Ada efek lelah? |
|-------|-----------|----------------|-----------------|
| A1 | | | Ya / Tidak |
| A2 | | | Ya / Tidak |
| A3 | | | Ya / Tidak |
| A4 | | | Ya / Tidak |

---

## M. Ringkasan laporan

Sajikan 3 sub-bagian terpisah:

1. **Sub-1:** tabel interaksi 3×2 + grafik efek arah kamera + grafik efek jarak
2. **Sub-2:** tabel interaksi 3×2 + tabel efek cahaya + tabel efek baju
3. **Sub-3:** tabel kedalaman (3 baris)
4. **Kontrol:** tabel kelelahan (4 baris) — catat di batasan penelitian

---

## N. Ringkasan 1 menit (tempel di dinding)

1. Baseline = **serong, 2 m, terang, baju pas, squat penuh, 10 rep**
2. **14 video per atlet:** 6 (arah×jarak) + 5 (cahaya×baju) + 2 (kedalaman) + 1 (base-end)
3. Tiap kondisi **1 take**. Baseline di **awal & akhir**.
4. Nama file: `A1_base_t1.mp4` (atlet_kode_t1)
5. Seluruh badan **masuk layar**. Lakukan **10 rep**.
6. Semua video → `videos/` → `python scripts/batch.py --workers 4` → `dataset.csv`
7. **Analisis per sub-eks** (filter kolom `sub_eks`) — jangan campur
8. Buang `status ≠ ok` sebelum hitung akurasi
