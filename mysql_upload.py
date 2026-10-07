# import pandas as pd
# import mysql.connector

# # =========================================================
# # 1. CLEANED EXCEL FILE
# # =========================================================

# file_path = "Cleaned_Lead_Conversion_Data.xlsx"

# leads = pd.read_excel(file_path, sheet_name="Leads")
# interactions = pd.read_excel(file_path, sheet_name="Lead_Interactions")
# salespersons = pd.read_excel(file_path, sheet_name="Salespersons")
# products = pd.read_excel(file_path, sheet_name="Products")

# print("======================================")
# print("EXCEL DATA LOADED SUCCESSFULLY")
# print("======================================")
# print("Leads:", len(leads))
# print("Interactions:", len(interactions))
# print("Salespersons:", len(salespersons))
# print("Products:", len(products))


# # =========================================================
# # 2. MYSQL CONNECTION
# # =========================================================

# try:

#     conn = mysql.connector.connect(
#         host="localhost",
#         port=3306,
#         user="root",
#         password="root123",
#         database="lead_db"
#     )

#     cursor = conn.cursor()

#     print("\nMySQL connected successfully!")


#     # =====================================================
#     # 3. CREATE LEADS TABLE
#     # =====================================================

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS Leads (
#         Lead_ID VARCHAR(50) PRIMARY KEY,
#         Lead_Date DATE,
#         Lead_Source VARCHAR(100),
#         Industry VARCHAR(100),
#         Company_Size VARCHAR(50),
#         City VARCHAR(100),
#         Lead_Type VARCHAR(100),
#         Product_Interest VARCHAR(100),
#         Budget DECIMAL(15,2),
#         Salesperson_ID VARCHAR(50),
#         First_Contact_Date DATE,
#         Followup_Count INT,
#         Response_Time_Hours INT,
#         Engagement_Score INT,
#         Opportunity_Value DECIMAL(15,2),
#         Lead_Status VARCHAR(50),
#         Lost_Reason VARCHAR(150),
#         Conversion_Date DATE
#     )
#     """)


#     # =====================================================
#     # 4. CREATE INTERACTIONS TABLE
#     # =====================================================

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS Lead_Interactions (
#         Interaction_ID VARCHAR(50) PRIMARY KEY,
#         Lead_ID VARCHAR(50),
#         Interaction_Date DATE,
#         Interaction_Type VARCHAR(100),
#         Response VARCHAR(100),
#         Duration_Minutes INT,
#         Outcome VARCHAR(100),
#         FOREIGN KEY (Lead_ID)
#         REFERENCES Leads(Lead_ID)
#     )
#     """)


#     # =====================================================
#     # 5. CREATE SALESPERSONS TABLE
#     # =====================================================

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS Salespersons (
#         Salesperson_ID VARCHAR(50) PRIMARY KEY,
#         Salesperson_Name VARCHAR(100),
#         Team VARCHAR(100),
#         Experience_Years INT
#     )
#     """)


#     # =====================================================
#     # 6. CREATE PRODUCTS TABLE
#     # =====================================================

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS Products (
#         Product_ID VARCHAR(50) PRIMARY KEY,
#         Product_Name VARCHAR(150),
#         Category VARCHAR(100),
#         Price DECIMAL(15,2)
#     )
#     """)

#     conn.commit()

#     print("Tables created successfully!")


#     # =====================================================
#     # 7. INSERT LEADS
#     # =====================================================

#     lead_query = """
#     INSERT IGNORE INTO Leads (
#         Lead_ID,
#         Lead_Date,
#         Lead_Source,
#         Industry,
#         Company_Size,
#         City,
#         Lead_Type,
#         Product_Interest,
#         Budget,
#         Salesperson_ID,
#         First_Contact_Date,
#         Followup_Count,
#         Response_Time_Hours,
#         Engagement_Score,
#         Opportunity_Value,
#         Lead_Status,
#         Lost_Reason,
#         Conversion_Date
#     )
#     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
#             %s,%s,%s,%s,%s,%s,%s,%s)
#     """

#     for _, row in leads.iterrows():

#         values = (
#             row["Lead_ID"],
#             row["Lead_Date"].date()
#                 if pd.notna(row["Lead_Date"]) else None,

#             row["Lead_Source"],
#             row["Industry"],
#             row["Company_Size"],
#             row["City"],
#             row["Lead_Type"],
#             row["Product_Interest"],

#             row["Budget"]
#                 if pd.notna(row["Budget"]) else None,

#             row["Salesperson_ID"],

#             row["First_Contact_Date"].date()
#                 if pd.notna(row["First_Contact_Date"]) else None,

#             row["Followup_Count"]
#                 if pd.notna(row["Followup_Count"]) else None,

#             row["Response_Time_Hours"]
#                 if pd.notna(row["Response_Time_Hours"]) else None,

#             row["Engagement_Score"]
#                 if pd.notna(row["Engagement_Score"]) else None,

#             row["Opportunity_Value"]
#                 if pd.notna(row["Opportunity_Value"]) else None,

#             row["Lead_Status"],

#             None
#                 if pd.isna(row["Lost_Reason"])
#                 else row["Lost_Reason"],

#             None
#                 if pd.isna(row["Conversion_Date"])
#                 else row["Conversion_Date"].date()
#         )

#         cursor.execute(lead_query, values)


#     print("Leads inserted successfully!")


#     # =====================================================
#     # 8. INSERT INTERACTIONS
#     # =====================================================

#     interaction_query = """
#     INSERT IGNORE INTO Lead_Interactions (
#         Interaction_ID,
#         Lead_ID,
#         Interaction_Date,
#         Interaction_Type,
#         Response,
#         Duration_Minutes,
#         Outcome
#     )
#     VALUES (%s,%s,%s,%s,%s,%s,%s)
#     """

#     for _, row in interactions.iterrows():

#         values = (
#             row["Interaction_ID"],
#             row["Lead_ID"],

#             row["Interaction_Date"].date()
#                 if pd.notna(row["Interaction_Date"]) else None,

#             row["Interaction_Type"],
#             row["Response"],

#             row["Duration_Minutes"]
#                 if pd.notna(row["Duration_Minutes"]) else None,

#             row["Outcome"]
#         )

#         cursor.execute(interaction_query, values)


#     print("Interactions inserted successfully!")


#     # =====================================================
#     # 9. INSERT SALESPERSONS
#     # =====================================================

#     salesperson_query = """
#     INSERT IGNORE INTO Salespersons (
#         Salesperson_ID,
#         Salesperson_Name,
#         Team,
#         Experience_Years
#     )
#     VALUES (%s,%s,%s,%s)
#     """

#     for _, row in salespersons.iterrows():

#         values = (
#             row["Salesperson_ID"],
#             row["Salesperson_Name"],
#             row["Team"],

#             row["Experience_Years"]
#                 if pd.notna(row["Experience_Years"]) else None
#         )

#         cursor.execute(salesperson_query, values)


#     print("Salespersons inserted successfully!")


#     # =====================================================
#     # 10. INSERT PRODUCTS
#     # =====================================================

#     product_query = """
#     INSERT IGNORE INTO Products (
#         Product_ID,
#         Product_Name,
#         Category,
#         Price
#     )
#     VALUES (%s,%s,%s,%s)
#     """

#     for _, row in products.iterrows():

#         values = (
#             row["Product_ID"],
#             row["Product_Name"],
#             row["Category"],

#             row["Price"]
#                 if pd.notna(row["Price"]) else None
#         )

#         cursor.execute(product_query, values)


#     print("Products inserted successfully!")


#     # =====================================================
#     # 11. COMMIT
#     # =====================================================

#     conn.commit()


#     # =====================================================
#     # 12. VERIFY DATA
#     # =====================================================

#     print("\n======================================")
#     print("DATA INSERTED SUCCESSFULLY!")
#     print("======================================")

#     cursor.execute("SELECT COUNT(*) FROM Leads")
#     print("Leads:", cursor.fetchone()[0])

#     cursor.execute("SELECT COUNT(*) FROM Lead_Interactions")
#     print("Interactions:", cursor.fetchone()[0])

#     cursor.execute("SELECT COUNT(*) FROM Salespersons")
#     print("Salespersons:", cursor.fetchone()[0])

#     cursor.execute("SELECT COUNT(*) FROM Products")
#     print("Products:", cursor.fetchone()[0])


#     # =====================================================
#     # 13. CLOSE CONNECTION
#     # =====================================================

#     cursor.close()
#     conn.close()

#     print("\nMySQL connection closed.")
#     print("======================================")
#     print("MYSQL PROCESS COMPLETED")
#     print("======================================")


# except mysql.connector.Error as error:

#     print("\nMYSQL ERROR:")
#     print(error)


# except Exception as error:

#     print("\nPYTHON ERROR:")
#     print(error)

# ============================================================
# LEAD CONVERSION, PIPELINE & REVENUE INTELLIGENCE PLATFORM
# CRM ANALYTICS DASHBOARD
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector
from io import BytesIO

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="CRM Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# THEME COLORS
# ============================================================

CHARCOAL = "#202024"
CHARCOAL_2 = "#29292F"
CHARCOAL_3 = "#323238"

DUSTY_ROSE = "#C98F9B"
DUSTY_ROSE_LIGHT = "#E3B6BE"
DUSTY_ROSE_DARK = "#A96F7B"

WHITE = "#FFF8F8"
LIGHT_TEXT = "#E9DDE0"
MUTED_TEXT = "#BDAFB3"
GRID = "#4A4145"

GREEN = "#9CC9B1"
RED = "#D9959F"
YELLOW = "#D8C18C"

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* MAIN BACKGROUND */
    .stApp {
        background: linear-gradient(
            135deg,
            #202024 0%,
            #25252B 50%,
            #202024 100%
        );
        color: #FFF8F8;
    }

    /* SIDEBAR */
    section[data-testid="stSidebar"] {
        background: #19191D;
        border-right: 1px solid #3B3437;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #FFF8F8 !important;
    }

    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] label {
        color: #E9DDE0 !important;
    }

    /* HEADINGS */
    h1 {
        color: #FFF8F8 !important;
        font-weight: 800 !important;
        letter-spacing: 0.5px;
    }

    h2, h3 {
        color: #FFF8F8 !important;
        font-weight: 700 !important;
    }

    /* NORMAL TEXT */
    p {
        color: #E9DDE0;
    }

    /* METRIC CARDS */
    [data-testid="stMetric"] {
        background: linear-gradient(
            145deg,
            #323238,
            #25252A
        );
        border: 1px solid #5A464C;
        border-radius: 18px;
        padding: 18px;
        min-height: 125px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.25);
        transition: all 0.25s ease;
    }

    [data-testid="stMetric"]:hover {
        transform: translateY(-4px);
        border-color: #C98F9B;
        box-shadow: 0 12px 30px rgba(201,143,155,0.18);
    }

    [data-testid="stMetricLabel"] {
        color: #D9C4C8 !important;
        font-weight: 600 !important;
    }

    [data-testid="stMetricValue"] {
        color: #FFF8F8 !important;
        font-weight: 800 !important;
    }

    [data-testid="stMetricDelta"] {
        color: #E3B6BE !important;
    }

    /* SELECTBOX / MULTISELECT */
    div[data-baseweb="select"] > div {
        background-color: #29292F !important;
        border-color: #59474D !important;
        color: #FFF8F8 !important;
        border-radius: 10px !important;
    }

    div[data-baseweb="select"] span {
        color: #FFF8F8 !important;
    }

    /* DATE INPUT */
    div[data-baseweb="input"] {
        background-color: #29292F !important;
        border-radius: 10px !important;
    }

    input {
        color: #FFF8F8 !important;
    }

    /* BUTTON */
    .stButton button,
    .stDownloadButton button {
        background: #C98F9B !important;
        color: #201F23 !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
    }

    .stButton button:hover,
    .stDownloadButton button:hover {
        background: #E3B6BE !important;
        color: #201F23 !important;
    }

    /* DATAFRAME */
    [data-testid="stDataFrame"] {
        border: 1px solid #514247;
        border-radius: 12px;
        overflow: hidden;
    }

    /* INFO / SUCCESS / WARNING */
    div[data-testid="stAlert"] {
        border-radius: 12px;
    }

    /* DIVIDER */
    hr {
        border-color: #493D41 !important;
    }

    /* CAPTION */
    .stCaption {
        color: #BDAFB3 !important;
    }

    /* TABS */
    button[data-baseweb="tab"] {
        color: #D9C4C8 !important;
        font-weight: 600;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: #E3B6BE !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def clean_dataframe(df):
    """Clean and prepare CRM dataframe."""

    df = df.copy()

    # Remove duplicate columns
    df = df.loc[:, ~df.columns.duplicated()]

    # Clean column names
    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
    )

    # Clean text columns
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .replace({
                "nan": np.nan,
                "None": np.nan,
                "NaN": np.nan
            })
        )

    # Date columns
    date_columns = [
        "Lead_Date",
        "First_Contact_Date",
        "Conversion_Date"
    ]

    for col in date_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(
                df[col],
                errors="coerce"
            )

    # Numeric columns
    numeric_columns = [
        "Budget",
        "Followup_Count",
        "Response_Time_Hours",
        "Engagement_Score",
        "Opportunity_Value"
    ]

    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    return df


def load_mysql_data(
    host,
    port,
    user,
    password,
    database,
    table
):
    """Load data from MySQL."""

    conn = mysql.connector.connect(
        host=host,
        port=int(port),
        user=user,
        password=password,
        database=database
    )

    cursor = conn.cursor()

    cursor.execute(
        f"SELECT * FROM `{table}`"
    )

    rows = cursor.fetchall()

    columns = [
        description[0]
        for description in cursor.description
    ]

    cursor.close()
    conn.close()

    return pd.DataFrame(
        rows,
        columns=columns
    )


def money(value):
    """Format currency."""

    if pd.isna(value):
        return "₹0"

    value = float(value)

    if value >= 10000000:
        return f"₹{value/10000000:.2f} Cr"

    if value >= 100000:
        return f"₹{value/100000:.2f} L"

    if value >= 1000:
        return f"₹{value/1000:.1f} K"

    return f"₹{value:,.0f}"


def safe_unique(df, column):
    """Return safe unique sorted values."""

    if column not in df.columns:
        return []

    values = (
        df[column]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    return sorted(values)


def apply_filter(df, column, selected):
    """Apply multiselect filter."""

    if (
        column in df.columns
        and selected
        and "All" not in selected
    ):
        return df[
            df[column].astype(str).isin(selected)
        ]

    return df


# ============================================================
# CHART STYLE
# ============================================================

def style_chart(ax, title):
    """Apply CRM dark theme to charts."""

    ax.set_facecolor(CHARCOAL_2)

    ax.set_title(
        title,
        color=WHITE,
        fontsize=12,
        fontweight="bold",
        pad=12
    )

    ax.tick_params(
        colors=LIGHT_TEXT,
        labelsize=8
    )

    for spine in ax.spines.values():
        spine.set_color(GRID)

    ax.grid(
        axis="y",
        color=GRID,
        alpha=0.35,
        linestyle="--",
        linewidth=0.7
    )

    ax.xaxis.label.set_color(MUTED_TEXT)
    ax.yaxis.label.set_color(MUTED_TEXT)


def finish_figure(fig):
    """Apply final chart background."""

    fig.patch.set_facecolor(CHARCOAL_2)
    fig.tight_layout()


def show_no_data(message="No data available for this filter."):
    st.info(message)


# ============================================================
# HEADER
# ============================================================

st.title(
    "Lead Conversion, Pipeline & Revenue Intelligence"
)

st.caption(
    "CRM Analytics Dashboard  •  Interactive Sales Intelligence  •  "
    "Pipeline Monitoring  •  Revenue Insights"
)

st.divider()

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("◈ CRM INTELLIGENCE")

    st.caption(
        "LEAD • PIPELINE • REVENUE"
    )

    st.divider()

    st.subheader("📂 Data Source")

    data_source = st.radio(
        "Select Data Source",
        [
            "Upload File",
            "MySQL Database"
        ],
        index=0
    )

    uploaded_file = None

    # --------------------------------------------------------
    # FILE UPLOAD
    # --------------------------------------------------------

    if data_source == "Upload File":

        uploaded_file = st.file_uploader(
            "Upload CRM Dataset",
            type=["csv", "xlsx"],
            help="Upload your cleaned CRM CSV or Excel file."
        )

    # --------------------------------------------------------
    # MYSQL
    # --------------------------------------------------------

    else:

        st.caption(
            "Enter your MySQL connection details."
        )

        mysql_host = st.text_input(
            "Host",
            value="localhost"
        )

        mysql_port = st.number_input(
            "Port",
            min_value=1,
            max_value=65535,
            value=3306
        )

        mysql_user = st.text_input(
            "Username",
            value="root"
        )

        mysql_password = st.text_input(
            "Password",
            type="password"
        )

        mysql_database = st.text_input(
            "Database",
            value="crm_database"
        )

        mysql_table = st.text_input(
            "Table",
            value="leads"
        )

        load_mysql = st.button(
            "🔌 Connect MySQL",
            use_container_width=True
        )

    st.divider()

    st.subheader("🎛️ Filters")

# ============================================================
# LOAD DATA
# ============================================================

df = None

# ------------------------------------------------------------
# UPLOAD FILE
# ------------------------------------------------------------

if data_source == "Upload File":

    if uploaded_file is not None:

        try:

            if uploaded_file.name.lower().endswith(".csv"):

                df = pd.read_csv(
                    uploaded_file
                )

            else:

                df = pd.read_excel(
                    uploaded_file
                )

            st.sidebar.success(
                "Dataset loaded successfully."
            )

        except Exception as e:

            st.error(
                f"Unable to read file: {e}"
            )

            st.stop()

    else:

        st.info(
            "👈 Upload your cleaned CRM CSV/Excel file from the sidebar."
        )

        st.stop()

# ------------------------------------------------------------
# MYSQL
# ------------------------------------------------------------

else:

    if load_mysql:

        try:

            df = load_mysql_data(
                mysql_host,
                mysql_port,
                mysql_user,
                mysql_password,
                mysql_database,
                mysql_table
            )

            st.sidebar.success(
                "MySQL connected successfully."
            )

        except Exception as e:

            st.error(
                f"MySQL connection failed: {e}"
            )

            st.stop()

    else:

        st.info(
            "👈 Enter MySQL details and click Connect MySQL."
        )

        st.stop()

# ============================================================
# CLEAN DATA
# ============================================================

df = clean_dataframe(df)

# Remove completely empty rows
df = df.dropna(
    how="all"
).reset_index(drop=True)

# ============================================================
# CHECK REQUIRED COLUMNS
# ============================================================

required_columns = [
    "Lead_ID",
    "Lead_Date",
    "Lead_Source",
    "Industry",
    "Company_Size",
    "City",
    "Lead_Type",
    "Product_Interest",
    "Budget",
    "Salesperson_ID",
    "First_Contact_Date",
    "Followup_Count",
    "Response_Time_Hours",
    "Engagement_Score",
    "Opportunity_Value",
    "Lead_Status",
    "Lost_Reason",
    "Conversion_Date"
]

missing_columns = [
    col
    for col in required_columns
    if col not in df.columns
]

if missing_columns:

    st.error(
        "Missing required columns: "
        + ", ".join(missing_columns)
    )

    st.info(
        "Please check your cleaned CRM dataset column names."
    )

    st.stop()

# ============================================================
# EXECUTIVE SALES OVERVIEW
# ============================================================

st.subheader("📊 Executive Sales Overview")

total_leads = len(df)

converted_leads = (
    df["Lead_Status"]
    .astype(str)
    .str.lower()
    .eq("converted")
    .sum()
)

qualified_leads = (
    df["Lead_Status"]
    .astype(str)
    .str.lower()
    .eq("qualified")
    .sum()
)

pipeline_value = pd.to_numeric(
    df["Opportunity_Value"],
    errors="coerce"
).fillna(0).sum()

conversion_rate = (
    converted_leads / total_leads * 100
    if total_leads > 0
    else 0
)

avg_deal_value = (
    pipeline_value / converted_leads
    if converted_leads > 0
    else 0
)

k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    st.metric(
        "Total Leads",
        f"{total_leads:,}"
    )

with k2:
    st.metric(
        "Converted Leads",
        f"{converted_leads:,}"
    )

with k3:
    st.metric(
        "Conversion Rate",
        f"{conversion_rate:.1f}%"
    )

with k4:
    st.metric(
        "Pipeline Value",
        money(pipeline_value)
    )

with k5:
    st.metric(
        "Avg. Deal Value",
        money(avg_deal_value)
    )

st.divider()

# ============================================================
# SIDEBAR FILTERS
# ============================================================

with st.sidebar:

    status_options = safe_unique(
        df,
        "Lead_Status"
    )

    source_options = safe_unique(
        df,
        "Lead_Source"
    )

    industry_options = safe_unique(
        df,
        "Industry"
    )

    city_options = safe_unique(
        df,
        "City"
    )

    selected_status = st.multiselect(
        "Lead Status",
        ["All"] + status_options,
        default=["All"]
    )

    selected_source = st.multiselect(
        "Lead Source",
        ["All"] + source_options,
        default=["All"]
    )

    selected_industry = st.multiselect(
        "Industry",
        ["All"] + industry_options,
        default=["All"]
    )

    selected_city = st.multiselect(
        "City",
        ["All"] + city_options,
        default=["All"]
    )

    st.caption("Lead Date Range")

    valid_dates = df["Lead_Date"].dropna()

    if len(valid_dates) > 0:

        min_date = valid_dates.min().date()
        max_date = valid_dates.max().date()

        selected_dates = st.date_input(
            "Select Date Range",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date
        )

    else:

        selected_dates = ()

# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()

filtered_df = apply_filter(
    filtered_df,
    "Lead_Status",
    selected_status
)

filtered_df = apply_filter(
    filtered_df,
    "Lead_Source",
    selected_source
)

filtered_df = apply_filter(
    filtered_df,
    "Industry",
    selected_industry
)

filtered_df = apply_filter(
    filtered_df,
    "City",
    selected_city
)

# Date filter
if (
    isinstance(selected_dates, tuple)
    and len(selected_dates) == 2
):

    start_date = pd.Timestamp(
        selected_dates[0]
    )

    end_date = pd.Timestamp(
        selected_dates[1]
    )

    filtered_df = filtered_df[
        filtered_df["Lead_Date"].between(
            start_date,
            end_date
        )
    ]

# ============================================================
# FILTER SUMMARY
# ============================================================

st.subheader("🎯 Active Filter Summary")

f1, f2, f3, f4 = st.columns(4)

filtered_leads = len(filtered_df)

filtered_converted = (
    filtered_df["Lead_Status"]
    .astype(str)
    .str.lower()
    .eq("converted")
    .sum()
)

filtered_pipeline = pd.to_numeric(
    filtered_df["Opportunity_Value"],
    errors="coerce"
).fillna(0).sum()

filtered_conversion_rate = (
    filtered_converted / filtered_leads * 100
    if filtered_leads > 0
    else 0
)

with f1:
    st.metric(
        "Filtered Leads",
        f"{filtered_leads:,}"
    )

with f2:
    st.metric(
        "Filtered Converted",
        f"{filtered_converted:,}"
    )

with f3:
    st.metric(
        "Filtered Pipeline",
        money(filtered_pipeline)
    )

with f4:
    st.metric(
        "Filtered Conversion",
        f"{filtered_conversion_rate:.1f}%"
    )

st.divider()

# ============================================================
# 9 CHART DASHBOARD
# ============================================================

st.subheader("📈 CRM Analytics Dashboard")

if filtered_df.empty:

    st.warning(
        "No records match the selected filters. "
        "Please change the filters."
    )

else:

    # ========================================================
    # ROW 1
    # ========================================================

    c1, c2, c3 = st.columns(3)

    # --------------------------------------------------------
    # 1. DONUT CHART - LEAD STATUS
    # --------------------------------------------------------

    with c1:

        fig, ax = plt.subplots(
            figsize=(5, 4)
        )

        status_counts = (
            filtered_df["Lead_Status"]
            .value_counts()
        )

        if len(status_counts) > 0:

            wedges, texts = ax.pie(
                status_counts.values,
                startangle=90,
                wedgeprops={
                    "width": 0.40,
                    "edgecolor": CHARCOAL_2
                }
            )

            ax.legend(
                wedges,
                [
                    f"{label}  ({value})"
                    for label, value
                    in zip(
                        status_counts.index,
                        status_counts.values
                    )
                ],
                loc="center left",
                bbox_to_anchor=(0.95, 0.5),
                frameon=False,
                labelcolor=WHITE,
                fontsize=8
            )

            ax.set_title(
                "Lead Status Distribution",
                color=WHITE,
                fontsize=12,
                fontweight="bold",
                pad=15
            )

        finish_figure(fig)

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)

    # --------------------------------------------------------
    # 2. COLUMN CHART - LEAD SOURCE
    # --------------------------------------------------------

    with c2:

        fig, ax = plt.subplots(
            figsize=(5, 4)
        )

        source_counts = (
            filtered_df["Lead_Source"]
            .value_counts()
            .head(8)
        )

        if len(source_counts) > 0:

            bars = ax.bar(
                source_counts.index.astype(str),
                source_counts.values,
                color=DUSTY_ROSE,
                edgecolor=DUSTY_ROSE_LIGHT,
                linewidth=0.8
            )

            ax.set_title(
                "Leads by Lead Source",
                color=WHITE,
                fontsize=12,
                fontweight="bold"
            )

            ax.set_ylabel(
                "Number of Leads",
                color=MUTED_TEXT
            )

            ax.tick_params(
                axis="x",
                rotation=35
            )

            style_chart(
                ax,
                "Leads by Lead Source"
            )

            for bar in bars:

                height = bar.get_height()

                ax.text(
                    bar.get_x()
                    + bar.get_width() / 2,
                    height,
                    f"{int(height)}",
                    ha="center",
                    va="bottom",
                    color=WHITE,
                    fontsize=8
                )

        finish_figure(fig)

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)

    # --------------------------------------------------------
    # 3. LINE CHART - MONTHLY LEAD TREND
    # --------------------------------------------------------

    with c3:

        fig, ax = plt.subplots(
            figsize=(5, 4)
        )

        monthly = (
            filtered_df
            .dropna(subset=["Lead_Date"])
            .assign(
                Month=lambda x:
                x["Lead_Date"].dt.to_period("M")
            )
            .groupby("Month")
            .size()
        )

        if len(monthly) > 0:

            x_labels = [
                str(x)
                for x in monthly.index
            ]

            ax.plot(
                x_labels,
                monthly.values,
                color=DUSTY_ROSE_LIGHT,
                marker="o",
                markersize=5,
                linewidth=2.5
            )

            ax.fill_between(
                range(len(monthly)),
                monthly.values,
                alpha=0.12
            )

            ax.set_title(
                "Monthly Lead Trend",
                color=WHITE,
                fontsize=12,
                fontweight="bold"
            )

            ax.set_ylabel(
                "Leads",
                color=MUTED_TEXT
            )

            ax.tick_params(
                axis="x",
                rotation=35
            )

            style_chart(
                ax,
                "Monthly Lead Trend"
            )

        finish_figure(fig)

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)

    # ========================================================
    # ROW 2
    # ========================================================

    c4, c5, c6 = st.columns(3)

    # --------------------------------------------------------
    # 4. HORIZONTAL BAR - PIPELINE BY SOURCE
    # --------------------------------------------------------

    with c4:

        fig, ax = plt.subplots(
            figsize=(5, 4)
        )

        pipeline_source = (
            filtered_df
            .groupby("Lead_Source")["Opportunity_Value"]
            .sum()
            .sort_values()
            .tail(8)
        )

        if len(pipeline_source) > 0:

            bars = ax.barh(
                pipeline_source.index.astype(str),
                pipeline_source.values,
                color=DUSTY_ROSE_DARK,
                edgecolor=DUSTY_ROSE_LIGHT
            )

            ax.set_title(
                "Pipeline Value by Lead Source",
                color=WHITE,
                fontsize=12,
                fontweight="bold"
            )

            ax.set_xlabel(
                "Opportunity Value",
                color=MUTED_TEXT
            )

            style_chart(
                ax,
                "Pipeline Value by Lead Source"
            )

            ax.grid(
                axis="x",
                color=GRID,
                alpha=0.35,
                linestyle="--"
            )

            for bar in bars:

                value = bar.get_width()

                ax.text(
                    value,
                    bar.get_y()
                    + bar.get_height() / 2,
                    f" ₹{value/1000:.0f}K",
                    va="center",
                    color=WHITE,
                    fontsize=8
                )

        finish_figure(fig)

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)

    # --------------------------------------------------------
    # 5. HORIZONTAL BAR - INDUSTRY OPPORTUNITY VALUE
    # --------------------------------------------------------

    with c5:

        fig, ax = plt.subplots(
            figsize=(5, 4)
        )

        industry_value = (
            filtered_df
            .groupby("Industry")["Opportunity_Value"]
            .sum()
            .sort_values()
            .tail(8)
        )

        if len(industry_value) > 0:

            bars = ax.barh(
                industry_value.index.astype(str),
                industry_value.values,
                color=DUSTY_ROSE,
                edgecolor=DUSTY_ROSE_LIGHT
            )

            ax.set_title(
                "Industry-wise Opportunity Value",
                color=WHITE,
                fontsize=12,
                fontweight="bold"
            )

            ax.set_xlabel(
                "Opportunity Value",
                color=MUTED_TEXT
            )

            style_chart(
                ax,
                "Industry-wise Opportunity Value"
            )

            ax.grid(
                axis="x",
                color=GRID,
                alpha=0.35,
                linestyle="--"
            )

            for bar in bars:

                value = bar.get_width()

                ax.text(
                    value,
                    bar.get_y()
                    + bar.get_height() / 2,
                    f" ₹{value/1000:.0f}K",
                    va="center",
                    color=WHITE,
                    fontsize=8
                )

        finish_figure(fig)

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)

    # --------------------------------------------------------
    # 6. COLUMN CHART - CITY
    # --------------------------------------------------------

    with c6:

        fig, ax = plt.subplots(
            figsize=(5, 4)
        )

        city_counts = (
            filtered_df["City"]
            .value_counts()
            .head(8)
        )

        if len(city_counts) > 0:

            bars = ax.bar(
                city_counts.index.astype(str),
                city_counts.values,
                color=DUSTY_ROSE_LIGHT,
                edgecolor=DUSTY_ROSE
            )

            ax.set_title(
                "City-wise Lead Distribution",
                color=WHITE,
                fontsize=12,
                fontweight="bold"
            )

            ax.set_ylabel(
                "Leads",
                color=MUTED_TEXT
            )

            ax.tick_params(
                axis="x",
                rotation=35
            )

            style_chart(
                ax,
                "City-wise Lead Distribution"
            )

            for bar in bars:

                height = bar.get_height()

                ax.text(
                    bar.get_x()
                    + bar.get_width() / 2,
                    height,
                    f"{int(height)}",
                    ha="center",
                    va="bottom",
                    color=WHITE,
                    fontsize=8
                )

        finish_figure(fig)

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)

    # ========================================================
    # ROW 3
    # ========================================================

    c7, c8, c9 = st.columns(3)

    # --------------------------------------------------------
    # 7. SCATTER - BUDGET VS OPPORTUNITY VALUE
    # --------------------------------------------------------

    with c7:

        fig, ax = plt.subplots(
            figsize=(5, 4)
        )

        scatter_df = filtered_df[
            [
                "Budget",
                "Opportunity_Value"
            ]
        ].dropna()

        if len(scatter_df) > 0:

            ax.scatter(
                scatter_df["Budget"],
                scatter_df["Opportunity_Value"],
                s=55,
                alpha=0.72,
                color=DUSTY_ROSE_LIGHT,
                edgecolor=DUSTY_ROSE_DARK,
                linewidth=0.8
            )

            ax.set_title(
                "Budget vs Opportunity Value",
                color=WHITE,
                fontsize=12,
                fontweight="bold"
            )

            ax.set_xlabel(
                "Budget",
                color=MUTED_TEXT
            )

            ax.set_ylabel(
                "Opportunity Value",
                color=MUTED_TEXT
            )

            style_chart(
                ax,
                "Budget vs Opportunity Value"
            )

            ax.grid(
                color=GRID,
                alpha=0.25,
                linestyle="--"
            )

        finish_figure(fig)

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)

    # --------------------------------------------------------
    # 8. BAR - ENGAGEMENT BY STATUS
    # --------------------------------------------------------

    with c8:

        fig, ax = plt.subplots(
            figsize=(5, 4)
        )

        engagement = (
            filtered_df
            .groupby("Lead_Status")[
                "Engagement_Score"
            ]
            .mean()
            .sort_values()
        )

        if len(engagement) > 0:

            bars = ax.bar(
                engagement.index.astype(str),
                engagement.values,
                color=DUSTY_ROSE_DARK,
                edgecolor=DUSTY_ROSE_LIGHT
            )

            ax.set_title(
                "Average Engagement by Lead Status",
                color=WHITE,
                fontsize=12,
                fontweight="bold"
            )

            ax.set_ylabel(
                "Average Engagement Score",
                color=MUTED_TEXT
            )

            ax.tick_params(
                axis="x",
                rotation=25
            )

            style_chart(
                ax,
                "Average Engagement by Lead Status"
            )

            for bar in bars:

                height = bar.get_height()

                ax.text(
                    bar.get_x()
                    + bar.get_width() / 2,
                    height,
                    f"{height:.1f}",
                    ha="center",
                    va="bottom",
                    color=WHITE,
                    fontsize=8
                )

        finish_figure(fig)

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)

    # --------------------------------------------------------
    # 9. SALESPERSON PIPELINE
    # --------------------------------------------------------

    with c9:

        fig, ax = plt.subplots(
            figsize=(5, 4)
        )

        salesperson_pipeline = (
            filtered_df
            .groupby("Salesperson_ID")[
                "Opportunity_Value"
            ]
            .sum()
            .sort_values()
            .tail(8)
        )

        if len(salesperson_pipeline) > 0:

            bars = ax.barh(
                salesperson_pipeline.index.astype(str),
                salesperson_pipeline.values,
                color=DUSTY_ROSE_LIGHT,
                edgecolor=DUSTY_ROSE
            )

            ax.set_title(
                "Salesperson-wise Pipeline Value",
                color=WHITE,
                fontsize=12,
                fontweight="bold"
            )

            ax.set_xlabel(
                "Pipeline Value",
                color=MUTED_TEXT
            )

            style_chart(
                ax,
                "Salesperson-wise Pipeline Value"
            )

            ax.grid(
                axis="x",
                color=GRID,
                alpha=0.35,
                linestyle="--"
            )

            for bar in bars:

                value = bar.get_width()

                ax.text(
                    value,
                    bar.get_y()
                    + bar.get_height() / 2,
                    f" ₹{value/1000:.0f}K",
                    va="center",
                    color=WHITE,
                    fontsize=8
                )

        finish_figure(fig)

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)

