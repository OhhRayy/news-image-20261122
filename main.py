"""Morning Edition: the world news of Sunday 22 November 2026, in one image.

This program writes the entry image to ``entry.png`` in the output
folder. The image itself is ``entry.png`` in this repository: a
single-page newspaper front page, "THE WORLD IN ONE PAGE", drawn by
``draw.py`` (PIL) from six stories that were first reported on Sunday
22 November 2026:

1. BAHRAIN -- Iran's Revolutionary Guards fired missiles and drones
   at US military positions in Bahrain; Bahrain said on Sunday that a
   civilian industrial facility was hit and caught fire, no one was
   hurt, and air defences intercepted other attacks (Reuters / AFP).
2. COP31 -- climate talks in Antalya entered a second day of overtime
   on Sunday; a last-minute draft deal still fails to name fossil
   fuels (Reuters).
3. INDONESIA -- rescuers searched on Sunday for 36 workers missing
   after a fire at a candy factory in Serang, west of Jakarta; three
   were killed (AFP / Reuters).
4. NVIDIA -- the board will not bring back former chief Jensen Huang;
   US Treasury chief Scott Bessent demanded answers on chip sales to
   China in a Sunday TV interview (FT / CNBC).
5. CAMBODIA -- first new mpox case in two and a half years, confirmed
   by the Health Ministry on Sunday; the patient is in hospital
   (Xinhua).
6. CALIFORNIA -- record-high king tides run along the coast from
   Sunday to Thursday, with El Nino storms behind them; San
   Francisco's mayor urged residents to avoid non-essential travel
   (IANS / NWS).

Only the Python standard library is used. The program copies the
shipped image byte for byte, so two runs write byte-identical files.

The output folder comes from the ``MAKEFUN_OUTPUT_DIR`` environment
variable and falls back to ``/output`` when it is absent. Written for
Python 3.13, standard library only.
"""

import hashlib
import os
import sys
from pathlib import Path


def out_folder():
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    folder = Path(raw)
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def main():
    here = Path(__file__).resolve().parent
    data = (here / "entry.png").read_bytes()
    target = out_folder() / "entry.png"
    target.write_bytes(data)
    print(f"entry ready: {target} ({len(data)} bytes)")
    print(f"SHA-256: {hashlib.sha256(data).hexdigest()}")
    print("size: 1024x1024")
    return 0


if __name__ == "__main__":
    sys.exit(main())
