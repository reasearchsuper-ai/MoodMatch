# 🎵 MoodMatch — AI-Powered Emotion-to-Music App

> Upload a video → AI detects your emotions → Get a perfect playlist

---

## 📁 Full Folder Structure

```
moodmatch/
│
├── app.py                          ← Flask entry point (run this!)
├── requirements.txt                ← Python dependencies
├── moodmatch.db                    ← SQLite DB (auto-created on first run)
│
├── backend/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── upload.py               ← POST /api/upload, GET /api/status/<id>
│   │   ├── emotion.py              ← GET /api/emotions/<id>, /timeline
│   │   ├── songs.py                ← GET /api/recommendations/<id>, /songs
│   │   ├── analytics.py            ← GET /api/analytics, /history
│   │   └── history.py              ← re-exports history_bp
│   ├── services/
│   │   ├── __init__.py
│   │   ├── emotion_service.py      ← DeepFace analysis pipeline
│   │   └── recommendation_service.py ← Song matching engine
│   ├── models/
│   │   ├── __init__.py
│   │   ├── database.py             ← SQLite CRUD functions
│   │   └── songs_data.py           ← 50+ song catalog
│   └── utils/
│       └── __init__.py
│
├── frontend/                       ← Flask-served App UI
│   ├── templates/
│   │   ├── index.html              ← Upload page
│   │   ├── playlist.html           ← Results & playlist page
│   │   ├── history.html            ← Session history page
│   │   └── dashboard.html          ← Analytics page
│   └── static/
│       ├── css/
│       │   ├── app.css             ← Global dark luxury styles
│       │   └── playlist.css        ← Playlist page styles
│       └── js/
│           ├── upload.js           ← Drag/drop, upload, polling
│           ├── playlist.js         ← Charts, song cards, interactions
│           ├── history.js          ← History grid rendering
│           └── dashboard.js        ← Analytics charts
│
├── website/
│   └── index.html                  ← Marketing website (standalone HTML)
│
└── uploads/                        ← Auto-created, stores uploaded videos
```

---

## ⚡ Installation & Setup

### Step 1 — Prerequisites

Make sure you have:
- Python 3.9 or 3.10 (recommended — TensorFlow requires this)
- pip (Python package manager)
- VS Code (optional but recommended)

Check your version:
```bash
python --version
```

---

### Step 2 — Clone or Create the Project

If you received this as files, open the `moodmatch/` folder in VS Code:
```
File → Open Folder → select moodmatch/
```

---

### Step 3 — Create a Virtual Environment

```bash
# In the moodmatch/ folder:
python -m venv venv

# Activate it:
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```

---

### Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ This will install TensorFlow (~500MB) and DeepFace. It may take 5–10 minutes.

---

### Step 5 — Run the App

```bash
python app.py
```

You should see:
```
🎵 MoodMatch is running at http://localhost:5000
✅ Database initialized successfully
```

---

### Step 6 — Open in Browser

| Page       | URL                           |
|------------|-------------------------------|
| Upload     | http://localhost:5000/        |
| History    | http://localhost:5000/history |
| Analytics  | http://localhost:5000/dashboard |
| Website    | Open `website/index.html` in browser |

---

## 🌐 Website (Marketing Page)

The `website/index.html` is a **standalone HTML file** — no server needed!

Just double-click it or open in browser:
```
moodmatch/website/index.html
```

Or right-click in VS Code → "Open with Live Server" (if you have the extension).

---

## 📡 API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/upload` | Upload video file |
| GET | `/api/status/<id>` | Poll processing status |
| GET | `/api/emotions/<id>` | Get emotion summary |
| GET | `/api/emotions/<id>/timeline` | Get per-frame emotion data |
| GET | `/api/recommendations/<id>` | Get song recommendations |
| GET | `/api/songs` | List all songs |
| POST | `/api/interact` | Log like/skip/play |
| GET | `/api/history` | Get all sessions |
| GET | `/api/analytics` | Global analytics |

---

## 🧠 How Emotion Detection Works

1. **Frame Extraction** — OpenCV extracts 1 frame/second (up to 60 frames)
2. **DeepFace Analysis** — Each frame is analyzed for 7 emotions
3. **Weighted Aggregation** — Time-weighted averages calculated (recent frames weighted slightly higher)
4. **Summary Generation** — Primary/secondary emotions, mood label, intensity
5. **Song Matching** — Cosine similarity between emotion vectors + BPM/energy alignment

---

## 🎵 Supported Emotions & Songs

| Emotion   | Emoji | Sample Artists |
|-----------|-------|----------------|
| Happy     | 😊 | Pharrell, Dua Lipa, Harry Styles |
| Sad       | 😢 | Adele, Bon Iver, Radiohead |
| Angry     | 😠 | Kendrick Lamar, Linkin Park, RATM |
| Neutral   | 😌 | Debussy, Marconi Union, Coldplay |
| Surprised | 😲 | The Killers, BTS, AC/DC |
| Fearful   | 😨 | Radiohead, Billie Eilish, Ariana Grande |
| Disgusted | 🤢 | Nirvana, Green Day, Sex Pistols |

---

## 🔧 Troubleshooting

**DeepFace import error:**
```bash
pip install deepface tensorflow --upgrade
```

**OpenCV issues:**
```bash
pip install opencv-python-headless
```

**Port already in use:**
```bash
# Change port in app.py line: app.run(port=5001)
```

**TensorFlow not compatible:**
- Use Python 3.9 or 3.10
- `pip install tensorflow==2.13.0`

---

## 🚀 Production Deployment

```bash
# Install gunicorn
pip install gunicorn

# Run production server
gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"
```

---

## 📈 Roadmap

- [ ] Spotify API integration (live song previews)
- [ ] Real-time webcam emotion detection
- [ ] Multi-face support in group videos
- [ ] User accounts & cloud sync
- [ ] Mobile app (React Native)
- [ ] Mood journal & trend analysis

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.10, Flask 3.0 |
| AI/ML | DeepFace 0.0.93, TensorFlow 2.17 |
| Video | OpenCV 4.10 |
| Database | SQLite (via Python stdlib) |
| Frontend | Vanilla HTML/CSS/JS |
| Charts | Chart.js 4.4 |
| Fonts | Syne, DM Sans (Google Fonts) |