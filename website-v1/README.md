# Web Development Consulting Firm Website

A modern, professional marketing website for a web development consulting firm. Built with Python Flask, Jinja2 templates, and Tailwind CSS.

## 🚀 Features

- **Modern Design**: Clean, professional layout with gradient accents and smooth animations
- **Fully Responsive**: Works perfectly on desktop, tablet, and mobile devices
- **SEO Optimized**: Proper meta tags, semantic HTML, and heading structure
- **5 Core Pages**:
  - Home (hero, services overview, featured projects, testimonials)
  - Services (detailed service descriptions with deliverables and outcomes)
  - Projects (case studies with tech stack and measurable results)
  - About (company story, tech stack, values and working style)
  - Contact (working contact form with validation)
- **Working Contact Form**: Captures leads with name, email, company, budget, and message
- **Zero JavaScript Complexity**: No build tools, no npm, just Python and Tailwind CSS CDN
- **Easy Customization**: All content centralized in `app.py` for quick updates

## 📁 Project Structure

```
website-v1/
├── app.py                 # Flask application with routes and data
├── requirements.txt       # Python dependencies
├── templates/            # Jinja2 HTML templates
│   ├── base.html         # Base template with navigation and footer
│   ├── home.html         # Home page
│   ├── services.html     # Services page
│   ├── projects.html     # Projects listing
│   ├── project_detail.html  # Individual case study
│   ├── about.html        # About page
│   └── contact.html      # Contact form page
└── static/               # Static assets (CSS, images, etc.)
    └── css/
```

## 🛠️ Tech Stack

- **Backend**: Python Flask 3.0
- **Templating**: Jinja2
- **Styling**: Tailwind CSS (via CDN)
- **Fonts**: Google Fonts (Inter)
- **Icons**: Heroicons (inline SVG)

