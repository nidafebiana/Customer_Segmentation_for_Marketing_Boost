# Customer Segmentation for Marketing Boost

📊 **Objective:**
This project aims to analyze customer personality data to identify customer segments and optimize marketing campaigns.  
By understanding customer behavior and spending patterns, the company can focus marketing budgets on high-value segments.

---

## 🧠 Project Overview
- Data cleaning and preprocessing (handle missing values, duplicates)
- Feature engineering (total spend, total purchases, online ratio)
- Clustering customers based on behavior
- Business recommendations for marketing optimization

---

## 🧩 Dataset
- Source: [Customer Personality Analysis Dataset (Kaggle)](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)
- Size: 2240 records, 29 features
- Target: Grouping customers into behavioral segments

---

## 🧰 Tools & Libraries
```
Python   
pandas  
numpy  
matplotlib  
seaborn  
scikit-learn  
```

---

## 🚀 Results & Insights

Based on the customer segmentation process using K-Means clustering, three distinct clusters were identified:

1. Cluster 0 – “Premium Loyal Spenders”

Size: 660 customers (≈29% of total population)

Profile: High-income customers with consistent and high spending behavior across product categories.

Behavioral Traits:

- Frequently purchase both online and in-store.
- Responsive to campaigns and tend to accept promotions.
- Contribute the largest portion of GMV (Gross Merchandise Value).

Marketing Strategy:
- Focus marketing efforts and personalized campaigns here — this group drives high revenue and has strong brand loyalty.

2. Cluster 1 – “Active Mid-Level Shoppers”

Size: 549 customers (≈25% of total population)

Profile: Middle-income segment with active engagement across multiple channels.

Behavioral Traits:

Average to high frequency in online purchases.

- Moderate campaign acceptance rate.
- Stable contribution to total GMV.

Marketing Strategy:
- Maintain engagement with regular promotions and loyalty programs. Upselling and cross-selling can be effective here.

3. Cluster 2 – “Low Spenders / Minimal Responders”

Size: 1,031 customers (≈46% of total population)

Profile: Low-income or low-activity customers who spend the least.

Behavioral Traits:

- Rarely purchase products and have minimal campaign interaction.

- Low contribution to overall GMV.

Marketing Strategy:
- Reduce heavy promotional spending for this segment. Focus only on cost-efficient retention tactics or targeted reactivation campaigns.

💡 Strategic Recommendation

By focusing the campaign budget on Cluster 0 and 1 (total 1,209 customers or 54% of population),
the company can still retain 92.7% of total GMV, approximately Rp 1,258,502,000.

Since Cluster 2 requires minimal promotional cost, reducing its campaign budget by 50% could yield
cost savings of around Rp 25,775,000 annually.

---

## 🧾 File Structure
```
notebooks/
 └── Customer_Segmentation_for_Marketing_Boost.ipynb  # main analysis
src/
 └── data_preprocessing.py  # helper functions
data/
 └── (optional) marketing_campaign_data.csv
```

---

## 📈 How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/username/Customer_Segmentation_for_Marketing_Boost.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Open the Jupyter Notebook and run all cells.

or

## 🚀 Setup & Usage

You can run this project directly on **Google Colab** without local installation.

1. Open the notebook file in Google Colab:
   - [Open in Colab](https://colab.research.google.com/github/nidafebiana/Customer_Segmentation_for_Marketing_Boost/blob/main/Customer_Segmentation_for_Marketing_Boost.ipynb)

2. If any module is missing, install it inside a Colab cell:
   ```python
   !pip install pandas numpy matplotlib seaborn scikit-learn


---

## 🧑‍💼 Author
**Nida Febiana**  
_Data Analyst Enthusiast_
