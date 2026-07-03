"""Home page module for Sales Hub dashboard."""
import streamlit as st
from datetime import datetime


def render_home() -> None:
    """Render the Sales Hub home page with preview cards."""
    st.markdown(
        """
        <div style='padding: 18px 0 10px 0; text-align: center;'>
                <h1 style='margin:0; font-size: 44px; letter-spacing: 0.02em; color:#ffffff;'>WELCOME TO SALES DASHBOARD</h1>
            <p style='margin:8px 0 0 0; font-size: 16px; color:#d8d8ff;'>
                Welcome to the Dashboard Hub. Select a page preview card below to explore.
            </p>
        </div>
        <style>
            .preview-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 18px;
                margin-top: 24px;
            }
            .preview-card {
                display: block;
                padding: 24px;
                border-radius: 20px;
                border: 1px solid rgba(255,255,255,0.14);
                background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02));
                color: #ffffff !important;
                text-decoration: none !important;
                box-shadow: 0 18px 40px rgba(0,0,0,0.28);
                transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
            }
            .preview-card:hover {
                transform: translateY(-3px);
                border-color: rgba(255,255,255,0.26);
                box-shadow: 0 24px 60px rgba(0,0,0,0.4);
            }
            .preview-card h3 {
                margin: 0 0 12px 0;
                color: #ffffff;
                font-size: 26px;
            }
            .preview-card p {
                margin: 0;
                color: #d8d8ff;
                line-height: 1.6;
            }
            .preview-card .preview-tag {
                display: inline-flex;
                margin-top: 18px;
                padding: 8px 14px;
                border-radius: 999px;
                background: rgba(255,255,255,0.08);
                color: #ffffff;
                font-size: 13px;
                letter-spacing: 0.04em;
                text-transform: uppercase;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    _, col_time = st.columns([3, 1])
    with col_time:
        current_time = datetime.now().strftime("%a, %b %d, %I:%M %p")
        st.markdown(
            f"<div style='text-align: right;'><strong>{current_time}</strong><br><span style='font-size:11px; color:#ffffff;'>SYSTEM LAST SNAPSHOT</span></div>",
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class='preview-grid'>
            <a class='preview-card' href='?page=TARGET%20vs%20ACTUAL'>
                <h3>TARGET vs ACTUAL</h3>
                <p>View performance vs quota, growth trends and store-level target coverage in one page.</p>
                <div class='preview-tag'>Open target dashboard</div>
            </a>
            <a class='preview-card' href='?page=EMPLOYEE%20PERFORMANCE'>
                <h3>EMPLOYEE PERFORMANCE</h3>
                <p>Explore individual rep results, KPI summaries, and top performer analytics.</p>
                <div class='preview-tag'>Open employee dashboard</div>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )
