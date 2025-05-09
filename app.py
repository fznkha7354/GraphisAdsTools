import streamlit as st
import pandas as pd

# Load your data
df = pd.read_csv("data.csv")
# Title
st.title("Graphisads AI Content Vault")

# Search box
query = st.text_input("Search your content")

# Show matching results
if query:
    results = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
    if not results.empty:
        st.write("Search Results:")
        st.dataframe(results)
    else:
        st.write("No results found.")
