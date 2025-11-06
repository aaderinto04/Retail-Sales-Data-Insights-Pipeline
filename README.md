
# Sales-Analytics-Data-Pipeline

## Overview
  The Sales Analytics Data Pipeline is a Python-based data analytics project designed to explore patterns within a sample sales dataset.
  Using Pandas and Matplotlib, the project extracts and visualizes insights such as total revenue, top-selling products, and sales trends over time.
  All data extraction, transformation, and visualization steps are automated through Python scripts.

---

## Tech Stack
- **Python** — data processing and automation
- **Pandas** — data manipulation and analysis
- **Matplotlib** — static visualizations


---

## Dataset

**Source:** [Sample Sales Data on Kaggle](https://www.kaggle.com/datasets/kyanyoga/sample-sales-data?resource=download)

**Columns include:**
- OrderID
- Product
- Quantity
- Price
- OrderDate
- CustomerID
- Region


---

## How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/aaderinto04/Retail-Sales-Data-Insights-Pipeline.git
cd sales-analytics-data-pipeline
```
### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # for macOS/Linux
venv\Scripts\activate      # for Windows
```
### 3. Install Dependencies
```bash
pip install pandas matplotlib
```
### 4. Add the Dataset

Place the CSV file `sales_data_sample.csv` in the project directory.  

**Dataset Source:** [Sample Sales Data on Kaggle](https://www.kaggle.com/datasets/kyanyoga/sample-sales-data?resource=download)
### 5. Run the ETL Script
```bash
python etl.py
```
### 6. Outputs

**KPIs printed in terminal:**
- Total revenue
- Top-selling product line

**Visualization with Matplotlib:**
- Daily or monthly revenue trend line chart
