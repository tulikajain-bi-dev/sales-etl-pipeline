# Sales ETL Pipeline

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline built using Python and Pandas.

## Project Workflow

Extract  
Raw sales data is extracted from a CSV dataset.

Transform  
Data cleaning and transformation steps include:
- Removing duplicate rows
- Converting date columns
- Creating a Profit Margin column

Load  
The cleaned dataset is stored in the output folder for further analytics or dashboarding.

## Project Structure

etl-sales-pipeline
│
├── data
│   └── Sample - Superstore.csv
│
├── scripts
│   └── etl_pipeline.py
│
├── output
│   └── clean_superstore_sales.csv
│
└── README.md

## Tools Used

Python  
Pandas  
VS Code  
GitHub