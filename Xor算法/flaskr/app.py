from flask import (
    Flask, g, render_template, request
)
import os
import mimaxue

app = Flask(__name__)
@app.route('/')
def xor():
    return render_template('xor.html')

@app.route('/en', methods=('GET', 'POST'))
def en():
    if request.method == 'POST':
        enfile = request.files['enfilename']
        key = bytes(request.form['key'],'utf8')
        xor = mimaxue.xor(key)
        xor.enfile(enfile)
        g.enmessage = '已加密，文件路径： '+ os.path.abspath(os.path.dirname(__file__)) + '\\' + enfile.filename + '_en'

    return render_template('xor.html')

@app.route('/de', methods=('GET', 'POST'))
def de():
    if request.method == 'POST':
        defile = request.files['defilename']
        key = bytes(request.form['key'],'utf8')
        xor = mimaxue.xor(key)
        if '_en' in defile.filename:
            defile.filename = defile.filename[:-3]
        xor.defile(defile)
        g.demessage =  '已解密，文件路径： '+ os.path.abspath(os.path.dirname(__file__)) + '\\' + defile.filename + '_de'

    return render_template('xor.html')

if __name__ == '__main__':
    app.run(debug=True)
