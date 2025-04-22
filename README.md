# Data Quality Check Streamlit App

This repository contains a Streamlit-based application designed to perform data quality checks between a SQL Server database and Snowflake.

## 🔧 Setup Instructions

Follow these steps to set up and run the application on your local machine:

1. **Install Python**  
   Make sure Python is installed on your system. You can download it from: https://www.python.org/downloads/

2. **Install dependencies**  
   Navigate to the main project folder in your terminal and run: pip install -r requirements.txt

3. **Configure SQL Server connection**  
Update your SQL Server credentials in the following file: config/sqlserver_config.py

4. **Configure Snowflake connection**  
Edit the Snowflake credentials located in: .streamlit/secrets.toml

5. **(Optional) Generate sample data**  
If you'd like to load some sample data into SQL Server/Snowflake, you can use the following script: scripts/create_mock_data.py

6. **Run the application**  
Use the command below to start the Streamlit app: streamlit run streamlit_app.py

This app enables comparison between SQL Server and Snowflake datasets, including schema validation, row counts, and basic data profiling. Ideal for quick data quality checks during migration or sync processes.