# ============================================================
# SALES INTELLIGENCE
# ============================================================

st.divider()

st.subheader("💡 Sales Intelligence")

if not filtered_df.empty:

    si1, si2, si3 = st.columns(3)

    # Top source
    source_count = (
        filtered_df["Lead_Source"]
        .value_counts()
    )

    top_source = (
        source_count.index[0]
        if len(source_count) > 0
        else "N/A"
    )

    # Top industry
    industry_value = (
        filtered_df
        .groupby("Industry")[
            "Opportunity_Value"
        ]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    top_industry = (
        industry_value.index[0]
        if len(industry_value) > 0
        else "N/A"
    )

    # Top city
    city_count = (
        filtered_df["City"]
        .value_counts()
    )

    top_city = (
        city_count.index[0]
        if len(city_count) > 0
        else "N/A"
    )

    with si1:

        st.metric(
            "Top Lead Source",
            str(top_source)
        )

    with si2:

        st.metric(
            "Top Industry by Pipeline",
            str(top_industry)
        )

    with si3:

        st.metric(
            "Top Lead City",
            str(top_city)
        )

# ============================================================
# SALESPERSON PERFORMANCE
# ============================================================

st.divider()

st.subheader("👥 Salesperson Performance")

if not filtered_df.empty:

    salesperson_summary = (
        filtered_df
        .groupby("Salesperson_ID")
        .agg(
            Leads=("Lead_ID", "count"),
            Converted=(
                "Lead_Status",
                lambda x:
                x.astype(str)
                .str.lower()
                .eq("converted")
                .sum()
            ),
            Pipeline_Value=(
                "Opportunity_Value",
                "sum"
            ),
            Avg_Engagement=(
                "Engagement_Score",
                "mean"
            )
        )
        .reset_index()
    )

    salesperson_summary[
        "Conversion_Rate"
    ] = np.where(
        salesperson_summary["Leads"] > 0,
        salesperson_summary["Converted"]
        / salesperson_summary["Leads"]
        * 100,
        0
    )

    salesperson_summary[
        "Pipeline_Value"
    ] = salesperson_summary[
        "Pipeline_Value"
    ].round(0)

    salesperson_summary[
        "Avg_Engagement"
    ] = salesperson_summary[
        "Avg_Engagement"
    ].round(1)

    salesperson_summary[
        "Conversion_Rate"
    ] = salesperson_summary[
        "Conversion_Rate"
    ].round(1)

    salesperson_summary = (
        salesperson_summary
        .sort_values(
            "Pipeline_Value",
            ascending=False
        )
        .reset_index(drop=True)
    )

    st.dataframe(
        salesperson_summary,
        use_container_width=True,
        hide_index=True
    )

# ============================================================
# DATA EXPLORER
# ============================================================

st.divider()

st.subheader("🔎 Data Explorer")

tab1, tab2 = st.tabs(
    [
        "📋 Data Preview",
        "📊 Summary"
    ]
)

with tab1:

    st.caption(
        f"Showing {len(filtered_df):,} filtered records"
    )

    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=420,
        hide_index=True
    )

with tab2:

    summary1, summary2, summary3 = st.columns(3)

    with summary1:

        st.metric(
            "Rows",
            f"{len(filtered_df):,}"
        )

    with summary2:

        st.metric(
            "Columns",
            f"{len(filtered_df.columns):,}"
        )

    with summary3:

        missing_count = (
            filtered_df.isna()
            .sum()
            .sum()
        )

        st.metric(
            "Missing Cells",
            f"{missing_count:,}"
        )

# ============================================================
# DOWNLOAD
# ============================================================

st.divider()

st.subheader("⬇️ Export Filtered Data")

download_df = filtered_df.copy()

csv_data = download_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="📥 Download Filtered CRM Data (CSV)",
    data=csv_data,
    file_name="filtered_crm_leads.csv",
    mime="text/csv",
    use_container_width=False
)

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Lead Conversion, Pipeline & Revenue Intelligence Platform  |  "
    "Built with Python • Pandas • NumPy • Matplotlib • Streamlit • MySQL • Power BI"
)

st.caption(
    "CRM Analytics Dashboard • Interactive Sales Intelligence"
)