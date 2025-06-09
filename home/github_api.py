import requests

def get_github_repos(username, token=None, sort='updated', per_page=6):
    headers = {
        'Accept': 'application/vnd.github.v3+json'
    }
    if token:
        headers['Authorization'] = f'token {token}'

    url = f"https://api.github.com/users/{username}/repos"
    params = {
        'sort': sort,
        'per_page': per_page
    }

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        repos = response.json()
        return repos
    else:
        return []
