import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('grades.csv')
print(df.head())

df1 = df.dropna()

cols=df1.columns
print(cols)
courses = df1['Course'].unique()[:10]  
finalcourses = df1[df1['Course'].isin(courses)]

finalcourses.to_csv('finalcourses.csv', index=False)

print(finalcourses.to_string())

plt.figure(figsize=(12, 8))


for course in courses:
    course_data = finalcourses[finalcourses['Course'] == course]
    plt.plot(course_data['Year'], course_data['Grade'], marker='o', label=course)

plt.title('Grading Data for Selected Courses Over the Last 10 Years')
plt.xlabel('Year')
plt.ylabel('Grade')
plt.xticks(rotation=45)
plt.legend()
plt.grid()


plt.tight_layout()
plt.show()
