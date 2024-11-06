import streamlit as st

# Initialize session state
if 'x' not in st.session_state:
    st.session_state.x = 0

st.title("صلوات شمار")    

col1, col2, col3 = st.columns(3)


with col1:
    minus_btn = st.button("➖", type='primary')
    st.write("فحش دادی کم کن")

with col3:
    plus_btn = st.button("➕", type='primary')
    st.write("بفرست بی ثواب")

if minus_btn:
    st.session_state.x -= 1
    print(st.session_state.x)

if plus_btn:
    st.session_state.x += 1
    print(st.session_state.x)


with col2:
    st.header(st.session_state.x)