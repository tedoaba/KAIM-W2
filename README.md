# KAIM Weak 2 Challenges Task 1

## **Project Overview**

This project involves a detailed analysis of a telecommunications dataset from TellCo, a mobile service provider in the Republic of Pefkakia. The objective is to analyze various aspects of customer behavior, engagement, experience, and satisfaction. The insights derived from the analysis will help a potential investor determine whether to acquire TellCo by highlighting growth opportunities and profitability potential.

The project is divided into four main tasks:

1. **User Overview Analysis**
2. **User Engagement Analysis**
3. **User Experience Analysis**
4. **Customer Satisfaction Analysis**

Each task will be developed in a separate branch and merged into the **main branch** upon completion.

## **Tasks Breakdown**

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

### **Task 3: User Experience Analysis**

**Objective**: Analyze network performance metrics (TCP retransmission, RTT, throughput) and customer device characteristics to assess user experience.

- Aggregate network parameters per customer (TCP retransmission, RTT, throughput).
- Report the top 10, bottom 10, and most frequent values for each network parameter.
- Analyze the distribution of throughput and TCP retransmission per handset type.
- Perform k-means clustering (k=3) to group customers based on experience metrics.
- Provide interpretations and visualizations.

**Branch**: `task-3`

### **Task 4: Customer Satisfaction Analysis**

**Objective**: Analyze customer satisfaction based on engagement and experience scores and build predictive models to assess satisfaction.

- Assign engagement and experience scores using Euclidean distance from the least engaged and worst experience clusters.
- Calculate the satisfaction score as the average of engagement and experience scores.
- Build a regression model to predict satisfaction scores.
- Perform k-means clustering (k=2) on the engagement and experience scores.
- Export the final table of user IDs with engagement, experience, and satisfaction scores to a local MySQL database.
- Deploy and track the satisfaction prediction model using Docker or an MLOps tool.

**Branch**: `task-4`

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
   ```

2. **Install Dependencies**:
   All necessary Python packages are listed in the `requirements.txt` file. Install them using the following command:

   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**:
   - Ensure you have a local PostgreSQL database set up with the dataset. Use the provided SQL script in `scripts/data_extraction.sql` to set up the schema and populate the data.

4. **Run Unit Tests**:
   Test the core functionality by running the unit tests:

   ```bash
   pytest
   ```

5. **Dashboard Deployment**:
   The dashboard is built using Streamlit. After completing all the analysis, deploy the dashboard locally with:

   ```bash
   streamlit run scripts/dashboard_deployment.py
   ```

## **Development Workflow**

1. **Create a Branch**:
   - For each task, create a new branch using the task-specific branch name:

     ```bash
     git checkout -b task-1
     ```

2. **Complete the Task**:
   - Write code and add documentation for the respective task.

3. **Testing and Code Review**:
   - Ensure the code passes all tests and adheres to project guidelines.
   - Create a pull request and request a code review.

4. **Merge to Main**:
   - Once approved, merge the changes to the `main` branch:

     ```bash
     git checkout main
     git merge task-1
     ```

## **CI/CD and Docker Setup**

1. **CI/CD Integration**:
   - The project is integrated with GitHub Actions for automated testing. Any new pull request triggers the test suite.

2. **Docker Setup**:
   - A `Dockerfile` is provided to containerize the application for easy deployment. To build and run the Docker image:

     ```bash
     docker build -t KAIM-W2
     docker run -p 8501:8501 telecom-insights
     ```

## **Key Insights and Recommendations**

As the analysis progresses, key insights and recommendations will be provided for each task. These insights will help stakeholders understand user behavior, engagement, experience, and satisfaction, ultimately informing the decision on whether to invest in TellCo.

## **Contributing**

Contributions are welcome! Please ensure your code is well-tested and documented. Open a pull request for any features or bug fixes you want to add.

## **License**

This project is licensed under the ... License. See the `LICENSE` file for details.
