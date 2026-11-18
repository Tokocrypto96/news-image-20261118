# World News — Wednesday, 18 November 2026

A one-image summary of the world's news on Wednesday 18 November 2026,
for the make.fun competition
[news-image-20261118](https://make.fun/bounty/news-image-20261118)
("Sum up 18 November's world news in one image").

## The image

`entry.png` (1024×1024, PNG) is a newspaper front page with the day's
four biggest stories, each with an illustration, a headline and a
one-line summary:

1. **Middle East — Gulf on edge.** US jets struck a Revolutionary Guard
   missile site on Qeshm Island, Iran; Iran answered with drones at US
   bases in Bahrain and Kuwait.
2. **Ukraine — War.** Ukraine hit the Kerch Bridge to Crimea for a second
   day; a road span collapsed into the strait.
3. **Diplomacy — Shenzhen.** Trump, Xi and Putin meet in Shenzhen for the
   first-ever trilateral summit on 19 November, as APEC opens in the city
   and the QUAD gathers in Manila.
4. **Health — DR Congo.** The Ebola outbreak more than doubled: over
   11,000 cases and 5,400 deaths, the UN says; three in four infected
   children under five do not survive.

The four illustrations are AI-generated; the facts were checked against
Reuters / AP / AFP / UN reporting of 18 November 2026.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the
bundled `entry.png` to `/output/entry.png`. It is deterministic: running
it twice writes the same bytes both times.

```sh
python3 main.py   # writes /output/entry.png
```

## License

MIT — see `LICENSE`.
