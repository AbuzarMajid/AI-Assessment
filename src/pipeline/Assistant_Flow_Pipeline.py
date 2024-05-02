import sys
from logger import logging
from exceptions import CustomExcetions
from openai import OpenAI
from src.pipeline.Function_Calling_pipeline import FunctionCallingPipeline
from src.components.Create_Run import CreateRun
from src.components.Messages import Messages
from src.components.Assisstant_Definition import Assistants
import time

class AssistantFlow:
    def __init__(self, client: OpenAI, model_name, difficulty_level, category, number_of_questions, skill_name):
        self.client = client
        self.model_name = model_name 
        self.role = "user"
        self.difficulty_level = difficulty_level
        self.category = category
        self.number_of_questions = number_of_questions
        self.skill_name = skill_name
    
    def assisstant_flow(self):
        try:
            assistant_obj = Assistants(client=self.client, model_name=self.model_name, skill_name=self.skill_name)
            thread_id, assisstant_id = assistant_obj.question_generation()

            content = f"Generate {self.number_of_questions} {self.difficulty_level} questions for the category {self.category}. Make sure to include query and table if needed only. Make sure no questions would take more than 2.5 minutes to answer"
            
            create_message = Messages(client=self.client, thread_id=thread_id)
            message = create_message.create_messages(role=self.role, content=content)
            logging.info('Message created in thread successfully')
            
            create_run = CreateRun(assistant_id=assisstant_id, thread_id=thread_id, client=self.client)
            run = create_run.create_run()
            logging.info('Run created successfully')

            status = True

            while status:
                retrieved_run = create_run.retrieve_run(run_id=run.id)
                logging.info('Run retrieved successfully')
                logging.info(f'Status: {retrieved_run.status}')

                if retrieved_run.status in ['queued', 'in_progress']:
                    time.sleep(3)
                    
                    continue

                elif retrieved_run.status == 'requires_action':
                    if retrieved_run.required_action.submit_tool_outputs.tool_calls[0].function.name == "finish_session":
                        return "Thanks"
                    
                    else:
                        function_calling_obj = FunctionCallingPipeline(run_retrieved=retrieved_run,
                                                                    client=self.client,
                                                                    run_id=run.id,
                                                                    thread_id=thread_id,
                                                                    model_name=self.model_name,
                                                                    skill_name=self.skill_name
                                                                    )
                        function_calling_obj.function_calling()
                        continue

                elif retrieved_run.status == 'completed':

                    show_message = create_message.show_messages()
                    logging.info('Successfully shown message')
                    status = False
                    return (show_message)

                elif retrieved_run.status in ['cancelling', 'cancelled', 'failed', 'expired']:
                    user_message = f'Run Status: {retrieved_run.status}'
                    logging.info(user_message)
                    return user_message
                

                break
                
        except Exception as e:
            raise CustomExcetions(e, sys)