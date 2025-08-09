🎵 Spotify Data Pipeline – AWS + Snowflake + Power BI
This project implements a serverless, scalable, and automated ETL pipeline to extract, transform, and load Spotify data for analytics. It leverages AWS Lambda, AWS Glue, Snowflake, and Power BI for an end-to-end data workflow.

📌 Workflow Overview
Extract

Trigger: Amazon CloudWatch triggers AWS Lambda daily.

Extraction: AWS Lambda (Python) calls the Spotify API to fetch music data.

Storage: Raw JSON/CSV files are saved to Amazon S3 (Raw Zone).

Transform

Event Trigger: An S3 ObjectPut event triggers AWS Glue.

Processing: AWS Glue (Apache Spark) cleans, normalizes, and structures the raw data.

Storage: Processed data is saved in Amazon S3 (Transformed Zone).

Load

Snowpipe automatically ingests transformed data from S3 into Snowflake.

Data is then available for reporting and visualization in Power BI.

🔹 Architecture


Spotify API → AWS CloudWatch → AWS Lambda → Amazon S3 (Raw)

S3 Event Trigger → AWS Glue (Spark) → Amazon S3 (Transformed)

Snowpipe → Snowflake → Power BI

🚀 Features
Automated Scheduling – CloudWatch triggers Lambda daily.

Serverless Processing – Lambda & Glue handle extraction and transformation.

Event-Driven ETL – S3 triggers automate the pipeline without manual intervention.

Scalable Storage – Raw & transformed data stored in separate S3 buckets.

Cloud Data Warehouse – Snowflake stores analytics-ready datasets.

Interactive Dashboards – Power BI visualizes trends, recommendations, and KPIs.

🛠️ Tech Stack
Tool / Service	Purpose
Spotify API	Source of music & artist data
AWS Lambda	Serverless data extraction
Amazon CloudWatch	Scheduling Lambda jobs
Amazon S3	Raw & transformed data storage
AWS Glue (Spark)	Data transformation & cleaning
Snowpipe	Automated Snowflake ingestion
Snowflake	Cloud data warehouse

🔮 Future Enhancements
Real-time ingestion using AWS Kinesis.
Additional data sources (YouTube, Apple Music).
Machine learning with AWS SageMaker to predict trends.
Dashboard automation with Power BI REST API.

