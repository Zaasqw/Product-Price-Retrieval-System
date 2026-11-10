import pandas as pd
import streamlit as st

# عنوان النظام
st.title("Product Price Retrieval System")

# قراءة البيانات
df = pd.read_excel("Product_Data.xlsx")

# طريقة البحث
search_by = st.selectbox(
    "Search By",
    ["Product ID", "Product Name"]
)

# البحث برقم المنتج
if search_by == "Product ID":

    selected_id = st.selectbox(
        "Select Product ID",
        sorted(df["ProductID"].unique())
    )

# البحث باسم المنتج
else:

    selected_name = st.selectbox(
        "Select Product Name",
        sorted(df["Name"].unique())
    )

# زر البحث
if st.button("Search"):

    if search_by == "Product ID":
        result = df[df["ProductID"] == selected_id]

    else:
        result = df[df["Name"] == selected_name]

    if not result.empty:

        st.subheader("Product Information")

        st.write(f"**Product ID:** {result.iloc[0]['ProductID']}")

        st.write(f"**Product Name:** {result.iloc[0]['Name']}")

        st.write(f"**List Price:** ${result.iloc[0]['ListPrice']}")