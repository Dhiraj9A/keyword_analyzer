# 🔍 Website Keyword Analyzer & AI SEO Suggestions

A Django-based web application for website keyword analysis and AI-powered SEO auditing.

The application allows users to enter a website URL, fetch and analyze its HTML content, extract keywords and SEO information, calculate an SEO score out of 100, detect SEO issues, and generate AI-powered recommendations for improving website SEO.

## 🚀 Features

### 🔍 Keyword Analyzer

- Analyze any accessible website URL
- Extract webpage content
- Extract page title
- Extract meta description
- Extract H1, H2 and H3 headings
- Extract website text
- Extract top keywords
- Calculate keyword frequency
- Calculate word count
- Display keyword analysis
- Export keyword analysis data to Excel file
- Requests-based website fetching
- Playwright fallback for JavaScript-rendered websites
- BeautifulSoup HTML parsing

### 📊 SEO Analyzer

- Calculate SEO score out of 100
- Technical SEO analysis
- On-page SEO analysis
- Content SEO analysis
- HTML structure analysis
- Meta title analysis
- Meta description analysis
- Heading analysis
- Image ALT analysis
- Canonical URL analysis
- Detect SEO issues
- Category-wise SEO scores
- Issue priority

### 🤖 AI SEO Suggestions

The application uses Gemini AI to analyze detected SEO issues and provide developer-friendly recommendations.

AI recommendations can include:

- SEO issue explanation
- Why the issue matters
- Issue priority
- HTML/code location
- Current implementation
- Recommended implementation
- Before/After code
- Developer action
- Validation instructions
- Current SEO score
- Expected SEO score
- Expected score improvement

Example:

```text
Current SEO Score
72 / 100

Issue
Missing Meta Description

Priority
HIGH

Recommendation
Add a unique and relevant meta description.

Before:

<head>
    <title>Website Analyzer</title>
</head>

After:

<head>
    <title>Website Analyzer</title>

    <meta
        name="description"
        content="Analyze and improve your website SEO with AI-powered recommendations."
    >
</head>

Expected SEO Score
77 / 100

Potential Improvement
+5 points

⚙️ How It Works

User enters website URL
          ↓
URL Validation
          ↓
Website Crawler
          ↓
Fetch HTML
          ↓
BeautifulSoup / Playwright
          ↓
Content Extraction
          ↓
Keyword Analysis
          ↓
SEO Analysis
          ↓
SEO Score / 100
          ↓
Detect SEO Issues
          ↓
Gemini AI Analysis
          ↓
AI SEO Recommendations
          ↓
Developer-Friendly Report

📊 SEO Report

The application can generate information such as:

Website URL
HTTP Status
Page Title
Meta Description
H1 / H2 / H3
Word Count
Top Keywords
Keyword Frequency
Current SEO Score
Category Scores
Detected Issues
AI Recommendations
Expected SEO Score
Score Improvement


Example: - 
SEO Score

78 / 100

Technical SEO       17 / 20
On-Page SEO         25 / 30
Content SEO         21 / 25
HTML Structure      10 / 15
Images               5 / 10

🛠️ Technologies
Python
Django
Django REST Framework
HTML5
CSS3
JavaScript
Bootstrap
Requests
BeautifulSoup
Playwright
Chromium
Gemini API
📁 Project Structure

keyword_analyzer/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── analyzer/
│   ├── migrations/
│   ├── services/
│   │   ├── __init__.py
│   │   └── fetcher.py
│   │
│   ├── templates/
│   │   └── analyzer/
│   │       ├── home.html
│   │       └── results.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── seo_suggestions/
│   ├── migrations/
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── crawler.py
│   │   ├── seo_analyzer.py
│   │   └── gemini.py
│   │
│   ├── templates/
│   │   └── seo_suggestions/
│   │       ├── home.html
│   │       └── analyze.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md

📦 Installation
1. Clone Repository

git clone git@github.com:Dhiraj9A/keyword_analyzer.git

2. Open Project
cd keyword_analyzer
3. Create Virtual Environment

Windows:

python -m venv venv
4. Activate Virtual Environment

Windows:

venv\Scripts\activate

Linux/macOS:

source venv/bin/activate
5. Install Dependencies
pip install -r requirements.txt
6. Install Playwright
python -m playwright install chromium
7. Configure Gemini API

Create a .env file:

GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.6-flash

Never commit your Gemini API key to GitHub.

Add this to .gitignore:

.env
venv/
__pycache__/
*.pyc
db.sqlite3
8. Run Migrations
python manage.py migrate
9. Start Server
python manage.py runserver

Open:

http://127.0.0.1:8000/
🧪 Example

Enter a website URL:

https://www.python.org

The application will:

Fetch Website
      ↓
Extract HTML
      ↓
Analyze Keywords
      ↓
Analyze SEO
      ↓
Calculate SEO Score
      ↓
Detect SEO Issues
      ↓
Analyze With Gemini AI
      ↓
Generate SEO Suggestions
⚠️ Limitations

Some websites may block automated requests using:

CAPTCHA
Bot protection
Firewalls
Rate limiting
Access-control systems
Login requirements

Playwright can handle many JavaScript-rendered websites, but websites that actively block automated browsers may still be unavailable.

AI-generated recommendations should be reviewed by a developer before applying them to a production website.

The expected SEO score is an estimate based on the application's SEO scoring rules and AI recommendations. It does not guarantee search-engine ranking improvements.

🔮 Future Improvements
Keyword density
Keyword clustering
Search intent detection
Primary keyword detection
Secondary keyword detection
Advanced technical SEO
Internal link analysis
External link analysis
Broken link detection
Image ALT analysis
Open Graph analysis
Twitter Card analysis
Schema.org validation
Canonical URL analysis
Robots.txt analysis
XML Sitemap analysis
Core Web Vitals
PageSpeed integration
AI-generated meta titles
AI-generated meta descriptions
AI content optimization
Automated HTML SEO fixes
PDF SEO reports
SEO history
Website monitoring
Scheduled SEO audits
User dashboard
Public API
🔒 Security

Never commit sensitive information.

Do not expose:

GEMINI_API_KEY
.env
Database credentials
Private API keys
Production secrets

Always use environment variables for sensitive configuration.

👨‍💻 Author

Dhiraj Kumar

GitHub:

https://github.com/Dhiraj9A

📄 License

This project is currently developed for learning, experimentation, and further development.


### Bas ab kya karna hai

1. Project me `README.md` open karo.
2. Purana content **Ctrl + A → Delete** karo.
3. Upar wala content paste karo.
4. `Ctrl + S`.
5. Terminal me:

```bash
git add README.md
git commit -m "Update README with AI SEO analyzer"
git push origin main
