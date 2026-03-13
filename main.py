from fastapi import FastAPI, Request
from github_service import get_pr_files, comment_on_pr
from ai_reviewer import review_code

app = FastAPI()

@app.post("/webhook")
async def github_webhook(request: Request):

    payload = await request.json()

    if "pull_request" not in payload:
        return {"status": "ignored"}

    pr = payload["pull_request"]
    repo = payload["repository"]["name"]
    owner = payload["repository"]["owner"]["login"]
    pr_number = pr["number"]

    files = get_pr_files(owner, repo, pr_number)

    diff_text = ""

    for file in files:
        diff_text += file.get("patch", "")

    review = review_code(diff_text)

    comment_on_pr(owner, repo, pr_number, review)

    return {"status": "review posted"}

@app.get("/")
def home():
    return {"message": "PR Review Agent Running"}
