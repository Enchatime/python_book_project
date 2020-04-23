from flask import Flask, render_template, request #redirect - module for redirect to another url
from examples.def_ex import search4letters

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def search() -> str:
    title = 'Here are you results:'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           the_results=results,
                           the_letters=letters,
                           the_title=title,
                           the_phrase=phrase,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome')


if __name__ == '__main__':
    app.run(debug=True)
