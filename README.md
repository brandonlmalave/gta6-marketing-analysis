📊 GTA 6 Marketing Analysis

A data-driven look at Take-Two Interactive's marketing strategy leading up to GTA 6 — tracking stock movement, announcement timing, and the mechanics behind one of the most anticipated releases in entertainment history.


🔍 What This Project Does
This project analyzes how Take-Two Interactive (TTWO) has strategically managed its GTA 6 marketing campaign by examining:

Stock price movement around key announcements (trailers, leaks, delay announcements)
Earnings call alignment — how Rockstar times reveals around investor events
Organic vs. paid reach — GTA's social media footprint without traditional advertising
Release timing patterns across the GTA and Red Dead Redemption franchises

Built as a portfolio project combining Python data analysis with an interactive Streamlit dashboard.

🗂️ Project Structure
gta6-marketing-analysis/
├── app.py              # Streamlit dashboard (main application)
├── launcher.py         # App launcher script
├── gta6_data.csv       # Core dataset (key events, stock data, dates)
├── requirements.txt    # Python dependencies
└── README.md

📈 Key Findings

Trailer 1 (Dec 2023): TTWO stock jumped +8.39% — the strongest single-event reaction, amplified by a surprise early leak
Trailer 2 (May 2025): Another +7.87% gain, confirming sustained investor confidence tied to marketing momentum
Delay Announcement (May 2026): The only negative event at -5.97%, showing markets punish uncertainty even for a guaranteed blockbuster
Projected Release (Nov 2026): Historical Rockstar release patterns suggest an estimated +10.26% gain anticipated

Pattern: Take-Two consistently times major announcements around earnings calls to maintain investor confidence, while organic social media reach reduces reliance on traditional paid marketing.

🚀 Running the App
Prerequisites

Python 3.8+
pip

Setup
bash# Clone the repo
git clone https://github.com/brandonlmalave/gta6-marketing-analysis.git
cd gta6-marketing-analysis

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
Or use the launcher:
bashpython launcher.py

🛠️ Tech Stack
ToolPurposePythonCore analysis and data processingpandasData manipulationStreamlitInteractive dashboardmatplotlibCharts and visualizationsCSV / ExcelData storage

📌 Pages

Overview & Timeline — Full event table with TTWO stock price before/after each milestone
Stock Analysis — Bar chart of percent change per key event with written analysis
About This Project — Hypothesis, methodology, and project context


🧠 Hypothesis

Rockstar Games and Take-Two Interactive use a deliberate, earnings-aligned announcement strategy that maximizes organic reach and investor confidence — making GTA 6 one of the most efficiently marketed products in entertainment history.


👤 Author
Brandon Malave
IT & Computer Programming | Fayetteville Technical Community College
GitHub

This project is for educational and portfolio purposes. All stock data sourced from public financial records.
