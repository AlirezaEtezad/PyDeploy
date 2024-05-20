# from dotenv import load_dotenv
# import os
import streamlit as st
from sqlmodel import Session
import requests
import json
from models import User, Message
from database import create_db_and_tables, engine, create_user, authenticate_user, select




# load_dotenv()
# api_key = os.getenv("API_EdenAI")
api_key = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYjZjZGRiMDctOWJkMC00YWQxLTg0YTYtMGNlYTkzYjEwYTI0IiwidHlwZSI6ImFwaV90b2tlbiJ9.xOO_tymL2zwe4a4_DWQ3GbfrPmzOR8O_p445aVWIneM"


# Initialize database
create_db_and_tables()

@st.cache_resource
def database_connection():
    return engine

engine = database_connection()




import requests

def get_edenai_response(prompt: str) -> str:


    headers = {"Authorization": api_key}
    url = "https://api.edenai.run/v2/text/chat"
    payload = {
        "providers": "openai",
        "text": prompt,
        "chatbot_global_action": "Act as an assistant",
        "previous_history": [],
        "temperature": 0.0,
        "max_tokens": 150,
        "fallback_providers": "OpenAI - gpt-3.5-turbo, OpenAI - gpt-3.5-turbo-1106, OpenAI ,  OpenAI - gpt-3.5-turbo-0301"
    }
    response = requests.post(url,json=payload, headers=headers)
    result = json.loads(response.text)
    generated_text = result['openai']['generated_text']
    # print(result['openai']['generated_text'])
    print(result)
    
    if response.status_code == 200:
       # return response.json()["answer"]
        return generated_text
    else:
        error_message = f"Error: {response.status_code} - {response.text}"
        print(error_message)
        return "Error: Unable to fetch response from Eden AI"


# def ai(user_text_message):
#     ai_text_message = user_text_message * 3
#     return ai_text_message

def process(user_text_message, user_id):
    ai_text_message = get_edenai_response(user_text_message)
    user_message = Message(text=user_text_message, type="user", user_id=user_id)
    ai_message = Message(text=ai_text_message, type="ai", user_id=user_id)

    with Session(engine) as session:
        session.add(user_message)
        session.add(ai_message)
        session.commit()

def get_user_messages(user_id):
    with Session(engine) as session:
        statement = select(Message).where(Message.user_id == user_id)
        messages = session.exec(statement).all()
    return messages

if "user" not in st.session_state:
    st.session_state.user = None

with st.sidebar:
    if st.session_state.user is None:
        choice = st.selectbox("Choose Action", ["Login", "Sign Up"])

        if choice == "Sign Up":
            st.subheader("Create a new account")
            name = st.text_input("Name")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")

            if st.button("Sign Up"):
                user = create_user(name, email, password)
                if user:
                    st.success("Account created successfully!")
                    st.session_state.user = user
                else:
                    st.error("User with this email already exists.")

        elif choice == "Login":
            st.subheader("Login to your account")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")

            if st.button("Login"):
                user = authenticate_user(email, password)
                if user:
                    st.success("Login successful!")
                    st.session_state.user = user
                else:
                    st.error("Invalid email or password")

    if st.session_state.user:
        st.write(f"Welcome, {st.session_state.user.name}")
        if st.button("Logout"):
            st.session_state.user = None
            st.experimental_rerun()

if st.session_state.user:
    messages = get_user_messages(st.session_state.user.id)
    for message in messages:
        with st.chat_message(message.type):
            st.write(message.text)

    if user_text_message := st.chat_input("Send a new message ..."):
        process(user_text_message, st.session_state.user.id)

        with st.chat_message("user"):
            st.write(user_text_message)

        with st.chat_message("ai"):
            st.write(get_edenai_response(user_text_message))