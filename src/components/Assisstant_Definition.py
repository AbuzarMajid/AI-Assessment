import sys
from openai import OpenAI
from exceptions import CustomExcetions
from logger import logging
from src.constants import Prompts, FunctionCallingTools

class Assistants:
    def __init__(self, client: OpenAI, model_name, skill_name):
        self.client = client
        self.model_name = model_name
        self.skill_name = skill_name

    def question_generation(self):
        try:
            function_calling_tools = FunctionCallingTools()
            #defining an assisstant

            if self.skill_name == "sql":
                assistant = self.client.beta.assistants.create(
                    instructions=Prompts.SQL_assisstant_instructions,
                    name="SQL Question generation",
                    tools=[function_calling_tools.generate_easy_questions, function_calling_tools.generate_medium_questions, function_calling_tools.generate_advanced_level_questions],
                    model=self.model_name,
                    temperature=0.4,
                    response_format= { "type": "json_object" }
                )
                assistant_id = assistant.id

            if self.skill_name == "python":
                assistant = self.client.beta.assistants.create(
                    instructions=Prompts.python_assisstant_instructions,
                    name="SQL Question generation",
                    tools=[function_calling_tools.generate_easy_questions, function_calling_tools.generate_medium_questions, function_calling_tools.generate_advanced_level_questions],
                    model=self.model_name,
                    temperature=0.4,
                    response_format= { "type": "json_object" }
                )
                assistant_id = assistant.id

            if self.skill_name == "ml":
                assistant = self.client.beta.assistants.create(
                    instructions=Prompts.ML_assistant_instructions,
                    name="SQL Question generation",
                    tools=[function_calling_tools.generate_easy_questions, function_calling_tools.generate_medium_questions, function_calling_tools.generate_advanced_level_questions],
                    model=self.model_name,
                    temperature=0.4,
                    response_format= { "type": "json_object" }
                )
                assistant_id = assistant.id

            if self.skill_name == "statistics":
                assistant = self.client.beta.assistants.create(
                    instructions=Prompts.statistics_assisstant_instructions,
                    name="SQL Question generation",
                    tools=[function_calling_tools.generate_easy_questions, function_calling_tools.generate_medium_questions, function_calling_tools.generate_advanced_level_questions],
                    model=self.model_name,
                    temperature=0.4,
                    response_format= { "type": "json_object" }
                )
                assistant_id = assistant.id
            
            logging.info(f'{self.skill_name} Assistant defined')

            #defining a thread for that assistant
            thread = self.client.beta.threads.create()
            thread_id = thread.id
            logging.info('Thread defined for JD given assisatant')
            return thread_id, assistant_id
        
        except Exception as e:
            raise CustomExcetions(e, sys)