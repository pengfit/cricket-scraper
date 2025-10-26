import requests

class DifyAPIClient:
    def __init__(self, base_url: str, api_key: str, logger):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.logger = logger
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        })

    def run_workflow(self, values: str, gov_module: str, timeout: int = 30):
        url = f"{self.base_url}/v1/workflows/run"
        payload = {
            "inputs": {
                "values": values,
                "module": gov_module
            },
            "user": gov_module
        }
        try:
            self.logger.info(f"➡️ Sending workflow request for module: {gov_module}")
            response = self.session.post(url, json=payload, timeout=timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            self.logger.error(f"❌ Dify API error for {gov_module}: {e}")
            return None

    def close(self):
        """Close the session when done"""
        self.session.close()
