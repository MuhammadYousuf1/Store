# PowerShell script to overwrite modified files if you can't use git
# Run this from the project root (where these files live).

$files = @{
    "home.py" = @'
"""Home page module for Sales Hub dashboard."""
import streamlit as st
from datetime import datetime


def render_home() -> None:
    """Render the Sales Hub home page with preview cards."""
    st.markdown(
        """
        <div style='padding: 18px 0 10px 0; text-align: center;'>
            <h1 style='margin:0; font-size: 44px; letter-spacing: 0.02em; color:#ffffff;'>WELCOME TO SOFT-RAPIDO WIRELESS</h1>
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
'@

    "target_vs_actual.py" = @'
' + (Get-Content -Raw 'e:\Python\target_vs_actual.py') + "'"

    "employee_performance.py" = @'
' + (Get-Content -Raw 'e:\Python\employee_performance.py') + "'"
}

foreach ($name in $files.Keys) {
    $path = Join-Path (Get-Location) $name
    Write-Host "Writing $path"
    Set-Content -Path $path -Value $files[$name] -Encoding UTF8
}

Write-Host "Files written. Run 'python -m streamlit run app.py' to verify."# PowerShell script to apply updated files to the workspace
# Run from PowerShell with: .\apply_changes.ps1

$files = @{
    "e:\\Python\\home.py" = @"
"""Home page module for Sales Hub dashboard."""
import streamlit as st
from datetime import datetime


def render_home() -> None:
    """Render the Sales Hub home page with preview cards."""
    st.markdown(
        """
        <div style='padding: 18px 0 10px 0; text-align: center;'>
            <h1 style='margin:0; font-size: 44px; letter-spacing: 0.02em; color:#ffffff;'>WELCOME TO SOFT-RAPIDO WIRELESS</h1>
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
"@

    "e:\\Python\\target_vs_actual.py" = @"
"""
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime


def render_target_vs_actual() -> None:
    """Renders the Target vs Actual Performance Dashboard."""

    df = pd.read_excel("PB GROWTH%.xlsx", engine="openpyxl")

    def get_status(pb):
        if pd.isna(pb):
            return "No Data"
        if pb >= 1.0:
            return "Exceeding"
        elif pb >= 0.75:
            return "On Track"
        elif pb >= 0.50:
            return "Behind"
        return "At Risk"

    status_series = df["PB Growth%"].apply(get_status)
    if "PB Growth%" in df.columns:
        pb_idx = df.columns.get_loc("PB Growth%")
        df.insert(pb_idx + 1, "Status", status_series)
    else:
        df["Status"] = status_series

    col_title, col_time = st.columns([2, 1])
    with col_title:
        st.markdown(
            "# TARGET VS <span style='color:#00e5ff'>ACTUAL</span>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "#### REPORTING PERIOD · CURRENT CYCLE",
            unsafe_allow_html=True,
        )

    with col_time:
        current_time = datetime.now().strftime("%a, %b %d, %I:%M %p")
        st.markdown(
            f"<div style='text-align: right;'><strong>{current_time}</strong><br><span style='font-size:11px; color:#ffffff;'>SYSTEM LAST SNAPSHOT</span></div>",
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # Safely handle NaNs for aggregates to avoid numpy runtime warnings
    total_quota = int(df[["Voice Line", "BTS", "HSI", "ELB Quota"]].fillna(0).sum().sum())
    total_act = int(df["Tot Act"].fillna(0).sum())
    avg_pb = df["PB Growth%"].dropna().mean()
    if pd.isna(avg_pb):
        avg_pb = 0.0
    avg_ret = df["95 Days Act Retention"].dropna().mean()
    if pd.isna(avg_ret):
        avg_ret = 0.0
    avg_mim = df["MIM"].dropna().mean()
    if pd.isna(avg_mim):
        avg_mim = 0.0
    exceeding_count = int((df["PB Growth%"].fillna(0) >= 1.0).sum())

    if avg_pb >= 1.0:
        PB_TARGET = "On Target"
    elif avg_pb >= 0.75:
        PB_TARGET = "Near Target"
    else:
        PB_TARGET = "Below Target"

    st.markdown(
        """
    <style>
        .metric-grid {
            display: grid;
            grid-template-columns: repeat(6, 1fr);
            gap: 16px;
            margin-bottom: 20px;
        }

        @media (max-width: 1200px) {
            .metric-grid { grid-template-columns: repeat(3, 1fr); }
        }
        @media (max-width: 768px) {
            .metric-grid { grid-template-columns: repeat(2, 1fr); }
        }
        @media (max-width: 400px) {
            .metric-grid { grid-template-columns: repeat(1, 1fr); }
        }

        .metric-box {
            background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(167,139,250,0.06));
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px;
            padding: 14px 18px;
            text-align: center;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.35);
            backdrop-filter: blur(6px);
            transition: transform 160ms ease, box-shadow 160ms ease;
            min-height: 84px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            width: 100%; 
            box-sizing: border-box;
        }
        .metric-box:hover {
            transform: translateY(-6px);
            box-shadow: 0 14px 36px rgba(0,0,0,0.5);
            border: 2px solid #ffffff;
        }
        .metric-label {
            font-size: 11px !important;
            letter-spacing: 1px;
            text-transform: uppercase;
            color: #ffffff !important;
            margin-bottom: 6px;
            font-weight: 600;
        }
        .metric-val {
            font-size: 28px !important;
            font-weight: 800 !important;
            color: #ffffff;
            margin-bottom: 6px;
            line-height: 1;
        }
        .metric-delta {
            font-size: 14px;
            color: #ffffff;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )

    kpi_html = f"""
    <div class="metric-grid">
        <div class="metric-box">
            <div class="metric-label">Total Stores</div>
            <div class="metric-val">{len(df)}</div>
            <div class="metric-delta">Active markets</div>
        </div>
        <div class="metric-box">
            <div class="metric-label">Total Actuals</div>
            <div class="metric-val">{total_act:,}</div>
            <div class="metric-delta">vs {total_quota:,} quota</div>
        </div>
        <div class="metric-box">
            <div class="metric-label">Avg PB Growth</div>
            <div class="metric-val">{avg_pb * 100:.1f}%</div>
            <div class="metric-delta">{PB_TARGET}</div>
        </div>
        <div class="metric-box">
            <div class="metric-label">Avg Retention</div>
            <div class="metric-val">{avg_ret * 100:.1f}%</div>
            <div class="metric-delta">95-day activity</div>
        </div>
        <div class="metric-box">
            <div class="metric-label">Avg MIM Growth</div>
            <div class="metric-val">{avg_mim:.1f}%</div>
            <div class="metric-delta">Inc. MIM growth</div>
        </div>
        <div class="metric-box">
            <div class="metric-label">Exceeding 100%</div>
            <div class="metric-val">{exceeding_count}</div>
            <div class="metric-delta">{(exceeding_count/len(df)*100):.0f}% of stores</div>
        </div>
    </div>
    """

    st.markdown(kpi_html, unsafe_allow_html=True)
    st.markdown("---")

    search_query = st.text_input(
        "Search bar",
        placeholder="Search store / market / DM...",
        label_visibility="collapsed",
        key="store_search_input",
    )

    ctrl_col1, ctrl_col2 = st.columns([1, 1])

    with ctrl_col1:
        st.markdown(
            """
            <style>
                [data-testid="stRadio"] * { color: #ffffff !important; }
                [data-testid="stRadio"] label { color: #ffffff !important; }
            </style>
            """,
            unsafe_allow_html=True,
        )
        filter_status = st.radio(
            "Filter by status",
            ["All Stores", "Exceeding 100%", "75–100%", "50–75%", "Below 50%"],
            horizontal=True,
            label_visibility="collapsed",
        )

    with ctrl_col2:
        sort_option = st.selectbox(
            "Sort options",
            options=[
                "Default",
                "PB Highest to Lowest ↓",
                "PB Lowest to Highest ↑",
                "Retention % ↓",
                "Retention % ↑",
                "MIM Growth % ↓",
                "MIM Growth % ↑",
            ],
            label_visibility="collapsed",
            key="sort_option",
        )

        st.markdown(
            """
            <style>
                [data-testid="stSelectbox"] * { color: #ffffff !important; }
                [data-testid="stSelectbox"] label,
                [data-testid="stSelectbox"] div {
                    color: #000000 !important;
                }
                [data-testid="stSelectbox"] select,
                [data-testid="stSelectbox"] input,
                [data-testid="stSelectbox"] button {
                    border: none !important;
                    box-shadow: none !important;
                    outline: none !important;
                    user-select: none !important;
                }
                [role="option"] {
                    color: #ffffff !important;
                    background-color: #000000 !important;
                }
                [role="option"]:hover {
                    color: #ffffff !important;
                    background-color: #31333f !important;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )

    filtered_df = df.copy()
    if search_query:
        filtered_df = filtered_df[
            filtered_df["STORE"].str.contains(search_query, case=False, regex=False, na=False) |
            filtered_df["MARKET"].str.contains(search_query, case=False, regex=False, na=False) |
            filtered_df["DM"].str.contains(search_query, case=False, regex=False, na=False)
        ]

    if filter_status == "Exceeding 100%":
        filtered_df = filtered_df[filtered_df["PB Growth%"] >= 1.0]
    elif filter_status == "75–100%":
        filtered_df = filtered_df[(filtered_df["PB Growth%"] >= 0.75) & (filtered_df["PB Growth%"] < 1.0)]
    elif filter_status == "50–75%":
        filtered_df = filtered_df[(filtered_df["PB Growth%"] >= 0.5) & (filtered_df["PB Growth%"] < 0.75)]
    elif filter_status == "Below 50%":
        filtered_df = filtered_df[filtered_df["PB Growth%"] < 0.5]

    sort_mapping = {
        "PB Highest to Lowest ↓": ("PB Growth%", False),
        "PB Lowest to Highest ↑": ("PB Growth%", True),
        "Retention % ↓": ("95 Days Act Retention", False),
        "Retention % ↑": ("95 Days Act Retention", True),
        "MIM Growth % ↓": ("MIM", False),
        "MIM Growth % ↑": ("MIM", True),
    }

    if sort_option in sort_mapping:
        col_name, asc_flag = sort_mapping[sort_option]
        filtered_df = filtered_df.sort_values(by=col_name, ascending=asc_flag)

    st.markdown(
        f"<h3 style='text-align: center; text-transform: uppercase;'>Store Performance Overview ({len(filtered_df)} stores)</h3>",
        unsafe_allow_html=True,
    )

    df_render = filtered_df.copy()
    df_render.insert(0, "S.NO", range(1, len(df_render) + 1))
    styled_df = (
        df_render.style
        .set_properties(**{
            'background-color': "#ffffff",
            'color': "#000000",
            'border-color': 'rgba(255,255,255,0.1)',
        })
        .set_table_styles(
            [
                {'selector': 'td', 'props': [('text-align', 'center')]},
                {'selector': 'th', 'props': [('text-align', 'center')]},
            ]
        )
    )

    rem_cols = [f for f in df_render.columns if "rem" in f.lower()]
    if rem_cols:
        def _highlight_col(col):
            out = []
            for v in col:
                try:
                    val = float(v)
                except (ValueError, TypeError):
                    out.append("")
                else:
                    out.append("background-color: #beffb2; color: #000000;" if val < 1 else "background-color: #ff8c8c; color: #000000;")
            return out

        styled_df = styled_df.apply(_highlight_col, subset=rem_cols)

    st.markdown(
        """
        <style>
            [data-testid="stDataFrame"] table th,
            [data-testid="stDataFrame"] table td,
            [data-testid="stDataFrame"] [role="gridcell"],
            [data-testid="stDataFrame"] [role="columnheader"] {
                text-align: center !important;
                justify-content: center !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    column_settings = {}
    for col in df_render.columns:
        if col == "S.NO":
            column_settings[col] = st.column_config.NumberColumn("S.NO", alignment="center", width="small")
        elif col == "PB Growth%":
            column_settings[col] = st.column_config.ProgressColumn(
                "PB Growth%", min_value=0.0, max_value=1.0, color="auto"
            )
        elif col == "95 Days Act Retention":
            column_settings[col] = st.column_config.ProgressColumn(
                "95 Days Act Retention", min_value=0.0, max_value=1.14, color="auto", format="percent"
            )
        elif col in {"Hit 75%", "Hit 100%", "Hit 125%"}:
            column_settings[col] = st.column_config.NumberColumn(col, format="%.0f", alignment="center")
        elif pd.api.types.is_numeric_dtype(df_render[col]):
            column_settings[col] = st.column_config.NumberColumn(col, alignment="center")
        else:
            column_settings[col] = st.column_config.TextColumn(col, alignment="center")

    st.dataframe(
        styled_df,
        column_config=column_settings,
        width="stretch",
        hide_index=True,
    )

    st.markdown("---")

    panel_left, panel_right = st.columns(2)

    with panel_left:
        st.markdown(
            "<h3 style='text-align:center; color:#ffffff'>🏆 Top 10 — PB Growth%</h3>",
            unsafe_allow_html=True,
        )
        top_10 = filtered_df.sort_values(by="PB Growth%", ascending=False).head(10).copy()
        top_10["PB Growth Display"] = top_10["PB Growth%"] * 100

        fig_top10 = px.bar(
            top_10,
            x="PB Growth%",
            y="STORE",
            orientation="h",
            text="PB Growth Display",
            color="PB Growth%",
            color_continuous_scale="Spectral",
            hover_data=["MARKET", "DM"],
        )
        fig_top10.update_layout(
            coloraxis_showscale=False,
            paper_bgcolor="rgba(255, 255, 255, 0.1)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="#ffffff",
            yaxis={
                "categoryorder": "total ascending",
                "tickfont": {"color": "#ffffff"},
            },
            xaxis={
                "tickfont": {"color": "#ffffff"},
            },
            height=380,
            margin=dict(l=10, r=10, t=20, b=10),
        )
        fig_top10.update_xaxes(showticklabels=False, title_text="PB GROWTH%", showline=False, title_font={"color": "#ffffff"})
        fig_top10.update_yaxes(title_font={"color": "#ffffff"})
        fig_top10.update_traces(texttemplate="<b>%{text:.1f}%</b>", textposition="inside", textfont={"color": "#ffffff"})
        st.plotly_chart(fig_top10, width="stretch", config={"displayModeBar": False})

    with panel_right:
        st.markdown(
            "<h3 style='text-align:center; color:#ffffff'>📊 PERFORMANCE DISTRIBUTION</h3>",
            unsafe_allow_html=True,
        )

        def get_tier(pb):
            if pb >= 1.25:
                return "≥ 125%"
            if pb >= 1.0:
                return "100–125%"
            if pb >= 0.75:
                return "75–100%"
            if pb >= 0.5:
                return "50–75%"
            return "< 50%"

        tier_df = filtered_df.copy()
        tier_df["Tier"] = tier_df["PB Growth%"].apply(get_tier)
        tier_order = ["≥ 125%", "100–125%", "75–100%", "50–75%", "< 50%"]

        dist_df = (
            tier_df["Tier"]
            .value_counts()
            .reindex(tier_order, fill_value=0)
            .reset_index()
        )
        dist_df.columns = ["Tier", "Store Count"]

        fig_dist = px.bar(
            dist_df,
            x="Store Count",
            y="Tier",
            orientation="h",
            text="Store Count",
            color="Tier",
            color_discrete_map={
                "≥ 125%": "#ff7bff",
                "100–125%": "#2ecc71",
                "75–100%": "#00642D",
                "50–75%": "#ffd32a",
                "< 50%": "#ff4757",
            },
        )
        fig_dist.update_layout(
            paper_bgcolor="rgba(255, 255, 255, 0.1)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="#ffffff",
            showlegend=False,
            yaxis={"categoryorder": "array", "categoryarray": tier_order[::-1]},
            height=380,
            margin=dict(l=10, r=10, t=20, b=10),
        )
        fig_dist.update_traces(textangle=0, texttemplate="<b>%{text} STORES</b>", textposition="inside", textfont={"color": "#ffffff"})
        fig_dist.update_xaxes(showticklabels=False, title_text="STORE COUNT", showline=False, title_font={"color": "#ffffff"})
        fig_dist.update_yaxes(title_text="TIER %", title_font={"color": "#ffffff"}, tickfont={"color": "#ffffff"})

        st.plotly_chart(fig_dist, width="stretch", config={"displayModeBar": False})

        st.markdown(
            """
            <style>
                [data-testid="stPlotlyChart"] {
                    border-radius: 12px !important;
                    overflow: hidden !important;
                }
                [data-testid="stPlotlyChart"] iframe {
                    border-radius: 12px !important;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
"@

    "e:\\Python\\employee_performance.py" = @"
"""
"""
import streamlit as st
import pandas as pd
import plotly.express as px


def render_employee_performance() -> None:
    """Renders the Store Sales Performance workspace page."""
    st.markdown(
        "# STORE SALES <span style='color:#a78bfa'>PERFORMANCE</span>",
        unsafe_allow_html=True,
    )
    st.markdown("#### EMPLOYEE PERFORMANCE ANALYTICS · LIVE MATRIX", unsafe_allow_html=True)
    st.markdown("---")

    try:
        df_emp = pd.read_excel("Emplyee Performance Data.xlsx", engine="openpyxl")
        if df_emp.empty:
            st.warning("The employee performance data file is empty.")
            return

        text_cols = df_emp.select_dtypes(include=["object", "category"]).columns.tolist()
        num_cols = df_emp.select_dtypes(include=["number"]).columns.tolist()

        emp_col = text_cols[0] if text_cols else df_emp.columns[0]
        metric_col = num_cols[0] if num_cols else None
        secondary_metric = num_cols[1] if len(num_cols) > 1 else None

        total_employees = len(df_emp)
        if metric_col:
            # handle NaNs for sums/means
            total_metric_sum = df_emp[metric_col].fillna(0).sum()
            avg_metric_val = df_emp[metric_col].dropna().mean()
            if pd.isna(avg_metric_val):
                avg_metric_val = 0.0
            if df_emp[metric_col].notna().any():
                top_emp_row = df_emp.loc[df_emp[metric_col].idxmax()]
                top_employee = f"{top_emp_row[emp_col]}"
                top_emp_val = top_emp_row[metric_col]
            else:
                top_employee = "N/A"
                top_emp_val = 0
        else:
            total_metric_sum = 0
            avg_metric_val = 0
            top_employee = "N/A"
            top_emp_val = 0

        st.markdown(
            """
        <style>
            .metric-grid {
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 16px;
                margin-bottom: 20px;
            }
            @media (max-width: 1024px) { .metric-grid { grid-template-columns: repeat(2, 1fr); } }
            @media (max-width: 600px) { .metric-grid { grid-template-columns: repeat(1, 1fr); } }
            .metric-box {
                background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(167,139,250,0.06));
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 12px;
                padding: 14px 18px;
                text-align: center;
                box-shadow: 0 6px 18px rgba(0, 0, 0, 0.35);
                backdrop-filter: blur(6px);
                transition: transform 160ms ease, box-shadow 160ms ease;
                min-height: 84px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                width: 100%; 
                box-sizing: border-box;
            }
            .metric-box:hover {
                transform: translateY(-6px);
                box-shadow: 0 14px 36px rgba(0,0,0,0.5);
                border: 2px solid #a78bfa;
            }
            .metric-label {
                font-size: 11px !important;
                letter-spacing: 1px;
                text-transform: uppercase;
                color: #ffffff !important;
                margin-bottom: 6px;
                font-weight: 600;
            }
            .metric-val {
                font-size: 24px !important;
                font-weight: 800 !important;
                color: #ffffff;
                margin-bottom: 6px;
                line-height: 1;
            }
            .metric-delta { font-size: 13px; color: #a78bfa; }
        </style>
        """,
            unsafe_allow_html=True,
        )

        metric_title = metric_col.replace("_", " ").title() if metric_col else "Metrics"
        kpi_html = f"""
        <div class="metric-grid">
            <div class="metric-box">
                <div class="metric-label">Headcount</div>
                <div class="metric-val">{total_employees}</div>
                <div class="metric-delta">Active Staff</div>
            </div>
            <div class="metric-box">
                <div class="metric-label">Total {metric_title}</div>
                <div class="metric-val">{total_metric_sum:,.0f}</div>
                <div class="metric-delta">Combined Output</div>
            </div>
            <div class="metric-box">
                <div class="metric-label">Average per Rep</div>
                <div class="metric-val">{avg_metric_val:,.1f}</div>
                <div class="metric-delta">Team Performance Baseline</div>
            </div>
            <div class="metric-box">
                <div class="metric-label">Top Performer</div>
                <div class="metric-val" style="font-size: 18px !important;">{top_employee}</div>
                <div class="metric-delta">Leader ({top_emp_val:,.0f})</div>
            </div>
        </div>
        """

        st.markdown(kpi_html, unsafe_allow_html=True)
        st.markdown("---")

        search_query = st.text_input(
            "Search workspace matrix",
            placeholder="Search employee name, ID, role or metric parameters...",
            label_visibility="collapsed",
            key="emp_search_input",
        )

        filtered_emp = df_emp.copy()
        if search_query and text_cols:
            mask = filtered_emp[text_cols].astype(str).apply(
                lambda x: x.str.contains(search_query, case=False, na=False)
            ).any(axis=1)
            filtered_emp = filtered_emp[mask]

        if metric_col and len(filtered_emp) > 0:
            panel_left, panel_right = st.columns(2)

            with panel_left:
                st.markdown(
                    f"<h3 style='text-align:center; color:#ffffff'>🏆 Top Performers ({metric_title})</h3>",
                    unsafe_allow_html=True,
                )
                top_perf = filtered_emp.sort_values(by=metric_col, ascending=False).head(10).copy()
                fig_emp = px.bar(
                    top_perf,
                    x=metric_col,
                    y=emp_col,
                    orientation="h",
                    color=metric_col,
                    color_continuous_scale="Purples",
                    hover_data=text_cols[:3],
                )
                fig_emp.update_layout(
                    coloraxis_showscale=False,
                    paper_bgcolor="rgba(255, 255, 255, 0.05)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font_color="#ffffff",
                    yaxis={"categoryorder": "total ascending", "tickfont": {"color": "#ffffff"}},
                    xaxis={"tickfont": {"color": "#ffffff"}},
                    height=340,
                    margin=dict(l=10, r=10, t=20, b=10),
                )
                fig_emp.update_xaxes(title_text=metric_title, showgrid=False, title_font={"color": "#ffffff"})
                fig_emp.update_yaxes(title_text="Employee", title_font={"color": "#ffffff"})
                st.plotly_chart(fig_emp, width="stretch", config={"displayModeBar": False})

            with panel_right:
                if secondary_metric:
                    st.markdown(
                        f"<h3 style='text-align:center; color:#ffffff'>📊 {metric_title} vs {secondary_metric.replace('_',' ').title()}</h3>",
                        unsafe_allow_html=True,
                    )
                    fig_comp = px.scatter(
                        filtered_emp,
                        x=metric_col,
                        y=secondary_metric,
                        hover_name=emp_col,
                        color_discrete_sequence=["#a78bfa"],
                    )
                    fig_comp.update_layout(
                        paper_bgcolor="rgba(255, 255, 255, 0.05)",
                        plot_bgcolor="rgba(0,0,0,0)",
                        font_color="#ffffff",
                        xaxis={"tickfont": {"color": "#ffffff"}},
                        yaxis={"tickfont": {"color": "#ffffff"}},
                        height=340,
                        margin=dict(l=10, r=10, t=20, b=10),
                    )
                    fig_comp.update_xaxes(title_text=metric_title, showgrid=True, gridcolor="rgba(255,255,255,0.1)", title_font={"color": "#ffffff"})
                    fig_comp.update_yaxes(title_text=secondary_metric.replace('_',' ').title(), showgrid=True, gridcolor="rgba(255,255,255,0.1)", title_font={"color": "#ffffff"})
                    st.plotly_chart(fig_comp, width="stretch", config={"displayModeBar": False})

                elif len(text_cols) > 1:
                    cat_col = text_cols[1]
                    st.markdown(
                        f"<h3 style='text-align:center; color:#ffffff'>📊 Staff Share by {cat_col.title()}</h3>",
                        unsafe_allow_html=True,
                    )
                    role_dist = filtered_emp[cat_col].value_counts().reset_index()
                    role_dist.columns = [cat_col, "Count"]
                    fig_pie = px.pie(
                        role_dist,
                        values="Count",
                        names=cat_col,
                        hole=0.4,
                        color_discrete_sequence=px.colors.sequential.Purp,
                    )
                    fig_pie.update_layout(
                        paper_bgcolor="rgba(255, 255, 255, 0.05)",
                        plot_bgcolor="rgba(0,0,0,0)",
                        font_color="#ffffff",
                        showlegend=True,
                        height=340,
                        margin=dict(l=10, r=10, t=20, b=10),
                    )
                    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
                    st.plotly_chart(fig_pie, width="stretch", config={"displayModeBar": False})

            st.markdown("---")

        st.markdown(
            f"<h3 style='text-align: center; text-transform: uppercase;'>Employee Matrix Record ({len(filtered_emp)} listings)</h3>",
            unsafe_allow_html=True,
        )

        emp_df_render = filtered_emp.copy()
        emp_df_render.insert(0, "S.NO", range(1, len(emp_df_render) + 1))
        styled_emp_df = (
            emp_df_render.style
            .set_properties(**{'background-color': "#ffffff", 'color': "#000000", 'border-color': 'rgba(255,255,255,0.1)'})
            .set_table_styles([
                {'selector': 'td', 'props': [('text-align', 'center')]},
                {'selector': 'th', 'props': [('text-align', 'center')]},
            ])
        )

        emp_column_settings = {}
        for col in emp_df_render.columns:
            if col == "S.NO":
                emp_column_settings[col] = st.column_config.NumberColumn("S.NO", alignment="center", width="small")
            elif pd.api.types.is_numeric_dtype(emp_df_render[col]):
                emp_column_settings[col] = st.column_config.NumberColumn(col, alignment="center")
            else:
                emp_column_settings[col] = st.column_config.TextColumn(col, alignment="center")

        st.dataframe(styled_emp_df, column_config=emp_column_settings, width="stretch", hide_index=True)

    except FileNotFoundError:
        st.error("⚠️ System Error: 'Emplyee Performance Data.xlsx' could not be found in the root directory structure.")
    except (KeyError, IndexError, TypeError, ValueError) as e:
        st.error(f"⚠️ Operational Processing Error: {str(e)}")
"@
}

foreach ($path in $files.Keys) {
    $content = $files[$path]
    Write-Output "Writing $path"
    $dir = Split-Path $path -Parent
    if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
    $content | Out-File -FilePath $path -Encoding UTF8 -Force
}

Write-Output "All files written."
