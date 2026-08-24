import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)
def understand_question(question, columns):

    prompt = f"""
You are an AI data analysis agent.

Your job is to understand the user's question and select
the correct analysis tool.

Available tools:

1. average
Use when the user asks for an average or mean.

2. maximum
Use when the user asks for the highest, maximum, largest,
or greatest value.

3. minimum
Use when the user asks for the lowest, minimum, smallest,
or least value.

4. most_frequent
Use when the user asks which value/category appears most,
is most common, or occurs most frequently.

5. sum
Use when the user asks for total, sum, total sales,
total revenue, or total amount.

6. count
Use when the user asks how many records, values,
customers, products, or entries there are.

7. median
Use when the user asks for the median or middle value.

8. unique_count
Use when the user asks how many different, distinct,
or unique values exist.

Return ONLY valid JSON.

The JSON format must be:

{{
    "operation": "tool_name",
    "column": "exact_column_name"
}}

Available dataset columns:
{columns}

User question:
{question}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content



    
def explain_result(question, result):

    prompt = f"""
You are a data analysis assistant.

The user asked:

{question}

The Python data analysis produced this result:

{result}

Explain the result clearly and briefly.

Do not invent any additional numbers or facts.
Only explain what can be supported by the result.

Return 2-3 sentences.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content