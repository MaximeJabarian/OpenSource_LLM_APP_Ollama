# Chat with AI Models Using Streamlit and Ollama
![Alt text for the image](path/to/chat-interface-app.png)

This repository contains the code for a chat application that leverages Streamlit and the Ollama language model (LLM) to interact with users in real-time. This application allows users to select different AI models and receive instant responses to their queries.

## Features

- Real-time chat interface using Streamlit.
- Integration with Ollama LLM for generating responses.
- Model selection from the sidebar (supports Llama3, Phi3, and Mistral).
- Logging for debugging and monitoring.

## Installation

### Prerequisites

- Python 3.7 or later
- Streamlit
- Ollama

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MaximeJabarian/OpenSource_LLM_APP_Ollama.git
   cd OpenSource_LLM_APP_Ollama
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**

   ```bash
   streamlit run ollama-streamlit-app.py
   ```

## Usage

1. Open your web browser and navigate to `http://localhost:8501`.
2. Select a model from the sidebar (`Llama3`, `Phi3`, `Mistral`).
3. Enter your question in the chat input box and press Enter.
4. View the model's response in real-time.

## Code Overview

- **Initialization**: Sets up logging and initializes chat history in session state.
- **Model Selection**: Users can select from Llama3, Phi3, and Mistral models.
- **Chat Input**: Captures user input and appends it to the session state.
- **Streaming Responses**: Uses the Ollama LLM to generate responses and streams them back to the user.
- **Error Handling**: Logs errors and displays them in the UI if they occur.

## Example

Here's an example of how the app works:

1. User selects the "Llama3" model from the sidebar.
2. User enters a question: "What is the capital of France?"
3. The application sends the question to the Llama3 model.
4. The model processes the question and streams the response back to the user: "The capital of France is Paris."

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is open-sourced. 

## Acknowledgements

This project uses the following libraries:
- [Streamlit](https://streamlit.io/)
- [Ollama](https://ollama.com/)

Feel free to reach out if you have any questions or need further assistance. Happy coding!
