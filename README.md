# KAIM Weak 2 Challenges Task 4

## **Project Overview**

This project involves a detailed analysis of a telecommunications dataset from TellCo, a mobile service provider in the Republic of Pefkakia. The objective is to analyze various aspects of customer behavior, engagement, experience, and satisfaction. The insights derived from the analysis will help a potential investor determine whether to acquire TellCo by highlighting growth opportunities and profitability potential.

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
│   └── workflows/
│       └── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
│   ├── __init__.py
│   ├── data_preparation.py
│   ├── eda_analysis.py
│   ├── model_training.py
├── notebooks/
│   ├── __init__.py
│   ├── KAIM_Week2_task_4.ipynb
├── tests/
│   ├── __init__.py
│   ├── test_data_preparation.py
│   ├── test_eda_analysis.py
│   ├── test_model_training.py
└── scripts/
    ├── __init__.py
    ├── main.py
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

## **Development Workflow**

1. **Create a Branch**:
   - For each task, create a new branch using the task-specific branch name:

     ```bash
     git checkout -b task-4
     ```

## **Key Insights and Recommendations**

As the analysis progresses, key insights and recommendations will be provided for each task. These insights will help stakeholders understand user behavior, engagement, experience, and satisfaction, ultimately informing the decision on whether to invest in TellCo.

## **Contributing**

Contributions are welcome! Please ensure your code is well-tested and documented. Open a pull request for any features or bug fixes you want to add.

## **License**

This project is licensed under the ... License. See the `LICENSE` file for details.
