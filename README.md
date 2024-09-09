# KAIM Weak 2 Challenges

## **Project Overview**

This project involves a detailed analysis of a telecommunications dataset from TellCo, a mobile service provider in the Republic of Pefkakia. The objective is to analyze various aspects of customer behavior, engagement, experience, and satisfaction. The insights derived from the analysis will help a potential investor determine whether to acquire TellCo by highlighting growth opportunities and profitability potential.

### **Task 1: User Overview Analysis**

**Objective**: Explore the dataset to understand user behavior and handset usage patterns.

- Identify the top 10 handsets used by customers.
- Identify the top 3 handset manufacturers and the top 5 handsets per manufacturer.
- Analyze user behavior on different applications (social media, YouTube, Netflix, etc.).
- Provide recommendations for marketing teams based on the analysis.

**Branch**: `task-1`

### **Task 2: User Engagement Analysis**

**Objective**: Measure customer engagement by analyzing session frequency, duration, and total data traffic.

- Aggregate session frequency, session duration, and total data traffic (download and upload).
- Report the top 10 customers based on each engagement metric.
- Normalize the metrics and perform k-means clustering (k=3) to group customers into engagement clusters.
- Visualize the top 3 most used applications.
- Determine the optimal value of k using the elbow method.

**Branch**: `task-2`


## **Project Structure**

The project follows a modular and scalable structure for ease of use and reusability.

```script
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows
│       ├── unittests.yml  # CI/CD pipeline
├── .gitignore
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
├── src/                   # Core modules
│   ├── __init__.py
│   ├── data_processing.py # Data loading, cleaning, and aggregation
    ├── data_loader.py       # For loading data
│   ├── data_preprocessing.py # For cleaning and scaling
│   ├── clustering.py      # Clustering and engagement classification
│   ├── visualization.py   # Visualization functions
│   └── analysis.py        # Application-wise user analysis
├── tests/                 # Unit test cases
│   ├── __init__.py
│   ├── test_data_processing.py
│   ├── test_clustering.py
│   ├── test_visualization.py
│   └── test_analysis.py
├── scripts/
│   ├── __init__.py
│   └── main.py            # Main entry point for running tasks
├── data/
│   └── data.csv           # Dataset location
└── notebooks/
    ├── __init__.py
    └── README.md
```

- **src/**: Contains Python modules for data preparation, exploratory data analysis, and model training.
- **notebooks/**: Jupyter notebooks for step-by-step exploration and development of each task.
- **tests/**: Unit tests to ensure the functionality of the code.
- **scripts/**: SQL scripts for data extraction and Python scripts for database interaction and dashboard deployment.

## **Installation and Setup**

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/tedoaba/KAIM-W2.git
   cd KAIM-W2

   git checkout task-1
   git checkout task-2
   ```

2. **Install Dependencies**:
   All necessary Python packages are listed in the `requirements.txt` file. Install them using the following command:

   ```bash
   pip install -r requirements.txt
   ```

## **Key Insights and Recommendations**

As the analysis progresses, key insights and recommendations will be provided for each task. These insights will help stakeholders understand user behavior, engagement, experience, and satisfaction, ultimately informing the decision on whether to invest in TellCo.

## **Contributing**

Contributions are welcome! Please ensure your code is well-tested and documented. Open a pull request for any features or bug fixes you want to add.

## **License**

This project is licensed under the ... License. See the `LICENSE` file for details.
