"""Sales Hub main application with HOME, TARGET vs ACTUAL, and EMPLOYEE PERFORMANCE pages."""
import streamlit as st
from common import (
    inject_global_css,
    inject_sidebar_button_css,
    render_footer,
    render_home_icon,
)
from employee_performance import render_employee_performance
from target_vs_actual import render_target_vs_actual
from home import render_home

# --- Page Configuration ---
st.set_page_config(page_title="Sales Hub", page_icon="📊", layout="wide")

# --- UI & Styling Injection ---
inject_global_css()
inject_sidebar_button_css()

page_renderers = {
    "HOME": render_home,
    "TARGET vs ACTUAL": render_target_vs_actual,
    "EMPLOYEE PERFORMANCE": render_employee_performance,
}

# Safely get the current page from the URL query parameters using the new API
selected_page = st.query_params.get("page", "HOME")

# Fallback if the page parameter exists but isn't a valid renderer
if selected_page not in page_renderers:
    selected_page = "HOME"

# Render the top Home icon on every non-home page
if selected_page != "HOME":
    render_home_icon()

# Execute the render function for the selected page
page_renderers[selected_page]()

# Render the global footer
render_footer()