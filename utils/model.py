import pandas as pd
from langchain_community.llms import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from constants import Base

class BiblicPlan(Base):
    def __init__(self) -> None:
        super().__init__()
    
    @property
    def llm_model(self):
        return (
            HuggingFaceEndpoint(
                repo_id=self.model_id,
                huggingfacehub_api_token=self.ACCESS_TOKEN_HF,
                **self.llm_params
                )
        )

    @property
    def chain_corrected_biblical_plan(self):
        prompt_biblical_plan_template = self.prompt_biblical_plan_template
        prompt_correction_template = self.prompt_correction_template
        llm = self.llm_model

        prompt_biblical_plan = PromptTemplate(
            input_variables=["creed_jiump", "personal_info"], 
            template=prompt_biblical_plan_template
            )
        prompt_correction = PromptTemplate(
            input_variables=["biblical_plan"], 
            template=prompt_correction_template
            )
        
        return (
            {
                "biblical_plan": (
                    prompt_biblical_plan 
                    | llm
                    ),
                }
                | prompt_correction
                | llm
                )
    

    def personal_info(self, **kwargs):
        weeks_plan = 4 * kwargs["months"]

        if kwargs["age"] or kwargs["age"] is not None:
            age = kwargs["age"]
        else:
            age ? ""


        """I need to create a personalized biblical plan for 18 weeks for Juan. Juan is a 22-year-old man characterized by the following points:
        1) He has an advanced knowledge of the Bible.
        2) He studies Engineering at university.
        3) He has been a Christian for 10 years so is not a new christian."""


    def get_biblical_plan(self):
        creed_jiump_json = self.creed_jiump_json
        creed_jiump = f"{creed_jiump_json["trinity"]}\n{creed_jiump_json["jesus"]}\n{creed_jiump_json["holy_spirit"]}\n{creed_jiump_json["sola_scriptura"]}"