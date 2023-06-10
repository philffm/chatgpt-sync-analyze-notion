# ChatGPT local analysis in Jupyter Notebook 🤖

In this notebook I deliver a foundation on how to analyse the personal ChatGPT conversation history. 

After a few months of using ChatGPT, I have collected a large amount of data and want to reflect on old conversations and spark ideas on how to use it in the future.

Using the Superpower ChatGPT extension for Chrome you can automatically sync your conversations for offline usage. Since all your conversations are now stored locally, you can analyse the local database to get insights into your conversations.

## Demo
Feel free to check out the notebook [here](./chatgpt_analysis.ipynb): 
## Requirements

- Superpower ChatGPT extension: https://github.com/saeedezzati/superpower-chatgpt
- Python 3.8
- Streamlit


## Current state

- [x] Get data from local database to a pandas dataframe
    - [x] df_conversations
    - [x] df_messages

- [x] Streamlint Dashboard
    - [x] Basic setup
    - [x] Table with conversations
    - [x] Wordcloud of all messages
    - [x] Exclusion list in custom_stop_words.txt
    
    - [ ] Conversation overview
    - [ ] Graph network of conversations / words / topics

## Future features

- Graph network of conversations / words / topics (Can someone help me with this?) 
    - Not sure how to do this, but I think it would be cool to see how conversations are connected and how topics are connected to each other
    - https://towardsdatascience.com/how-to-deploy-interactive-pyvis-network-graphs-on-streamlit-6c401d4c99db

## Pull requests are welcome!
Feel free to contribute to this project and contribute ideas on how to analyse the data.