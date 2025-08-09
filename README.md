# Spotify Data Pipeline – Extract, Transform, and Analyze with AWS and Snowflake 
**Author:** Lagudu Sai teja 

---
# ✨ Project Overview  
This project builds a **fully automated ETL pipeline** to extract, transform, and load Spotify data into **Snowflake** for analytics and reporting in **Power BI**.  

The pipeline integrates with the **Spotify API** to fetch music data, processes it with **AWS Glue** using **Apache Spark**, and loads it into **Snowflake** through **Snowpipe** for real-time ingestion. The processed data is then visualized in **Power BI** dashboards to provide insights into music trends, popularity, and listener behavior.  

The architecture is **serverless**, **scalable**, and supports **daily automated refreshes**.

---

## 📚 Reflection  

### **Key Steps:**  
1. **Extract Data** from the **Spotify API** using **AWS Lambda**, scheduled with **Amazon CloudWatch**.  
2. **Store Raw Data** in an **Amazon S3 bucket**.  
3. **Transform Data** using **AWS Glue (Apache Spark)**, triggered by **S3 events**.  
4. **Store Transformed Data** in another **S3 bucket** for loading.  
5. **Ingest Data into Snowflake** using **Snowpipe** for continuous, automated loading.  
6. **Analyze & Visualize** data in **Power BI** directly from Snowflake.

---

## 🚀 Methodology  

### **1. Data Extraction**  
- **Goal:** Retrieve data from the Spotify API and store it as raw data in S3.  
- **Implementation:**  
  - **Amazon CloudWatch** triggers the AWS Lambda extraction script daily.  
  - **AWS Lambda** (Python) connects to the Spotify API and fetches playlists, tracks, artists, and metadata.  
  - The raw JSON/CSV data is saved into **Amazon S3 (Raw Data Bucket)**.

---

### **2. Data Transformation**  
- **Goal:** Clean, normalize, and prepare the raw data for analytics.  
- **Implementation:**  
  - **S3 Event Notification** triggers an **AWS Glue Job** when new data is added to the raw bucket.  
  - **AWS Glue (Apache Spark)** processes data by:  
    - Flattening nested JSON.  
    - Normalizing timestamps and formats.  
    - Removing duplicates and missing values.  
  - The transformed data is saved into **Amazon S3 (Transformed Data Bucket)**.

---

### **3. Data Loading into Snowflake**  
- **Goal:** Continuously load transformed data into Snowflake.  
- **Implementation:**  
  - **Snowpipe** monitors the transformed S3 bucket.  
  - On new file arrival, Snowpipe loads the data into **Snowflake tables** in near real-time.  
  - Data is ready for querying and analysis.

---

### **4. Data Visualization in Power BI**  
- **Goal:** Build interactive dashboards for insights.  
- **Implementation:**  
  - **Power BI** connects directly to Snowflake.  
  - Dashboards visualize:  
    - Top artists & tracks.  
    - Genre popularity trends.  
    - Listening behavior over time.

---

## 📌 Architecture Diagram  
![Spotify pipeline architecture](https://github.com/user-attachments/assets/4e5b5f2d-b830-4999-abd6-7e8a31b41597)

---

## 📝 Lessons Learned  

✅ **Event-Driven Processing:** S3 triggers enable seamless Glue job execution.  
✅ **Automated Ingestion:** Snowpipe removes the need for manual loads.  
✅ **Scalability:** Serverless AWS services scale based on demand.  
✅ **Low Maintenance:** No servers to manage.  
✅ **BI Integration:** Snowflake provides a high-performance backend for Power BI.

---

## 📂 Output  

### **Key Observations**  
- Successfully extracted Spotify data and stored it in S3.  
- Transformed and loaded data into Snowflake via Snowpipe.  
- Built Power BI dashboards to visualize music insights.  

### **Significance**  
- Provides **real-time analytics** for music data.  
- Supports **trend detection, listener analysis, and recommendation insights**.  
- Fully automated with minimal operational overhead.

---

## 🛠️ Tools Used  

| **Service / Tool**      | **Purpose** |
|------------------------|-------------|
| **Spotify API**        | Source of music streaming data. |
| **Amazon CloudWatch**  | Schedules Lambda extractions daily. |
| **AWS Lambda**         | Extracts data from Spotify API and stores in S3. |
| **Amazon S3**          | Stores raw and transformed data. |
| **S3 Event Notifications** | Triggers Glue jobs on data arrival. |
| **AWS Glue (Apache Spark)** | Transforms, cleans, and prepares data. |
| **Snowpipe**           | Automatically loads S3 data into Snowflake. |
| **Snowflake**          | Data warehouse for analytics. |
| **Power BI**           | Visualization and reporting. |

---

## 📂 How to Run  

### **1. Set Up AWS Environment**  
- Create raw and transformed data buckets in Amazon S3.  
- Configure CloudWatch to trigger Lambda daily.  

### **2. Implement Data Extraction**  
- Write AWS Lambda (Python) to call Spotify API and save data to raw S3 bucket.  

### **3. Data Transformation**  
- Create an AWS Glue Job to clean and format data.  
- Trigger Glue job via S3 event notification.  

### **4. Load into Snowflake**  
- Configure Snowpipe to monitor transformed S3 bucket.  
- Create target Snowflake tables and ingestion pipelines.  

### **5. Visualize Data**  
- Connect Power BI to Snowflake and build dashboards.  


## 🔮 Future Enhancements  

- **Expand Data Sources:** Integrate with more APIs (e.g., YouTube, Apple Music).  
- **Real-Time Processing:** Use AWS Kinesis for **streaming** rather than batch processing.  
- **Visualization:** Connect **Athena** to **Amazon QuickSight** for dashboarding.  
- **Machine Learning:** Use AWS SageMaker to **predict music trends**.  

---

## 📜 References  

- **AWS Documentation:** [https://docs.aws.amazon.com](https://docs.aws.amazon.com)  
- **Spotify API Docs:** [https://developer.spotify.com](https://developer.spotify.com)  

---

