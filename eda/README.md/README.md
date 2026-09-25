Beyond Discounts: Exploring Sales, Discounts and Profit in Retail
Project Overview

This project uses exploratory data analysis (EDA) to investigate the relationship between sales, discounts, and profit in a retail dataset.

The goal is to identify patterns in profitability across product categories and discount levels and translate those findings into practical business recommendations.

Business Question

How are discounts related to profitability, and which product categories generate the most profit?

The analysis explores:

Which product category generates the most sales and profit?
How are discount levels related to profit?
How many transactions result in a loss?
Which categories show differences between sales and profitability?
What business decisions can be informed by these findings?
Dataset

The dataset contains 9,994 retail transactions and 21 columns, including information about:

Orders and customers
Product categories and sub-categories
Sales
Quantity
Discounts
Profit
Geographic information
Order and shipping dates
Tools Used
Python
Pandas
NumPy
Matplotlib
Google Colab
Methodology

The project followed these main steps:

Loaded and inspected the dataset.
Examined the dataset structure and data types.
Checked for missing values.
Generated descriptive statistics.
Analyzed sales and profit across product categories.
Examined the relationship between discounts and profit.
Identified loss-making transactions.
Interpreted the findings and developed business recommendations.
Key Findings
Technology generated the highest total profit at approximately $145,455.
Office Supplies generated approximately $122,491 in profit.
Furniture generated approximately $18,451 in profit despite generating approximately $742,000 in sales.
Furniture had the highest average discount at approximately 17.4%, while Technology had the lowest at approximately 13.2%.
Discount and profit had a correlation of approximately -0.22, indicating a weak negative relationship.
Average profit became negative at higher discount levels, particularly around 30% discount and above.
1,871 out of 9,994 transactions (18.72%) were loss-making.
Business Recommendations

Based on the findings:

Review high discount levels: Discounts around 30% and above should be carefully evaluated because they were associated with negative average profit in the dataset.
Use targeted discounting: Rather than applying large discounts broadly, discounts should be targeted toward products or customer segments where they are more likely to remain profitable.
Review Furniture profitability: The Furniture category generated substantial sales but relatively low profit. Its pricing, costs, and discount strategy should be investigated further.
Protect profitable categories: The factors contributing to Technology's strong profitability should be examined when making future pricing and discount decisions.
Investigate loss-making transactions: Products, sub-categories, and discount levels associated with losses should be examined in greater detail.
Prioritize profit alongside sales: High sales volume does not necessarily translate into high profit, so profitability should be considered when evaluating business performance.
Conclusion

The analysis suggests that higher discount levels are associated with lower profitability, although discounting alone does not explain all differences in profit.

The results demonstrate how exploratory data analysis can help businesses identify patterns in sales and profitability and make more informed decisions.

Further analysis of individual products and sub-categories could provide deeper insight into where losses are concentrated.

Project Structure
Beyond_Discounts_EDA/
│
├── README.md
│
├── notebooks/
│   └── Beyond_Discounts_EDA.ipynb
│
├── images/
│
└── data/

Author

Rosetta Gibson-White

Computer Engineering Student | AI & Data Projects