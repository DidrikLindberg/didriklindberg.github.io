# Quick Start Guide

## Get the website running in 5 minutes

### 1. Install Python
Make sure you have Python 3.8 or higher installed:
```bash
python --version
```

### 2. Set Up Virtual Environment
```bash
cd website-v1
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
python app.py
```

### 5. Open in Browser
Go to: http://localhost:5000

---

## First Customizations (5 minutes)

### Edit Company Info
Open `app.py` and update lines 13-19:
```python
SITE_CONFIG = {
    'company_name': 'Your Company Name',
    'tagline': 'Your tagline',
    'email': 'you@yourcompany.com',
    'linkedin': 'https://linkedin.com/in/yourprofile',
    'phone': '+1 (555) 123-4567',
}
```

Save the file, refresh your browser, and you'll see your changes!

---

## What's Next?

1. **Add Your Services**: Edit the `SERVICES` list in `app.py` (lines 22-140)
2. **Add Your Projects**: Edit the `PROJECTS` list in `app.py` (lines 143-250)
3. **Add Testimonials**: Edit the `TESTIMONIALS` list in `app.py` (lines 253-280)
4. **Customize About Page**: Edit `templates/about.html` to tell your story

See the full README.md for detailed customization instructions.

---

## Testing the Contact Form

1. Fill out the contact form at http://localhost:5000/contact
2. Check your terminal/console for the submission (it will print there)
3. To send actual emails, follow the email setup in README.md

---

## Deploy to Production

See "Deployment" section in README.md for instructions on deploying to:
- Heroku
- AWS/Azure/GCP
- DigitalOcean
- Railway/Render

---

**Need help?** Check the README.md or troubleshooting section.
