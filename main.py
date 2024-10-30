import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from my_controller import search_by_Student_ID, get_Income_data, open_csv_file, set_edited_csv, get_school_data, create_bar_chart, get_whole_data

df = open_csv_file(".\dataset.csv")

st.title("Student Data Visualization")

# function 1
st.subheader("1.Display student data by Student_ID")
user_input_p1 = st.text_input("Enter Student_ID to search:", "0001", max_chars=4)
st.write(search_by_Student_ID(user_input_p1, df))

# function 2
st.subheader("2.All student data in csv")
st.write(df)

# function 3
st.subheader("3.Summary of All data")
[all_stu_number, gender_chart] = get_whole_data(df)
st.write(f"***Number Of Student = {all_stu_number}***")
st.pyplot(gender_chart)

a = create_bar_chart(df, "Parental_Education_Level")
st.pyplot(a)

# function 4
st.subheader("4.Data summary for Private or public school")
user_input_p4 = st.multiselect("What are your favorite colors", ["Public", "Private"], max_selections = 1, default = "Public")
string_input = user_input_p4[0] if user_input_p4 else "Public"

st.write(f"***{string_input} School***")
[student_number, average_score, score_counts_df, tea_chart] = get_school_data(string_input, df)

st.write(f"***Number Of Student = {student_number}***")
st.write(f"***Average Of Exam Scores = {average_score:.2f}***")
st.write("***Bar Chart Of Exam Scores.***")
st.bar_chart(score_counts_df)
st.write("***Pie Chart Of Teacher Quality.***")
st.pyplot(tea_chart)


# function 5
st.subheader("5.Edit csv file")
user_input_p5 = st.text_input("Enter Student_ID to search:")
if user_input_p5:
    edited_df = st.data_editor(search_by_Student_ID(user_input_p5, df), num_rows="dynamic")
    if st.button("Save Changes"):
            set_edited_csv(edited_df, df)
            st.success(f"Changes saved to dataset.csv for Student_ID {user_input_p5}")

# function 6
st.subheader("6.Show the proportion of Family_Income of the data.")
data_p6 = get_Income_data(df)
st.bar_chart(data_p6.set_index('Labels'))

data = open_csv_file(".\dataset.csv")

# function 7
st.subheader("7. Displaying the Ranking of Students' Scores")
num_top = st.selectbox("Select the number of top ranks", [10, 20, 50, 100])
sorted_exam_score = data.sort_values(by='Exam_Score', ascending=False).head(num_top)
st.write(f"Top {num_top} scores:")    
st.write(sorted_exam_score[['Student_ID', 'Hours_Studied', 'Attendance', 'Previous_Scores', 'Exam_Score']])

# function 8
st.subheader("Class Attendance Statistics")

bins = [60, 65, 70, 75, 80, 85, 90, 95, 100]
labels = ["60-65", "66-70", "71-75", "76-80", "81-85", "86-90", "91-95", "96-100"]
data['Attendance_Bin'] = pd.cut(data['Attendance'], bins=bins, labels=labels, right=True)
attendance_counts = data['Attendance_Bin'].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=attendance_counts.index, y=attendance_counts.values, palette="Blues", ax=ax)
ax.set_xlabel("Attendance", fontsize=10, weight='bold')
ax.set_ylabel("Number of Students", fontsize=10, weight='bold')
ax.tick_params(axis='x', rotation=45)  

for i, value in enumerate(attendance_counts.values):
    ax.text(i, value + 1, str(value), ha='center', va='bottom', color='black', fontsize=9, weight='bold')

st.pyplot(fig)

# function 9
st.subheader("Check Exam Score")
student_id = st.text_input("Enter the Student ID to check:")

if student_id:
    if student_id in data['Student_ID'].astype(str).values:
        data['Student_ID'] = data['Student_ID'].astype(str)
        student_data = data[data['Student_ID'] == student_id]

        data_sorted = data.sort_values(by='Exam_Score', ascending=False).reset_index(drop=True)
        rank = data_sorted[data_sorted['Student_ID'] == student_id].index[0] + 1

        st.write(f"Student ID : {student_id}")
        st.write(f"Previous Scores : {student_data['Previous_Scores'].values[0]}")
        avg_exam_score = data['Exam_Score'].mean()
        st.write(f"Mean Exam Score: {avg_exam_score:.2f}")
        st.write(f"Exam Score : {student_data['Exam_Score'].values[0]}")
        st.write(f"Rank : {rank}")
    else:
        st.error("cannot found this Student ID")

# function 10
st.subheader("10. Graph Showing the Number of Students with Improved Exam Scores")

more_than_previous = (data['Exam_Score'] > data['Previous_Scores']).sum()
less_or_equal_to_previous = (data['Exam_Score'] <= data['Previous_Scores']).sum()

labels = ['Exam Score > Previous Score', 'Exam Score < Previous Score']
sizes = [more_than_previous, less_or_equal_to_previous]
colors = ['#b4e0e3', '#fac357']  
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, textprops={'fontsize': 8})
ax.axis('equal') 

st.pyplot(fig)
