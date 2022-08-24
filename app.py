from flask import Flask, render_template, request, redirect, url_for
import os
app = Flask(__name__)
directory_path = './static/files/'

for i in ('os', 'directory_path'):
    app.jinja_env.globals[i] = eval(i)

@app.route('/s/', methods = ['GET', 'POST'])
@app.route('/s/<path:path>/', methods = ['GET', 'POST'])
def browseDir(path = ''):
    local_path = directory_path + path
    if(request.method == 'POST' and os.path.isdir(local_path)):
        files = request.files.getlist('uploaded_files')
        for f in files:
            if(f):
                f.save(os.path.join(local_path, f.filename))
    if(os.path.isdir(local_path)):
        return render_template('browseDir.html', path=path)
    return redirect('/s/')

@app.route('/')
def Index():
    return redirect('/s/')

if(__name__ == '__main__'):
    app.run()
        
