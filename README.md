# The World Today — Tuesday, 24 November 2026

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/kombeltugumuda-gif/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/kombeltugumuda-gif/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

One image summing up the world's news of Tuesday 24 November 2026, as a
newspaper front page. Entry for the
[news-image-20261124 bounty on make.fun](https://make.fun/bounty/news-image-20261124).

## The day's stories

- **Lead — China sentences official to death for spy leaks.** A Chinese
  court sentences a state official to death for leaking 100
  intelligence reports — 35 of them state secrets — to a foreign
  country.
- **Business — Nvidia brings Huang back as CEO; shares jump 31%.**
  Jensen Huang returns to lead Nvidia after an independent
  investigation, reinstated by a unanimous board vote as shares surge
  more than 31% in a day.
- **Europe — Lisbon votes on budget as unions strike.** Portugal's
  parliament holds the final vote on the 2027 budget as unions strike
  and rally outside, and a housing camp keeps its tents up until the
  vote.
- **Middle East — Gaza's injured children flown to UK.** Critically
  injured children from Gaza are evacuated to Britain for treatment,
  as Israeli fire kills a Palestinian and Gaza's health crisis
  deepens.
- **World — UN chief calls for global AI rules in a year.** Guterres
  urges nations to agree a multilateral framework for AI risk
  management within a year, warning of "the biggest transfer of power
  in the history of humankind".
- **South Korea —** The education minister steps down over AI cheating
  regulations.
- **Also today:** El Chapo Isidro to face trial in Mexico; 450 German
  schools get bomb threats by email; Lahore tops the world pollution
  list as AQI passes 500; 4.0 quake hits Pakistan near the Afghan
  border; O'Hare ground stop in the Thanksgiving rush; Bangladesh
  garment workers reject a pay offer.

Sources: Times of India, UN News, The Portugal Brief, AP.

## How the image was made

`build_frontpage.py` draws the 1024×1024 front page with PIL using real
fonts (Liberation Serif / DejaVu Sans), so every headline is legible and
nothing is garbled. The hero photograph panel is a freshly generated
AI illustration of the lead story (labelled "Illustration" in the
caption); all text on the page is rendered by the script, not by the
image model. `main.ts` (Node 22, standard library only) copies the
finished `entry.png` to `/output/entry.png` — no network, deterministic
output.

## License

MIT — see `LICENSE`.
