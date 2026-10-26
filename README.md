# Pesa Pulse — Customer API Data Analysis

## Project Overview

Pesa Pulse is a fictional Nairobi-based fintech start-up seeking to understand its customer distribution before planning regional marketing campaigns.

In this project, I developed a Python data analysis pipeline to retrieve customer records from a REST API, explore nested JSON data, extract relevant attributes, and analyse customer distributions using Python data structures.

I then used pandas to validate the analysis, exported the cleaned data into CSV files, and created visualisations using Matplotlib.

The project demonstrates practical skills in API integration, data manipulation, exploratory data analysis, data validation, and visualisation.

## Project Objectives

- Retrieve customer records from an API using Python Requests and handle request failures.
- Explore nested JSON structures using recursion.
- Extract and flatten customer attributes.
- Identify unique customer cities using sets.
- Count customers by city and email top-level domain using dictionaries and comprehensions.
- Convert customer data into a pandas DataFrame.
- Validate Python aggregation results using pandas.
- Export cleaned datasets and aggregated results to CSV.
- Visualise customer distributions using Matplotlib.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| uv | Virtual environment and dependency management |
| Requests | Retrieving customer records from the REST API |
| Pandas | Data manipulation, validation and CSV exports |
| Matplotlib | Data visualisation |
| Git and GitHub | Version control and project hosting |

## Data Source

**API:** https://jsonplaceholder.typicode.com/users

The JSONPlaceholder Users API provides 10 fictional customer records containing personal, geographical, contact and company information.

The API response includes nested dictionaries, particularly the `address`, `geo` and `company` objects.

For example, the customer's latitude is accessed using:

```python
customer["address"]["geo"]["lat"]
```

Latitude and longitude values are converted from strings to floats during data extraction.

## Project Structure

```text
day1-api-analysis/
├── main.py
├── analysis.py
├── README.md
├── requirements.txt
├── pyproject.toml
├── uv.lock
├── .gitignore
└── output/
    ├── customers.csv
    ├── city_counts.csv
    ├── customer_distribution.png
    └── email_domain_distribution.png
```

**main.py:** Entry point that coordinates the workflow, including API retrieval, analysis, validation, exports and visualisation.

**analysis.py:** Contains reusable functions for retrieving customer data, exploring nested dictionaries, extracting attributes, counting categories, creating DataFrames and generating charts.

**output/:** Stores the generated CSV files and charts.

## Methodology

### 1. Data Retrieval

I used the Requests library to retrieve customer records from the JSONPlaceholder API.

The request includes a timeout and exception handling to provide clear error messages if retrieval fails.

### 2. Exploring Nested JSON

I implemented a recursive `explore()` function to display the keys and Python data types within each customer record.

The exploration showed that `address` and `company` are nested dictionaries, with `geo` nested further inside `address`.

### 3. Data Extraction and Cleaning

I developed `extract_attributes()` to transform nested customer records into a flat structure containing 12 attributes:

- Customer ID, name and username
- Email and email top-level domain
- Phone number
- City and zipcode
- Latitude and longitude
- Company and website

The flattened structure makes the records easier to analyse with pandas.

### 4. Customer Distribution Analysis

I used sets to identify unique customer cities and dictionaries to calculate customer counts by city.

I also used a dictionary comprehension to calculate email-domain frequencies.

These aggregations were performed without pandas or `collections.Counter`.

### 5. Data Validation

I converted the flattened records into a pandas DataFrame and compared pandas customer counts with the results calculated using Python dictionaries.

Both methods produced matching results.

### 6. Data Export and Visualisation

The cleaned customer records and city counts were exported as CSV files without the pandas index.

I created two bar charts:

- Customer distribution by city
- Customer distribution by email top-level domain

Both charts were saved as PNG files.

## Key Findings

### 1. Customer Geographical Distribution

The dataset contains **10 customers across 10 unique cities**.

Each city has exactly one customer, meaning no single city has a higher customer concentration.

### 2. Email-Domain Distribution

The `.biz` top-level domain is the most common, representing **3 customers (30%)**.

The seven remaining domains each represent one customer (10%).

### 3. Data Validation

The customer counts calculated using Python dictionaries matched those produced using pandas.

The cleaned DataFrame contains **10 rows and 12 columns**.

## Business Insights and Recommendations

### Recommendation 1: Improve Geographical Customer Insights

The sample shows an equal distribution across 10 cities, making it difficult to identify a priority region for marketing campaigns.

Pesa Pulse should collect a larger, more representative dataset and compare customer counts with local market potential to identify underserved areas and growth opportunities.

### Recommendation 2: Develop More Meaningful Customer Segments

The email-domain distribution provides more variation than the city distribution. However, email domains are not reliable indicators of customer location or purchasing behaviour.

Additional information, such as customer activity, acquisition channels and transaction patterns, would help Pesa Pulse create more meaningful customer segments.

## Assumptions and Limitations

- The API provides fictional customer records rather than actual Pesa Pulse customer data.
- Email top-level domains are extracted from the last portion of each email address.
- Latitude and longitude are converted from strings into floating-point numbers.
- Customer records are assumed to contain the expected nested attributes.
- The dataset contains only 10 records and is insufficient for reliable regional marketing decisions.
- The analysis does not include customer transaction history, demographics or engagement metrics.

## How to Run the Project

### Prerequisites

Install Python and the [uv package manager](https://docs.astral.sh/uv/).

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/day1-api-analysis.git
cd day1-api-analysis
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Install Dependencies

```bash
uv sync
```

This creates or synchronises the project's virtual environment and installs the required dependencies.

### 3. Run the Analysis

```bash
uv run python main.py
```

The script retrieves the customer records, performs the analysis, validates the results and generates the output files.

An internet connection is required to retrieve the API data.

### 4. View the Output

The generated files are saved in the `output/` directory:

| File | Description |
|---|---|
| `customers.csv` | Flattened customer records |
| `city_counts.csv` | Customer counts by city |
| `customer_distribution.png` | Customer distribution across cities |
| `email_domain_distribution.png` | Customer email-domain distribution |

## Conclusion

This project strengthened my understanding of working with REST APIs, navigating nested JSON structures, manipulating Python dictionaries and sets, and performing exploratory data analysis using pandas.

It also demonstrated the importance of validating results, documenting assumptions and translating technical findings into business insights.

Although the sample dataset is small and fictional, the workflow can serve as a foundation for analysing larger customer datasets.

## Author

Gideon Kiprono Kipkemoi

Python | Data Analytics | Data Science | AI
