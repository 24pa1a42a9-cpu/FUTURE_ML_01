Walmart Sales Forecasting using Machine Learning

Project Overview

This project aims to forecast future Walmart weekly sales using historical sales data and machine learning techniques. Accurate sales forecasting helps businesses improve inventory management, workforce planning, promotional strategies, and supply chain operations.

The project uses Walmart sales, store, and feature datasets to build a predictive model capable of estimating future weekly sales based on historical trends, economic indicators, seasonal patterns, and promotional activities.

---

Objectives

- Analyze historical Walmart sales data.
- Perform data cleaning and exploratory data analysis (EDA).
- Create time-based features from date information.
- Train a machine learning model for sales prediction.
- Evaluate model performance using standard regression metrics.
- Visualize actual and predicted sales trends.

---

Dataset

The project uses the Walmart Store Sales Forecasting dataset containing:

- Weekly Sales
- Store Information
- Holiday Information
- Temperature
- Fuel Price
- Consumer Price Index (CPI)
- Unemployment Rate
- Promotional MarkDown Features

---

Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Google Colab
- Streamlit

---

Feature Engineering

The following features were used:

- Store
- Department
- IsHoliday
- Temperature
- Fuel_Price
- MarkDown1
- MarkDown2
- MarkDown3
- MarkDown4
- MarkDown5
- CPI
- Unemployment
- Year
- Month
- Day
- WeekOfYear

Date columns were converted into meaningful time-based features to capture seasonal sales patterns.

---

Machine Learning Model

Model Used:

- Random Forest Regressor

The model was trained on historical sales data and evaluated on unseen test data.

---

Model Performance

Metric| Value
R² Score| 0.9684
MAE| 1513
RMSE| 4058.70
MSE| 16,473,070

Interpretation

- The model explains approximately 96.84% of the variation in weekly sales.
- Average prediction error is approximately 1513 sales units.
- The model demonstrates strong forecasting performance and reliability.

---

Business Impact

This forecasting system can help businesses:

- Predict future product demand.
- Optimize inventory levels.
- Reduce stock shortages and overstocking.
- Improve workforce scheduling.
- Plan promotional campaigns effectively.
- Support data-driven decision making.

---

Project Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Sales Forecasting
8. Visualization and Reporting

---

Results

The predicted sales closely follow actual sales trends, indicating strong predictive capability and successful model training.

---
Note
Due to GitHub file size limitations, the trained Random Forest model file (sales_forecast_model.pkl) is not included in this repository.
The complete training pipeline, feature engineering steps, model development process, and evaluation results are provided in the Jupyter Notebook. The model can be reproduced by running the notebook from start to finish.

Future Improvements

- Incorporate lag features and rolling averages.
- Experiment with XGBoost and LightGBM.
- Deploy as a fully interactive Streamlit dashboard.
- Add real-time forecasting capabilities.

---

Author

Akhil Lakshmi Narasimha

B.Tech CSE (AI & ML)

Machine Learning Project – Walmart Sales Forecasting
