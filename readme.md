<h1 align="center">🚀 Retail AWS Data Warehouse Pipeline 🚀</h1>

## 📌 Tổng quan

Dự án này là một hệ thống **Data Warehouse có khả năng mở rộng**, được thiết kế để xử lý và phân tích dữ liệu chuỗi cung ứng bán lẻ. Hệ thống sử dụng các dịch vụ **AWS** và các công cụ **Data Engineering hiện đại** nhằm xây dựng một **hạ tầng dữ liệu mạnh mẽ**, hỗ trợ doanh nghiệp đưa ra quyết định dựa trên dữ liệu.

## 🔍 Mục tiêu & Ứng dụng thực tế  
Hệ thống này giúp doanh nghiệp **tối ưu hoạt động kinh doanh** thông qua các phân tích chuyên sâu (*insight*), bao gồm:

- **📊 Hiệu suất bán hàng** – Xác định sản phẩm bán chạy, xu hướng theo mùa và sự tăng trưởng doanh thu.
- **📦 Tối ưu tồn kho** – Phân tích cung cầu để tránh tình trạng thiếu hàng hoặc dư thừa hàng hóa.
- **🛒 Hành vi khách hàng** – Phân khúc khách hàng dựa trên thói quen mua sắm để cá nhân hóa chiến lược marketing.
- **⚙️ Hiệu suất vận hành** – Phát hiện các nút thắt trong chuỗi cung ứng để tối ưu hóa logistics và thời gian giao hàng.

## 🎯 Objectives
- **Centralized Data Warehouse**: Store structured data in **Amazon Redshift**.
- **Efficient ETL Process**: Use **PySpark** and **Airflow** to process and load data.
- **Scalable Storage**: Store raw & staging data in **AWS S3**.
- **Interactive Analytics**: Create business intelligence dashboards with **Power BI**.
- **Containerized Deployment**: Use **Docker** for easy orchestration.

---

## 🏗️ Architecture Diagram
## Data Pipeline Diagram
![Alt text](data/image/pipeline.PNG)

[Click here to view the diagram](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&dark=auto#G1z

## 🛠️ Tech Stack

| Tool/Service        | Purpose                                |
|---------------------|----------------------------------------|
| **Amazon Redshift** | Data Warehouse                         |
| **AWS S3**         | Storage for raw & staging data         |
| **Apache Airflow**  | Orchestration for ETL workflows       |
| **PySpark**        | Data processing & transformations      |
| **Power BI**       | Business Intelligence & visualization  |
| **Docker**         | Containerized deployment              |

---

## 🔄 Data Pipeline Workflow

1. **Ingestion**: Raw data is downloaded from [Kaggle Dataset](https://www.kaggle.com/datasets/alinoranianesfahani/dataco-smart-supply-chain-for-big-data-analysis) and stored in **AWS S3**.
2. **Processing (ETL)**:
   - PySpark processes the data, performs transformations, and loads it into **staging S3**.
3. **Loading**: Transformed data is loaded into **Amazon Redshift**.
4. **Analysis**: Power BI connects to Redshift for interactive dashboards.
5. **Automation**: Airflow schedules and monitors the pipeline.

---

## 📦 Setup & Deployment

### Prerequisites
- AWS account (S3, Redshift setup)
- Docker & Docker Compose
- Airflow installed
- PySpark installed

### Steps to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Duong27102001/retail_aws_pipeline.git
   cd retail_aws_pipeline
