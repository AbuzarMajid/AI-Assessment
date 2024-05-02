from openai import OpenAI
from exceptions import CustomExcetions
from logger import logging
import sys

class Messages:
    def __init__(self, client: OpenAI, thread_id, role, content):
        self.client = client
        self.thread_id = thread_id
        self.role = role
        self.content = content
        
    def create_messages(self):
        try:
            message = self.client.beta.threads.messages.create(
            thread_id=self.thread_id,
            role=self.role,
            content=self.content
            )
            return message.id
        except Exception as e:
            print(e)
            raise e
        
    def show_messages(self):
        try:
            messages = self.client.beta.threads.messages.retrieve(
            message_id=self.create_messages(),
            thread_id= self.thread_id)
            response = (messages)
            logging.info('Successfully retrieved message')
            return (response)
        except Exception as e:
            raise CustomExcetions(e, sys)
        
    