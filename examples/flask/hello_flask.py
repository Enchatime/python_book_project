from flask import Flask, render_template, request, escape #redirect - module for redirect to another url
from examples.def_ex import search4letters

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as logs:
        print(req.form, req.remote_addr, req.user_agent, res, file=logs, sep="|")


@app.route('/search4', methods=['POST'])
def search() -> str:
    title = 'Here are you results:'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_results=results,
                           the_letters=letters,
                           the_title=title,
                           the_phrase=phrase,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome')


@app.route('/viewlog')
def view_logs() -> str:
    with open('vsearch.log', 'r') as log:
        contents = log.read()
    return escape(contents)


if __name__ == '__main__':
    app.run(debug=True)
