# get_env.py
import os
import logging


def get_env_vars():
    """Read environment variables GOV_MODULE and MODULE_URL"""
    gov_module = os.environ.get("GOV_MODULE")
    module_url = os.environ.get("MODULE_URL")
    reports_dir = os.environ.get("REPORTS_DIR")
    api_key = os.environ.get("API_KEY")
    if not gov_module or not module_url:
        raise EnvironmentError("GOV_MODULE or MODULE_URL is not set!")
    return gov_module, module_url, f'{reports_dir}/{gov_module}/reports',api_key