# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Salesforce consulting firm marketing website built with Python Flask, Jinja2 templates, and Tailwind CSS. The site is a single Flask application with template-based routing for services, projects, about, and contact pages. All business content (services, projects, testimonials, company info) is defined as Python dictionaries in `app.py`.

## Working Directory

The main application code is located in `website-v1/` subdirectory. Always `cd website-v1` before running commands.

## Development Commands

### Setup
```bash
cd website-v1
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # macOS/Linux
pip install -r requirements.txt
```

### Running the Development Server
```bash
cd website-v1
python app.py
```
The application runs on http://localhost:5000 with debug mode enabled by default.

### Dependencies
- **Flask 3.0.0**: Web framework
- **Jinja2 3.1.2**: Template engine (included with Flask)
- **python-dotenv 1.0.0**: Environment variable management
- **Werkzeug 3.0.1**: WSGI utilities (included with Flask)

No build tools, npm, or JavaScript bundlers required. Tailwind CSS loads via CDN in base template.

## Architecture

### Application Structure
```
website-v1/
├── app.py                     # Flask app + all route handlers + content data
├── templates/                 # Jinja2 HTML templates
│   ├── base.html             # Base template with nav, footer, Tailwind config
│   ├── home.html             # Home page with hero, services, projects, testimonials
│   ├── services.html         # Service listing page
│   ├── service_detail.html   # Individual service detail page
│   ├── projects.html         # Project/case study listing
│   ├── project_detail.html   # Individual project detail page
│   ├── about.html            # About/company story page
│   └── contact.html          # Contact form with budget selector
├── static/css/               # Empty (Tailwind via CDN)
├── requirements.txt
└── .env.example
```

### Core Data Structures (in app.py)

1. **SITE_CONFIG** (lines 8-26): Company name, tagline, contact info, certifications, partner status
2. **SERVICES** (lines 29-179): List of service dictionaries with full descriptions, deliverables, outcomes
3. **PROJECTS** (lines 183-340): Case studies with problem/solution, tech stack, results
4. **TESTIMONIALS** (lines 343-377): Client testimonials with quotes and attribution
5. **STATS** (lines 379-384): Company statistics for homepage

### Routes (lines 387-468)

- `GET /` → home page (featured projects + services preview)
- `GET /services` → all services listing
- `GET /services/<service_id>` → individual service detail with related projects
- `GET /projects` → all projects/case studies
- `GET /projects/<project_id>` → individual project detail with related projects
- `GET /about` → about page
- `GET|POST /contact` → contact form (logs to console by default)

All routes pass `config=SITE_CONFIG` to templates for consistent site-wide data access.

### Template Inheritance

All pages extend `base.html`, which includes:
- Navigation with responsive mobile menu
- Tailwind CSS CDN configuration with custom color palette (purple/blue gradients)
- Footer with company info and links
- Flash message display for form submissions

### Content Management Philosophy

**All editable content lives in `app.py` as Python data structures.** This centralizes content editing and avoids scattered hardcoded strings in templates. Templates are purely presentational.

To add/modify content:
1. Edit the relevant dictionary in `app.py` (SERVICES, PROJECTS, etc.)
2. Restart Flask development server (auto-reload should pick up changes)
3. No template changes needed unless modifying layout/design

## Customization Patterns

### Adding a New Service
Add dictionary to SERVICES list with required keys: `id`, `title`, `icon`, `short_description`, `full_description`, `deliverables`, `ideal_for`, `outcomes`, `tech_highlights`.

### Adding a New Project
Add dictionary to PROJECTS list with required keys: `id`, `title`, `client`, `tagline`, `image_placeholder`, `problem`, `solution`, `tech_stack`, `results`. Set `featured: True` to show on home page.

### Contact Form Email Setup
By default, contact form prints to console. To send emails:
1. Install Flask-Mail: `pip install Flask-Mail`
2. Configure MAIL_* settings in app.py (see README.md lines 183-211 for example)
3. Replace print statements in `/contact` route with mail.send(msg)

## Design System

- **Framework**: Tailwind CSS 3.x via CDN
- **Colors**: Custom purple/blue gradient palette defined in base.html Tailwind config
- **Icons**: Emoji in data structures (can replace with actual icon libraries)
- **Typography**: Google Fonts (Inter) loaded in base.html
- **Responsive**: Mobile-first design, all templates responsive
- **Dark Mode**: Full dark mode support with toggle button

### Dark Mode Implementation

The site includes a fully functional dark mode toggle that works across all pages:

**Features:**
- Toggle button in navigation (both desktop and mobile)
- Persists user preference in localStorage
- Respects system dark mode preference on first visit
- Prevents FOUC (Flash of Unstyled Content) with initialization script
- Smooth transitions between light/dark modes

**Implementation Details:**
- Tailwind CSS `darkMode: 'class'` configuration in base.html (line 20)
- Dark mode initialization script in base.html (lines 50-59) runs before page render
- Toggle buttons in navigation bar (desktop: lines 144-157, mobile: lines 199-216)
- JavaScript toggle logic in base.html (lines 338-377)
- All templates use `dark:` utility classes for dark mode styles

**Usage Pattern:**
When adding new styles to templates, always include dark mode variants:
```html
<!-- Light mode background, dark mode background -->
<div class="bg-white dark:bg-gray-800">
  <!-- Light mode text, dark mode text -->
  <h1 class="text-gray-900 dark:text-white">Heading</h1>
  <p class="text-gray-700 dark:text-gray-300">Body text</p>
</div>
```

**Common Dark Mode Color Patterns:**
- Backgrounds: `bg-white dark:bg-gray-800` or `bg-gray-50 dark:bg-gray-900`
- Headings: `text-gray-900 dark:text-white`
- Body text: `text-gray-700 dark:text-gray-300`
- Muted text: `text-gray-600 dark:text-gray-400`
- Borders: `border-gray-200 dark:border-gray-700`
- Cards: `bg-white dark:bg-gray-800 border border-gray-100 dark:border-gray-700`
- Colored elements: Use lighter shades in dark mode (e.g., `text-primary-600 dark:text-primary-400`)

## Important Notes

- **No Tests**: This is a simple marketing site with no test suite
- **No Database**: All content is in-memory Python dictionaries
- **No API**: Pure server-rendered Flask application
- **No JavaScript Build**: No webpack, no npm, no build step
- **Development Only Secret Key**: `app.py:5` has placeholder secret key - change in production
- **Debug Mode On**: `app.py:475` runs with `debug=True` - disable in production

## Deployment Considerations

When deploying to production:
1. Change SECRET_KEY to secure random value (use environment variable)
2. Set `debug=False` in `app.run()`
3. Use production WSGI server (gunicorn): `gunicorn -w 4 app:app`
4. Configure email settings if using contact form notifications
5. See README.md lines 223-248 for platform-specific deployment instructions

## Recent Context

This repository was recently rebranded from a generic web development consultancy to "A-frame Solutions," a Salesforce-focused consulting firm. The services, projects, and content reflect Salesforce expertise (Apex development, Lightning Web Components, Health Cloud, Financial Services Cloud, integrations).

**Latest Updates:**
- **Dark Mode Toggle** (November 2025): Implemented comprehensive dark mode support across all pages with toggle buttons in navigation, localStorage persistence, system preference detection, and FOUC prevention. All templates now include `dark:` utility classes for seamless theme switching.
