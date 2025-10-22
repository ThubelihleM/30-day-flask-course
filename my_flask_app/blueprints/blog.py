from flask import Blueprint, render_template, request, redirect, url_for, flash

blog = Blueprint('blog', __name__, template_folder='blog')

# In-memory storage for posts
posts = [
  {'id': 1, 'title': 'First Post', 'content': 'Welcome to my blog!'},
  {'id': 2, 'title': 'Learning Flask', 'content': 'Flask is awesome!'}
]

# Get and display all posts on the home page
@blog.route('/blog')
def blog_index():
  return render_template('blog/blog_index.html', posts=posts)

# Displat form to create and post new post
@blog.route('/blog/new', methods=['GET', 'POST'])
def new_post():
  if request.method == 'POST':
    title = request.form['title']
    content = request.form['content']
    if not title or not content:
      flash('Please fill out all fields.', 'error')
      return render_template('blog/new_post.html')
    elif len(title) < 3:
      flash('Title must be more than 3 charecters.', 'error')
      return render_template('blog/new_post.html')
    new_post = {
      'id': len(posts) + 1,
      'title': title, 
      'content': content
    }
    posts.append(new_post)
    flash('Post created successfully!', 'success')
    return redirect(url_for('blog.blog_index'))
  return render_template('blog/new_post.html')

# Get a single blog post
@blog.route('/blog/<int:id>')
def post(id):
  post = next((p for p in posts if p['id'] == id), None)
  if not post:
    flash('Post not found.', 'error')
    return redirect(url_for('blog.blog_index'))
  return render_template('blog/post.html', post=post)