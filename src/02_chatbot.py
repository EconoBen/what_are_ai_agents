import streamlit as st
from hugchat import hugchat
from hugchat.login import Login


class HugChatAgent:
    def __init__(self):
        self.login_to_hugchat()

    def login_to_hugchat(self):
        # login
        self.email = st.secrets["HUGGINGFACE_EMAIL"]
        self.password = st.secrets["HUGGINGFACE_PASSWORD"]
        if not (self.email and self.password):
            raise ValueError("Missing HuggingFace Chat Credentials!")

        sign = Login(self.email, self.password)
        cookies = sign.login()

        # start a new conversation
        self.chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
        chatbot_id = self.chatbot.new_conversation()
        self.chatbot.change_conversation(chatbot_id)

    def response(self, prompt: str):
        try:
            return self.chatbot.chat(prompt)
        except Exception as e:
            raise e


if __name__ == "__main__":
    st.set_page_config(page_title="🤗 HuggingFace Chatbot Agent for O'Reilly Readers")

    agent = HugChatAgent()

    if "messages" not in st.session_state.keys():
        st.session_state["messages"] = [
            {
                "role": "assistant",
                "content": "Hello O'Reilly Reader! What would you like to talk about?",
            }
        ]
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            agent_response = agent.response(prompt)
            st.write(agent_response)
        cache = {"role": "assistant", "content": agent_response}
        st.session_state.messages.append(cache)
