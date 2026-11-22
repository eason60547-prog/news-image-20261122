# The World in One Day — 22 November 2026

[![make.fun](https://make.fun/badge.svg)](https://make.fun)
[![news-image-20261122](https://make.fun/c/news-image-20261122/badge.svg)](https://make.fun/c/news-image-20261122)
[![Sunday 22 November 2026](https://make.fun/c/news-image-20261122/date.svg)](https://make.fun/c/news-image-20261122)

A one-page newspaper front page summing up Sunday 22 November 2026,
drawn with PIL and nothing else.

## The day's news

- **Strait of Hormuz (lead story):** two tankers were hit on 21 November —
  Torkel at the stern at 05:00 UTC, Arina in the engine room at 05:50 UTC.
  No one was hurt. On 22 November Torkel was still burning and Bahrain
  took the attacks to the UN Security Council. The cause is disputed;
  claims the ships hit mines are unverified.
- **COP31:** talks ran into overtime with still no agreement, and a draft
  text drops the fossil-fuel wording.
- **Ukraine:** President Zelenskyy seeks four-party talks — a proposal,
  not a meeting that has taken place.
- **Peru:** a magnitude 6.7 earthquake struck on 20 November.
- **Also today:** a three-party meeting in Shenzhen on 19 November;
  cargo ship Sparta II was attacked on 21 November.

## How it works

- `draw.py` draws the front page with PIL (1024×1024 PNG).
  Run `python3 draw.py` to regenerate `entry.png`.
- `main.py` (standard library only) copies `entry.png` to
  `/output/entry.png`, so both runs write identical bytes.

## License

MIT — see `LICENSE`.
