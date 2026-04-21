import streamlit as st

st.title("✅ TODO List")

if "todos" not in st.session_state:
    st.session_state.todos = []

# 添加待办
with st.form("add_todo", clear_on_submit=True):
    new_todo = st.text_input("添加新待办")
    if st.form_submit_button("添加", type="primary") and new_todo:
        st.session_state.todos.append({"text": new_todo, "done": False})
        st.rerun()

# 展示待办列表
for i, todo in enumerate(st.session_state.todos):
    col1, col2 = st.columns([0.9, 0.1])
    with col1:
        done = st.checkbox(todo["text"], value=todo["done"], key=f"todo_{i}")
        st.session_state.todos[i]["done"] = done
    with col2:
        if st.button("🗑️", key=f"del_{i}"):
            st.session_state.todos.pop(i)
            st.rerun()

# 统计
if st.session_state.todos:
    done_count = sum(1 for t in st.session_state.todos if t["done"])
    st.progress(done_count / len(st.session_state.todos))
    st.caption(f"完成 {done_count}/{len(st.session_state.todos)}")