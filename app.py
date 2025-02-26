# ch03/app.py

from flask import Flask, request, render_template
import openai
import config

app = Flask(__name__)

# API Token
openai.api_key = config.OPENAI_API_KEY

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        code = request.form["code"]
        error = request.form["error"]

        error_prompt = (f"Explain the error in this code without fixing it:"
                        f"\n\n{code}\n\nError: \n\n{error}")
        
        model = "gpt-4o-mini"

        explanation_completion = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", 
                 "content": (
                     f"You are a senior software engineer expert in code review.\n"
                     f"You are passionate about coding and have a knack for explaining complex concepts in an easy-to-understand manner.\n"
                 )},
                 {
                     "role": "user",
                     "content": (f"{error_prompt}")
                 },
            ],
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.2,
        )

        explanation = explanation_completion.choices[0].message.content.strip()

        fix_code_prompt = (f"Fix this code: \n\n{code}\n\nError: \n\n{error}."
                           f"\n Respond only with the fixed code. Do not include any text or comments.")
        
        fix_code_completion = openai.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a senior software engineer expert in code review.\n"
                        "You are passionate about coding and have a knack for writing clean, efficient,\n"
                        "maintainable, and documented code.\n"
                    )
                },
                {
                    "role": "user",
                    "content": (f"{fix_code_prompt}")
                },
            ],
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.2,
        )

        fixed_code = fix_code_completion.choices[0].message.content.strip()

        return render_template("index.html", 
                               explanation=explanation, 
                               fixed_code=fixed_code)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
