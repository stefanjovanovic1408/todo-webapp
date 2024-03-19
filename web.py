import streamlit as st
from helper_functions import *

#todos = get_todos()
todos = get_set_todos()


def add_todo():
    new_todo = st.session_state["new_todo"]+"\n"
    todos.append(new_todo)
    #write_todos(todos)
    get_set_todos(bool_get=False, string_todo=todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    item_key = str(index)+todo
    checkbox = st.checkbox(todo, key=item_key)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del item_key # must be delted from session state dictionary
        st.experimental_rerun() # necessary for checkboxes

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

st.session_state