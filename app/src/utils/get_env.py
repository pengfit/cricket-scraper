# get_env.py
import os
from dotenv import load_dotenv

load_dotenv()

def get_env_vars():
    """Read environment variables GOV_MODULE and MODULE_URL"""
    gov_module = os.getenv("GOV_MODULE")
    module_url = os.getenv("MODULE_URL")
    api_key = os.getenv("API_KEY")
    api_host = os.getenv("API_HOST")
    if not gov_module or not module_url:
        raise EnvironmentError("GOV_MODULE or MODULE_URL is not set!")
    return gov_module, module_url,api_key,api_host