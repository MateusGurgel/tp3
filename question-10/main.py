import streamlit as st
import pandas as pd
import plotly.express as px

# Function to load the CSV file
def load_results(file_path='./data/results.csv'):
    """
    Loads the results from a CSV file into memory using pandas.

    Parameters:
        file_path (str): The path to the CSV file. Defaults to './data/results.csv'.

    Returns:
        pd.DataFrame: A DataFrame containing the CSV data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        st.error(f"Error: File not found at {file_path}. Please check the path and try again.")
        return None
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Streamlit app
def main():
    # Set page config with dark theme
    st.set_page_config(
        page_title="Simpsons Sentiment Analysis",
        page_icon="📊",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    # Apply custom CSS for dark mode
    dark_mode_css = """
    <style>
        body {
            color: #f5f5f5;
            background-color: #0e1117;
        }
        .stButton>button {
            background-color: #24292e;
            color: #f5f5f5;
            border: 1px solid #30363d;
        }
        .stButton>button:hover {
            background-color: #1f2428;
            border: 1px solid #f0f0f0;
        }
        .stTable {
            color: #f5f5f5;
        }
    </style>
    """
    st.markdown(dark_mode_css, unsafe_allow_html=True)

    # Title and description
    st.title("📊 Simpsons Sentiment Analysis Dashboard")
    st.markdown("""
    This dashboard visualizes sentiment analysis results from Simpsons quotes using a **pizza chart**. 
    Upload a CSV file to see the data breakdown.
    """)

    # Load data
    data = load_results()

    if data is not None:
        # Display the loaded data
        st.subheader("Loaded Data")
        st.write(data)

        # Prepare data for the pie chart
        sentiment_counts = data['result'].value_counts().reset_index()
        sentiment_counts.columns = ['Sentiment', 'Count']

        # Create pizza chart
        fig = px.pie(
            sentiment_counts,
            names='Sentiment',
            values='Count',
            hole=0.3,
            title="Sentiment Analysis Results",
            color_discrete_sequence=px.colors.sequential.Viridis
        )
        fig.update_layout(
            showlegend=True,
            paper_bgcolor="#0e1117",
            font_color="white",
        )

        # Display chart
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
