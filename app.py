from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    filenames = os.listdir('.')
    return render_template('index.html', filenames=filenames)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(file.filename)
    return redirect(url_for('index'))

@app.route('/<filename>.html')
def view_html(filename):
    file_path = os.path.join(os.getcwd(), filename + '.html')
    if not os.path.exists(file_path):
        return 'File not found.', 404
    with open(file_path, 'r') as file:
        html_content = file.read()
    return html_content

if __name__ == '__main__':
    app.run(debug=True)
