# import streamlit as st
# from sqlmodel import Field, Session, SQLModel, create_engine, select, Relationship
# from models import User, Message



# @st.cache_resource
# def database_connection():
#     engine = create_engine("sqlite:///database.db")
#     SQLModel.metadata.create_all(engine)
#     return engine

# engine = database_connection()

# def ai(user_text_message):
#     ai_text_message = user_text_message * 3
#     return ai_text_message
    

# def process(user_text_message):

#     ai_text_message = ai(user_text_message)

#     user_message = Message(text=user_text_message, type="user", user_id=1)
#     ai_message = Message(text=ai_text_message, type="ai", user_id=1)




#     # backend



#     with Session(engine) as session:
#         session.add(user_message)
#         session.add(ai_message)
#         session.commit()



#     # frontend
#     st.session_state.messages.append({'type': 'user', 'text': user_text_message})
#     st.session_state.messages.append({'type': 'ai', 'text': ai_text_message})  
#     return ai_text_message

# if "messages" not in st.session_state:
#     st.session_state.messages = []


# for message in st.session_state.messages:
#     with st.chat_message(message["type"]):
#         st.write(message["text"])





# if user_text_message := st.chat_input("Send a new message ..."):

#     ai_text_message = process(user_text_message)


#     with st.chat_message("User"):
#         st.write(user_text_message)

#     with st.chat_message("ai"):
#         st.write(ai_text_message)



import streamlit as st
from sqlmodel import Session
from models import User, Message
from database import create_db_and_tables, engine, create_user, authenticate_user, select


# Initialize database
create_db_and_tables()

@st.cache_resource
def database_connection():
    return engine

engine = database_connection()

def ai(user_text_message):
    ai_text_message = user_text_message * 3
    return ai_text_message

def process(user_text_message, user_id):
    ai_text_message = ai(user_text_message)
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
            st.write(ai(user_text_message))
