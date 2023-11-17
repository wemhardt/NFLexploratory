import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
st.title('Exploratory Data Analysis of NFL with Streamlit')
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
@st.cache_data
def load_data(file):
	data = pd.read_csv(file)
	return data
if uploaded_file is not None:
	df = load_data(uploaded_file)
if st.checkbox('Histogram plot of a column'):
        column = st.selectbox('Select column for histogram', df.columns, index=2)
        sns.histplot(df[column], bins=25)
        st.pyplot(plt.gcf())

else:
    st.write("Upload a CSV file to get started")


    