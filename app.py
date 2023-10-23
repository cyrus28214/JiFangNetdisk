from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
app = Flask(__name__)
directory_path = './static/files/'
template_vars = ('os', 'directory_path')

for i in template_vars:
    app.jinja_env.globals[i] = eval(i)

@app.route('/', methods = ['GET'])
@app.route('/<path:path>', methods = ['GET'])
def browse(path = ''):
    print(path)
    local_path = os.path.join(directory_path, path)
    if os.path.isdir(local_path):
        return render_template('browse.j2', path=path)
    if os.path.isfile(local_path):
        return send_from_directory('', local_path)
    return redirect('/')

@app.route('/', methods = ['POST'])
@app.route('/<path:path>', methods = ['POST'])
def upload(path = ''):
    failed_list = []
    local_path = os.path.join(directory_path, path)
    if(os.path.isdir(local_path)):
        files = request.files.getlist('uploaded_files')
        for f in files:
            if(f):
                f.save(os.path.join(local_path, f.filename))
    return render_template('uploadResponse.j2', redirect_url='/'+path, message='文件上传成功')


if(__name__ == '__main__'):
    app.run(debug=True)
        
