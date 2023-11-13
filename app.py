import streamlit as st
from PIL import Image
import base64
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import StringIO

# Function to get base64 string of an image
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Function to set a background image
def set_background_image(image_path):
    base64_image = get_image_base64(image_path)
    background_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{base64_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)

# Assuming you've saved the image in the same directory as your script
# with the name 'background.png'
set_background_image('img.png')

# Title of the application
st.title('Exploratory Data Analysis of NFL with Streamlit')

# File uploader widget
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# Function to load data
@st.cache
def load_data(file):
    data = pd.read_csv(file)
    return data

# If a file is uploaded, then display data and EDA options
if uploaded_file is not None:
    # Load data
    df = load_data(uploaded_file)

    # Display first few rows of the dataframe
    if st.checkbox('Show first few rows of the data'):
        st.write(df.head())

    # Display a random sample of the data
    if st.checkbox('Show a random sample of the data'):
        st.write(df.sample(15))

    # Display dataframe info
    if st.checkbox('Show dataframe information'):
        buffer = StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

    # Display unique values in a specific column
    if st.checkbox('Show unique values in a column'):
        column = st.selectbox('Select column', df.columns)
        st.write(df[column].nunique())

    # Display value counts of a specific column
    if st.checkbox('Show value counts of a column'):
        column = st.selectbox('Select column for value counts', df.columns, index=1)
        st.write(df[column].value_counts())

    # Histogram plot of a specific column
    if st.checkbox('Histogram plot of a column'):
        column = st.selectbox('Select column for histogram', df.columns, index=2)
        sns.histplot(df[column], bins=25)
        st.pyplot(plt.gcf())

    # Histogram with hue based on another column
    if st.checkbox('Histogram with hue based on another column'):
        column = st.selectbox('Select column for histogram with hue', df.columns, index=3)
        hue_column = st.selectbox('Select hue column', df.columns, index=4)
        sns.histplot(x=df[column], hue=df[hue_column])
        st.pyplot(plt.gcf())

    # Box plot comparing two columns
    if st.checkbox('Box plot comparing two columns'):
        y_column = st.selectbox('Select y-axis column for box plot', df.columns, index=5)
        x_column = st.selectbox('Select x-axis column for box plot', df.columns, index=6)
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=x_column, y=y_column, data=df)
        st.pyplot(plt.gcf())

    # Line chart of a specific column
    if st.checkbox('Line chart of a column'):
        column = st.selectbox('Select column for line chart', df.columns, index=7)
        st.line_chart(df[column])

# Instructions when no file is uploaded
else:
    st.write("Upload a CSV file to get started")
