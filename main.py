import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from my_controller import search_by_Student_ID, get_Income_data, open_csv_file, set_edited_csv, get_school_data, create_pie_chart

df = open_csv_file(".\dataset.csv")

# st.title("Student Data Visualization")

# # p 1
# st.subheader("1.Display student data by Student_ID")
# user_input_p1 = st.text_input("Enter Student_ID to search:", "0001", max_chars=4)

# st.write(search_by_Student_ID(user_input_p1, df))

# # p 2
# st.subheader("2.All student data in csv")
# st.write(df)

# # p 3

# # p 4
st.subheader("4.Data summary for Private or public school")
user_input_p4 = st.multiselect("What are your favorite colors", ["Public", "Private"], max_selections = 1, default = "Public")
string_input = user_input_p4[0] if user_input_p4 else "Public"

st.write(string_input)

[student_number, average_score, score_counts_df, teacher_chart] = get_school_data(user_input_p4, df)

# st.write(f"***Number Of Student = {student_number}***")
# st.write(f"***Average Of Exam Scores = {average_score}***")
# st.write("***Bar Chart Of Exam Scores.***")
# st.bar_chart(score_counts_df)

# st.pyplot(teacher_chart)

# # p 5
# st.subheader("5.Edit csv file")
# user_input_p5 = st.text_input("Enter Student_ID to search:")
# if user_input_p5:
#     edited_df = st.data_editor(search_by_Student_ID(user_input_p5, df), num_rows="dynamic")
#     if st.button("Save Changes"):
#             set_edited_csv(edited_df, df)
#             st.success(f"Changes saved to dataset.csv for Student_ID {user_input_p5}")

# # p 6
# st.subheader("6.Show the proportion of Family_Income of the data.")
# data_p6 = get_Income_data(df)
# st.bar_chart(data_p6.set_index('Labels'))
