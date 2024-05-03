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
                    temperature=0.2,
                    response_format= { "type": "json_object" }
                )
                sql_assistant_id = assistant.id
                return sql_assistant_id

            if self.skill_name == "python":
                assistant = self.client.beta.assistants.create(
                    instructions=Prompts.python_assisstant_instructions,
                    name="Python Question generation",
                    tools=[function_calling_tools.generate_easy_questions, function_calling_tools.generate_medium_questions, function_calling_tools.generate_advanced_level_questions],
                    model=self.model_name,
                    temperature=0.2,
                    response_format= { "type": "json_object" }
                )
                python_assistant_id = assistant.id
                return python_assistant_id

            if self.skill_name == "ml":
                assistant = self.client.beta.assistants.create(
                    instructions=Prompts.ML_assistant_instructions,
                    name="ML Question generation",
                    tools=[function_calling_tools.generate_easy_questions, function_calling_tools.generate_medium_questions, function_calling_tools.generate_advanced_level_questions],
                    model=self.model_name,
                    temperature=0.2,
                    response_format= { "type": "json_object" }
                )
                ml_assistant_id = assistant.id
                return ml_assistant_id

            if self.skill_name == "statistics":
                assistant = self.client.beta.assistants.create(
                    instructions=Prompts.statistics_assisstant_instructions,
                    name="SQL Question generation",
                    tools=[function_calling_tools.generate_easy_questions, function_calling_tools.generate_medium_questions, function_calling_tools.generate_advanced_level_questions],
                    model=self.model_name,
                    temperature=0.4,
                    response_format= { "type": "json_object" }
                )
                statistics_assistant_id = assistant.id
                return statistics_assistant_id
                
        except Exception as e:
            raise CustomExcetions(e, sys)
        
    def fetch_assisstant_id(self):
        if self.skill_name == "sql":
            thread = self.client.beta.threads.create()
            return thread.id, "asst_rCkqSH8D3rTRL9U7k29WlkKM"
        
        if self.skill_name == "python":
            thread = self.client.beta.threads.create()
            return thread.id, 'asst_rJKprAt1CfkgINDeSEMWuKGP'
        
        if self.skill_name == "ml":
            thread = self.client.beta.threads.create()
            return thread.id, 'asst_5ybd58oa52cFV8IVyczOfe9K'
        
        if self.skill_name == "statistics":
            thread = self.client.beta.threads.create()
            return thread.id, 'asst_vGxuHyE6l7YCXpZdmxAFmlJy'

        

        

            

