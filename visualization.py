import matplotlib.pyplot as plt


# -----------------------------------------
# Bar Chart
# -----------------------------------------

def create_category_chart(df, column):

    counts = df[column].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(10, 5))

    counts.plot(
        kind="bar",
        ax=ax,
        edgecolor="black"
    )

    ax.set_title(
        f"Top Categories in {column}"
    )

    ax.set_xlabel(column)
    ax.set_ylabel("Count")

    ax.tick_params(
        axis="x",
        rotation=45
    )

    fig.tight_layout()

    return fig


# -----------------------------------------
# Histogram
# -----------------------------------------

def create_numeric_histogram(df, column):

    fig, ax = plt.subplots(figsize=(10, 5))

    df[column].dropna().plot(
        kind="hist",
        bins=10,
        ax=ax,
        edgecolor="black"
    )

    ax.set_title(
        f"Distribution of {column}"
    )

    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")

    fig.tight_layout()

    return fig


# -----------------------------------------
# Scatter Plot
# -----------------------------------------

def create_scatter_chart(df, x_column, y_column):

    data = df[
        [x_column, y_column]
    ].dropna()

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.scatter(
        data[x_column],
        data[y_column],
        edgecolors="black"
    )

    ax.set_title(
        f"{x_column} vs {y_column}"
    )

    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)

    fig.tight_layout()

    return fig


# -----------------------------------------
# Automatic Chart Selection
# -----------------------------------------

def create_automatic_chart(df):

    numerical_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    categorical_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()


    # -----------------------------------------
    # Option 1: Two numeric columns
    # → Scatter plot
    # -----------------------------------------

    if len(numerical_columns) >= 2:

        x_column = numerical_columns[0]
        y_column = numerical_columns[1]

        fig = create_scatter_chart(
            df,
            x_column,
            y_column
        )

        message = (
            f"Created scatter plot: "
            f"{x_column} vs {y_column}."
        )

        return fig, message


    # -----------------------------------------
    # Option 2: Categorical column
    # → Bar chart
    # -----------------------------------------

    for column in categorical_columns:

        unique_values = df[column].nunique()

        if 2 <= unique_values <= 20:

            fig = create_category_chart(
                df,
                column
            )

            message = (
                f"Created bar chart for {column}."
            )

            return fig, message


    # -----------------------------------------
    # Option 3: One numeric column
    # → Histogram
    # -----------------------------------------

    if len(numerical_columns) >= 1:

        column = numerical_columns[0]

        fig = create_numeric_histogram(
            df,
            column
        )

        message = (
            f"Created histogram for {column}."
        )

        return fig, message


    # -----------------------------------------
    # No suitable chart
    # -----------------------------------------

    return (
        None,
        "No suitable columns were found "
        "for automatic visualization."
    )