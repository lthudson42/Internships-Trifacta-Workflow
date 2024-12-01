import pandas as pd
import openpyxl

# Read the file
with open("data.txt", "r") as file:
    data = file.read()

# Parse the data
lines = [line.strip() for line in data.splitlines() if not line.startswith("Internships")]  # Remove the title line
rows = [line.rsplit(' ', 1) for line in lines]  # Split into title and date

# Create the DataFrame
df = pd.DataFrame(rows, columns=["Company and Title", "Date Applied"])

# Split into Company and Internship Title
df[['Company', 'Internship Title']] = df['Company and Title'].str.extract(r'^(.+?) (.+)$')
df.drop(columns="Company and Title", inplace=True)

# Save to spreadsheet
df.to_excel("internships.xlsx", index=False)
print("Spreadsheet saved!")