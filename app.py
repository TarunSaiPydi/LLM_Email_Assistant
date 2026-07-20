import streamlit as st
import ollama


# 1. Page Configuration
st.set_page_config(
    page_title="Local AI Email Assistant",
    page_icon="✉️",
    layout="centered",
)
st.title("✉️ Local AI Email Responder")
st.write("Turn your rough notes into a professional email, running 100% locally.")

# 2. User Inputs
tone = st.selectbox(
    "Select Email Tone",
    ["Professional", "Friendly", "Apologetic", "Direct"],
)
user_input = st.text_area("Enter your rough draft or notes here:", height=150)

# 3. The Core Logic
if st.button("Generate Professional Email"):
    if not user_input.strip():
        st.warning("Please enter some text to get started.")
    else:
        with st.spinner("Drafting your email..."):
            # 4. Prompt Engineering
            system_prompt = f"""
            You are an expert corporate communicator. Your task is to rewrite the user's rough notes
            into a well-structured, grammatically correct email.
            The tone of the email must be: {tone}.
            Do not include any explanations or pleasantries in your output, just the email itself.
            """

            # 5. Local Model Invocation
            try:
                response = ollama.chat(
                    model="llama3",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_input},
                    ],
                )

                # 6. Displaying the Output
                st.subheader("Your Polished Email:")
                st.info(response["message"]["content"])

            except Exception as e:
                st.error(
                    f"An error occurred: {e}. Is Ollama running in the background?"
                )