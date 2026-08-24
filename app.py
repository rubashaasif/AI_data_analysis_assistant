import pandas as pd
import streamlit as st

from agent import process_question
from visualization import create_automatic_chart
from analysis import clean_dataset


# -----------------------------------------
# Page configuration
# -----------------------------------------

st.set_page_config(
    page_title="AI Data Analysis Assistant",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------------------
# Title
# -----------------------------------------

st.title("🤖 AI Data Analysis Assistant")

st.write(
    "Upload a CSV dataset and ask questions about "
    "your data using natural language."
)


# -----------------------------------------
# Upload CSV
# -----------------------------------------

uploaded_file = st.file_uploader(
    "Upload your CSV file",
    type=["csv"]
)


if uploaded_file is not None:

    try:

        # -----------------------------------------
        # Load dataset
        # -----------------------------------------

        df = pd.read_csv(uploaded_file)

        df = clean_dataset(df)

        st.success(
            f"Dataset loaded successfully: "
            f"{len(df)} rows × {len(df.columns)} columns"
        )
        st.info(
    f"Dataset contains {len(df)} rows "
    f"and {len(df.columns)} columns after cleaning."
)


        # -----------------------------------------
        # Dataset Preview
        # -----------------------------------------

        st.subheader("📋 Dataset Preview")

        st.dataframe(
            df.head(10),
            use_container_width=True
        )


        # -----------------------------------------
        # Dataset Information
        # -----------------------------------------

        st.subheader("📊 Dataset Information")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Rows",
                len(df)
            )

        with col2:

            st.metric(
                "Columns",
                len(df.columns)
            )

        with col3:

            st.metric(
                "Missing Values",
                int(df.isnull().sum().sum())
            )


        # -----------------------------------------
        # Automatic Visualization
        # -----------------------------------------

        st.subheader("📈 Automatic Visualization")

        chart, chart_message = create_automatic_chart(df)

        st.write(chart_message)

        if chart is not None:

            st.pyplot(
                chart,
                use_container_width=True
            )


        # -----------------------------------------
        # Ask Question
        # -----------------------------------------

        st.subheader("💬 Ask a Question")

        question = st.text_input(
            "Example: What is the average age?"
        )


        # -----------------------------------------
        # Analyze Button
        # -----------------------------------------

        if st.button("🔍 Analyze"):

            if question.strip() == "":

                st.warning(
                    "Please enter a question."
                )

            else:

                with st.spinner(
                    "🤖 AI is analyzing your question..."
                ):

                    try:

                        answer = process_question(
                            df,
                            question
                        )

                        st.subheader(
                            "🤖 AI Analysis"
                        )

                        st.write(answer)

                    except Exception as e:

                        st.error(
                            f"Something went wrong: {e}"
                        )


    except Exception as e:

        st.error(
            f"Could not read the CSV file: {e}"
        )


else:

    st.info(
        "👆 Upload a CSV file to get started."
    )