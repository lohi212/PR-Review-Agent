from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def review_code(diff):

    prompt = f"""
You are a senior software engineer performing a code review.

Analyze this pull request diff and identify:

1. Bad logging (console.log etc)
2. Naming issues
3. Performance issues
4. Missing error handling
5. General best practices

Respond with a clear review summary.

Code diff:
{diff}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
