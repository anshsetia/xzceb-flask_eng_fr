from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")

def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    french_text = translator.englishtofrench(textToTranslate)
    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    english_text = translator.frenchtoenglish(textToTranslate)
    return english_text

@app.route("/")
def renderIndexPage():
    return render_template('index.html')
    # Write the code to render template

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port=8080)

