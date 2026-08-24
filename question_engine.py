from analysis import (
    average_value,
    maximum_value,
    minimum_value,
    most_frequent
)


def answer_question(df, question):

    question = question.lower()

    # --------------------------------
    # AVERAGE AGE
    # --------------------------------
    if (
        ("average" in question or "mean" in question)
        and "age" in question
    ):
        answer = average_value(df, "Age")
        return f"The average age is {answer:.2f}."

    # --------------------------------
    # MAXIMUM SALES
    # --------------------------------
    elif (
        ("maximum" in question or
         "highest" in question or
         "greatest" in question)
        and "sales" in question
    ):
        answer = maximum_value(df, "Sales")
        return f"The maximum sales value is {answer}."

    # --------------------------------
    # MINIMUM SALES
    # --------------------------------
    elif (
        ("minimum" in question or
         "lowest" in question or
         "smallest" in question)
        and "sales" in question
    ):
        answer = minimum_value(df, "Sales")
        return f"The minimum sales value is {answer}."

    # --------------------------------
    # MOST FREQUENT CITY
    # --------------------------------
    elif (
        "city" in question
        and (
            "most" in question
            or "maximum" in question
            or "highest" in question
        )
    ):
        answer = most_frequent(df, "City")
        return f"The city with the most orders is {answer}."

    # --------------------------------
    # UNKNOWN QUESTION
    # --------------------------------
    else:
        return "Sorry, I don't understand this question yet."