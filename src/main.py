from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from src.resume_read import parse_resume
from src.mongoDbOperations import insertToMongoDB

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = '/home/vedanta/AllResume'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))
        file.save(file_path) # Then save the file
        payload = parse_resume(file_path,"https://default")
        if payload:
            insertToMongoDB(payload)

        return "File has been uploaded."
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3001')
    app.run(debug=True)