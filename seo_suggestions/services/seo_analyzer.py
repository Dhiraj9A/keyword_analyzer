from config.seo_rules import (
    SEO_CATEGORIES,
    SEO_RULES
)


def calculate_seo_score(page):

    data = page["data"]

    issues = []

    def add_issue(
        rule,
        message,
        selector="",
        element=""
    ):

        config = SEO_RULES.get(rule)

        if not config:
            return

        issues.append({

            "rule": rule,

            "category":
                config["category"],

            "penalty":
                config["penalty"],

            "priority":
                config["priority"],

            "message":
                message,

            "selector":
                selector,

            "element":
                element
        })


    # --------------------------------
    # TITLE
    # --------------------------------

    title = data.get("title")

    if not title:

        add_issue(
            "title_missing",
            "Page title is missing.",
            "head > title"
        )

    elif len(title.strip()) < 20:

        add_issue(
            "title_too_short",
            "Page title appears too short.",
            "head > title",
            f"<title>{title}</title>"
        )


    # --------------------------------
    # META DESCRIPTION
    # --------------------------------

    if not data.get("meta_description"):

        add_issue(
            "meta_description_missing",
            "Meta description is missing.",
            'meta[name="description"]'
        )


    # --------------------------------
    # CANONICAL
    # --------------------------------

    if not data.get("canonical"):

        add_issue(
            "canonical_missing",
            "Canonical URL is missing.",
            'link[rel="canonical"]'
        )


    # --------------------------------
    # H1
    # --------------------------------

    h1_count = data.get(
        "h1_count",
        0
    )

    if h1_count == 0:

        add_issue(
            "h1_missing",
            "No H1 heading was found.",
            "h1"
        )

    elif h1_count > 1:

        add_issue(
            "multiple_h1",
            f"Found {h1_count} H1 elements.",
            "h1"
        )


    # --------------------------------
    # VIEWPORT
    # --------------------------------

    if not data.get("viewport"):

        add_issue(
            "viewport_missing",
            "Viewport meta tag is missing.",
            'meta[name="viewport"]'
        )


    # --------------------------------
    # LANG
    # --------------------------------

    if not data.get("lang"):

        add_issue(
            "lang_missing",
            "HTML lang attribute is missing.",
            "html"
        )


    # --------------------------------
    # IMAGES
    # --------------------------------

    images = data.get(
        "images",
        []
    )

    missing_alt = [

        image
        for image in images

        if image.get("alt") is None
        and not image.get(
            "src",
            ""
        ).startswith("data:")
    ]

    if missing_alt:

        add_issue(
            "images_missing_alt",
            f"{len(missing_alt)} images "
            "do not have alt attributes.",
            "img"
        )


    missing_dimensions = [

        image
        for image in images

        if not image.get("width")
        or not image.get("height")
    ]

    if missing_dimensions:

        add_issue(
            "images_missing_dimensions",
            f"{len(missing_dimensions)} images "
            "do not define width/height.",
            "img"
        )


    # --------------------------------
    # LINKS
    # --------------------------------

    links = data.get(
        "links",
        []
    )

    internal_links = []

    page_url = data.get("url")

    try:

        from urllib.parse import (
            urlparse
        )

        page_host = urlparse(
            page_url
        ).netloc

        for link in links:

            href = link.get("href")

            if not href:
                continue

            if urlparse(href).netloc == page_host:

                internal_links.append(link)

    except Exception:
        pass


    if len(internal_links) < 3:

        add_issue(
            "internal_links_low",
            "Very few internal links were detected.",
            "a"
        )


    generic_words = {

        "click here",
        "here",
        "read more",
        "learn more"
    }

    generic_anchors = [

        link

        for link in links

        if link.get(
            "text",
            ""
        ).lower() in generic_words
    ]


    if generic_anchors:

        add_issue(
            "generic_anchor_text",
            f"{len(generic_anchors)} "
            "generic anchor texts detected.",
            "a"
        )


    # --------------------------------
    # SEMANTIC HTML
    # --------------------------------

    semantic = data.get(
        "semantic",
        {}
    )

    if not semantic.get("main"):

        add_issue(
            "main_missing",
            "Main landmark element is missing.",
            "main"
        )


    # --------------------------------
    # STRUCTURED DATA
    # --------------------------------

    if not data.get("json_ld"):

        add_issue(
            "structured_data_missing",
            "No JSON-LD structured data detected.",
            'script[type="application/ld+json"]'
        )


    # --------------------------------
    # CATEGORY SCORE
    # --------------------------------

    category_scores = {}

    for category, config in SEO_CATEGORIES.items():

        category_scores[category] = {

            "score":
                config["max"],

            "maximum":
                config["max"]
        }


    for issue in issues:

        category = issue["category"]

        if category not in category_scores:
            continue

        category_scores[category]["score"] = max(

            0,

            category_scores[category]["score"]
            - issue["penalty"]
        )


    current_score = sum(

        item["score"]

        for item
        in category_scores.values()
    )


    current_score = round(
        current_score,
        1
    )


    return {

        "current_score":
            current_score,

        "category_scores":
            category_scores,

        "issues":
            issues
    }
