# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
from app.home import blueprint
from flask import render_template, redirect, url_for, request, abort
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound
from datetime import date

from werkzeug.utils import secure_filename


from predict import predictWithTrainedModels

valid_upload_extensions = ['.txt', '.c', '.cpp']

upload_path = "tmp/"


@blueprint.route('/index', methods = ['GET', 'POST'])
@login_required
def index():
    files = os.listdir(upload_path)
    return render_template('index.html', files = files, segment='index')

@blueprint.route('/process', methods = ['GET', 'POST'])
@login_required
def process():
    files = os.listdir(upload_path)
    return render_template('process.html', files = files, segment='index')

@blueprint.route('/result', methods = ['GET', 'POST'])
@login_required
def result():
    fileName = request.form["fileName"]
    print(fileName)
    c119,c120,c469,c476,binaryModel = predictWithTrainedModels(fileName)
    cwe_119_V,cwe_119_C = computeVals(c119)
    cwe_120_V,cwe_120_C = computeVals(c120)
    cwe_469_V,cwe_469_C = computeVals(c469)
    cwe_476_V,cwe_476_C = computeVals(c476)
    cwe_binary_V,cwe_binary_C = computeVals(binaryModel)
    today = date.today()
    return render_template('result.html', fileName = fileName, date = today, cwe_119_C = cwe_119_C,cwe_120_C = cwe_120_C,cwe_469_C = cwe_469_C,cwe_476_C = cwe_476_C,cwe_binary_C = cwe_binary_C, cwe_119_V = cwe_119_V,cwe_120_V = cwe_120_V,cwe_469_V = cwe_469_V,cwe_476_V = cwe_476_V,cwe_binary_V = cwe_binary_V, cwe_119 = f'{c119*100:.2f}',cwe_120 = f'{c120*100:.2f}', cwe_469 =f'{c469*100:.2f}', cwe_476 = f'{c476*100:.2f}', cwe_binary =f'{binaryModel*100:.2f}',segment='index')

@blueprint.route('/remove', methods = ['GET', 'POST'])
@login_required
def remove():
    fileName = request.form["fileName"]
    print(fileName)
    os.remove('tmp/'+fileName)
    files = os.listdir(upload_path)
    return render_template('index.html', files = files, segment='index')

@blueprint.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in valid_upload_extensions:
                abort(400)
            uploaded_file.save(os.path.join(upload_path, filename))
    return render_template('file-uploaded.html'), 200 

@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith( '.html' ):
            template += '.html'

        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template( template, segment=segment )

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except:
        return render_template('page-500.html'), 500

# Helper - Extract current page name from request 
def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  

def computeVals(cX):
    cwe_V = 'No'
    color = 'success'
    if(cX<0.25):
        color = 'success'
    elif(cX<0.5):
        color = 'warning'
    else:
        cwe_V = 'Yes'
        color = 'danger'
    return cwe_V,color

## Errors


@blueprint.errorhandler(413)
def too_large(e):
    return render_template('page-413.html'), 413

@blueprint.errorhandler(400)
def wrong_file_type(e):
    return render_template('page-400.html'), 400

