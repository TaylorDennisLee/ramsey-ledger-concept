from flask import Flask, url_for
from flask import render_template
app = Flask(__name__)
from DB import object_map, departmentize_db

@app.route('/')
def home():
    return render_template('home_ii.html')

@app.route('/title/')
@app.route('/title/<title>/')
def title(title=None):
    entry = object_map[title]

    return render_template('ItemEntries_ii.html', entry=entry)

@app.route('/about/')
def about():
    return render_template('about_ii.html')

@app.route('/departments/')
def departments():
    def title_row(row):
        return row['title']
    dept_db = departmentize_db(object_map.values())
    return render_template('departments_ii.html', departments=dept_db,
                           sorted=sorted, title_row=title_row)

@app.route('/wishlists/')
def wishlists():
    return render_template('wishlists_ii.html')

@app.route('/documents/')
def documents():
    return render_template('documents_ii.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
