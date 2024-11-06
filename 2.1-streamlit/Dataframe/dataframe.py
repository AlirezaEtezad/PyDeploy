import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():



    my_btn = st.button("Click on it Dear Sajjad Aemmi")
    if my_btn:
        st.markdown(
    """
    <h1 style='color: #790074; font-size: 36px;'>You Touch The Future; You Teach 👨‍💻📚🎉 
    HTD</h1>
    """,
    unsafe_allow_html=True
)


    with st.sidebar:
        st.title("Notes:")
        st.warning("You have to upload a CSV file")
        st.warning("Only choose numeric columns")



    # File uploader
    st.title("CSV File Uploader and DataFrame Viewer")
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded_file is not None:
        # Read the uploaded CSV file into a pandas DataFrame
        df = pd.read_csv(uploaded_file)
        
        #st.line_chart(df)


        # Display the DataFrame as a table
        st.dataframe(df)

        # Select columns for chart
        selected_columns = st.multiselect("Select columns for chart", df.columns)

        if selected_columns:
            # Draw chart
            st.subheader("Chart")
            chart_type = st.selectbox("Select chart type", ["Line", "Bar", "Scatter"])

            if chart_type == "Line":
                df[selected_columns].plot(kind="line")
            elif chart_type == "Bar":
                df[selected_columns].plot(kind="bar")
            elif chart_type == "Scatter":
                df[selected_columns].plot(kind="scatter", x=selected_columns[0], y=selected_columns[1])
            
            st.pyplot(plt)


if __name__ == "__main__":
    main()
