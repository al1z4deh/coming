#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path

def find_by_name(directory: str, term: str):
    # find <dir> -type f -name "*term*"
    pattern = f"*{term}*"
    try:
        res = subprocess.run(
            ["find", directory, "-type", "f", "-name", pattern],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        return [line for line in res.stdout.splitlines() if line.strip()]
    except subprocess.CalledProcessError as e:
        print(f"[find] xəta: {e.stderr.strip()}")
        return []

def main():
    # İstifadəçidən yalnız qovluq və axtarış termini alınır
    directory = input("Axtarılacaq qovluq (məs: / və ya /etc): ").strip() or "/"
    term = input("Axtarış sözü (məs: passwd): ").strip()

    if not term:
        print("[x] Axtarış sözü boş ola bilməz.")
        return

    # Kim kimi icra edir – informasiya üçün (sudoers ilə root olmalıdır)
    try:
        euid = os.geteuid()
        who = subprocess.check_output(["id", "-u", "-n"], text=True).strip()
        print(f"[info] effective uid: {euid} ({who})")
    except Exception:
        pass

    print(f"\n[find] '{directory}' içində adında '{term}' olan fayllar:")
    files = find_by_name(directory, term)
    if files:
        for f in files:
            print(f"  - {f}")
    else:
        print("  (heç nə tapılmadı)")

if __name__ == "__main__":
    main()
