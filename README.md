# spacehog 🐖💾

**EN | Find what is eating your disk space — read-only, offline, zero install.**
**TR | DiskDomuzu — Disk alanınızı yiyeni bulun — salt okunur, çevrimdışı, kurumsuz.**

"Disk nereye doldu?" sorusunun cevabı: spacehog bir klasörü tarar, en büyük
alt klasörleri ve dosyaları yüzdeli çubuklarla listeler. Hiçbir şey silmez ya
da taşımaz — sadece bakar.

*(EN: Scan a folder, instantly see the biggest folders & files with share
bars. It never deletes or moves anything — it only looks.)*

```bash
python spacehog.py                       # EN: scan current folder | TR: bulunulan klasör
python spacehog.py C:\                   # EN: scan a drive | TR: diski tara
python spacehog.py ~/Downloads --files   # EN: + biggest files | TR: + en büyük dosyalar
python spacehog.py D:\ --depth 2 -n 30   # EN: deeper, more rows | TR: derin, çok satır
```

```
Scanning / Taranıyor: C:\Users\you  ...

  ####################....  82.4%      96.2 GB  Downloads/
      ############..       68.0%      65.4 GB  videos/
  ###...................    9.1%      10.6 GB  AppData/
  ##....................    4.7%       5.5 GB  Documents/

  Total / Toplam: 116.7 GB
```

---

## 🇬🇧 English

### Why?

Every few months everyone asks the same thing: *"Why is my disk full?"*
GUI tools are paid, bloated, or want to "clean" things for you (risky).
`spacehog` is a read-only viewer: it never deletes, never moves, never
"optimizes". It just shows you the truth so *you* decide.

### Features

- Instant size bars with percentages
- `--depth 2` expands the biggest folders one more level (top 5 children each)
- `--files` lists the 10 biggest single files
- `-n N` controls how many rows to show (default 20)
- System noise skipped: `$RECYCLE.BIN`, `System Volume Information`, `.git`, `node_modules`
- Permission errors are shown but never crash the scan

### Install

Python 3.9+ — that's all:

```bash
curl -LO https://raw.githubusercontent.com/Volvox6767/spacehog/main/spacehog.py
```

Single file, **zero dependencies**, works offline.

### Usage

```
python spacehog.py [FOLDER] [-n N] [--depth N] [--files]

FOLDER      folder or drive to scan (default: current dir)
-n N        show top N folders (default 20)
--depth N   expand N levels (default 1; top 5 children per level)
--files     also list the 10 biggest single files
```

### FAQ

**Does it delete anything?** No. Strictly read-only.

**Slow on huge drives?** First scan of a full 1 TB drive takes a minute or two; the biggest folders usually appear near the end of the scan window. Start from `C:\Users\you` instead of `C:\` to find the hog faster.

**Network drives?** Works, but speed depends on the share.

---

## 🇹🇷 Türkçe

### Neden?

Her birkaç ayda bir herkes aynı soruyu sorar: *"Diskim neden doldu?"*
Grafik araçları ya ücretli, ya şişkin, ya da sizin yerinize "temizlik" yapmak
istiyor (riskli). `spacehog` salt okunur bir görüntüleyicidir: hiçbir şey
silmez, taşımaz, "optimize" etmez. Sadece gerçeği gösterir; kararı siz verirsiniz.

### Özellikler

- Yüzdeli, anında boyut çubukları
- `--depth 2` en büyük klasörleri bir seviye daha açar (her birinde ilk 5)
- `--files` en büyük 10 tek dosyayı listeler
- `-n N` gösterilecek satır sayısı (varsayılan 20)
- Sistem gürültüsü atlanır: `$RECYCLE.BIN`, `System Volume Information`, `.git`, `node_modules`
- Erişim hataları gösterilir ama taramayı asla çökertmez

### Kurulum

Python 3.9+ — hepsi bu:

```bash
curl -LO https://raw.githubusercontent.com/Volvox6767/spacehog/main/spacehog.py
```

Tek dosya, **sıfır bağımlılık**, çevrimdışı çalışır.

### Kullanım

```
python spacehog.py [KLASÖR] [-n N] [--depth N] [--files]

KLASÖR       taranacak klasör veya disk (varsayılan: bulunulan klasör)
-n N         en büyük N klasör (varsayılan 20)
--depth N    N seviye aç (varsayılan 1; her seviyede ilk 5)
--files      en büyük 10 dosyayı da listele
```

### SSS

**Bir şey siler mi?** Hayır. Kesinlikle salt okunur.

**Büyük disklerde yavaş mı?** Dolu 1 TB diskin ilk taraması bir-iki dakika sürer; en büyük klasörler genelde tarama penceresinin sonunda belirir. `C:\` yerine `C:\Users\adiniz` ile başlamak domuzu daha hızlı buldurur.

**Ağ sürücüleri?** Çalışır ama hız paylaşıma bağlıdır.

---

Made with ❤ by **Ahmet Gedik** — [instagram.com/ahmetgedik67](https://www.instagram.com/ahmetgedik67)
Follow on Instagram for more free everyday tools.
Daha fazla ücretsiz günlük araç için Instagram'da takip edin.

License / Lisans: [MIT](LICENSE)
