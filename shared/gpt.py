import requests
import yaml

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

def make_request(config, history: list):
    url = 'https://api.gilas.io/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {config["gilas"]}'
    }
    payload = {
        'model': 'gpt-3.5-turbo',
        "messages": history
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()


# sample usage

# if __name__ == "__main__":
#     d = [{"role": "user", "content": "A synonym for lofty?"}]
#     result = make_request(config, d)
#     print(result['choices'][0]['message']['content'])
