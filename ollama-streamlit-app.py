import streamlit as st
from llama_index.core.llms import ChatMessage
import logging
import time
from llama_index.llms.ollama import Ollama

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize chat history in session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Function to stream chat response based on selected model
def stream_chat(model, messages):
    # Integrate with actual LLM streaming method
    try:
        llm = Ollama(model=model, request_timeout=120.0) 
        resp = llm.stream_chat(messages)
        response = ""
        response_placeholder = st.empty()
        for r in resp:
            response += r.delta
            response_placeholder.write(response)
        logging.info(f"Model: {model}, Messages: {messages}, Response: {response}")
        return response
    except Exception as e:
        logging.error(f"Error during streaming: {str(e)}")
        raise e

# Streamlit app setup
def main():
    st.title("Chat with AI Models")
    logging.info("App started")

    # Sidebar for model selection
    model = st.sidebar.selectbox("Choose a model", ["llama3", "phi3", "mistral"])
    logging.info(f"Model selected: {model}")
    
    # Prompt for user input and save to chat history
    if prompt := st.chat_input("Votre question"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        logging.info(f"User input: {prompt}")

        # Immediately display the user's query
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
        
        # If last message is not from assistant, generate a new response
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                # Start timing
                start_time = time.time()
                logging.info("Generating response")
                # Generate the bot's response with error handling for missing files
                with st.spinner("En train d'écrire..."):
                    try:
                        messages = [ChatMessage(role=msg["role"], content=msg["content"]) for msg in st.session_state.messages]
                        response_message = stream_chat(model, messages)
                        # Calculate the duration
                        duration = time.time() - start_time
                        response_message_with_duration = f"{response_message}\n\nDuration: {duration:.2f} seconds"
                        st.session_state.messages.append({"role": "assistant", "content": response_message_with_duration})
                        st.write(f"Duration: {duration:.2f} seconds")
                        logging.info(f"Response: {response_message}, Duration: {duration:.2f} s")
                    except Exception as e:
                        st.session_state.messages.append({"role": "assistant", "content": str(e)})
                        st.error("Une erreur s'est produite lors de la génération de la réponse.")
                        logging.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()

