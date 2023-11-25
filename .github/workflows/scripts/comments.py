import os, requests

pr_number, repo = os.getenv("PR_NUMBER"), os.getenv("GITHUB_REPO")
token, api_url = os.getenv("GITHUB_TOKEN"), f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
comment_body = f"Docs are available at: [https://pr-{pr_number}.docs.mekstack.ru](https://pr-{pr_number}.docs.mekstack.ru)"

if "github-actions[bot]" not in [c['user']['login'] for c in requests.get(api_url, headers={"Authorization": f"token {token}"}).json():
    requests.post(api_url, headers={"Authorization": f"token {token}"}, json={"body": comment_body})
