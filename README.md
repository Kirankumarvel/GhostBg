
# GhostBG - Background Remover Tool

![GhostBG Logo](https://via.placeholder.com/150) *(Consider adding a logo/image here)*

A web application that removes backgrounds from images using AI-powered technology. Built with Python Flask and the `rembg` library.

## Features

- 🖼️ Upload JPG, JPEG, or PNG images
- ✂️ Automatically remove backgrounds with AI
- 🔍 Preview before/after comparison
- ⬇️ Download transparent PNG results
- 📱 Responsive design works on all devices
- 🗑️ Automatic cleanup of processed files

## Demo

[Live Demo](#) *(Add your deployment link here when available)*

## Screenshots

![Screenshot 1](https://via.placeholder.com/600x400?text=Upload+Screen)
![Screenshot 2](https://via.placeholder.com/600x400?text=Result+Screen)

## Installation

### Prerequisites

- Python 3.8+
- pip

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/GhostBG.git
   cd GhostBG
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create the uploads folder:
   ```bash
   mkdir uploads
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Open your browser and visit:
   ```
   http://localhost:5000
   ```

## Deployment

### Render (Recommended)

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set Python version to 3.9 or higher
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `gunicorn app:app`

### Other Options

- **Replit**: Upload files and run
- **Railway**: Connect GitHub repo and deploy
- **Heroku**: Use the Procfile included

## Configuration

You can modify these settings in `app.py`:

```python
app.config['UPLOAD_FOLDER'] = 'uploads'  # Upload directory
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB file size limit
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}  # Allowed file types
```

## Troubleshooting

**Issue**: "The system cannot find the path specified"
- Solution: Ensure the `uploads` folder exists and has proper permissions

**Issue**: "File not found" when downloading
- Solution: Check the file paths in the template and route handlers

**Issue**: Large files not uploading
- Solution: Increase `MAX_CONTENT_LENGTH` in the configuration

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - [@kirananrik](https://twitter.com/kirananrik) 

Project Link: [https://github.com/Kirankumarvel/GhostBG](https://github.com/Kirankumarvel/GhostBG)

