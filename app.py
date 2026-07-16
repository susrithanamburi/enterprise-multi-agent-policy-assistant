import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from src.rag_pipeline import run_pipeline


load_dotenv()

st.set_page_config(
    page_title="Enterprise Policy Assistant",
    page_icon="🤖",
    layout="wide",
)

st.title("Enterprise Multi-Agent Policy Assistant")
st.caption(
    "Ask questions about the fictional enterprise policy library. "
    "Responses are grounded in retrieved policy documents."
)

if not os.getenv("OPENAI_API_KEY"):
    st.error(
        "OpenAI API key was not found. Add OPENAI_API_KEY to the local .env file."
    )
    st.stop()

question = st.text_input(
    "Ask a policy question",
    placeholder="Example: Can employees work remotely from another state?",
)

ask_button = st.button("Ask Question", type="primary")

if ask_button:
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Searching policies and generating a validated answer..."):
            try:
                result = run_pipeline(question.strip())
            except Exception as error:
                st.error(f"The request could not be completed: {error}")
            else:
                st.subheader("Answer")
                st.write(result["response"])

                validation_column, confidence_column = st.columns(2)

                with validation_column:
                    st.subheader("Validation")
                    validation_text = result["validation"]

                    if "PASS" in validation_text.upper():
                        st.success(validation_text)
                    else:
                        st.error(validation_text)

                with confidence_column:
                    st.subheader("Confidence")
                    confidence = result["confidence"]
                    st.metric(
                        label="Confidence score",
                        value=f'{confidence["score"]}%',
                    )
                    st.write(f'Status: **{confidence["status"]}**')

                st.subheader("Sources")

                for source in result["sources"]:
                    st.write(f"- {Path(source).name}")

st.divider()

st.caption(
    "Independent portfolio project built with Python, LangChain, "
    "OpenAI, FAISS, and Streamlit."
)