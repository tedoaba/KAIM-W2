# KAIM Weak 2 Challenges

## **Project Overview**

This project involves a detailed analysis of a telecommunications dataset from TellCo, a mobile service provider in the Republic of Pefkakia. The objective is to analyze various aspects of customer behavior, engagement, experience, and satisfaction. The insights derived from the analysis will help a potential investor determine whether to acquire TellCo by highlighting growth opportunities and profitability potential.

### **Task 5: Dashboard Development**

**Objective:**
    To design and develop a comprehensive dashboard that visualizes the insights gained from the analyses conducted in previous tasks. The goal is to present the data in an accessible and interactive manner to facilitate easier interpretation and decision-making.

    **Scope of Work:**

    1. **Dashboard Design:**
       - The dashboard is organized into separate pages, each dedicated to a specific analysis task:
         - **User Overview Analysis**
         - **User Engagement Analysis**
         - **Experience Analysis**
         - **Satisfaction Analysis**

    2. **Visualization:**
       - Each page includes relevant plots and visualizations to represent the data insights effectively:
         - **User Overview Analysis:** Visualizations related to handset popularity, user behavior, and device preferences.
         - **User Engagement Analysis:** Charts highlighting user engagement metrics, clustering results, and application usage.
         - **Experience Analysis:** Plots depicting network performance metrics, user experience data, and clustering outcomes.
         - **Satisfaction Analysis:** Visualizations of engagement and experience scores, satisfaction levels, and predictions.

    3. **Key Performance Indicators (KPIs):**
       - **Dashboard Usability:** Ensures that the dashboard is intuitive and easy to navigate, with clear labels and instructions.
       - **Interactive Elements:** Utilizes widgets and interactive features to enhance user engagement and allow for dynamic data exploration.
       - **Visual Appeal:** Adheres to a clean and professional design, effectively communicating data insights through well-structured layouts and visuals.
       - **Deployment Success:** Guarantees that the dashboard is fully functional and accessible via a public URL, ensuring stakeholders can interact with the data seamlessly.

    **Outcome:**
    The developed dashboard provides a user-friendly interface to explore and analyze the data insights derived from the comprehensive analyses. It supports informed decision-making by presenting key metrics and findings in an interactive and visually appealing format.

**Branch**: `task-5`


## **Project Structure**

The project follows a modular and scalable structure for ease of use and reusability.

```bash

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
├── streamlit/                 # Unit test cases
│   ├── __init__.py
│   ├── app.py
│   ├── challenge_description.py
│   ├── task_1_info.py
│   ├── task_2_info.py
│   ├── task_3_info.py
│   ├── task_4_info.py
│   ├── task_5_info.py
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

   git checkout task-5
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
