#!/usr/bin/env python3
"""
spacehog - Find what is eating your disk space. Offline, one file, zero deps.

EN: "Where did my free disk space go?" - spacehog scans a folder tree and
    shows the biggest folders and files, sorted by size, with a share bar.
    Read-only. 100% offline. No install.
TR: "Disk alanim nereye gitti?" - spacehog bir klasor agacini tarar ve en
    buyuk klasor/dosyalari boyuta gore siralayarak gosterir. Salt okunur,
    %100 cevrimdisi, kurulum gerektirmez.
"""

import argparse
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

AUTHOR = "Ahmet Gedik"
INSTAGRAM = "https://www.instagram.com/ahmetgedik67"
VERSION = "1.0.0"

SKIP_NAMES = {"$RECYCLE.BIN", "System Volume Information", ".git", "node_modules"}


def human(n):
    n = float(n)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if abs(n) < 1000 or unit == "TB":
            return f"{int(n)} B" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1000


def scan(path):
    """Return (total_size, [ (child_path, child_size) ]). Never raises."""
    total = 0
    children = {}
    try:
        entries = list(os.scandir(path))
    except OSError as e:
        print(f"  ? cannot read / okunamadi: {path} ({e.__class__.__name__})")
        return 0, []

    for e in entries:
        try:
            if e.is_symlink():
                continue
            if e.is_file():
                total += e.stat().st_size
            elif e.is_dir():
                if e.name in SKIP_NAMES:
                    continue
                d, kids = scan(e.path)
                total += d
                children[e.path] = (d, kids)
        except OSError:
            continue  # permission denied etc. / erisim reddi vb.

    return total, children


def bar(pct, width=24):
    """pct is a percentage 0-100. Returns a fixed-width share bar."""
    filled = max(0, min(width, int(round(pct / 100 * width))))
    return "#" * filled + "." * (width - filled)


def pick_bigger(pairs, min_size):
    return [(p, s) for p, s in pairs if s >= min_size]


def main():
    ap = argparse.ArgumentParser(
        prog="spacehog",
        description="Find what is eating your disk space - read-only, offline. / "
                    "Disk alanini yiyeni bulur - salt okunur, cevrimdisi.",
        epilog=f"Made with \u2764 by {AUTHOR} - {INSTAGRAM}\nVersion {VERSION} (MIT)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("folder", nargs="?", default=os.getcwd(),
                    help="folder to scan (default: current dir) / taranacak klasor (varsayilan: bulunulan)")
    ap.add_argument("-n", metavar="N", type=int, default=20,
                    help="show top N items (default 20) / en buyuk N oge")
    ap.add_argument("--files", action="store_true",
                    help="also list the biggest single files / en buyuk tek dosyalari da listele")
    ap.add_argument("--depth", type=int, default=1, metavar="N",
                    help="how many folder levels to expand (default 1) / kac klasor seviyesi")
    ap.add_argument("--version", action="version", version=f"spacehog {VERSION}")
    args = ap.parse_args()

    root = os.path.abspath(args.folder)
    if not os.path.isdir(root):
        print(f"ERROR: not a folder / klasor degil: {root}")
        sys.exit(1)

    print(f"Scanning / Taranıyor: {root}  ...\n")
    total, children = scan(root)
    if total == 0:
        print("Empty or unreadable / bos ya da okunamadi.")
        sys.exit(0)

    flat = sorted(children.items(), key=lambda kv: kv[1][0], reverse=True)
    shown = 0
    for path, (size, kids) in flat:
        if shown >= args.n or size == 0:
            break
        pct = size / total * 100
        print(f"  {bar(pct)} {pct:5.1f}%  {human(size):>9}  {os.path.basename(path)}{os.sep}")
        shown += 1
        if args.depth > 1 and kids:
            sub = sorted(kids.items(), key=lambda kv: kv[1][0], reverse=True)
            sub_shown = 0
            for spath, (ssize, _skids) in sub:
                if sub_shown >= 5 or ssize == 0:
                    break
                spct = ssize / size * 100 if size else 0
                print(f"      {bar(spct, 12)} {spct:5.1f}%  {human(ssize):>9}  {os.path.basename(spath)}{os.sep}")
                sub_shown += 1
            if len(sub) > 5:
                print(f"      ... and {len(sub) - 5} more / ve {len(sub) - 5} kalan")

    # biggest single files
    if args.files:
        bigfiles = []
        for dirpath, _dirnames, filenames in os.walk(root):
            parts = set(dirpath[len(root):].split(os.sep))
            if parts & SKIP_NAMES:
                continue
            for fn in filenames:
                fp = os.path.join(dirpath, fn)
                try:
                    if not os.path.islink(fp):
                        bigfiles.append((fp, os.path.getsize(fp)))
                except OSError:
                    continue
        bigfiles.sort(key=lambda t: t[1], reverse=True)
        print(f"\n  Biggest files / En buyuk dosyalar:")
        for fp, sz in bigfiles[:10]:
            pct = sz / total * 100
            print(f"    {pct:5.1f}%  {human(sz):>9}  {fp}")

    print(f"\n  Total / Toplam: {human(total)} in / icinde {root}")
    print(f"\n  Read-only tool: nothing was modified. / Salt okunur: hicbir sey degistirilmedi.")
    print(f"\nMade with \u2764 by {AUTHOR} - {INSTAGRAM}")


if __name__ == "__main__":
    main()
