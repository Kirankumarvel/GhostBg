from flask import Flask, render_template, request, send_file, redirect, url_for
from rembg import remove
from PIL import Image
import os
from io import BytesIO
import uuid
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB limit
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        
        # If user does not select file, browser submits an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            # Generate unique filename
            unique_id = str(uuid.uuid4())
            original_filename = secure_filename(file.filename)
            original_ext = original_filename.rsplit('.', 1)[1].lower()
            original_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{unique_id}_original.{original_ext}")
            result_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{unique_id}_nobg.png")
            
            # Save original file
            file.save(original_path)
            
            try:
                # Process the image
                with Image.open(original_path) as img:
                    # Remove background
                    result = remove(img)
                    
                    # Save result
                    result.save(result_path, format='PNG')
                    
                    # Prepare for download
                    img_io = BytesIO()
                    result.save(img_io, 'PNG')
                    img_io.seek(0)
                    
                    return render_template('index.html', 
                                         original_image=f"uploads/{unique_id}_original.{original_ext}",
                                         result_image=f"uploads/{unique_id}_nobg.png",
                                         download_ready=True)
            
            except Exception as e:
                # Clean up files if error occurs
                if os.path.exists(original_path):
                    os.remove(original_path)
                if os.path.exists(result_path):
                    os.remove(result_path)
                return render_template('index.html', error=str(e))
    
    return render_template('index.html')

@app.route('/download/<path:filename>')
def download(filename):
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(path, as_attachment=True, download_name='background_removed.png')

@app.route('/cleanup', methods=['POST'])
def cleanup():
    # Clean up uploaded files
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)