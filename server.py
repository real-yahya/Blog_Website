import flask
import requests

app = flask.Flask(__name__)


@app.route('/')
def home():
    blog = requests.get(" https://api.npoint.io/c790b4d5cab58020d391")
    blog_data = blog.json()
    blogs = len(blog_data)
    return flask.render_template("index.html", blog_data=blog_data, blogs=blogs, id=blog_data)


@app.route('/post/<blog_id>')
def blog(blog_id):
    blog = requests.get(" https://api.npoint.io/c790b4d5cab58020d391")
    blog_title = blog.json()[int(blog_id)-1]['title']
    blog_subtitle = blog.json()[int(blog_id)-1]['subtitle']
    blog_body = blog.json()[int(blog_id)-1]['body']
    return flask.render_template('post.html', body=blog_body, title=blog_title, subtitle=blog_subtitle)


if __name__ == "__main__":
    app.run(debug=True)