## ⚡ Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Navigate to the project directory**:
   ```bash
   cd website-v1
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the development server**:
   ```bash
   python app.py
   ```

6. **Open your browser** and visit:
   ```
   http://localhost:5000
   ```

That's it! The website should now be running locally.

## 🎨 Customization Guide

All the content you need to customize is in `app.py`. Here's what to change:

### 1. Company Information

Edit the `SITE_CONFIG` dictionary at the top of `app.py`:

```python
SITE_CONFIG = {
    'company_name': 'Your Company Name',        # Your company name
    'tagline': 'Your tagline here',             # Short tagline/value prop
    'email': 'contact@yourcompany.com',         # Contact email
    'linkedin': 'https://linkedin.com/in/...',  # LinkedIn URL
    'phone': '+1 (555) 123-4567',               # Phone number
}
```

### 2. Services

Edit the `SERVICES` list in `app.py`. Each service has:
- `id`: URL-friendly identifier (e.g., 'web-app-development')
- `title`: Service name
- `icon`: Emoji icon (or replace with image path)
- `short_description`: Brief 1-2 sentence description
- `full_description`: Longer explanation
- `deliverables`: List of what clients get
- `ideal_for`: Who this service is perfect for
- `outcomes`: Expected results/benefits

Example:
```python
{
    'id': 'web-app-development',
    'title': 'Web App Development',
    'icon': '🚀',
    'short_description': 'Custom web applications built with modern frameworks.',
    'full_description': 'We build scalable, maintainable web applications...',
    'deliverables': [
        'Custom web application development',
        'Database design and optimization',
        # ...
    ],
    'ideal_for': 'SaaS startups, businesses needing custom tools',
    'outcomes': [
        'Faster operations',
        'Scalable architecture',
        # ...
    ]
}
```

### 3. Projects / Case Studies

Edit the `PROJECTS` list in `app.py`. Each project has:
- `id`: URL-friendly identifier
- `title`: Project name
- `client`: Client name
- `tagline`: One-line summary with key metric
- `image_placeholder`: Emoji (or replace with image path)
- `problem`: What challenge the client faced
- `solution`: How you solved it
- `tech_stack`: List of technologies used
- `results`: List of measurable outcomes
- `featured`: Boolean - show on home page?

### 4. Testimonials

Edit the `TESTIMONIALS` list in `app.py`:

```python
{
    'quote': 'The testimonial text goes here...',
    'author': 'Client Name',
    'title': 'Job Title',
    'company': 'Company Name',
}
```

### 5. About Page Content

The about page pulls from `SITE_CONFIG` and displays your tech stack. To customize the story:

1. Open `templates/about.html`
2. Edit the "Our Story" section (look for the `<p>` tags in the "Story Section")
3. Update tech stack lists if needed (Backend, Frontend, Integration sections)

### 6. Contact Form Handling

By default, the contact form logs submissions to the console. To actually send emails:

1. Install Flask-Mail:
   ```bash
   pip install Flask-Mail
   ```

2. In `app.py`, find the contact form route (around line 220)

3. Replace the `print()` statements with email sending logic:
   ```python
   from flask_mail import Mail, Message
   
   # Configure Flask-Mail (add after app initialization)
   app.config['MAIL_SERVER'] = 'smtp.gmail.com'
   app.config['MAIL_PORT'] = 587
   app.config['MAIL_USE_TLS'] = True
   app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
   app.config['MAIL_PASSWORD'] = 'your-password'
   
   mail = Mail(app)
   
   # In the contact route:
   msg = Message(
       subject=f'New inquiry from {name}',
       sender='your-email@gmail.com',
       recipients=['your-email@gmail.com'],
       body=f'Name: {name}\nEmail: {email}\nCompany: {company}\n\n{message}'
   )
   mail.send(msg)
   ```

## 🎯 SEO Optimization

Each page has customizable:
- `<title>` tags
- `<meta description>` tags
- Semantic HTML structure
- Alt text placeholders for images

To customize SEO for each page, edit the `{% block title %}` and `{% block description %}` in each template file.

## 🚢 Deployment

### Deploy to Production

1. **Set a secure secret key**:
   ```bash
   export SECRET_KEY='your-very-secure-random-key-here'
   ```

2. **Use a production WSGI server** (e.g., Gunicorn):
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

3. **Deploy to your platform of choice**:
   - **Heroku**: Create a `Procfile` with `web: gunicorn app:app`
   - **AWS/Azure/GCP**: Follow their Python/Flask deployment guides
   - **DigitalOcean**: Use their App Platform or deploy to a Droplet
   - **Railway/Render**: Connect your repo and it auto-deploys

### Environment Variables

For production, set these environment variables:
- `SECRET_KEY`: Flask secret key for sessions
- `MAIL_SERVER`, `MAIL_USERNAME`, `MAIL_PASSWORD`: If using email

## 📝 Adding New Pages

To add a new page:

1. **Create a route in `app.py`**:
   ```python
   @app.route('/new-page')
   def new_page():
       return render_template('new_page.html', config=SITE_CONFIG)
   ```

2. **Create a template** in `templates/new_page.html`:
   ```html
   {% extends "base.html" %}
   
   {% block title %}New Page - {{ config.company_name }}{% endblock %}
   
   {% block content %}
   <!-- Your content here -->
   {% endblock %}
   ```

3. **Add navigation link** in `templates/base.html` (around line 30)

## 🎨 Styling Customization

The site uses Tailwind CSS via CDN. To customize colors:

1. Open `templates/base.html`
2. Find the `<script>` tag with `tailwind.config`
3. Modify the color values:
   ```javascript
   tailwind.config = {
       theme: {
           extend: {
               colors: {
                   primary: {
                       // Customize these color values
                       500: '#3b82f6',
                       600: '#2563eb',
                       // ...
                   }
               }
           }
       }
   }
   ```

## 🐛 Troubleshooting

### Port Already in Use
If port 5000 is taken, change it in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Use different port
```

### Templates Not Updating
Make sure debug mode is on (it is by default in `app.py`). If caching issues persist, try:
```python
app.config['TEMPLATES_AUTO_RELOAD'] = True
```

### Tailwind Styles Not Loading
Make sure you have internet connection (Tailwind is loaded via CDN). For offline development, follow Tailwind's standalone CLI setup.

## 📄 License

This is a template for your business. Customize it however you want!

## 🤝 Need Help?

This is a starter template - feel free to modify, extend, or completely rebuild parts of it to fit your needs. The code is intentionally simple and well-commented to make customization easy.

---

**Built with ❤️ using Python Flask and Tailwind CSS**