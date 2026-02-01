from flask import Flask, request, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/blog')
def blog():
    blog_id = request.args.get('blog_id')
    return f'博客id是: {blog_id}'

@app.get('/re')
def re():
    return redirect('https://www.baidu.com')


if __name__ == '__main__':
    app.run(debug=True)
