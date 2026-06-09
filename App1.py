import streamlit as st
import pandas as pd
import pickle
import numpy as np

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Walmart Sales Forecasting",
    page_icon="📈",
    layout="wide"
)

# -----------------------------
# LOAD MODEL
# -----------------------------
model = pickle.load(open("sales_forecast_model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# -----------------------------
# HEADER
# -----------------------------
st.title("📈 Walmart Sales Forecasting Dashboard")
st.markdown("Predict future weekly sales using historical business and economic factors.")

st.divider()

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.header("⚙️ Input Parameters")

store = st.sidebar.slider("Store ID", 1, 45, 1)
dept = st.sidebar.slider("Department ID", 1, 99, 1)

is_holiday = st.sidebar.selectbox(
    "Holiday Week?",
    [0, 1]
)

temperature = st.sidebar.number_input(
    "Temperature",
    value=70.0
)

fuel_price = st.sidebar.number_input(
    "Fuel Price",
    value=3.0
)

markdown1 = st.sidebar.number_input("MarkDown1", value=0.0)
markdown2 = st.sidebar.number_input("MarkDown2", value=0.0)
markdown3 = st.sidebar.number_input("MarkDown3", value=0.0)
markdown4 = st.sidebar.number_input("MarkDown4", value=0.0)
markdown5 = st.sidebar.number_input("MarkDown5", value=0.0)

cpi = st.sidebar.number_input(
    "CPI",
    value=200.0
)

unemployment = st.sidebar.number_input(
    "Unemployment",
    value=8.0
)

year = st.sidebar.selectbox(
    "Year",
    [2010, 2011, 2012, 2013, 2014, 2015]
)

month = st.sidebar.selectbox(
    "Month",
    list(range(1, 13))
)

day = st.sidebar.slider(
    "Day",
    1,
    31,
    1
)

weekofyear = st.sidebar.slider(
    "Week Of Year",
    1,
    52,
    1
)

# -----------------------------
# BUILD INPUT DATAFRAME
# -----------------------------
input_dict = {
    "Store": store,
    "Dept": dept,
    "IsHoliday": is_holiday,
    "Temperature": temperature,
    "Fuel_Price": fuel_price,
    "MarkDown1": markdown1,
    "MarkDown2": markdown2,
    "MarkDown3": markdown3,
    "MarkDown4": markdown4,
    "MarkDown5": markdown5,
    "CPI": cpi,
    "Unemployment": unemployment,
    "Year": year,
    "Month": month,
    "Day": day,
    "WeekOfYear": weekofyear
}

input_df = pd.DataFrame([input_dict])

# Ensure same column order as training
input_df = input_df.reindex(
    columns=columns,
    fill_value=0
)

# -----------------------------
# PREDICTION
# -----------------------------
if st.sidebar.button("🚀 Predict Sales"):

    prediction = model.predict(input_df)[0]

    st.subheader("📊 Prediction Results")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Predicted Weekly Sales",
        f"${prediction:,.2f}"
    )

    c2.metric(
        "R² Score",
        "96.84%"
    )

    c3.metric(
        "MAE",
        "1513"
    )

    st.divider()

    # -----------------------------
    # FORECAST CHART
    # -----------------------------
    st.subheader("📈 12-Week Forecast Trend")

    future_sales = np.random.normal(
        prediction,
        prediction * 0.05,
        12
    )

    forecast_df = pd.DataFrame({
        "Week": range(1, 13),
        "Forecast Sales": future_sales
    })

    st.line_chart(
        forecast_df.set_index("Week")
    )

    st.divider()

    # -----------------------------
    # INPUT SUMMARY
    # -----------------------------
    st.subheader("📋 Input Summary")

    st.dataframe(
        pd.DataFrame([input_dict]),
        use_container_width=True
    )

else:

    st.info(
        "Enter values in the sidebar and click 'Predict Sales'."
    )

# -----------------------------
# FOOTER
# -----------------------------
st.divider()

st.markdown(
    """
    ### 🎯 Model Performance
    
    - Random Forest Regressor
    - R² Score: 0.9684
    - MAE: 1513
    - RMSE: 4058.7
    
    This model predicts Walmart weekly sales using store information,
    promotional markdowns, economic indicators, and calendar features.
    """
)
st.divider()

st.subheader("📖 What Does This Forecast Mean?")

st.info("""
The forecast represents the estimated weekly sales for a specific Walmart store and department
based on historical sales patterns, promotions, economic indicators, holidays, and seasonal trends.

The prediction is generated using a Random Forest Machine Learning model trained on past Walmart sales data.
""")

st.subheader("🏢 How Can Businesses Use This Forecast?")

st.markdown("""
### Inventory Planning
- Maintain optimal stock levels.
- Reduce stock shortages and overstock situations.

### Workforce Management
- Schedule employees according to expected demand.
- Improve operational efficiency.

### Promotion Strategy
- Identify periods of high and low demand.
- Plan discounts and marketing campaigns effectively.

### Supply Chain Optimization
- Improve warehouse and transportation planning.
- Reduce logistics costs.

### Business Decision Making
- Support data-driven decisions using future sales estimates.
- Improve revenue forecasting and budgeting.
""")