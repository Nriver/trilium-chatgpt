import markdown2
import openai
from flask import Flask, request
from trilium_py.client import ETAPI

from settings import *

# testurl
# http://127.0.0.1:5000/query?keyword=Trilium+Notes
# Change Trilium search engine to http://127.0.0.1:5000/query?keyword={keyword}

# initialization
openai.proxy = proxies
openai.api_key = openai_api_key
ea = ETAPI(server_url, token)
app = Flask(__name__)


@app.route('/query', methods=['GET'])
def query():
    keyword = request.args.get('keyword')

    # query for ChatGPT
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": keyword}
        ]
    )
    content = completion.choices[0].message.content
    print(content)

    # convert markdown to html
    html = markdown2.markdown(content, extras=['fenced-code-blocks', 'strike', 'tables', 'task_list'])
    # create a note in trilium
    ea.create_note(
        parentNoteId=note_id,
        title=keyword,
        type="text",
        content=html,
    )

    return html


if __name__ == '__main__':
    app.run()
