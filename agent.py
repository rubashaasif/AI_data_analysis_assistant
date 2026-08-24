import json
import pandas as pd

from llm import understand_question, explain_result

from analysis import (
    average_value,
    maximum_value,
    minimum_value,
    most_frequent,
    sum_value,
    count_values,
    median_value,
    unique_count
)


def process_question(df, question):

    # Get dataset columns
    columns = df.columns.tolist()

    # Ask the LLM to understand the question
    llm_response = understand_question(
        question,
        columns
    )

    # Convert LLM JSON response into Python dictionary
    try:
        instruction = json.loads(llm_response)

    except json.JSONDecodeError:
        return "The AI returned an invalid response. Please try again."

    # Get operation and column
    operation = instruction.get("operation")
    column = instruction.get("column")

    # Check that both values were provided
    if not operation or not column:
        return "The AI could not determine the operation or column."

    # -----------------------------------------
    # Match AI column with real dataset column
    # -----------------------------------------

    column_map = {
        col.lower(): col
        for col in df.columns
    }

    if column.lower() in column_map:

        column = column_map[column.lower()]

    else:

        return (
            f"I could not find the column "
            f"'{column}' in the dataset."
        )


    # -----------------------------------------
    # Check supported operations
    # -----------------------------------------

    valid_operations = [
    "average",
    "maximum",
    "minimum",
    "most_frequent",
    "sum",
    "count",
    "median",
    "unique_count"
]
   
    if operation not in valid_operations:

        return f"Unsupported operation: {operation}"


    # -----------------------------------------
    # AVERAGE
    # -----------------------------------------

    if operation == "average":

        # Average only makes sense for numeric columns
        if not pd.api.types.is_numeric_dtype(df[column]):

            return (
                f"I cannot calculate the average of "
                f"'{column}' because it is not numeric."
            )

        result = average_value(
            df,
            column
        )

        answer = (
            f"The average {column} is "
            f"{result:.2f}."
        )


    # -----------------------------------------
    # MAXIMUM
    # -----------------------------------------

    elif operation == "maximum":

        # Maximum only makes sense for numeric columns
        if not pd.api.types.is_numeric_dtype(df[column]):

            return (
                f"I cannot calculate the maximum of "
                f"'{column}' because it is not numeric."
            )

        result = maximum_value(
            df,
            column
        )

        answer = (
            f"The maximum {column} is "
            f"{result}."
        )


    # -----------------------------------------
    # MINIMUM
    # -----------------------------------------

    elif operation == "minimum":

        # Minimum only makes sense for numeric columns
        if not pd.api.types.is_numeric_dtype(df[column]):

            return (
                f"I cannot calculate the minimum of "
                f"'{column}' because it is not numeric."
            )

        result = minimum_value(
            df,
            column
        )

        answer = (
            f"The minimum {column} is "
            f"{result}."
        )


    # -----------------------------------------
    # MOST FREQUENT
    # -----------------------------------------

    elif operation == "most_frequent":

        result = most_frequent(
            df,
            column
        )

        answer = (
            f"The most frequent {column} is "
            f"{result}."
        )
            # -----------------------------------------
    # SUM
    # -----------------------------------------

    elif operation == "sum":

        if not pd.api.types.is_numeric_dtype(df[column]):

            return (
                f"I cannot calculate the sum of "
                f"'{column}' because it is not numeric."
            )

        result = sum_value(
            df,
            column
        )

        answer = (
            f"The total {column} is "
            f"{result}."
        )


    # -----------------------------------------
    # COUNT
    # -----------------------------------------

    elif operation == "count":

        result = count_values(
            df,
            column
        )

        answer = (
            f"There are "
            f"{result} non-empty values in {column}."
        )


    # -----------------------------------------
    # MEDIAN
    # -----------------------------------------

    elif operation == "median":

        if not pd.api.types.is_numeric_dtype(df[column]):

            return (
                f"I cannot calculate the median of "
                f"'{column}' because it is not numeric."
            )

        result = median_value(
            df,
            column
        )

        answer = (
            f"The median {column} is "
            f"{result}."
        )


    # -----------------------------------------
    # UNIQUE COUNT
    # -----------------------------------------

    elif operation == "unique_count":

        result = unique_count(
            df,
            column
        )

        answer = (
            f"There are "
            f"{result} unique values in {column}."
        )


    # -----------------------------------------
    # Safety fallback
    # -----------------------------------------

    else:

        return "I could not determine the required analysis."


    # -----------------------------------------
    # Ask LLM to explain the REAL result
    # -----------------------------------------

    explanation = explain_result(
        question,
        answer
    )


    # -----------------------------------------
    # Return final answer
    # -----------------------------------------

    return (
        f"{answer}\n\n"
        f"Explanation: {explanation}"
    )