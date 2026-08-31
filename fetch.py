"""
Fetches every page in corpus.py as raw markdown and caches it to raw/.
No API key needed -- run this first to pull down the corpus.
"""

import pathlib
import sys
import time

import truststore

truststore.inject_into_ssl()  # use the OS trust store (needed behind SSL-inspecting proxies)

import requests

from corpus import URLS

RAW_DIR = pathlib.Path(__file__).parent / "raw"


def slug_for(url: str) -> str:
    path = url.split("/docs/", 1)[1].removesuffix(".md")
    return path.replace("/", "__") + ".md"


def main():
    RAW_DIR.mkdir(exist_ok=True)
    ok, failed = 0, []

    for url in URLS:
        out_path = RAW_DIR / slug_for(url)
        try:
            resp = requests.get(url, timeout=15)
            resp.raise_for_status()
            out_path.write_text(resp.text, encoding="utf-8")
            ok += 1
            print(f"  fetched  {url}")
        except requests.RequestException as e:
            failed.append((url, str(e)))
            print(f"  FAILED   {url} -- {e}")
        time.sleep(0.2)  # be polite

    print(f"\n{ok}/{len(URLS)} pages fetched into {RAW_DIR}/")
    if failed:
        print(f"{len(failed)} failed:")
        for url, err in failed:
            print(f"  - {url}: {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
