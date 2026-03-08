<<<<<<< HEAD

## Step 1: Data Understanding, Preprocessing & Visualization

In this step, I performed comprehensive data preprocessing and exploratory data analysis on a real-world online retail dataset following the KDD process.

Key tasks included:

- Data cleaning by removing missing customer records, invalid transactions, and duplicates
- Data transformation through feature engineering (e.g., transaction-level total amount)
- Exploratory visualization using histograms, bar charts, pie charts, and box plots
- Identification of skewness and outliers to guide downstream modeling and data reduction

# This step established a clean, reliable foundation for subsequent data mining tasks such as association rule mining, classification, clustering, and outlier detection.

# Retail-Data-Mining-System

Exploratory data mining project using Python, pandas, and Jupyter.

> > > > > > > 0b4088671f243ee54c1a7cb3e8c76190ffc33d8c

## Step 2: Data Mart Design & OLAP-Style Analysis

In this step, transactional retail data was transformed into an analytical data mart consisting of fact and dimension tables. OLAP-style aggregations were performed to analyze sales trends across time, products, and geographies, enabling efficient analytical querying and insight generation.

## 🔍 Step 3: Market Basket Analysis with FP-Growth

To identify frequently co-purchased products, I applied the `fpgrowth()` algorithm from `mlxtend.frequent_patterns`. Unlike Apriori, which caused memory issues due to the dataset size (330K+ transactions, 18K+ items), FP-Growth scales efficiently by using a prefix tree (FP-tree) to mine frequent itemsets without generating all combinations.

### 🛠️ Key Steps

- Transformed transaction data into a basket format (invoices × products)
- Converted quantities to booleans for binary encoding
- Applied FP-Growth with `min_support=0.01`
- Sorted itemsets by support to reveal top co-purchased products

### ✅ Sample Output

## 📈 Step 4: Association Rule Mining

Using the frequent itemsets from FP-Growth, I generated association rules to uncover product relationships.

### ⚙️ Process

- Applied `association_rules()` with `metric="lift"`
- Filtered rules with `confidence ≥ 0.6` and `lift ≥ 1.2`
- Sorted and visualized to highlight strong patterns

### 🧠 Example

> If a customer buys **Tea Cups**, they are likely to also buy **Saucers** (Lift = 1.45, Confidence = 68%).

This step enabled data-driven insights into co-purchasing behavior — setting the stage for product recommendations.

## ✅ Step 5 Summary: Product Recommendation System

- Built a rule-based recommender using association rules
- Extracted recommendations by matching antecedents
- Displayed top recommendations based on confidence and lift
- Tested on real product names like `'PINK REGENCY TEACUP AND SAUCER'`
