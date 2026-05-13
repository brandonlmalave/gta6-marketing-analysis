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

- **Trailer 1 (Dec 2023):** Stock jumped 8.39% — the strongest single reaction, 
likely amplified by the surprise early release due to leaks.

- **Trailer 2 (May 2025):** Another positive 7.87% bump, confirming sustained 
investor confidence tied to marketing momentum.

- **Delay Announcement (May 2026):** The only negative event at -5.97%, 
showing markets punish uncertainty even for a guaranteed blockbuster.

- **Projected Release (Nov 2026):** Estimated 10.26% gain anticipated, 
consistent with Rockstar's historical release performance.

**Pattern:** Take-Two strategically times announcements around earnings calls 
to maintain investor confidence while organic social media amplifies reach, 
reducing traditional marketing spend.
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
    - Marketing event timeline from 2022 to projected 2026 release
    - Percent change calculations to measure market reaction
    
    ## Tools Used
    - **Python** — data processing and application logic
    - **Pandas** — data manipulation and CSV reading
    - **Streamlit** — web application framework
    - **Matplotlib** — data visualization
    
    ## Data Notes
    Stock prices for Trailer 3 Expected and GTA 6 Release are projected estimates 
    based on historical patterns. All other figures are based on publicly reported data.
    
    *Created by Brandon Malave — FTCC, 2026*
    """)