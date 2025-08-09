🎵 Spotify ETL Pipeline – AWS | Snowflake | Power BI

📌 Project Description

This project automates the end-to-end ETL process for Spotify data, enabling analytics and reporting in Power BI.
It uses AWS Lambda for data extraction, AWS Glue (Apache Spark) for transformation, Snowpipe for loading into Snowflake, and Power BI for visualization.
The pipeline runs serverlessly and updates automatically every day.

🛠 Architecture Components
1. Data Extraction (EXTRACT)
Source: Spotify API (via Python script using spotipy or Requests library).

AWS Lambda:

Triggered by Amazon CloudWatch daily.

Fetches playlists, songs, artists, and metadata.

Saves raw data to Amazon S3 (Raw Data Bucket) in JSON/CSV format.

2. Data Transformation (TRANSFORM)
Trigger: S3 Object Put Event when new raw data arrives.

AWS Glue Job (Apache Spark):

Cleans, normalizes, and enriches the data.

Flattens nested JSON structures from Spotify API.

Formats timestamps & standardizes schema.

Removes duplicates & nulls.

Saves processed data to Amazon S3 (Transformed Data Bucket).

3. Data Loading (LOAD)
Snowpipe:

Continuously monitors S3 transformed bucket.

Automatically ingests new data into Snowflake tables without manual intervention.

Snowflake:

Acts as a centralized data warehouse for querying and analytics.

4. Data Visualization
Power BI:

Connects directly to Snowflake.

Builds dashboards for insights:

Top Artists & Tracks.

Genre Popularity Trends.

Listening Behavior Over Time.

🔄 Data Flow Summary
Spotify API → CloudWatch (daily trigger)

CloudWatch → AWS Lambda (extracts data)

Lambda → S3 Raw Data Bucket

S3 Event → AWS Glue (transforms data)

Glue → S3 Transformed Data Bucket

S3 → Snowpipe → Snowflake (data warehouse)

Snowflake → Power BI (dashboards & analytics)

🚀 Features & Benefits
✅ Fully Serverless – No manual infrastructure to manage.
✅ Automated Daily Refresh – Keeps dashboards always up-to-date.
✅ Scalable & Cost-Effective – Handles growing Spotify data efficiently.
✅ Real-Time Loading – Snowpipe ingests data within minutes.
✅ BI-Ready – Power BI can consume clean, analytics-ready da

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

