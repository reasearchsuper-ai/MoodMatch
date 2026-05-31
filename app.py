"""
MoodMatch - AI-Powered Emotion-to-Music App
Entry point for the Flask application
"""

import os
from flask import Flask
from flask_cors import CORS
from backend.routes.upload import upload_bp
from backend.routes.emotion import emotion_bp
from backend.routes.songs import songs_bp
from backend.routes.analytics import analytics_bp
from backend.routes.history import history_bp

def create_app():
    app = Flask(
        __name__,
        template_folder="frontend/templates",
        static_folder="frontend/static"
    )

    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'moodmatch-secret-2024')
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
    app.config['MAX_CONTENT_LENGTH'] = 200 * 1024 * 1024  # 200MB max upload
    app.config['ALLOWED_EXTENSIONS'] = {'mp4', 'avi', 'mov', 'mkv', 'webm', 'flv'}
    app.config['DATABASE'] = os.path.join(os.getcwd(), 'moodmatch.db')

    # Ensure upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Enable CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Register blueprints
    app.register_blueprint(upload_bp, url_prefix='/api')
    app.register_blueprint(emotion_bp, url_prefix='/api')
    app.register_blueprint(songs_bp, url_prefix='/api')
    app.register_blueprint(analytics_bp, url_prefix='/api')
    app.register_blueprint(history_bp, url_prefix='/api')

    # Main frontend route
    from flask import render_template
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/dashboard')
    def dashboard():
        return render_template('dashboard.html')

    @app.route('/history')
    def history_page():
        return render_template('history.html')

    @app.route('/playlist/<session_id>')
    def playlist(session_id):
        return render_template('playlist.html', session_id=session_id)

    return app

# --- THE FIX: Initialize the app here so Gunicorn can see it! ---
app = create_app()

if __name__ == '__main__':
    print("🎵 MoodMatch is running at http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
