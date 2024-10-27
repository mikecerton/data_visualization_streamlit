import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# first
def open_csv_file(filepath):
    return pd.read_csv(filepath)

# p 1
def search_by_Student_ID(stud_ID, df):
    stud_ID = int(stud_ID)
    student_row = df[df['student_ID'] == stud_ID]
    return student_row

# p 3
def get_whole_data(df):
    all_stu_number = df.shape[0]
    gender_chart = create_pie_chart(df, "Gender")

    return [all_stu_number, gender_chart]

# p 4
def get_school_data(string_input, df):
    school_df = df[df['School_Type'] == string_input]

    student_number = school_df.shape[0]                                         
    average_score = school_df['Exam_Score'].mean()                              
    score_counts_df = school_df['Exam_Score'].value_counts().sort_index()       
    tea_chart = create_pie_chart(school_df, "Teacher_Quality")

    return [student_number, average_score, score_counts_df, tea_chart]

# p 5
def set_edited_csv(edited_df, df):
    df.update(edited_df)
    df.to_csv("./dataset.csv", index=False)
    
# p 6
def get_Income_data(df):
    low_count = df[df['Family_Income'] == 'Low'].shape[0]
    medium_count = df[df['Family_Income'] == 'Medium'].shape[0]
    high_count = df[df['Family_Income'] == 'High'].shape[0]

    label = ["Low", "Medium", "High"]
    all_count = [low_count, medium_count, high_count]
    data = pd.DataFrame({'Labels': label,'Sizes': all_count})

    return data


def create_pie_chart(data, column, width=8, height=6):
    plt.figure(figsize=(width, height))
    counts = data[column].value_counts()
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
    plt.title(f'Distribution of {column}')
    plt.legend()
    plt.axis('equal') 

    return plt

def create_bar_chart(data, column, width=8, height=6):
    plt.figure(figsize=(width, height))
    counts = data[column].value_counts()
    colors = sns.color_palette("hsv", len(counts))
    
    plt.bar(counts.index, counts.values, color=colors)
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.title(f'Distribution of {column}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return plt


if __name__ == "__main__":

    df = pd.read_csv(".\dataset.csv")

    # print(search_by_Student_ID(500, df))

    # print(get_Income_data(df))

    # get_school_data(None, df)
    