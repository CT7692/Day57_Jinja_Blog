from flask import Flask, render_template
from security import safe_requests
from post import Post


app = Flask(import_name="blogs")
JSON = safe_requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()


def get_blog_list():
    blogs = []
    for i in JSON:
        post = Post(i['body'], i['title'], i['subtitle'])
        blogs.append(post)
    return blogs

@app.route('/')
def home():
    blogs = get_blog_list()

    return render_template("index.html",blogs=blogs)


@app.route('/blog/<index>')
def blog_post(index):
    array_index = int(index) - 1
    return render_template("post.html", blog=JSON[array_index], index=index)


if __name__ == "__main__":
    app.run(debug=True)