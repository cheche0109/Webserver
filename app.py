from flask import Flask, request, render_template
import main

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    name='Here is a test'
    return render_template('index.html', name=name)

@app.route('/submit-files', methods=['POST'])
def submit_files():

    if request.files['file1'].filename and request.files['file2'].filename != '':
        file1 = request.files['file1']
        file2 = request.files['file2']

        file1.save(file1.filename)
        file2.save(file2.filename)

        result = main.main(file1.filename, file2.filename)


    elif request.files['file1'].filename != '' and request.files['file2'].filename == '':
        file1 = request.files['file1']
        file1.save(file1.filename)

        text2 = request.form['PRO']
        with open('file2', 'w') as f:
            f.write(text2)

        result = main.main(file1.filename, 'file2')

    elif request.files['file1'].filename == '' and request.files['file2'].filename != '':
        text1 = request.form['SM']
        with open('file1', 'w') as f:
            f.write(text1)

        file2 = request.files['file2']
        file2.save(file2.filename)

        result = main.main('file1', file2.filename)

    
    else:
        text1 = request.form['SM']
        with open('file1', 'w') as f:
            f.write(text1)

        text2 = request.form['PRO']
        with open('file2', 'w') as f:
            f.write(text2)

        result = main.main('file1', 'file2')

    return result

if __name__ == '__main__':
    app.run(debug=True)