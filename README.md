# Morning Edition

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/OhhRayy/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/OhhRayy/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

Entry for the make.fun bounty
[news-image-20261122](https://make.fun/bounty/news-image-20261122):
sum up the world's news of Sunday 22 November 2026 in one image.

This is the morning edition, built about six hours into the UTC day:
every story below was first reported on Sunday 22 November 2026.

## What the image shows

"Morning Edition" is a single-page newspaper front page for
Sunday, 22 November 2026. Six stories from that day share the page,
chosen for breadth across regions and topics:

- **Iran's missiles hit Bahrain.** Bahrain on Sunday condemned
  Iranian missile and drone strikes on US military positions. A
  civilian industrial facility was hit and caught fire; no one was
  hurt. Air defences intercepted other attacks. (Reuters / AFP, 22 Nov)
- **COP31 talks drag into overtime.** Climate talks in Antalya
  entered a second day of overtime on Sunday. A last-minute draft
  deal still fails to name fossil fuels. (Reuters, 22 Nov)
- **36 still missing after factory fire.** Rescuers in Indonesia
  searched on Sunday for 36 workers missing after a fire at a candy
  factory in Serang, west of Jakarta. Three were killed.
  (AFP / Reuters, 22 Nov)
- **Nvidia board rejects Huang comeback.** Nvidia's board will not
  bring back former chief Jensen Huang. US Treasury chief Scott
  Bessent demanded answers on chip sales to China in a Sunday TV
  interview. (FT / CNBC, 22 Nov)
- **Mpox back in Cambodia after 30 months.** Cambodia confirmed its
  first new mpox case in two and a half years on Sunday; the patient
  is in hospital. (Xinhua, 22 Nov)
- **California braces for king tides.** Record-high king tides run
  along California's coast from Sunday to Thursday, with El Nino
  storms behind them. San Francisco's mayor urged residents to avoid
  non-essential travel. (IANS / NWS, 22 Nov)

## How it works

`draw.py` paints the page with PIL (DejaVu fonts, flat drawn emblems,
one per story) and writes `entry.png`. `main.py` (Python 3.13,
standard library only) copies that image to the output folder byte
for byte, so two runs produce byte-identical output.

Verified locally: two runs into separate directories produced
byte-identical copies of entry.png (SHA-256
`5568fe94a2982c9d18c083de9c6961fcd480b6a81287e131bde28cda3834ac1f`),
1024x1024 pixels, 135,538 bytes (limit 1 MiB).

Run it locally with:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
