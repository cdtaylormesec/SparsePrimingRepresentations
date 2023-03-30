import streamlit as st

if "agent_memory" not in st.session_state:
    st.session_state["agent_memory"] = {}  # Replace with the initial value you want to use for agent_memory

agent_chain = initialize_agent(tools,  llm, agent="conversational-react-description", memory=st.session_state["agent_memory"], verbose=True)

