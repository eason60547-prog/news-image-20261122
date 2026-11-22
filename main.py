"""Entrypoint: copy the drawn front page to /output/entry.png.

Standard library only. No network, no randomness: the output bytes
are exactly the entry.png this repository ships.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"),
                    os.path.join(out_dir, "entry.png"))

if __name__ == "__main__":
    main()
