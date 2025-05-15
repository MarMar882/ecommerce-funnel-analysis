# E-Commerce Funnel Analysis

This project analyzes user session behavior from a real-world multi-category e-commerce platform in Brazil.  
The goal is to understand where users drop off in the purchase funnel — from viewing a product, to adding it to cart, to completing a purchase.

---

## Dataset

The dataset is sourced from Kaggle and represents behavioral data from a large Brazilian e-commerce site.  
It contains over 40 million events between October and November 2019.

For performance reasons, a random sample of 200,000 rows is used.

- Source: [E-Commerce Behavior Data from Multi Category Store (Kaggle)](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)
- Format: CSV
- Columns used: `event_time`, `event_type`, `user_session`

---

## Funnel Stages Analyzed

Sessions are grouped and categorized into the following types:

- Only View  
- View + Cart (No Purchase)  
- View + Purchase (No Cart)  
- Full Funnel (View + Cart + Purchase)

Key finding:  
More than 96% of sessions include only a product view.  
However, users who add items to their cart are significantly more likely (≈55%) to complete a purchase.

---

## Project Structure

| File | Description |
|------|-------------|
| `src/01_load_data.py` | Loads and combines October & November data  
| `src/02_funnel_analysis.py` | Classifies sessions and computes funnel conversion  
| `charts/funnel_bar_horizontal.png` | Output chart showing session breakdown  
| `insights.md` | Key takeaways from the funnel analysis  
| `requirements.txt` | Python dependencies  
| `LICENSE` | MIT License  

---

## Sample Output

![Funnel Chart](charts/funnel_bar_horizontal.png)

---

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/ecommerce-funnel-analysis.git
cd ecommerce-funnel-analysis


pip install -r requirements.txt
