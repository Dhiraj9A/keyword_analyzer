import re

from collections import Counter

from bs4 import BeautifulSoup

from django.shortcuts import render

from .services.fetcher import fetch_website


def home(request):

    return render(
        request,
        "analyzer/home.html"
    )


def analyze_url(request):

    if request.method != "POST":

        return render(
            request,
            "analyzer/home.html"
        )

    url = request.POST.get(
        "url",
        ""
    ).strip()

    # ==========================================
    # URL VALIDATION
    # ==========================================

    if not url:

        return render(
            request,
            "analyzer/home.html",
            {
                "error": "Please enter a website URL."
            }
        )

    if not url.startswith(
        ("http://", "https://")
    ):

        url = "https://" + url

    # ==========================================
    # FETCH WEBSITE
    # ==========================================

    result = fetch_website(url)

    if not result["success"]:

        return render(
            request,
            "analyzer/home.html",
            {
                "error": (
                    "Unable to analyze website."
                ),
                "details": result["error"],
            }
        )

    html = result["html"]

    fetch_method = result["method"]

    # ==========================================
    # PARSE HTML
    # ==========================================

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    # ==========================================
    # REMOVE UNWANTED ELEMENTS
    # ==========================================

    for element in soup.find_all(
        [
            "script",
            "style",
            "noscript",
            "svg",
        ]
    ):

        element.decompose()

    # ==========================================
    # TITLE
    # ==========================================

    title = ""

    if soup.title:

        title = soup.title.get_text(
            strip=True
        )

    # ==========================================
    # META DESCRIPTION
    # ==========================================

    meta_description = ""

    meta = soup.find(
        "meta",
        attrs={
            "name": re.compile(
                "^description$",
                re.I
            )
        }
    )

    if meta:

        meta_description = meta.get(
            "content",
            ""
        ).strip()

    # ==========================================
    # HEADINGS
    # ==========================================

    headings = []

    for tag in soup.find_all(
        ["h1", "h2", "h3"]
    ):

        heading_text = tag.get_text(
            " ",
            strip=True
        )

        if heading_text:

            headings.append(
                {
                    "tag": tag.name.upper(),
                    "text": heading_text,
                }
            )

    # ==========================================
    # WEBSITE TEXT
    # ==========================================

    text = soup.get_text(
        " ",
        strip=True
    )

    text = text.lower()

    # ==========================================
    # WORD EXTRACTION
    # ==========================================

    words = re.findall(
        r"\b[a-zA-Z]{3,}\b",
        text
    )

    # ==========================================
    # STOPWORDS
    # ==========================================

    stopwords = {
        "the",
        "and",
        "for",
        "with",
        "that",
        "this",
        "from",
        "your",
        "you",
        "are",
        "was",
        "were",
        "have",
        "has",
        "had",
        "will",
        "can",
        "our",
        "about",
        "into",
        "more",
        "than",
        "their",
        "they",
        "them",
        "then",
        "also",
        "not",
        "but",
        "all",
        "www",
        "http",
        "https",
        "com",
        "html",
        "home",
        "page",
        "click",
        "here",
    }

    # ==========================================
    # FILTER WORDS
    # ==========================================

    filtered_words = [
        word
        for word in words
        if word not in stopwords
    ]

    # ==========================================
    # KEYWORD COUNT
    # ==========================================

    keyword_counter = Counter(
        filtered_words
    )

    keywords = keyword_counter.most_common(
        50
    )

    # ==========================================
    # RESULT
    # ==========================================

    context = {
        "url": url,

        "title": title,

        "meta_description": (
            meta_description
        ),

        "headings": headings,

        "keywords": keywords,

        "word_count": len(
            filtered_words
        ),

        "fetch_method": fetch_method,
    }

    return render(
        request,
        "analyzer/results.html",
        context
    )