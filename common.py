import streamlit as st


# def hide_streamlit_ui() -> None:
#     st.markdown(
#         """
#         <style>
#         #MainMenu {visibility: hidden;}
#         footer {visibility: hidden;}

#         /* Keep the header's sidebar toggle visible while simplifying the header */
#         header[data-testid="stHeader"] {
#             background: transparent !important;
#             padding: 0 !important;
#             margin: 0 !important;
#         }
#         header[data-testid="stHeader"] button[data-testid^="stSidebar"] {
#             display: inline-flex !important;
#             visibility: visible !important;
#             opacity: 1 !important;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )


__all__ = [
    # "hide_streamlit_ui",
    "inject_global_css",
    "inject_sidebar_button_css",
    # "inject_sidebar_nav_css",
    "render_footer",
]


def inject_global_css() -> None:
    """Inject global CSS styles for the Sales Hub theme."""
    st.markdown(
        """
    <style>
        .stApp {
            background: linear-gradient(
                135deg,
                rgba(15, 15, 15, 1) 0%,
                rgba(40, 20, 60, 1) 50%,
                rgba(120, 80, 180, 0.8) 100%
            );
            color: #ffffff !important;
            text-align: center;
        }

        h1, h2, h3, h4, h5, h6, p, span, label, strong, div {
            color: #ffffff !important;
        }

        [data-testid="stMetric"] {
            color: #ffffff !important;
        }

        [data-testid="stMetricLabel"] p {
            color: #ffffff !important;
            opacity: 1 !important;
            font-size: 11px !important;
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        [data-testid="stMetricValue"] {
            color: #ffffff !important;
            font-size: 26px !important;
            font-weight: 800 !important;
        }

        [data-testid="stMetricDelta"] {
            color: #ffffff !important;
        }

        [data-testid="stMetricDelta"] div {
            color: #ffffff !important;
        }

        @media (max-width: 768px) {
            [data-testid="stDataFrame"],
            [data-testid="stDataFrame"] > div {
                background-color: #ffffff !important;
            }
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #5b006f 0%, #2a0033 100%) !important;
            color: #ffffff !important;
        }

        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] .stRadio,
        [data-testid="stSidebar"] .stSelectbox {
            color: #ffffff !important;
        }

        [data-testid="stElementToolbarButtonContainer"],
        [data-testid="stElementToolbarButton"] {
            background-color: #000000 !important;
        }

        button[data-testid="stBaseButton-elementToolbar"] {
            background-color: #000000 !important;
            color: #ffffff !important;
            border-color: #000000 !important;
        }

        button[data-testid="stBaseButton-elementToolbar"]:hover {
            background-color: #67207f !important;
            color: #ffffff !important;
        }

        button[data-testid="stBaseButton-elementToolbar"] svg {
            color: #ffffff !important;
            fill: #ffffff !important;
        }

        [data-baseweb="checkbox"] {
            color: #000000 !important;
        }

        [data-baseweb="checkbox"] label {
            color: #000000 !important;
        }

        [data-baseweb="checkbox"] div {
            color: #000000 !important;
        }

        /* Hide index option in checkboxes */
        label[data-baseweb="checkbox"]:has(input[aria-label="(index)"]) {
            display: none !important;
        }

        /* DataFrame styling for index and cells */
        [data-testid="stDataFrame"] {
            color: #000000 !important;
        }

        [data-testid="stDataFrame"] thead {
            color: #000000 !important;
        }

        [data-testid="stDataFrame"] tbody {
            color: #000000 !important;
        }

        [data-testid="stDataFrame"] th,
        [data-testid="stDataFrame"] td {
            color: #000000 !important;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )


def inject_sidebar_button_css() -> None:
    """Inject CSS styles for sidebar expand/collapse buttons."""
    st.markdown(
        """
    <style>
        button[data-testid="stExpandSidebarButton"],
        button[data-testid="stSidebarCollapseButton"] {
            color: #ff0000 !important;
            background-color: rgba(69, 26, 114, 0.7) !important;
            border-color: #ff0000 !important;
            box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2) !important;
        }

        button[data-testid="stExpandSidebarButton"] span,
        button[data-testid="stSidebarCollapseButton"] span {
            color: #ffffff !important;
            fill: #ff0000 !important;
        }

        button[data-testid="stExpandSidebarButton"]:hover,
        button[data-testid="stSidebarCollapseButton"]:hover {
            background-color: rgba(106, 58, 179, 0.8) !important;
            color: #ffffff !important;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )


def render_home_icon() -> None:
    """Render a home navigation icon link at the top of the page."""
    st.markdown(
        """
        <style>
            .home-link {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                padding: 10px 16px;
                border-radius: 999px;
                border: 1px solid rgba(255,255,255,0.16);
                background: rgba(255,255,255,0.06);
                color: #ffffff !important;
                text-decoration: none !important;
                font-size: 14px;
                font-weight: 700;
                letter-spacing: 0.03em;
                transition: all 150ms ease;
                margin-bottom: 18px;
            }
            .home-link:hover {
                background: rgba(255,255,255,0.12);
                transform: translateY(-1px);
            }
        </style>
        <div style='display:flex; justify-content:flex-end; width:100%; padding-bottom: 12px;'>
            <a class='home-link' href='?page=HOME' target='_self'>🏠 Home</a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_footer() -> None:
    """Render the global footer with home link icon."""
    st.markdown(
        """
        <div style='display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 12px; margin-top: 30px; font-size: 10px; color: #ffffff; letter-spacing: 1px;'>
            <span>CONFIDENTIAL · FOR INTERNAL USE ONLY · SALES OPERATIONS</span>
        </div>
        """,
        unsafe_allow_html=True,
    )