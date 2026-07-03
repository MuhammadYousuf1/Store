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