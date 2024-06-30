import streamlit as st

st.set_page_config(page_title="Makeit Happen", page_icon="🎯")

# Function to add a new task to the list
def add_task():
    task = st.session_state["new_task"]
    if task:
        st.session_state["tasks"].append(task)
        st.session_state["new_task"] = ""  # Clear the input field

# Function to remove a task from the list
def remove_task(task):
    st.session_state["tasks"].remove(task)

# Initialize session state variables if not already present
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []
if "new_task" not in st.session_state:
    st.session_state["new_task"] = ""

# Streamlit app layout
st.title("Makeit Happen")

st.subheader("Lets do it")
st.text_input("Enter a task", key="new_task", on_change=add_task)

st.subheader("Targets")
if st.session_state["tasks"]:
    for task in st.session_state["tasks"]:
        st.checkbox(task, key=task, on_change=remove_task, args=(task,))
else:
    st.write("You nailed it all.")

