import os
from openai import OpenAI

# OPENAI_API_key set in environment variables 
client = OpenAI(api_key=os.environ.get("OPENAAI_API_KEY"))

