# 1. Import the pandas library and give it the nickname 'pd'
import pandas as pd

# 2. Create a small dataset directly in the code
data = {
    'PassengerId': [1, 2, 3, 4, 5, 6],
    'Name': ['Braund, Mr. Owen', 'Cumings, Mrs. John', 'Heikkinen, Miss. Laina', 'Futrelle, Mrs. Jacques', 'Allen, Mr. William', 'Moran, Mr. James'],
    'Sex': ['male', 'female', 'female', 'female', 'male', 'male'],
    'Survived': [0, 1, 1, 1, 0, 0] # 1 means survived, 0 means died
}

# 3. Load the data into a Pandas DataFrame (like a digital spreadsheet)
df = pd.DataFrame(data)

# 4. Print the original data so we can see it
print("--- Original Passenger Data ---")
print(df)

# 5. Group the data by 'Sex' and calculate the average survival rate
# Since 1 is survived and 0 is died, the mean gives us the survival percentage
survival_rate = df.groupby('Sex')['Survived'].mean()

# 6. Print the results
print("\n--- Survival Rate by Gender ---")
print(survival_rate)