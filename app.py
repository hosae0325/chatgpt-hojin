import openai
import streamlit as st

openai.api_key = "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"

st.title('mini chatgpt')
st.sidebar.title('submenu')
prompt = st.text_input('Prompt')

# message = ""
if st.button('submit') or prompt != "":
    with st.spinner('Waiting for response...'):
        response = openai.Completion.create(
            engine="text-curie-001",
            prompt=prompt,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.5,
        )

    message = response.choices[0].text.strip()
    st.write(message)
