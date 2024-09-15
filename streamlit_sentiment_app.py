
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('zomato_reviews.csv')

# Function to display sentiment analysis data
def display_sentiment_data():
    st.title('Zomato Reviews Sentiment Analysis')

    # Show the raw data
    st.subheader('Raw Zomato Reviews Data')
    st.write(data.head())

    # Display overall statistics
    st.subheader('Overall Sentiment Statistics')
    st.write(data[['rating', 'sentiment']].describe())

    # Plot distribution of sentiments
    st.subheader('Sentiment Distribution')
    plt.figure(figsize=(10, 6))
    plt.hist(data['sentiment'], bins=20, color='blue', edgecolor='black')
    plt.xlabel('Sentiment Polarity')
    plt.ylabel('Frequency')
    st.pyplot(plt)

    # Filter reviews based on rating or sentiment polarity
    st.subheader('Filter Reviews')
    sentiment_filter = st.slider('Select sentiment polarity range', -1.0, 1.0, (-1.0, 1.0))
    filtered_data = data[(data['sentiment'] >= sentiment_filter[0]) & (data['sentiment'] <= sentiment_filter[1])]
    st.write(filtered_data[['review', 'rating', 'sentiment']])

# Run the app
if __name__ == '__main__':
    display_sentiment_data()
