"""Sunday Edition: the world news of Sunday 22 November 2026, in one image.

This program writes the entry image to ``entry.png`` in the output
folder. The image itself ships in this repository as ``entry.png``: a
single-page newspaper front page, "THE WORLD IN ONE PAGE", drawn by
``draw.py`` with Pillow. This program only copies those bytes, so both
runs produce identical output. No network, no clock, no randomness.

The six stories on the page, all first reported Sunday 22 Nov 2026:
1. COP31 collapses with no deal (Antalya) - WRI; Reuters via Sowetan.
2. 186 Russian drones strike overnight; apartment block near Kyiv
   collapses - 112.ua; EuropeSays.
3. Nepal PM Balendra Shah arrives in Delhi for a two-day state visit
   - IANS; New Kerala.
4. India declare at 720/9 vs New Zealand, Wellington (day four)
   - GeoSuper/AFP; ESPNcricinfo.
5. Candy factory fire in Cikande, Serang, Banten: 3 dead, 36-50
   workers missing - AP; Reuters.
6. South Korea education minister Choi Kyo-jin resigns over Suneung
   AI-cheating chaos - Korea JoongAng Daily; TBS News.
"""

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(SRC, dest)
    data = dest.read_bytes()
    print(f"wrote {dest}  {len(data)} bytes")
    print(f"sha256 {hashlib.sha256(data).hexdigest()}")


if __name__ == "__main__":
    main()
