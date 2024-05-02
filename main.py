from fastapi import FastAPI 
from pydantic import BaseModel, StringConstraints
from src.pipeline.Assistant_Flow_Pipeline import AssistantFlow
from openai import OpenAI
import os
import json
from src.utils import categories
from logger import logging
import sys
from exceptions import CustomExcetions
from dotenv import load_dotenv
from src.constants import models
import concurrent.futures
from typing import Annotated
import concurrent.futures
load_dotenv()

api_key = os.getenv("OPEN_AI_KEY")
client = OpenAI(api_key=api_key)

class AssistantResponseRequest(BaseModel):
    difficulty: Annotated[str, StringConstraints(min_length=1, strict=True)]
    number_of_questions: int = 2
    skill_list: list

app = FastAPI()

@app.post("/v1/questions_generation")
async def questions_generation(request: AssistantResponseRequest):
    try:
        responses = []
    # Assuming this block of code is within a function or method
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for skill in request.skill_list:
                category = categories(skill_name=skill, number_of_questions=request.number_of_questions)
                assistant_obj = AssistantFlow(client=client, model_name=models[1], 
                                            difficulty_level=request.difficulty, 
                                            category=category, 
                                            number_of_questions=request.number_of_questions, 
                                            skill_name=skill)
                future = executor.submit(assistant_obj.assisstant_flow)
                futures.append(future)

            # Wait for all tasks to complete
            for future in (futures):
                response = future.result()
                responses.append(response)
                # responses.extend(response)
            

        return responses
    
    except Exception as e:
        return CustomExcetions(e, sys)

        


        
        
