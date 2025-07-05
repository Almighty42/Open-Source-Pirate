from flask import redirect, render_template, flash, request
from app.admin import bp
from app.admin.forms import LoginForm

@bp.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate() and form.password.data == 'pass123':
        flash('Admin login requested!')
        flash('Password data - {}'.format(form.password.data))
        return redirect('/')
    return render_template("login.jinja", title="Login", form=form)
