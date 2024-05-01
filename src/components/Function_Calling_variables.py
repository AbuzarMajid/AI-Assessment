from openai import OpenAI
from logger import logging
import sys
from exceptions import CustomExcetions

class FunctionCalling:
    def __init__(self, client:OpenAI, run_retrieved):
        self.run_retrieved = run_retrieved
        self.client = client
    
    def function_name(self):
        # everytime when the function calling will be called the status will change to requires action
        try:
            function_name = self.run_retrieved.required_action.submit_tool_outputs.tool_calls[0].function.name
            logging.info('function name retrieved')
            return function_name
        except Exception as e:
            raise CustomExcetions(e, sys)
    
    def _tool_call_id(self):
        try:
            tool_call_id = self.run_retrieved.required_action.submit_tool_outputs.tool_calls[0]
            logging.info('Tool Call ID retrieved')
            return tool_call_id.id
        except Exception as e:
            raise CustomExcetions(e, sys)

    def submit_tool_output(self, thread_id, function_response, run_id):
        try:
            run = self.client.beta.threads.runs.submit_tool_outputs(
            thread_id=thread_id,
            run_id=run_id,
            tool_outputs=[
                {
                    "tool_call_id": self._tool_call_id(),
                    "output": function_response
                }
            ],
        )   
            logging.info("Successfully Function Response Submitted")
            return run.status
        except Exception as e:
            raise CustomExcetions(e, sys)