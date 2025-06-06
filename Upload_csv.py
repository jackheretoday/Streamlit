import streamlit as st
import pandas as pd

st.write("Hello, Peeps!")
st.title("Let's begin!")
st.subheader("Here you can plot a :red[csv] Dataset.")
st.text("This dataset can be any csv file you want to visualize.")
st.write("We have used pandas to read the dataset.")
st.write("We will use streamlit to visualize the dataset in different styles.")

file = st.file_uploader("Upload csv file", type="csv")

# Check if a file is uploaded before reading
if file is not None:
    try:
        df = pd.read_csv(file)
        st.write("Data Preview:")
        st.dataframe(df)

        st.markdown("This web-app represents an unclean dataset in 3 different styles:"
                    " **:blue[Line Graph, Bar Graph, Area Graph]**")

        name = st.text_input("Enter your name:")
        if name:
            st.write(f"Hello {name}, Welcome to the App!") 

        graph = st.selectbox("Your Favourite Representation:", ["Line Graph", "Bar Graph", "Area Graph"])
        st.write(f"Your choice is {graph}. Good Choice!")

        if st.button("Confirm?"):
            st.success(f"{graph} Noted!")

        ml = st.checkbox("Are you doing for Machine Learning?")
        if ml:
            st.text("Okay ML Enthusiast!")
            status = st.selectbox("Choose your current status.", ["Student", "Job", "Internship"])
            exp = st.slider("Experience Level", 0, 10, 5)
            exp_date = st.date_input("When did you start learning ML?", value=pd.to_datetime("2020-01-01"))
            st.write(f"Your experience level is {exp} years and you started learning on {exp_date}.") 
            projects = st.number_input("How many projects have you done?", min_value=0, max_value=5, step=1)

            st.write("How do you want to view the data?")
            view = st.radio("Choose your option:", ["Line", "Bar", "Area"])
            if view == "Line":
                st.line_chart(df)
            elif view == "Bar":
                st.bar_chart(df)
            else:
                st.area_chart(df)

    except Exception as e:
        st.error(f"Error reading CSV: {e}")
else:
    st.warning("Please upload a CSV file.")
