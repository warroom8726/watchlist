from sys import path
from flask import Flask
from flask import url_for, request, send_from_directory
from flask.templating import render_template
from werkzeug.utils import escape, redirect
from werkzeug.utils import secure_filename
import os


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'txt', 'h', 'cpp', 'c'])
UPLOAD_FOLDER = 'D:/work/python/s/Watchlist/upload'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER #os.getcwd()
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


'''html=
<!DOCTYPE html>
<html lang="en">
	<h1>图片上传</h1>
    <form method=post enctype=multipart/form-data>
         <input type=file name=file>
         <input type=submit value=上传>
    </form>
    <footer>
        <small>&copy; 2022 <a href="https://www.baidu.com"> Baidu </a></small>
    </footer>
</html>'''

'''
@app.route('/x', methods=['GET', 'POST'])
def hello():
    file = request.files['file']
    return html
'''


html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>图片上传</h1>
    <form method=post enctype=multipart/form-data>
         <input type=file name=file>
         <input type=submit value=上传>
    </form>
    '''

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)



@app.route('/a', methods=['GET', 'POST'])
def upload_a():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_url = url_for('uploaded_file', filename=filename)
            return html + '<br><img src=' + file_url + '>'
    return html

@app.route('/b', methods=['GET', 'POST'])
def upload_b():
    if request.method == 'POST':
        file = request.files['file']
        if file :
            filename = secure_filename(file.filename)
            path = "./upload/"
            img_name = filename
            file_path = path + img_name
            file.save(file_path)
            file_url = url_for('uploaded_file', filename=filename)
            return html + '<br><img src=' + file_url + '>'
    return html




@app.route('/baidu')
def hello_redirect():
    return redirect('https://www.baidu.com')

@app.route('/local')
def hello_local():
    return redirect(url_for('func_ico'))

@app.route('/user/<name>')
def hello_name(name):
    return 'user is: %s' % escape(name)

@app.route('/ico')
def func_ico():
    return render_template('ico-ext.html', name='cwww')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    html
    img = request.files.get('file')
    path = "./upload/"
    img_name = img.filename
    file_path = path + img_name
    img.save(file_path)
    return file_path

@app.route('/upload/<uid>', methods=['POST', 'GET'])
def upload2(uid):
     #得到普通参数
    print(f"request.values:{request.values}")
    print(f"request.values.get('name'): {request.values.get('name')}")

    #得到文件类型的参数
    print(f"request.files: {request.files}")
    print(f"request.files.get('file_name'): {request.files.get('file_name')}")

    #获取上传文件的流
    #print(f"request.files.get('get_name').read(): {request.files.get('file_name').read()}")
    img = request.files.get('file_name')
    img_path = './upload/'
    img_path += uid
    img_path += '/'
    if (os.path.exists(img_path)):
        print(f"exist!")
    else:
        os.makedirs(img_path)

    #img_name = uid
    #img_name += img.filename
    img_name = img.filename
    file_path = img_path + img_name

    img.save(file_path)

    return file_path

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)  # 使其他主机可以访问服务




