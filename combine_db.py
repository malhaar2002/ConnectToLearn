import pandas as pd

def make_database():
    # Read in the data
    faculty_df = pd.read_excel("excel/faculty.xlsx")
    founders_df = pd.read_excel("excel/founders.xlsx")

    # Add source column
    faculty_df["source"] = "faculty"
    founders_df["source"] = "founder"

    # Combine the dataframes
    combined_df = pd.concat([faculty_df, founders_df])

    # Write the combined dataframe to a new Excel file
    combined_df.to_excel("excel/database.xlsx", index=False)

if __name__ == "__main__":
    make_database()