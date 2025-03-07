<h1 align="center">🚀 Retail AWS Data Warehouse Pipeline 🚀</h1>

## 📌 Tổng quan

Dự án này là một hệ thống **Data Warehouse có khả năng mở rộng**, được thiết kế để xử lý và phân tích dữ liệu chuỗi cung ứng bán lẻ. Hệ thống sử dụng các dịch vụ **AWS** và các công cụ **Data Engineering hiện đại** nhằm xây dựng một **hạ tầng dữ liệu mạnh mẽ**, hỗ trợ doanh nghiệp đưa ra quyết định dựa trên dữ liệu.

Hệ thống này giúp doanh nghiệp **tối ưu hoạt động kinh doanh** thông qua các phân tích chuyên sâu (*insight*), bao gồm:

- **📊 Phân tích quá trình đặt hàng và giao hàng** – Phân tích thời gian giao hàng và phương thức vận chuyển để tối ưu hóa quy trình giao hàng và giảm thiểu các trường hợp giao hàng muộn.
- **📦 Phân tích doanh thu bán hàng** – Phân tích cung cầu để tránh tình trạng thiếu hàng hoặc dư thừa hàng hóa.
- **🛒 Phân tích hành vi khách hàng và phương thức thanh toán** – Phân khúc khách hàng dựa trên thói quen mua sắm để cá nhân hóa chiến lược marketing.
- **⚙️ Hiệu suất vận hành** – Phát hiện các nút thắt trong chuỗi cung ứng để tối ưu hóa logistics và thời gian giao hàng.
---
## 🎯 Mục tiêu và công nghệ sử dụng
- **Centralized Data Warehouse**: Store structured data in **Amazon Redshift**.
- **Efficient ETL Process**: Use **PySpark** and **Airflow** to process and load data.
- **Scalable Storage**: Store raw & staging data in **AWS S3**.
- **Interactive Analytics**: Create business intelligence dashboards with **Power BI**.
- **Containerized Deployment**: Use **Docker** for easy orchestration.

### 🏗️ Architecture Diagram
![Alt text](data/image/pipeline.PNG)

### 🔄 Data Pipeline Workflow

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
