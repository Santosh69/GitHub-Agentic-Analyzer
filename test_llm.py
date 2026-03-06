import requests


def test_llm():
    response = requests.post(
        "http://localhost:11434/api/generate",
        json= {
            "model": "llama3.2:3b",
            "prompt": "explain what is a Github Repo and how can I start one?",
            "stream" : False
        }
    )

    print(response.json()["response"])


test_llm()