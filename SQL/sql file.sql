CREATE DATABASE retail_analysis;
USE retail_analysis;

CREATE TABLE superstore (
    row_id INT,
    order_id VARCHAR(30),
    order_date DATE,
    ship_date DATE,
    ship_mode VARCHAR(30),
    customer_id VARCHAR(30),
    customer_name VARCHAR(100),
    segment VARCHAR(30),
    country VARCHAR(50),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20),
    region VARCHAR(30),
    product_id VARCHAR(30),
    category VARCHAR(50),
    sub_category VARCHAR(50),
    product_name VARCHAR(255),
    sales DECIMAL(10,2),
    quantity INT,
    discount DECIMAL(4,2),
    profit DECIMAL(10,2)
);
USE retail_analysis;

ALTER TABLE superstore
ADD COLUMN profit_margin DECIMAL(10,2);
SELECT COUNT(*) FROM superstore;
-- Calculate total sales and total profit of the business
SELECT
    SUM(sales) AS Total_Sales,
    SUM(profit) AS Total_Profit
FROM superstore;
-- Calculate the total number of orders and unique customers
SELECT
    COUNT(DISTINCT order_id) AS Total_Orders,
    COUNT(DISTINCT customer_id) AS Total_Customers
FROM superstore;
-- Compare sales and profit across different product categories
SELECT
    category,
    SUM(sales) AS Total_Sales,
    SUM(profit) AS Total_Profit
FROM superstore
GROUP BY category
ORDER BY Total_Profit DESC;
-- Identify subcategories that generate an overall loss
SELECT
    sub_category,
    SUM(sales) AS Total_Sales,
    SUM(profit) AS Total_Profit
FROM superstore
GROUP BY sub_category
HAVING SUM(profit) < 0
ORDER BY Total_Profit;
-- Compare sales and profit across different regions
SELECT
    region,
    SUM(sales) AS Total_Sales,
    SUM(profit) AS Total_Profit,
    AVG(profit) AS Average_Profit
FROM superstore
GROUP BY region
ORDER BY Total_Profit DESC;
-- Analyze sales and profit at different discount levels
SELECT
    discount,
    SUM(sales) AS Total_Sales,
    SUM(profit) AS Total_Profit,
    AVG(profit) AS Average_Profit
FROM superstore
GROUP BY discount
ORDER BY discount;
-- Identify the products with the lowest total profit
SELECT
    product_name,
    SUM(sales) AS Total_Sales,
    SUM(profit) AS Total_Profit
FROM superstore
GROUP BY product_name
ORDER BY Total_Profit ASC
LIMIT 10;
-- Identify the top 10 products based on total profit
SELECT
    product_name,
    SUM(sales) AS Total_Sales,
    SUM(profit) AS Total_Profit
FROM superstore
GROUP BY product_name
ORDER BY Total_Profit DESC
LIMIT 10;
-- Compare sales and profit across customer segments
SELECT
    segment,
    SUM(sales) AS Total_Sales,
    SUM(profit) AS Total_Profit
FROM superstore
GROUP BY segment
ORDER BY Total_Profit DESC;
-- Calculate the overall profit margin as a percentage of sales
SELECT
    SUM(profit) AS Total_Profit,
    SUM(sales) AS Total_Sales,
    (SUM(profit) / SUM(sales)) * 100 AS Profit_Margin_Percentage
FROM superstore;