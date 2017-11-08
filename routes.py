@app.route('/users/')
def show_users(page):
    users = User.query.all()
    return render_template('users.html', users=users)