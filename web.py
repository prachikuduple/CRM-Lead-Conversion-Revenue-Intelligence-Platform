import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from PIL import Image

# ==========================================
# 1. APPLICATION & PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Revenue Intelligence Platform",
    page_icon="https://cdn-icons-png.flaticon.com/512/3135/3135715.png",  # Custom Clean Icon
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================
# 2. CUSTOM THEME & TYPOGRAPHY
# ==========================================
custom_css = """
<style>
    /* Google Fonts: Plus Jakarta Sans & Noto Sans Devanagari */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;600;700;800;900&display=swap');

    /* Global Font Overrides */
    html, body, [class*="css"], .stMarkdown, p, span, label, div {
        font-family: 'Noto Sans Devanagari', 'Plus Jakarta Sans', sans-serif !important;
        color: #E2E8F0 !important;
    }

    .stApp {
        background: radial-gradient(circle at 10% 20%, rgba(15, 23, 42, 0.98) 0%, rgba(2, 6, 23, 0.99) 90%),
                    url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1920&auto=format&fit=crop') no-repeat center center fixed;
        background-size: cover;
        color: #F8FAFC !important;
    }

    h1, h2, h3, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        font-weight: 900 !important;
        letter-spacing: -0.5px !important;
        background: linear-gradient(90deg, #FFFFFF 0%, #B5EAD7 50%, #FFF4BD 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        text-shadow: 0 4px 20px rgba(181, 234, 215, 0.25);
    }

    [data-testid="stHeader"] {
        background: rgba(0,0,0,0) !important;
    }

    div[data-testid="stSubheader"] {
        font-weight: 800 !important;
        font-size: 22px !important;
        margin-top: 15px !important;
        margin-bottom: 12px !important;
    }

    /* Dark Glassmorphic Sidebar Styling */
    section[data-testid="stSidebar"] {
        background: rgba(11, 15, 25, 0.98) !important;
        backdrop-filter: blur(25px) saturate(200%);
        -webkit-backdrop-filter: blur(25px) saturate(200%);
        border-right: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 10px 0 40px rgba(0, 0, 0, 0.8);
    }

    section[data-testid="stSidebar"] h3 {
        font-size: 16px !important;
        font-weight: 800 !important;
        color: #94A3B8 !important;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        margin-top: 22px !important;
        margin-bottom: 12px !important;
    }

    /* Custom Button & Nav Styling */
    div.stButton > button,
    div[data-testid="stSidebar"] div.stButton > button,
    div[data-testid="stSidebar"] button[kind="secondary"],
    div[data-testid="stSidebar"] button[kind="primary"] {
        background-color: #0F172A !important;
        background-image: none !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
        padding: 10px 14px !important;
        margin-bottom: 6px !important;
        width: 100% !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.4) !important;
        transition: all 0.2s ease-in-out !important;
    }

    /* Inner Button Typography */
    div.stButton > button *,
    div.stButton > button p,
    div.stButton > button span,
    div[data-testid="stSidebar"] div.stButton > button *,
    div[data-testid="stSidebar"] div.stButton > button p,
    div[data-testid="stSidebar"] div.stButton > button span {
        color: #5EEAD4 !important;
        font-size: 14px !important;
        font-weight: 700 !important;
        -webkit-text-fill-color: #5EEAD4 !important;
        opacity: 1 !important;
        font-family: 'Noto Sans Devanagari', 'Plus Jakarta Sans', sans-serif !important;
    }

    /* Button Hover Behavior */
    div.stButton > button:hover,
    div[data-testid="stSidebar"] div.stButton > button:hover {
        background-color: #1E293B !important;
        border-color: #5EEAD4 !important;
        transform: translateX(4px) !important;
    }

    div.stButton > button:hover *,
    div[data-testid="stSidebar"] div.stButton > button:hover * {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }

    /* Active State Indicator */
    .active-nav-btn {
        background: linear-gradient(135deg, #0D9488 0%, #115E59 100%) !important;
        border: 1px solid #2DD4BF !important;
        border-radius: 10px;
        padding: 10px 14px;
        margin-bottom: 6px;
        box-shadow: 0 4px 14px rgba(13, 148, 136, 0.3);
    }

    .active-nav-btn p {
        color: #FFFFFF !important;
        font-size: 14px !important;
        font-weight: 800 !important;
        margin: 0;
        -webkit-text-fill-color: #FFFFFF !important;
        font-family: 'Noto Sans Devanagari', 'Plus Jakarta Sans', sans-serif !important;
    }

    /* Top Banner Layout */
    .header-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(20px);
        padding: 20px 28px;
        border-radius: 16px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }

    .header-title {
        font-size: 28px;
        font-weight: 900;
        letter-spacing: -0.5px;
        background: linear-gradient(90deg, #FFFFFF, #B5EAD7, #FFF4BD);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }

    .header-subtitle {
        font-size: 13px;
        color: #B5EAD7 !important;
        margin-top: 4px;
        font-weight: 700;
    }

    .project-intro-card {
        background: rgba(15, 23, 42, 0.85);
        border-left: 4px solid #0D9488;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        border-right: 1px solid rgba(255, 255, 255, 0.08);
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(12px);
        border-radius: 12px;
        padding: 16px 20px;
        margin-bottom: 20px;
    }

    /* Metric Cards - Minimalist Styling */
    .metric-card {
        border-radius: 14px;
        padding: 18px 14px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
        transition: all 0.25s ease;
        border: 1px solid rgba(255, 255, 255, 0.15);
    }

    .metric-card:hover {
        transform: translateY(-3px);
    }

    .metric-card-pink   { background: linear-gradient(135deg, rgba(255, 183, 178, 0.95), rgba(255, 218, 193, 0.9)); }
    .metric-card-mint   { background: linear-gradient(135deg, rgba(181, 234, 215, 0.95), rgba(199, 206, 234, 0.9)); }
    .metric-card-yellow { background: linear-gradient(135deg, rgba(255, 244, 189, 0.95), rgba(255, 218, 193, 0.9)); }
    .metric-card-blue   { background: linear-gradient(135deg, rgba(212, 240, 240, 0.95), rgba(181, 234, 215, 0.9)); }
    .metric-card-purple { background: linear-gradient(135deg, rgba(232, 223, 245, 0.95), rgba(255, 183, 178, 0.9)); }

    .metric-title { 
        font-size: 12px; 
        font-weight: 800; 
        color: #0F172A !important; 
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }
    .metric-value { 
        font-size: 26px; 
        font-weight: 900; 
        color: #020617 !important; 
        margin-top: 4px; 
    }

    div[data-testid="stDataFrame"] { 
        background-color: rgba(15, 23, 42, 0.8) !important; 
        border-radius: 12px; 
        padding: 8px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ==========================================
# 3. DATA ENGINE & CACHING
# ==========================================
@st.cache_data
def load_full_dataset():
    file_path = "Cleaned_Lead_Conversion_Data.xlsx"
    try:
        xls = pd.ExcelFile(file_path)
        leads = pd.read_excel(xls, "Leads")
        interactions = pd.read_excel(xls, "Lead_Interactions")
        salespersons = pd.read_excel(xls, "Salespersons")
        products = pd.read_excel(xls, "Products")

        leads["Lead_Date"] = pd.to_datetime(leads["Lead_Date"])
        leads["Conversion_Date"] = pd.to_datetime(leads["Conversion_Date"])
        interactions["Interaction_Date"] = pd.to_datetime(interactions["Interaction_Date"])

        return leads, interactions, salespersons, products
    except Exception as e:
        st.error(f"Data Source Error: Unable to access primary dataset ({e})")
        return None, None, None, None

leads_df, interactions_df, salespersons_df, products_df = load_full_dataset()

pastel_colors = [
    "#B5EAD7", "#FFDAC1", "#FFB7B2", "#E2F0CB",
    "#C7CEEA", "#FFF4BD", "#D4F0F0", "#E8DFF5"
]

def style_chart(fig, height=330):
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Noto Sans Devanagari, Plus Jakarta Sans", size=12, color="#E2E8F0"),
        margin=dict(l=20, r=20, t=40, b=20),
        height=height,
        xaxis=dict(gridcolor="rgba(255,255,255,0.06)", zerolinecolor="rgba(255,255,255,0.06)"),
        yaxis=dict(gridcolor="rgba(255,255,255,0.06)", zerolinecolor="rgba(255,255,255,0.06)"),
        legend=dict(font=dict(color="#F8FAFC", size=12), bgcolor="rgba(0,0,0,0)")
    )
    return fig

if leads_df is not None:
    # ==========================================
    # 4. SIDEBAR NAVIGATION & FILTERS
    # ==========================================

    try:
        # Updated to use_container_width instead of deprecated use_column_width
        st.sidebar.image("logob.png", use_container_width=True)
    except Exception:
        st.sidebar.error("Brand Asset Missing: 'logob.png'")

    st.sidebar.markdown("### Navigation")
    
    # State Management for Navigation
    if "selected_page" not in st.session_state:
        st.session_state.selected_page = "Executive Overview"

    # Human-styled clean navigation labels without explicit emojis
    pages_map = {
        "Executive Overview": "Executive Overview (9 Key Metrics)",
        "Advanced Data Explorer": "Advanced Filter & Data Explorer",
        "Interaction Insights": "Interaction Insights & Logs",
        "Sales Team Performance": "Sales Representative Performance",
        "Products & Demand": "Product Demand & Pipeline Status",
        "Cohort Analysis": "Cohort & Time Series Analysis"
    }

    # Render Navigation
    for page_key, display_name in pages_map.items():
        is_active = (st.session_state.selected_page == page_key)
        if is_active:
            st.sidebar.markdown(f'<div class="active-nav-btn"><p>› {display_name}</p></div>', unsafe_allow_html=True)
        else:
            if st.sidebar.button(f"  {display_name}", key=f"nav_{page_key}", use_container_width=True):
                st.session_state.selected_page = page_key
                st.rerun()

    page = st.session_state.selected_page

    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    st.sidebar.markdown("### Control Panel")

    industry_filter = st.sidebar.multiselect(
        "Industry Sector:",
        options=sorted(leads_df["Industry"].unique()),
        default=list(leads_df["Industry"].unique()),
    )

    source_filter = st.sidebar.multiselect(
        "Lead Channel / Source:",
        options=sorted(leads_df["Lead_Source"].unique()),
        default=list(leads_df["Lead_Source"].unique()),
    )

    city_filter = st.sidebar.multiselect(
        "Target Location / City:",
        options=sorted(leads_df["City"].unique()),
        default=list(leads_df["City"].unique()),
    )

    min_budget = int(leads_df["Budget"].min())
    max_budget = int(leads_df["Budget"].max())
    selected_budget = st.sidebar.slider(
        "Budget Range (INR):",
        min_value=min_budget,
        max_value=max_budget,
        value=(min_budget, max_budget),
    )

    if st.sidebar.button("Reset Applied Filters"):
        st.rerun()

    filtered_leads = leads_df[
        (leads_df["Industry"].isin(industry_filter))
        & (leads_df["Lead_Source"].isin(source_filter))
        & (leads_df["City"].isin(city_filter))
        & (leads_df["Budget"].between(selected_budget[0], selected_budget[1]))
    ]

    # Global Top Header
    st.markdown(
        """
        <div class="header-container">
            <div>
                <div class="header-title">Lead Conversion Pipeline & Revenue Intelligence Platform</div>
                <div class="header-subtitle">Real-Time Enterprise Analytics & Conversion Performance Dashboard</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # PAGE 1: EXECUTIVE OVERVIEW
    if page == "Executive Overview":
        st.markdown(
            """
            <div class="project-intro-card">
                <div style="font-weight: 800; font-size: 15px; color: #5EEAD4;">Executive Summary & Platform Scope:</div>
                <div style="font-size: 14px; color: #CBD5E1; line-height: 1.6; margin-top: 4px;">
                    An <b>End-to-End Revenue Intelligence Dashboard</b> providing 360° Real-time insights into lead pipelines, conversion efficiency, rep performance, and demand forecasting.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if filtered_leads.empty:
            st.warning("No records matched the selected filter criteria. Adjust your settings on the left sidebar.")
        else:
            tot_leads = len(filtered_leads)
            conv_leads = len(filtered_leads[filtered_leads["Lead_Status"] == "Converted"])
            conv_rate = (conv_leads / tot_leads * 100) if tot_leads > 0 else 0
            tot_opp = filtered_leads["Opportunity_Value"].sum()
            avg_engagement = filtered_leads["Engagement_Score"].mean()

            m1, m2, m3, m4, m5 = st.columns(5)
            m1.markdown(f'<div class="metric-card metric-card-pink"><div class="metric-title">Total Leads</div><div class="metric-value">{tot_leads:,}</div></div>', unsafe_allow_html=True)
            m2.markdown(f'<div class="metric-card metric-card-mint"><div class="metric-title">Converted</div><div class="metric-value">{conv_leads:,}</div></div>', unsafe_allow_html=True)
            m3.markdown(f'<div class="metric-card metric-card-yellow"><div class="metric-title">Conversion Rate</div><div class="metric-value">{conv_rate:.1f}%</div></div>', unsafe_allow_html=True)
            m4.markdown(f'<div class="metric-card metric-card-blue"><div class="metric-title">Pipeline Value</div><div class="metric-value">₹{tot_opp:,.0f}</div></div>', unsafe_allow_html=True)
            m5.markdown(f'<div class="metric-card metric-card-purple"><div class="metric-title">Avg Engagement</div><div class="metric-value">{avg_engagement:.1f}/100</div></div>', unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            c1, c2, c3 = st.columns(3)
            with c1:
                st.subheader("1. Lead Status Share")
                df1 = filtered_leads["Lead_Status"].value_counts().reset_index(name="Count")
                fig1 = px.pie(df1, names="Lead_Status", values="Count", hole=0.45, color_discrete_sequence=pastel_colors)
                fig1.update_traces(textinfo="percent+value")
                st.plotly_chart(style_chart(fig1), use_container_width=True)

            with c2:
                st.subheader("2. Leads by Acquisition Channel")
                df2 = filtered_leads["Lead_Source"].value_counts().reset_index(name="Count")
                fig2 = px.bar(df2, x="Lead_Source", y="Count", text="Count", color="Lead_Source", color_discrete_sequence=pastel_colors)
                fig2.update_traces(textposition="outside")
                fig2.update_layout(showlegend=False)
                st.plotly_chart(style_chart(fig2), use_container_width=True)

            with c3:
                st.subheader("3. Pipeline Value by Industry")
                df3 = filtered_leads.groupby("Industry")["Opportunity_Value"].sum().reset_index()
                fig3 = px.bar(df3, x="Opportunity_Value", y="Industry", text="Opportunity_Value", orientation="h", color_discrete_sequence=["#C7CEEA"])
                fig3.update_traces(texttemplate="%{text:.2s}", textposition="outside")
                st.plotly_chart(style_chart(fig3), use_container_width=True)

            c4, c5, c6 = st.columns(3)
            with c4:
                st.subheader("4. Company Size Distribution")
                df4 = filtered_leads["Company_Size"].value_counts().reset_index(name="Count")
                fig4 = px.pie(df4, names="Company_Size", values="Count", color_discrete_sequence=["#FFDAC1", "#B5EAD7", "#FFB7B2"])
                fig4.update_traces(textinfo="percent+value")
                st.plotly_chart(style_chart(fig4), use_container_width=True)

            with c5:
                st.subheader("5. Engagement vs Opportunity Value")
                fig5 = px.scatter(filtered_leads, x="Engagement_Score", y="Opportunity_Value", color="Lead_Status", color_discrete_sequence=pastel_colors)
                st.plotly_chart(style_chart(fig5), use_container_width=True)

            with c6:
                st.subheader("6. Product Demand Volume")
                df6 = filtered_leads["Product_Interest"].value_counts().reset_index(name="Count")
                fig6 = px.bar(df6, x="Product_Interest", y="Count", text="Count", color_discrete_sequence=["#FFF4BD"])
                fig6.update_traces(textposition="outside")
                st.plotly_chart(style_chart(fig6), use_container_width=True)

            c7, c8, c9 = st.columns(3)
            with c7:
                st.subheader("7. Monthly Acquisition Trend")
                temp_df = filtered_leads.copy()
                temp_df["Month"] = temp_df["Lead_Date"].dt.to_period("M").astype(str)
                df_line = temp_df.groupby("Month")["Lead_ID"].count().reset_index(name="Leads_Count")

                fig7 = px.line(df_line, x="Month", y="Leads_Count", text="Leads_Count", markers=True, line_shape="spline", color_discrete_sequence=["#FFB7B2"])
                fig7.update_traces(line=dict(width=3), marker=dict(size=8), textposition="top center")
                st.plotly_chart(style_chart(fig7), use_container_width=True)

            with c8:
                st.subheader("8. Conversion Efficiency by Source")
                df8 = (pd.crosstab(filtered_leads["Lead_Source"], filtered_leads["Lead_Status"], normalize="index") * 100).reset_index()
                if "Converted" in df8.columns:
                    df8["Converted_Formatted"] = df8["Converted"].apply(lambda x: f"{x:.1f}%")
                    fig8 = px.bar(df8, x="Lead_Source", y="Converted", text="Converted_Formatted", labels={"Converted": "Conversion Rate (%)"}, color_discrete_sequence=["#B5EAD7"])
                    fig8.update_traces(textposition="outside")
                else:
                    fig8 = px.bar(title="No Converted Records Found")
                st.plotly_chart(style_chart(fig8), use_container_width=True)

            with c9:
                st.subheader("9. Churn & Lost Reason Analysis")
                df9 = filtered_leads[filtered_leads["Lead_Status"] == "Lost"]["Lost_Reason"].value_counts().reset_index(name="Count")
                if not df9.empty:
                    fig9 = px.bar(df9, x="Lost_Reason", y="Count", text="Count", color_discrete_sequence=["#FFB7B2"])
                    fig9.update_traces(textposition="outside")
                else:
                    fig9 = px.bar(title="No Lost Records Found")
                st.plotly_chart(style_chart(fig9), use_container_width=True)

    elif page == "Advanced Data Explorer":
        st.subheader("Advanced Data Explorer & Filters")
        st.write(f"Total Filtered Records Displayed: **{len(filtered_leads)}**")

        all_cols = list(filtered_leads.columns)
        selected_cols = st.multiselect("Select Columns to Render:", options=all_cols, default=all_cols[:10])

        st.dataframe(filtered_leads[selected_cols] if selected_cols else filtered_leads, use_container_width=True)

        col_d1, col_d2 = st.columns(2)
        with col_d1:
            csv_data = filtered_leads.to_csv(index=False).encode("utf-8")
            st.download_button("Export Lead Dataset (CSV)", data=csv_data, file_name="Filtered_Leads.csv", mime="text/csv")

        with col_d2:
            summary_stats = filtered_leads.describe()
            st.download_button("Export Summary Metrics (CSV)", data=summary_stats.to_csv().encode("utf-8"), file_name="Summary_Stats.csv", mime="text/csv")

    elif page == "Interaction Insights":
        st.subheader("Interaction Logs & Channel Insights")
        merged_int = interactions_df.merge(
            leads_df[["Lead_ID", "Lead_Source", "Lead_Status", "Industry"]],
            on="Lead_ID",
            how="left",
        )

        total_interactions = len(merged_int)
        avg_duration = merged_int['Duration_Minutes'].mean() if not merged_int.empty else 0
        positive_outcomes = (merged_int['Outcome'] == 'Interested').sum() if not merged_int.empty else 0

        i1, i2, i3 = st.columns(3)
        i1.markdown(f'<div class="metric-card metric-card-blue"><div class="metric-title">Total Touchpoints</div><div class="metric-value">{total_interactions:,}</div></div>', unsafe_allow_html=True)
        i2.markdown(f'<div class="metric-card metric-card-purple"><div class="metric-title">Average Duration</div><div class="metric-value">{avg_duration:.1f} mins</div></div>', unsafe_allow_html=True)
        i3.markdown(f'<div class="metric-card metric-card-mint"><div class="metric-title">Positive Outcomes</div><div class="metric-value">{positive_outcomes:,}</div></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        col_i1, col_i2 = st.columns(2)
        with col_i1:
            st.subheader("Interaction Channel Distribution")
            df_int_type = merged_int["Interaction_Type"].value_counts().reset_index(name="Count")
            fig_int1 = px.pie(df_int_type, names="Interaction_Type", values="Count", color_discrete_sequence=pastel_colors, hole=0.45)
            fig_int1.update_traces(textinfo="percent+value")
            st.plotly_chart(style_chart(fig_int1), use_container_width=True)

        with col_i2:
            st.subheader("Interaction Duration Spread by Outcome")
            outcome_colors = {
                "Interested": "#B5EAD7",
                "Not Interested": "#FFB7B2",
                "No Response": "#FFF4BD",
                "Follow-up Required": "#C7CEEA",
                "Converted": "#E2F0CB",
            }
            fig_int2 = px.box(merged_int, x="Outcome", y="Duration_Minutes", color="Outcome", color_discrete_map=outcome_colors)
            st.plotly_chart(style_chart(fig_int2), use_container_width=True)

        st.subheader("Detailed Interaction Records")
        st.dataframe(merged_int, use_container_width=True)

    elif page == "Sales Team Performance":
        st.subheader("Sales Representative Leaderboard")

        sales_summary = (
            leads_df.groupby("Salesperson_ID")
            .agg(
                Total_Assigned=("Lead_ID", "count"),
                Converted_Leads=("Lead_Status", lambda x: (x == "Converted").sum()),
                Won_Revenue=("Opportunity_Value", "sum"),
                Avg_Followups=("Followup_Count", "mean"),
            )
            .reset_index()
        )

        sales_merged = salespersons_df.merge(sales_summary, on="Salesperson_ID", how="left")
        sales_merged["Conversion_Rate (%)"] = (sales_merged["Converted_Leads"] / sales_merged["Total_Assigned"] * 100).round(1)

        col_s1, col_s2 = st.columns(2)
        with col_s1:
            st.subheader("Total Conversions by Representative")
            fig_s1 = px.bar(sales_merged, x="Salesperson_Name", y="Converted_Leads", text="Converted_Leads", color="Team", color_discrete_sequence=pastel_colors)
            fig_s1.update_traces(textposition="outside")
            st.plotly_chart(style_chart(fig_s1), use_container_width=True)

        with col_s2:
            st.subheader("Total Closed Revenue by Representative")
            fig_s2 = px.bar(sales_merged, x="Salesperson_Name", y="Won_Revenue", text="Won_Revenue", color_discrete_sequence=["#B5EAD7"])
            fig_s2.update_traces(texttemplate="%{text:.2s}", textposition="outside")
            st.plotly_chart(style_chart(fig_s2), use_container_width=True)

        st.subheader("Comprehensive Sales Rep Metrics")
        st.dataframe(sales_merged.sort_values(by="Converted_Leads", ascending=False), use_container_width=True)

    elif page == "Products & Demand":
        st.subheader("Product Demand & Revenue Pipeline")

        prod_demand = (
            leads_df.groupby("Product_Interest")
            .agg(
                Total_Leads=("Lead_ID", "count"),
                Pipeline_Value=("Opportunity_Value", "sum"),
                Avg_Budget=("Budget", "mean"),
            )
            .reset_index()
        )

        prod_merged = products_df.merge(prod_demand, left_on="Product_Name", right_on="Product_Interest", how="left")
        prod_merged["Pipeline_Value"] = prod_merged["Pipeline_Value"].fillna(0)
        prod_merged["Total_Leads"] = prod_merged["Total_Leads"].fillna(0)

        col_p1, col_p2 = st.columns(2)
        with col_p1:
            st.subheader("Pipeline Revenue by Product")
            fig_p1 = px.bar(prod_merged, x="Product_Name", y="Pipeline_Value", text="Pipeline_Value", color="Category", color_discrete_sequence=pastel_colors)
            fig_p1.update_traces(texttemplate="%{text:.2s}", textposition="outside")
            st.plotly_chart(style_chart(fig_p1), use_container_width=True)

        with col_p2:
            st.subheader("Product Price vs Lead Interest")
            fig_p2 = px.scatter(prod_merged, x="Price", y="Total_Leads", size="Pipeline_Value", color="Product_Name", color_discrete_sequence=pastel_colors)
            st.plotly_chart(style_chart(fig_p2), use_container_width=True)

        st.subheader("Product Portfolio Master Data")
        st.dataframe(prod_merged, use_container_width=True)

    elif page == "Cohort Analysis":
        st.subheader("Cohort Trends & Time-Series Metrics")

        leads_df["Lead_Month"] = leads_df["Lead_Date"].dt.to_period("M").astype(str)
        monthly_leads = (
            leads_df.groupby("Lead_Month")
            .agg(
                Total_Leads=("Lead_ID", "count"),
                Converted=("Lead_Status", lambda x: (x == "Converted").sum()),
            )
            .reset_index()
        )

        col_t1, col_t2 = st.columns(2)
        with col_t1:
            st.subheader("Monthly Acquisition Volume")
            fig_t1 = px.line(monthly_leads, x="Lead_Month", y="Total_Leads", text="Total_Leads", markers=True, color_discrete_sequence=["#FFB7B2"])
            fig_t1.update_traces(textposition="top center")
            st.plotly_chart(style_chart(fig_t1), use_container_width=True)

        with col_t2:
            st.subheader("Monthly Conversions Trend")
            fig_t2 = px.bar(monthly_leads, x="Lead_Month", y="Converted", text="Converted", color_discrete_sequence=["#B5EAD7"])
            fig_t2.update_traces(textposition="outside")
            st.plotly_chart(style_chart(fig_t2), use_container_width=True)

    st.markdown("---")
    if st.button("Reload System Cache"):
        st.cache_data.clear()
        st.rerun()