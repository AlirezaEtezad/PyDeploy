# from typing import Optional
# from sqlmodel import Field, Session, SQLModel, create_engine, select, Relationship




# # st.session_state.messages = []

# # if user_text_message := st.chat_input("Send a new message: ..."):
# #     with st.chat_message["type"]:
# #         st.session_state.messages.append({'type': 'user', "text": user_text_message})
# #         st.session_state.messages.append({'type': 'ai', "text": "ai feedback"})

# #         st.write(user_text_message)
# #     with st.chat_message("ai"):
# #         st.write("greetings")

# class User(SQLModel, table=True):
#     __table_args__ = {'extend_existing': True}
#     id : Optional[int] = Field(default=None, primary_key=True)
#     name: str
#     email: str
#     pasword: Optional[str]

#     messages: list["Message"] = Relationship(back_populates="user")




# class Message(SQLModel, table=True):
#     __table_args__ = {'extend_existing': True}
#     id : Optional[int] = Field(default=None, primary_key=True)
#     text: str
#     type: str

#     user_id: int = Field(default=None, foreign_key="user.id")

#     user: User = Relationship(back_populates= "messages")



from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(SQLModel, table=True):
    __tablename__ = 'users'
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    hashed_password: str

    messages: List["Message"] = Relationship(back_populates="user")

    def set_password(self, password: str):
        self.hashed_password = pwd_context.hash(password)

    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.hashed_password)


class Message(SQLModel, table=True):
    __tablename__ = 'messages'
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    type: str
    user_id: int = Field(default=None, foreign_key="users.id")

    user: User = Relationship(back_populates="messages")
