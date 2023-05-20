import streamlit as st
import openai

openai.api_key = st.secrets["api_key"] #다른사람이 사용할 수 있음 => secrets.toml에서 가져와 사용

st.title("ChatGPT Plus DALL-E")

#size도 입력받아야 함
with st.form("form"):
    user_input = st.text_input("Prompt") #저장
    size = st.selectbox("Size", ["1024x1024", "512x512", "256x256"])
    submit = st.form_submit_button("Submit") #submit을 누르면 실행이 됨

if submit and user_input: #submit을 누르고 한글짜라도 있을 때
    #Chatgpt에 명령할 command
    gpt_prompt = [{
        "role": "system",
        "content" : "Imagine the detail appeareance of the input. Response it shortly around 20 words."
    }]

    gpt_prompt.append({
        "role" : "user",
        "content" : user_input
    })

    with st.spinner("Waiting for ChatGPT..."): #대기창
        gpt_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=gpt_prompt
        )

    prompt = gpt_response["choices"][0]["message"]["content"] #여기에 response 저장돼 있음
    st.write(prompt)
    with st.spinner("Waiting for DALL-E..."): #대기창
        dalle_response = openai.Image.create(
            prompt=prompt,
            size = size #위에서 구함
        )

    st.image(dalle_response["data"][0]["url"])

