import requests

def get_github_repos(username, token=None):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {'Accept': 'application/vnd.github.v3+json'}
    if token:
        headers['Authorization'] = f'token {token}'

    response = requests.get(url, headers=headers)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
    return response.json()

get_github_repos("rays63")  # Replace with your GitHub username
