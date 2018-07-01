from flask import render_template, request, redirect, url_for, abort, flash
from flask_login import login_required, current_user
import secrets
import os
from app import db
from app.email import mail_message
from app.main.forms import UpdateAccountForm, PostForm, SubscribeForm, CommentForm
from app.models import User, Post, Subscription, Comments
from manage import app
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    """
    View root page function that returns the index page and its data
    """

    title = 'Home'
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=4)

    form = SubscribeForm()
    if form.validate_on_submit():
        email = Subscription(email=form.email.data)
        db.session.add(email)
        db.session.commit()
    return render_template('index.html', title=title, posts=posts, form=form)
@main.route('/about')
def about():
    title = 'About Us'

    return render_template('about.html', title=title)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile/', picture_fn)
    form_picture.save(picture_path)
    current_user.image_file = picture_fn
    image_file = url_for('static', filename='profile/' + current_user.image_file)


@main.route("/user", methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('main.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile/' + current_user.image_file)
    return render_template('profile/profile.html', title='Account', image_file=image_file, form=form)
@main.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    if current_user.username != 'Keith Mzaza':
        abort(403)

    form = PostForm()

    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        subs = Subscription.query.all()
        for sub in subs:
            mail_message("New ", "email/welcome_user", sub.email)

        return redirect(url_for('main.index'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')
