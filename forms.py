from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(Form):
  search = StringField('search', [DataRequired()])
  submit = SubmitField('Search',
                       render_kw={'class': 'btn btn-success btn-block'})