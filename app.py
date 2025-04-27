from flask import Flask, render_template, request
from langchain_utils import generate_summary, match_summary_with_article, highlight_summary_and_article
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        full_text = request.form['article']

        # توليد الملخص
        arabic_summary = generate_summary(full_text)

        # مطابقة الجمل
        matches = match_summary_with_article(full_text, arabic_summary)

        # تلوين
        highlighted_summary, highlighted_article = highlight_summary_and_article(full_text, arabic_summary, matches)

        return render_template('summary.html',
                               arabic_summary=arabic_summary,
                               highlighted_article=highlighted_article,
                               highlighted_summary=highlighted_summary)

    return render_template('form.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
