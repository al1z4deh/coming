#!/usr/bin/env python3
import subprocess

def main():
    directory = input("Axtarılacaq qovluq (məs: /): ").strip() or "/"
    term = input("Axtarış sözü (məs: passwd): ").strip()

    # QƏSDƏN zəif: shell=True istifadə olunur
    find_command = f"find {directory} -type f -name '*{term}*'"
    print(f"[debug] icra olunan: {find_command}")

    try:
        result = subprocess.run(find_command, shell=True,
                                check=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"xəta: {e.stderr}")

if __name__ == "__main__":
    main()
