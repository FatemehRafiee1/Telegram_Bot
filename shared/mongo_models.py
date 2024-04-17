from mongoengine import Document, StringField, IntField, ListField, ReferenceField, EmbeddedDocument, EmbeddedDocumentField

class User(Document):
    uid = IntField(required=True, unique=True)
    name = StringField(required=True)
    # gpt_history = ListField(StringField())
    # Define meta information
    meta = {
        "collection": "dragon_users"  # Specify the collection name 
    }

class Message(EmbeddedDocument):
    # user_id = ReferenceField(User, required=True)
    role = StringField(required=True)
    content = StringField(required=True)


class ChatSession(Document):
    user_instance = ReferenceField(User, required=True)
    messages = ListField(EmbeddedDocumentField(Message))

    meta = {
        "collection": "dragon_chat_sessions"
    }

class Question(Document):
    qid = IntField(required=True, unique=True)
    topic = StringField(required=True)
    question = StringField(required=True)

    meta = {
        "collection": "ielts_questions" 
    }
