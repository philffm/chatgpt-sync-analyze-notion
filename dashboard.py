

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# read custom_stop_words from txt file

custom_stop_words = []
with open('custom_stop_words.txt', 'r') as f:
    custom_stop_words = f.read().splitlines()


# Read the chat logs data into a DataFrame
df_messages = pd.read_csv('df_messages.txt', sep='	')
df_messages['cleaned_text'] = df_messages['cleaned_text'].astype(str)  # Convert 'cleaned_text' column to string type
# filter out code words in cleaned_text column 
df_messages['cleaned_text'] = df_messages['cleaned_text'].apply(lambda x: ' '.join([word for word in x.split() if word not in custom_stop_words]))

# Process the chat messages to extract words
all_words = ' '.join(df_messages['cleaned_text']).lower().split()
all_words = [word for word in all_words if word not in custom_stop_words]
word_counts = Counter(all_words)
most_common_words = word_counts.most_common(200)  # Change the number as per your requirement

# Create a DataFrame for the most common words
df_common_words = pd.DataFrame(most_common_words, columns=['Word', 'Count'])

# Display the most common words in a bar chart
fig, ax = plt.subplots()
df_common_words.plot.bar(x='Word', y='Count', ax=ax)
plt.xlabel('Word')
plt.ylabel('Count')
plt.title('Most Common Words in Chat Logs')
plt.xticks(rotation=45)
st.pyplot(fig)

# Display the raw data of the most common words
st.write(df_common_words)

# Display the raw data of the chat logs
st.write(df_messages)

# display a word cloud
from wordcloud import WordCloud

# Create a word cloud

wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=200).generate(' '.join(df_messages['cleaned_text']))

# Display the generated image:
# the matplotlib way:

fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()
st.pyplot(fig)
