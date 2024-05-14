from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/85e69c335fbe7d4809fb"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/blog/<int:num>")
def blog(num):
    print(num)
    blog_url = "https://api.npoint.io/85e69c335fbe7d4809fb"
    response = requests.get(blog_url)
    all_posts = response.json()
    post = all_posts[num]
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)