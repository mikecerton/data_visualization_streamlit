import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from my_controller import search_by_Student_ID, get_Income_data, open_csv_file, set_edited_csv, get_school_data, create_pie_chart

df = open_csv_file(".\dataset.csv")

st.title("Student Data Visualization")

# p 3

