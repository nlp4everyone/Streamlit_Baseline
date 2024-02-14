from components.streamlit_config import *
from components.log_state import *

def main():
    # Default config
    default_config()
    # Chat
    model_name = st.selectbox(label="OpenLLM", options=list_models, placeholder="Model name")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # When user input
    prompt = st.chat_input("Hello, how can I help you today?")

    if prompt:
        # User input
        with st.chat_message("user"):
            st.markdown(prompt)
            # Update to session
            st.session_state.messages.append({"role":"user","content":prompt})

        # Bot answer
        with st.chat_message("assistant"):
            response = "Hi. I'm chatbot"
            st.markdown(response)
            # Update to session
            st.session_state.messages.append({"role": "assistant", "content": response})

        # Save log
        save_json(model_name=model_name,data=st.session_state.messages)

if __name__ == "__main__":
    main()
