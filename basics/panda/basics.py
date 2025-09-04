import pandas as pd
conference = {
    "Day": [1, 2, 3, 4, 5, 6, 7],
    "Attendees": [100, 150, 200, 250, 300, 350, 400],
    "Overall rating": [4.5, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2],
    "Location": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio"]
}

df = pd.DataFrame(conference, index=[10, 20, 30, 40, 50, 60, 70])
print(df)
print("Top three cells:\n", df.head(3))
print("Bottom three cells:\n", df.tail(3))

conference2 = {
    "Day": [1, 2, 3],
    "Attendees": [450, 500, 550],
    "Overall rating": [5.3, 5.4, 5.5],
    "Location": ["San Diego", "Dallas", "San Jose"]
}
df2 = pd.DataFrame(conference2, index=[80, 90, 100])

print("Merging dataframes:\n", pd.merge(df, df2, on="Day"))
print("Joining dataframes:\n", df.join(df2, lsuffix='_left', rsuffix='_right'))

student_data = {
    "student_id": ["S1", "S2", "S3", "S4", "S5"],
    "name": [
        "Bradley Monroe",
        "Weston Potter",
        "Bryce Jensen",
        "Mariah Duarte",
        "Jayden West"
    ],
    "marks": [200, 210, 190, 222, 199]
}

student_df = pd.DataFrame(student_data, index=[0, 1, 2, 3, 4])
print("Student DataFrame:\n", student_df)

student_data2 = {
    "student_id": ["S4", "S5", "S6", "S7", "S8"],
    "name": [
        "Abel Burgess",
        "Carla Williamson",
        "Kendall Mccullough",
        "Ricky Taylor",
        "Tristen Khan"
    ],
    "marks": [201, 200, 198, 219, 201]
}

student_df2 = pd.DataFrame(student_data2, index=[0, 1, 2, 3, 4])
print("Student DataFrame 2:\n", student_df2)
print("Joined Student DataFrames:\n", pd.concat([student_df, student_df2], axis=0))