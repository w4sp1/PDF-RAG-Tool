import streamlit as st
from LLM.reader import Reader


class UI:
    def __init__(self):
        st.write("# PDF RAG Tool")
        st.caption("Built by W4sp")
        st.warning("Note answers produced by the tool maybe inaccurate. Fact check answers before proceeding")
        self.build_chat()

    def build_chat(self):
        with st.sidebar:
            st.write("## 📄 PDF RAG Tool")
            st.markdown("Uploads and analyzes PDF documents using natural language processing (NLP) algorithms to extract relevant information. The tool then returns answers to user-inputted questions based on the content of the uploaded PDF.")
            st.write("## Upload PDF Here")
            user_input = st.file_uploader("Choose a PDF File", type="pdf")

            with st.expander("Settings"):
                st.info("**Note**: Changing these values can impact model performance. Ensure you know what you are doing before adjusting values")
                st.slider("k value", 0, 10, 4)
            st.caption("🤖 Powered by llama 3.2")

        if "messages" not in st.session_state:
            st.session_state.messages = [{"role": "assistant", "content": "Hi there 👋! Let's start chatting! 👇"}]

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        if prompt := st.chat_input("Enter your query"):
            st.session_state.messages.append({"role" : "user", "content" : prompt})
            with st.chat_message("user"):
                st.write(prompt)
        
            if user_input is not None and prompt is not None:
                    data = user_input.read()
                    reader = Reader(data, prompt)
                    with st.chat_message("ai"):
                        placeholder = st.empty()
                        response = ""
                        reader_response = reader.respond()
                        for chunk in reader_response:
                            response += chunk
                            placeholder.markdown(response.strip() + "●")

                        st.session_state.messages.append({"role" : "ai", "content" : response})
                        
UI()