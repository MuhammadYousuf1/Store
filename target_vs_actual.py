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