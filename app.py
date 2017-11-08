#!flask/bin/python
from flask import Flask, render_template, request
from forms import SearchForm
from models import ScrapePage

app = Flask(__name__)
app.debug = True
app.secret_key = 's3cr3t'

@app.route('/login')
def login():
    return 'login'

@app.route('/', methods = ['GET', 'POST'])
def index():
	form = SearchForm()
	if request.method == 'POST':
		term = form.search.data
		page = ScrapePage()
		items = page.query(term)

		return render_template('torrent-list.html', form = form, items = items)

@app.route('/search', methods=['POST'])
def search():
	term = form.search.data
	page = ScrapePage()
	items = page.query(term)

if __name__ == '__main__':
    app.run(debug=True)