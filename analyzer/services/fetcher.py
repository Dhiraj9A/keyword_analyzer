import requests

from playwright.sync_api import sync_playwright


USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/151.0 Safari/537.36"
)


def fetch_with_requests(url):
    """
    First attempt:
    Fetch website using normal HTTP request.
    """

    headers = {
        "User-Agent": USER_AGENT,
        "Accept": (
            "text/html,application/xhtml+xml,"
            "application/xml;q=0.9,image/avif,"
            "image/webp,*/*;q=0.8"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=15,
        allow_redirects=True,
    )

    response.raise_for_status()

    return response.text


def fetch_with_playwright(url):
    """
    Second attempt:
    Open website in Chromium using Playwright.
    """

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page(
            user_agent=USER_AGENT
        )

        try:

            page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=30000,
            )

            # Give JavaScript some time to render.
            page.wait_for_timeout(2000)

            html = page.content()

            return html

        finally:

            browser.close()


def fetch_website(url):
    """
    Main fetching function.

    Flow:

    requests
        ↓
    success?
        ↓
    yes → return HTML

    no
        ↓
    Playwright
        ↓
    return rendered HTML
    """

    try:

        html = fetch_with_requests(url)

        return {
            "success": True,
            "html": html,
            "method": "requests",
            "error": None,
        }

    except Exception as requests_error:

        try:

            html = fetch_with_playwright(url)

            return {
                "success": True,
                "html": html,
                "method": "playwright",
                "error": None,
            }

        except Exception as playwright_error:

            return {
                "success": False,
                "html": None,
                "method": None,
                "error": (
                    f"Requests error: {requests_error} | "
                    f"Playwright error: {playwright_error}"
                ),
            }
