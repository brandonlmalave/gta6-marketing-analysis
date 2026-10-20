# GTA 6 Marketing Analysis

An interactive Streamlit dashboard that looks at how Take-Two Interactive's stock (TTWO) reacted to major GTA 6 marketing milestones: the development confirmation, trailers, and the release delay.

## Why I Built This

This is a personal project, not a class assignment. I've followed Rockstar for years, and I've always been interested in how they market their games. They spend very little on traditional advertising, yet every trailer becomes a global event. I wanted to see whether that hype shows up in hard numbers, so I started with the most measurable signal I could find: how Take-Two's stock moved after each major announcement.

It was also a chance to practice turning a question I actually care about into data, analysis, and a working app.

## Hypothesis

Rockstar Games and Take-Two Interactive follow a deliberate, repeatable marketing pattern, using controlled reveals, strategic delays, and earnings call timing to keep both investor confidence and player excitement high.

This first version tests one part of that idea: **how the stock price moved around each major GTA 6 event.**

## What It Does

- Loads a hand-built timeline of eight GTA 6 milestones from `gta6_data.csv`
- Shows TTWO's stock price before and after each event
- Calculates and charts the percent change for each event
- Explains the findings, methodology, and data limits in the app

## Key Findings

| Event | Date | Change |
|---|---|---|
| Development confirmed | Feb 2022 | +2.43% |
| Trailer 1 (leaked early) | Dec 2023 | **+8.39%**, the strongest reaction |
| Trailer 2 | May 2025 | +7.87% |
| Delay announced | 2026 | **−5.97%** |
| Gameplay leaks | Aug 2026 | **−5.47%** over the week the leaks spread |
| Extended Look (Trailer 3) | Aug 2026 | +1.03% at close (about +3% intraday) |
| Trailer 4 | Oct 2026 | +4.05% |
| Release | Nov 2026 | +10.26% *(projected)* |

**Takeaways:**
- The first two trailers produced the strongest gains, with Trailer 1 the largest, likely boosted by the surprise of the early leak.
- Later reveals moved the stock less. The Extended Look jumped about 3% during the day but closed only 1% higher, which suggests the market had already priced in much of the hype by 2026.
- Leaks cut both ways. The 2023 leak came right before a big gain, but the August 2026 gameplay leaks were followed by a drop of over 5%.
- Negative surprises (the delay and the 2026 leaks) hit the stock about as hard as the best trailers lifted it.

**Projection check:** an earlier version of this dataset projected a +3.17% move for Trailer 3. The real result was about +3% intraday and +1.03% at close: close on the intraday move, but too high for the closing price.

> **Note on the projected row:** "GTA 6 Release" uses estimated prices, not real market data. Treat it as a prediction, not a result.

> **How changes are measured:** each row compares the closing price before the event with the closing price after it. The gameplay leaks row covers a multi-day window (Aug 14 to Aug 26 closes) because the leaks spread over several days.

## Project Structure

```
gta6-marketing-analysis/
├── app.py            # Streamlit dashboard (3 pages)
├── launcher.py       # Windows launcher: starts the app and opens the browser
├── gta6_data.csv     # Event timeline with TTWO prices before and after
├── requirements.txt  # Python dependencies
└── README.md
```

## Dashboard Pages

1. **Overview & Timeline:** the full event table and a line chart of TTWO's price before and after each event
2. **Stock Analysis:** a bar chart of percent change per event, with written analysis
3. **About This Project:** hypothesis, methodology, tools, and data notes

## Running the App

**Requirements:** Python 3.8+

```bash
git clone https://github.com/brandonlmalave/gta6-marketing-analysis.git
cd gta6-marketing-analysis
pip install -r requirements.txt
streamlit run app.py
```

Then open `http://localhost:8501` if it doesn't open automatically.

**On Windows**, you can also run:

```bash
python launcher.py
```

It starts the app in a new console window and opens your browser.

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Data processing and app logic |
| pandas | Reading and shaping the CSV data |
| Streamlit | The dashboard and its built-in charts |
| CSV | Data storage |

## Future Work

The full hypothesis covers more than this version measures. Next steps:

- **Earnings call timing:** add Take-Two's earnings call dates and measure how close each reveal falls to one
- **Organic vs. paid reach:** add trailer view counts and social engagement data
- **Franchise comparison:** add the same event timeline for earlier Rockstar releases (GTA V, Red Dead Redemption 2) to test whether the pattern repeats
- **Better price data:** use daily closing prices from a market data source instead of hand-entered values, and compare TTWO's moves against the overall market

## Author

**Brandon Malave**
IT & Computer Programming, Fayetteville Technical Community College
[GitHub](https://github.com/brandonlmalave)

*For educational and portfolio purposes. Historical prices are from public records; projected rows are estimates.*
