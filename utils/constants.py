import json
import os
from dotenv import load_dotenv
load_dotenv()

class Base:
    @staticmethod
    def import_json(path):
        with open(path) as json_file:
            return json.load(json_file)
        
    ACCESS_TOKEN_HF = os.getenv("ACCESS_TOKEN_HF")
    model_id = "mistralai/Mistral-7B-Instruct-v0.2"
    llm_params = dict(
        temperature=0.1,
        max_new_tokens=5000,
    )
    path_creed = "../jsons/creed_jiump.json"
    path_prompts = "../jsons/prompts.json"

    creed_jiump_json = import_json(path_creed)
    prompt_biblical_plan_template = import_json(path_prompts)["biblical-plan"]
    prompt_correction_template = import_json(path_prompts)["correction"]