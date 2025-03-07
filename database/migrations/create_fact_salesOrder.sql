------------------- CREATE FACT SALES ORDER ------------------------------
CREATE TABLE Fact_SalesOrder (
    id INT PRIMARY KEY,
    order_date_key INT NOT NULL,
    territory_key INT NOT NULL,
    customer_key INT NOT NULL,
    revenue DECIMAL(18,4) NOT NULL,
    profit_per_order DECIMAL(18,4) NOT NULL,
    number_order INT NOT NULL
) DISTSTYLE KEY DISTKEY(order_date_key) SORTKEY(order_date_key, territory_key);
