import requests
from personal_keys import openai_api_key

# REF: https://platform.openai.com/docs/api-reference/completions

def calculator_promt():
    response = requests.post(
        url="https://api.openai.com/v1/completions",  # api endpoint
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai_api_key}",
        },
        json={
            "model": "text-davinci-003",  # ML model to use
            "prompt": "Write a calculator in Python",
            "max_tokens": 100,  #
            "temperature": 0.5,  # "creativeness"
        },
    )
    assert response.status_code == 200
    return response.json()["choices"][0]["text"]

if __name__ == "__main__":
    pass
