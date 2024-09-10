import streamlit as st

from challenge_description import show_overview, show_completed_tasks, show_next_steps
from task_1_info import show_task_1_description
from task_2_info import show_task_2_description
from task_3_info import show_task_3_description
from task_4_info import show_task_4_description
from task_5_info import show_task_5_description


# Initial page config
st.set_page_config(
    page_title='KAIM Week 2',
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    selected_task = app_sidebar()
    app_body(selected_task)
    
    st.markdown('---')
    st.header('Contact Information')
    st.markdown('**Name:** Tadesse Abateneh')
    st.markdown("**GitHub:** [Tadesse's GitHub](https://github.com/tedoaba)")
    st.markdown("**LinkedIn:** [Tadesse's LinkedIn](https://www.linkedin.com/in/tadesse-abateneh)")
    

# Sidebar
def app_sidebar():
    st.sidebar.header('KAIM Week 2 Challenges')
    
    tasks = ['Challenge Description', 'Task 1', 'Task 2', 'Task 3', 'Task 4', 'Task 5']
    selected_task = st.sidebar.selectbox('Select a task', tasks, key='task_selector')
    
    st.sidebar.markdown('---')
    st.sidebar.header('Contact Information')
    st.sidebar.markdown('**Name:** Tadesse Abateneh Walelign')
    st.sidebar.markdown('**GitHub:** [Tadesse GitHub](https://github.com/tedoaba)')
    st.sidebar.markdown('**LinkedIn:** [Tadesse LinkedIn](https://www.linkedin.com/in/tadesse-abateneh)')
    
    return selected_task

# Main body
def app_body(selected_task):
    st.title('KAIM Week 2 Challenges')
    
    if selected_task == 'Challenge Description':
        
        st.title("TellCo Investment Analysis Report")
        show_overview()
        show_completed_tasks()
        show_next_steps()
    
    elif selected_task == 'Task 1':
        st.title('Task 1 - User Overview Analysis Report')
        
        show_task_1_description()


    
    elif selected_task == 'Task 2':

        st.title('Task 2 - User Engagement Analysis Report')

        show_task_2_description()

    
    elif selected_task == 'Task 3':

        st.title('Task 3 - Experience Analytics Report')

        show_task_3_description()

    
    elif selected_task == 'Task 4':

        st.title('Task 4 - Satisfaction Analysis Report')

        show_task_4_description()


    elif selected_task == 'Task 5':
        st.title('Task 5 - Dashboard Development')
        
        show_task_5_description()
        

# Run main()
if __name__ == '__main__':
    main()
