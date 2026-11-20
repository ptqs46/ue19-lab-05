import requests

URL = "https://v2.jokeapi.dev/joke/Any?safe-mode"


def get_joke():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    data = response.json()
    if data["type"] == "single":
        return data["joke"]
    return f"{data['setup']}\n{data['delivery']}"


if __name__ == "__main__":
    try:
        print(get_joke())
    except requests.RequestException as e:
        print(f"Erreur lors de l'appel à l'API : {e}")
