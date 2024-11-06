import datetime
import streamlit as st


my_btn = st.button("Click me")

#with st.sidebar:
    

st.title("Streamlit App")
st.write("Hello World")

with st.sidebar:
    agree = st.checkbox("I agree")
    values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
    d = st.date_input("Birthday", datetime.date(2019, 7, 6))


if my_btn:
    st.write("سلام")
else:
    st.write("خداحافظ")


col1, col2 = st.columns(2)

with col1:
    name = st.text_input("First name:")
    last_name = st.text_input("last name:")

    weight = st.number_input("Enter Weight(kg): ")
    height = st.number_input("Enter your height(cm):")
    print(weight)

    btn_submit = st.button("Calculate BMI")

with col2:

    if btn_submit:
        bmi = weight / ((height/100)**2)

        st.info(bmi)

        if bmi < 18.5:
            st.write("لاغر")
        if 18.5 < bmi < 25:
            st.write("عالی")
        if 25 < bmi < 30:
            st.write(" کمی اضافه وزن")
        if 30 < bmi < 35:
            st.write("چاقالو")
        if 35 < bmi:
            st.write("افتضاح چاق")


st.warning("این یک سطر جدید است.")