# Brazilian E-Commerce (Olist) — End-to-End Data Analysis

An end-to-end exploratory data analysis project using the Brazilian Olist e-commerce dataset.

The project follows the original analysis notebook: loading nine related CSV tables, profiling
their structure, cleaning duplicates/missing values/data types, engineering delivery and sales
features, building a master item-level table, performing business-focused EDA, and segmenting
customers with RFM.

## Business Questions

- How much revenue does the marketplace generate and how does it change over time?
- Which product categories and Brazilian states drive the most revenue?
- How long do deliveries actually take versus the promised date?
- Does delivery speed affect customer review scores?
- How do customers pay and how many installments do they use?
- How concentrated is revenue among sellers?
- What is the repeat-purchase rate?
- Which customer segments are most valuable?

## Project Structure

```text
olist-ecommerce-data-analysis/
├── data/
│   ├── raw/
│   │   └── README.md
│   └── processed/
├── notebooks/
│   └── olist_ecommerce_eda.ipynb
├── src/
│   ├── cleaning.py
│   ├── data_loader.py
│   ├── features.py
│   ├── rfm.py
│   └── run_pipeline.py
├── reports/
│   ├── figures/
│   └── tables/
├── docs/
├── .gitignore
├── LICENSE
├── requirements.txt
└── README.md
```

## Dataset

The project uses these nine Olist files:

1. `olist_orders_dataset.csv`
2. `olist_order_items_dataset.csv`
3. `olist_order_payments_dataset.csv`
4. `olist_order_reviews_dataset.csv`
5. `olist_customers_dataset.csv`
6. `olist_products_dataset.csv`
7. `olist_sellers_dataset.csv`
8. `olist_geolocation_dataset.csv`
9. `product_category_name_translation.csv`

Put them in `data/raw/` using exactly those names.

The raw files are intentionally not committed to GitHub because the geolocation file is large
and GitHub has a 100 MB per-file limit.

## Analysis Workflow

### 1. Data loading
All nine tables are loaded into pandas DataFrames.

### 2. Data understanding
The notebook checks:

- table dimensions
- memory usage
- column names
- data types
- sample records
- relationships between tables

### 3. Data cleaning
The analysis includes:

- exact duplicate detection
- geolocation duplicate removal
- missing-value reporting
- timestamp conversion
- city-name standardisation
- product-category translation

### 4. Feature engineering
Derived fields include:

- actual delivery days
- estimated delivery days
- delay days
- late-order flag
- order year/month/day/hour
- item revenue
- same-state seller/customer flag

### 5. Master table
The item-level table is used as the base because price and freight are recorded at item level.
Order, customer, product and seller information are then attached.

### 6. EDA
The notebook analyses:

- order status
- revenue and order trends
- seasonality
- product categories
- price behaviour
- geography
- payment methods
- delivery performance
- reviews and satisfaction
- seller performance
- customer repeat behaviour
- correlations

### 7. RFM segmentation
Customers are scored on:

- **Recency** — how recently they purchased
- **Frequency** — how often they purchased
- **Monetary** — how much they spent

Segments:

- Champions
- Loyal
- Potential
- At Risk
- Lost

## Run Locally

```bash
git clone <your-repository-url>
cd olist-ecommerce-data-analysis

python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

Add the nine CSV files to `data/raw/`.

### Run the notebook

```bash
jupyter notebook
```

Open:

```text
notebooks/olist_ecommerce_eda.ipynb
```

### Run the reusable pipeline

From the project root:

```bash
python src/run_pipeline.py
```

It writes derived datasets to `data/processed/`.

## Key Deliverables

- End-to-end EDA notebook
- Reusable data loading and cleaning modules
- Feature-engineering pipeline
- RFM customer segmentation
- Business recommendations and insights inside the notebook
- Processed master and delivered-order tables when the pipeline is run

## Suggested GitHub Repository Topics

`python` `pandas` `numpy` `data-analysis` `eda` `data-visualization` `seaborn`
`matplotlib` `ecommerce` `olist` `customer-segmentation` `rfm-analysis`
`business-intelligence`

## Skills Demonstrated

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Data cleaning
- Missing-value analysis
- Duplicate handling
- Datetime analysis
- Feature engineering
- Multi-table joins
- Exploratory data analysis
- Customer segmentation
- Business insight generation
- Data storytelling
