from fastapi import FastAPI, Request
from github_service import get_pr_files, comment_on_pr
from ai_reviewer import review_code

app = FastAPI()

from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def github_webhook(request: Request):
    body = await request.body()

    if not body:
        return {"status": "empty"}

    try:
        payload = await request.json()
    except Exception:
        return {"status": "invalid json"}

    # ✅ Only handle PR events
    if payload.get("pull_request") is None:
        return {"status": "ignored"}

    action = payload.get("action")

    # ✅ Only act on relevant actions
    if action not in ["opened", "synchronize"]:
        return {"status": f"ignored action {action}"}

    pr = payload["pull_request"]
    repo = payload["repository"]["name"]
    owner = payload["repository"]["owner"]["login"]
    pr_number = pr["number"]

    print(f"Processing PR #{pr_number} in {owner}/{repo}")

    # 🔽 Your logic (keep this)
    files = get_pr_files(owner, repo, pr_number)

    diff_text = ""
    for file in files:
        diff_text += file.get("patch", "")

    review = review_code(diff_text)

    comment_on_pr(owner, repo, pr_number, review)

    return {"status": "review posted"}
    body = await request.body()

    if not body:
        return {"status": "empty"}

    try:
        payload = await request.json()
    except Exception:
        return {"status": "invalid json"}

    # ✅ Only handle PR events
    if payload.get("pull_request") is None:
        return {"status": "ignored"}

    action = payload.get("action")

    # ✅ Only act on relevant actions
    if action not in ["opened", "synchronize"]:
        return {"status": f"ignored action {action}"}

    pr = payload["pull_request"]
    repo = payload["repository"]["name"]
    owner = payload["repository"]["owner"]["login"]
    pr_number = pr["number"]

    print(f"Processing PR #{pr_number} in {owner}/{repo}")

    # 🔽 Your logic (keep this)
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
