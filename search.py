#!/usr/bin/env python3
import subprocess, shlex, os

def main():
    directory = input("Axtarılacaq qovluq (məs: / və ya /etc): ").strip() or "/"
    term = input("Axtarış sözü (məs: passwd;whoami): ").strip()

    # QƏSDƏN ZƏİF: term quotesuz verilir ki, ';', '&&' işləsin
    # Directory-ni təhlükəsiz saxlamaq üçün yalnız onu quote edirik:
    cmd = f"find {shlex.quote(directory)} -type f -name *{term}*"

    print(f"[debug] icra olunan: {cmd}")
    # shell=True -> OS command injection mümkün
    res = subprocess.run(cmd, shell=True, text=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.stdout: print(res.stdout, end="")
    if res.stderr: print(res.stderr, end="")

    # kim kimi icra edir?
    who = subprocess.run(["id","-un"], text=True, stdout=subprocess.PIPE).stdout.strip()
    euid = os.geteuid()
    print(f"[info] effective uid: {euid} ({who})")

if __name__ == "__main__":
    main()
