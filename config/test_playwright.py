from playwright.sync_api import sync_playwright


with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=True
    )

    page = browser.new_page()

    page.goto(
        "https://quotes.toscrape.com/js/",
        wait_until="domcontentloaded",
        timeout=30000
    )

    print("Title:", page.title())
    print("URL:", page.url)
    print("Content length:", len(page.content()))

    browser.close()