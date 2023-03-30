from langchain import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.chains.conversation.memory import ConversationBufferMemory

import streamlit as st


# define a function to calculate nth fibonacci number
def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1) + fib(n-2))
    
# define a function which sorts the input string alphabetically
def sort_string(string):
    return ''.join(sorted(string))
    
# define a function to turn a word in to an encrypted word
def encrypt(word):
    encrypted_word = ""
    for letter in word:
        encrypted_word += chr(ord(letter) + 1)
    return encrypted_word

# define a function to turn a word in to an decrypted word

def decrypt(word):
    decrypted_word = ""
    for letter in word:
        decrypted_word += chr(ord(letter) - 1)
    return decrypted_word

# return direct means that the output of the function will be returned after max iterations reached??
tools = [
    Tool(
        name = "Fibonacci",
        func= lambda n: str(fib(int(n))),
        description="use when you want to calculate the nth fibonacci number",
        # return_direct=True
    ),
    Tool(
        name = "Sort String",
        func= lambda string: sort_string(string),
        description="use when you want to sort a string alphabetically",
        # return_direct=True
    ),
    Tool(
        name = "Encrypt",
        func= lambda word: encrypt(word),
        description="use when you want to encrypt a word",
        # return_direct=True
    ),
    Tool(
        name = "Decrypt",
        func= lambda word: decrypt(word),
        description="use when you want to decrypt a word",
        # return_direct=True
    )
]

memory = ConversationBufferMemory(memory_key="chat_history") # You can use other memory types as well!
llm=OpenAI(temperature=0, verbose=True)
agent_chain = initialize_agent(tools,  llm, agent="conversational-react-description", memory=memory, verbose=True) # verbose=True to see the agent's thought process


st.header(":blue[Langchain chatbot with agent/tools and memory] :sunglasses:") # short term memory. no embedded vectorstore
user_input = st.text_input("You: ")
# initialize the memory buffer
if "memory" not in st.session_state:
    st.session_state["memory"] = ""
# streamlit button
if st.button("Submit"):

    st.markdown(agent_chain.run(input=user_input))
    # print the memory buffer
    # add conversation history to the memory buffer
    st.session_state["memory"] += memory.buffer
    print(st.session_state["memory"])