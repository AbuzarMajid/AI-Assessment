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
    def __init__(self, client: OpenAI, model_name):
        self.client = client
        self.model_name = model_name 
        self.role = "user"
    
    def assisstant_flow(self, difficulty_level, category, number_of_questions, skill_name):
        try:
            assistant_obj = Assistants(client=self.client, model_name=self.model_name, skill_name=skill_name)
            thread_id, assisstant_id = assistant_obj.question_generation()

            if skill_name == "sql":
                content = f"Generate {number_of_questions} {difficulty_level} questions for the category {category}. Make sure to include query and table if needed only. Answer type must only be coding or/and Audio-Video explanation. Use different answer types for different questions. For audio/video answers question should not take more than 2.5 mins to answer. For coding type questions give enough time to candidate so that he can figure out the solution"
            if skill_name == "python":
                content = f"Generate {number_of_questions} {difficulty_level} questions for the category {category}. Make sure to include code snippet if needed. Answer type must only be coding or/and Audio-Video explanation. Use different answer types for different questions."
            if skill_name == "statistics":
                content = f"Generate {number_of_questions} {difficulty_level} questions for the category {category}. Make sure no questions would take more than 2.5 minutes to answer. Answer type must only be Audio-Video explanation strictly."
            if skill_name == "ml":
                content = f"Generate {number_of_questions} {difficulty_level} questions for the category {category}. Make sure no questions would take more than 2.5 minutes to answer. Answer type must only be Audio-Video explanation strictly."


            create_message = Messages(client=self.client, thread_id=thread_id)
            create_message.create_messages(role = self.role, content = content)
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
                                                                    skill_name=skill_name
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