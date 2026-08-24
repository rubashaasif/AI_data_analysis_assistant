# 🤖 AI Data Analysis Assistant

An AI-powered data analysis assistant that allows users to upload a CSV dataset and ask questions about their data using natural language.

The system uses an AI agent to understand the user's question, select the appropriate analysis operation, perform the calculation using Python, and provide a clear explanation of the result.

---

## 🎯 Problem Statement

Analyzing datasets often requires users to write Python or SQL code even for simple questions such as:

- What is the average age?
- What is the highest salary?
- Which category occurs most frequently?
- What is the total sales?

This project provides a simple conversational interface where users can ask these questions in natural language.

---

## 💡 Solution

The AI Data Analysis Assistant combines:

- Python
- Pandas
- Streamlit
- OpenRouter LLM
- Automated data analysis
- Automatic visualization

The AI agent interprets the user's question and selects the appropriate analysis operation before Python performs the actual calculation.

---

## ✨ Features

### 📂 CSV Dataset Upload
Users can upload CSV datasets directly through the Streamlit interface.

### 🧹 Automatic Data Cleaning
The system automatically:

- Removes completely empty rows
- Removes completely empty columns
- Removes duplicate rows
- Attempts to convert numeric text columns into numeric data

### 📊 Dataset Information
The application displays:

- Number of rows
- Number of columns
- Missing values
- Dataset preview

### 📈 Automatic Visualization
The system automatically generates a visualization based on the dataset.

### 🤖 AI Agent
The AI agent understands natural-language questions and selects the appropriate analysis operation.

### 🔧 Analysis Tools

The agent can select from:

- Average
- Maximum
- Minimum
- Most Frequent
- Sum
- Count
- Median
- Unique Count

### 💬 Natural Language Results
After performing the calculation, the AI explains the result in simple language.

---

## 🧠 How the AI Agent Works

The system follows this workflow:

```text
User uploads CSV
       ↓
Dataset Cleaning
       ↓
Dataset Preview & Statistics
       ↓
Automatic Visualization
       ↓
User asks a question
       ↓
AI understands the question
       ↓
AI selects analysis operation
       ↓
Python analysis tool executes
       ↓
Analysis result
       ↓
AI explains the result
       ↓
Final answer shown to user
## 🛠️ Technologies Used
Python
Pandas
Streamlit
OpenAI Python SDK
OpenRouter
GPT-OSS-120B
Matplotlib
dotenv