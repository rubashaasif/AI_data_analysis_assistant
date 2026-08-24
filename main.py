import pandas as pd

from agent import process_question


# Load dataset
df = pd.read_csv("dataset.csv")
from visualization import create_automatic_chart


print("===================================")
print("     AI DATA ANALYSIS ASSISTANT")
print("===================================")

print("\nDataset loaded successfully.")

print("\nColumns:")
print(df.columns.tolist())
chart_message = create_automatic_chart(df)

print("\nVisualization:")
print(chart_message)


question = input("\nAsk a question about the dataset: ")


answer = process_question(
    df,
    question
)


print("\nAnswer:")
print(answer)