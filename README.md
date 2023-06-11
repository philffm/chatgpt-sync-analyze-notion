# ChatGPT local analysis in Jupyter Notebook 🤖 & Sync to Notion 📝

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

- [x] Sync ChatGPT conversations to Notion
    - [x] Add a Notion token to your .env file
    - [x] Just add a '📝' emoji to the conversation and it will be synced to Notion
    - [x] Avoid 2000 character limit by splitting the message into multiple messages
    - [ ] Add a link to the original conversation in the Notion page
    - [ ] Let it detect changes in already synced conversations

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
Feel free to contribute to this project - especially ideas on how to further analyse the data.


## Kudos to

- @saeedezzati for the awesome Superpower ChatGPT extension
