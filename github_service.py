import requests
from config import GITHUB_TOKEN

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_pr_files(owner, repo, pr_number):

    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"

    response = requests.get(url, headers=headers)

    return response.json()


def comment_on_pr(owner, repo, pr_number, comment):

    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments"

    data = {
        "body": comment
    }

    requests.post(url, headers=headers, json=data)
