# 🤖 GitHub PR Review Agent

An AI-powered agent that automatically reviews GitHub Pull Requests and provides feedback on code quality, logging practices, naming conventions, and documentation.

The agent listens to GitHub webhook events and analyzes the Pull Request using an LLM to generate structured review comments.


## 🚀 Features

- 🔍 Automated Pull Request reviews

- 📝 Checks for logging best practices

- 📛 Enforces naming conventions

- 💬 Comments directly on PRs

- ⚡ FastAPI webhook server

- 🤖 LLM-powered code analysis

- 🔗 Easy integration with GitHub repositories


## 🏗 Architecture

```
GitHub PR Event
      │
      ▼
GitHub Webhook
      │
      ▼
FastAPI Server
      │
      ▼
PR Code Fetcher
      │
      ▼
AI Review Engine
      │
      ▼
GitHub Review Comment
```

## ⚙️ Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/pr-review-agent.git
cd pr-review-agent
```

### 2️⃣ Create Virtual Environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Add Environment Variables

```
OPENAI_API_KEY=your_api_key
GITHUB_TOKEN=your_github_token
```

### 5️⃣ Running the Server

```
uvicorn main:app --reload
```

Server will start at:
```
http://127.0.0.1:8000
```

### 6️⃣ Expose Local Server to GitHub

Use ngrok to expose your webhook endpoint.
```
ngrok http 8000
```

You will get a public URL like:
```
https://abcd1234.ngrok-free.app
```

### 7️⃣ 🔗 Configure GitHub Webhook

In your GitHub repository:
```
Settings → Webhooks → Add Webhook
```

Set the following fields
payload URL:
```
https://your-ngrok-url/webhook
```

Select events:
```
Pull Request
```

Content type:
```
application/json
```

🧠 How the Agent Reviews Code

- When a Pull Request is opened or updated:

- GitHub sends a webhook event

- FastAPI receives the event

- PR code changes are fetched using GitHub API

- The code is sent to the AI review engine

- The AI generates feedback

- Comments are posted on the PR