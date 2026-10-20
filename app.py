import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

st.set_page_config(page_title="GTA 6 Marketing Analysis", layout="wide")

# Sidebar navigation
page = st.sidebar.selectbox("Navigate", ["Overview & Timeline", "Stock Analysis", "About This Project"])

if page == "Overview & Timeline":
    st.title("📊 GTA 6 Marketing Timeline Analysis")
    st.write("A data-driven look at Take-Two Interactive's marketing strategy for GTA 6.")
    
    df = pd.read_csv(resource_path("gta6_data.csv"))
    
    st.subheader("Key Events")
    st.dataframe(df)
    
    st.subheader("📈 Take-Two Stock Price Over Time")
    st.write("How the stock price moved across major GTA 6 milestones.")
    
    chart_data = df.set_index("Date")[["TTWO_Price_Before", "TTWO_Price_After"]]
    st.line_chart(chart_data)

elif page == "Stock Analysis":
    st.title("📈 Take-Two Stock Movement")
    st.write("How did Take-Two's stock price react to major GTA 6 announcements?")
    
    df = pd.read_csv(resource_path("gta6_data.csv"))
    st.subheader("Stock % Change Around Key Events")
    st.bar_chart(df.set_index("Event")["Percent_Change"])

    st.subheader("📝 Analysis")
    st.write("""
**Key Findings:**

- **Trailer 1 (Dec 2023):** Stock jumped 8.39%, the strongest single reaction,
likely amplified by the surprise early release due to leaks.

- **Trailer 2 (May 2025):** Another strong 7.87% gain, showing investor
confidence tied to marketing momentum.

- **Delay Announcement (2026):** A -5.97% drop, showing markets punish
uncertainty even for a guaranteed blockbuster.

- **Gameplay Leaks (Aug 2026):** A -5.47% slide over the week the leaks spread.
Unlike the 2023 leak, which came right before a big gain, these leaks hurt the stock.

- **Extended Look / Trailer 3 (Aug 2026):** The 26-minute gameplay video pushed
the stock up about 3% during the day, but it closed only 1.03% higher.

- **Trailer 4 (Oct 2026):** A 4.05% gain, a solid bump but still below the
first two trailers.

- **Projected Release (Nov 2026):** An estimated 10.26% gain. This row is a
projection, not real market data.

**Pattern:** The early trailers moved the stock the most, and later reveals
moved it less, which suggests much of the hype was already priced in by 2026.
Negative surprises like the delay and the 2026 leaks hit the stock about as
hard as the best trailers lifted it.

**Projection check:** An earlier version of this dataset projected +3.17% for
Trailer 3. The real move was about +3% intraday and +1.03% at close.
""")
elif page == "About This Project":
    st.title("🎮 About This Project")
    st.write("""
    ## Hypothesis
    Rockstar Games and Take-Two Interactive follow a deliberate, repeatable 
    marketing pattern across their major releases — using controlled information 
    releases, strategic delays, and earnings call timing to maximize both investor 
    confidence and consumer excitement.
    
    ## Methodology
    This application analyzes publicly available data including:
    - Take-Two Interactive (TTWO) stock prices around key GTA 6 announcements
    - Marketing event timeline from 2022 to the projected November 2026 release
    - Percent change from the closing price before each event to the closing
      price after it (the gameplay leaks row covers Aug 14 to Aug 26, 2026)
    
    ## Tools Used
    - **Python** — data processing and application logic
    - **Pandas** — data manipulation and CSV reading
    - **Streamlit** — web application framework
    - **Streamlit charts** — data visualization

    ## Data Notes
    Stock prices for GTA 6 Release are projected estimates. All other figures
    are based on publicly reported closing prices.
    
    *Created by Brandon Malave — FTCC, 2026*
    """)
