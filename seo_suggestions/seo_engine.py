# ============================================================
# SEO SUGGESTION ENGINE
# ============================================================


# ============================================================
# ADD SUGGESTION
# ============================================================

def add_suggestion(
    suggestions,
    category,
    severity,
    title,
    line,
    current,
    suggestion,
    reason
):
    """
    Common function to add an SEO suggestion.
    """

    suggestions.append({

        "category": category,

        "severity": severity,

        "title": title,

        "line": line,

        "current": current,

        "suggestion": suggestion,

        "reason": reason,

    })


# ============================================================
# SEO SCORE CALCULATOR
# ============================================================

def calculate_seo_score(
    suggestions
):
    """
    SEO score 100 se start hota hai.

    Har issue ki severity ke according
    score se penalty deduct hoti hai.

    Good = 0 penalty
    Low = 2
    Medium = 4
    High = 8
    Critical = 15
    """

    score = 100


    # ========================================================
    # PENALTY WEIGHTS
    # ========================================================

    penalties = {

        "critical": 15,

        "high": 8,

        "medium": 4,

        "low": 2,

        "good": 0,

    }


    # ========================================================
    # APPLY PENALTIES
    # ========================================================

    for item in suggestions:

        severity = item.get(
            "severity",
            "low"
        )

        penalty = penalties.get(
            severity,
            0
        )

        score -= penalty


    # ========================================================
    # SCORE LIMIT
    # ========================================================

    if score < 0:

        score = 0


    if score > 100:

        score = 100


    return score


# ============================================================
# SEO SCORE GRADE
# ============================================================

def get_score_grade(
    score
):
    """
    SEO score ke basis par readable grade return karta hai.
    """

    if score >= 90:

        return "Excellent"


    elif score >= 80:

        return "Very Good"


    elif score >= 70:

        return "Good"


    elif score >= 60:

        return "Needs Improvement"


    elif score >= 40:

        return "Poor"


    else:

        return "Critical"


# ============================================================
# TITLE ANALYSIS
# ============================================================

def analyze_title(
    title,
    title_line,
    suggestions
):

    # ========================================================
    # MISSING TITLE
    # ========================================================

    if not title:

        add_suggestion(

            suggestions=suggestions,

            category="On-Page SEO",

            severity="critical",

            title="Missing Page Title",

            line="Not found",

            current=(
                "No <title> tag found."
            ),

            suggestion=(
                "Add a unique and descriptive "
                "<title> tag for this page."
            ),

            reason=(
                "The page title helps search engines "
                "and users understand the main topic "
                "of the page."
            )

        )

        return


    title_length = len(
        title
    )


    # ========================================================
    # TOO SHORT
    # ========================================================

    if title_length < 30:

        add_suggestion(

            suggestions=suggestions,

            category="On-Page SEO",

            severity="high",

            title="Page Title Is Too Short",

            line=title_line,

            current=title,

            suggestion=(
                "Expand the title with the primary "
                "topic, service, product or page intent."
            ),

            reason=(
                f"The current title contains only "
                f"{title_length} characters."
            )

        )


    # ========================================================
    # TOO LONG
    # ========================================================

    elif title_length > 60:

        add_suggestion(

            suggestions=suggestions,

            category="On-Page SEO",

            severity="high",

            title="Page Title May Be Too Long",

            line=title_line,

            current=title,

            suggestion=(
                "Shorten the title and keep the most "
                "important keyword or topic near the beginning."
            ),

            reason=(
                f"The current title contains "
                f"{title_length} characters."
            )

        )


    # ========================================================
    # GOOD
    # ========================================================

    else:

        add_suggestion(

            suggestions=suggestions,

            category="On-Page SEO",

            severity="good",

            title="Page Title Length Looks Good",

            line=title_line,

            current=title,

            suggestion=(
                "No immediate length change is required. "
                "Verify that the title accurately represents "
                "the page content."
            ),

            reason=(
                f"The title contains "
                f"{title_length} characters."
            )

        )


# ============================================================
# META DESCRIPTION ANALYSIS
# ============================================================

def analyze_meta_description(
    meta_description,
    meta_description_line,
    suggestions
):

    # ========================================================
    # MISSING DESCRIPTION
    # ========================================================

    if not meta_description:

        add_suggestion(

            suggestions=suggestions,

            category="On-Page SEO",

            severity="high",

            title="Missing Meta Description",

            line="Not found",

            current=(
                "No meta description found."
            ),

            suggestion=(
                "Add a unique meta description that "
                "summarizes the page and naturally "
                "includes the primary search topic."
            ),

            reason=(
                "A useful meta description can improve "
                "how the page is represented in search results."
            )

        )

        return


    description_length = len(
        meta_description
    )


    # ========================================================
    # TOO SHORT
    # ========================================================

    if description_length < 120:

        add_suggestion(

            suggestions=suggestions,

            category="On-Page SEO",

            severity="high",

            title="Meta Description Is Short",

            line=meta_description_line,

            current=meta_description,

            suggestion=(
                "Expand the description with the page's "
                "main topic, value proposition and relevant "
                "keywords."
            ),

            reason=(
                f"The current description contains "
                f"{description_length} characters."
            )

        )


    # ========================================================
    # TOO LONG
    # ========================================================

    elif description_length > 160:

        add_suggestion(

            suggestions=suggestions,

            category="On-Page SEO",

            severity="high",

            title="Meta Description May Be Too Long",

            line=meta_description_line,

            current=meta_description,

            suggestion=(
                "Shorten the meta description while keeping "
                "the main topic and value proposition."
            ),

            reason=(
                f"The current description contains "
                f"{description_length} characters."
            )

        )


    # ========================================================
    # GOOD
    # ========================================================

    else:

        add_suggestion(

            suggestions=suggestions,

            category="On-Page SEO",

            severity="good",

            title="Meta Description Length Looks Good",

            line=meta_description_line,

            current=meta_description,

            suggestion=(
                "No immediate length change is required."
            ),

            reason=(
                f"The description contains "
                f"{description_length} characters."
            )

        )


# ============================================================
# HEADING ANALYSIS
# ============================================================

def analyze_headings(
    headings,
    suggestions
):

    h1_list = headings.get(
        "h1",
        []
    )


    # ========================================================
    # NO H1
    # ========================================================

    if not h1_list:

        add_suggestion(

            suggestions=suggestions,

            category="Content Structure",

            severity="high",

            title="Missing H1 Heading",

            line="Not found",

            current=(
                "No H1 heading found."
            ),

            suggestion=(
                "Add one clear H1 heading that describes "
                "the primary topic of the page."
            ),

            reason=(
                "The main heading helps establish the "
                "primary topic and page structure."
            )

        )


    # ========================================================
    # MULTIPLE H1
    # ========================================================

    elif len(h1_list) > 1:

        lines = [

            item.get("line")

            for item in h1_list

        ]


        text_values = [

            item.get("text")

            for item in h1_list

        ]


        add_suggestion(

            suggestions=suggestions,

            category="Content Structure",

            severity="high",

            title="Multiple H1 Headings Found",

            line=", ".join(

                str(line)

                for line in lines

                if line

            ),

            current=" | ".join(

                text_values

            ),

            suggestion=(
                "Use one primary H1 for the main page topic "
                "and organize supporting topics under H2/H3."
            ),

            reason=(
                f"{len(h1_list)} H1 headings were detected."
            )

        )


    # ========================================================
    # SINGLE H1
    # ========================================================

    else:

        h1 = h1_list[0]


        add_suggestion(

            suggestions=suggestions,

            category="Content Structure",

            severity="good",

            title="Single H1 Heading Found",

            line=h1.get("line"),

            current=h1.get("text"),

            suggestion=(
                "Keep the H1 focused on the primary topic "
                "and search intent."
            ),

            reason=(
                "One primary H1 provides a clear page structure."
            )

        )


    # ========================================================
    # H2 CHECK
    # ========================================================

    h2_list = headings.get(
        "h2",
        []
    )


    if not h2_list:

        add_suggestion(

            suggestions=suggestions,

            category="Content Structure",

            severity="low",

            title="No H2 Headings Found",

            line="Not found",

            current=(
                "No H2 headings detected."
            ),

            suggestion=(
                "Consider using descriptive H2 sections "
                "to organize longer content."
            ),

            reason=(
                "Subheadings can improve content structure "
                "and readability, although H2 is not required "
                "on every page."
            )

        )


# ============================================================
# CANONICAL ANALYSIS
# ============================================================

def analyze_canonical(
    canonical,
    canonical_line,
    suggestions
):

    # ========================================================
    # MISSING CANONICAL
    # ========================================================

    if not canonical:

        add_suggestion(

            suggestions=suggestions,

            category="Technical SEO",

            severity="medium",

            title="Canonical Tag Missing",

            line="Not found",

            current=(
                "No canonical tag found."
            ),

            suggestion=(
                "Add a canonical URL in the <head> that "
                "represents the preferred version of this page."
            ),

            reason=(
                "Canonicalization helps search engines "
                "understand the preferred URL when similar "
                "or duplicate URLs exist."
            )

        )


    # ========================================================
    # CANONICAL FOUND
    # ========================================================

    else:

        add_suggestion(

            suggestions=suggestions,

            category="Technical SEO",

            severity="good",

            title="Canonical Tag Found",

            line=canonical_line,

            current=canonical,

            suggestion=(
                "Verify that the canonical URL is the "
                "preferred indexable URL."
            ),

            reason=(
                "A canonical tag was detected."
            )

        )


# ============================================================
# ROBOTS ANALYSIS
# ============================================================

def analyze_robots(
    robots,
    robots_line,
    suggestions
):

    # ========================================================
    # ROBOTS TAG NOT FOUND
    # ========================================================

    if not robots:

        add_suggestion(

            suggestions=suggestions,

            category="Technical SEO",

            severity="low",

            title="Robots Meta Tag Not Found",

            line="Not found",

            current=(
                "No robots meta tag found."
            ),

            suggestion=(
                "Review whether this page needs an explicit "
                "robots directive. For normal indexable pages, "
                "make sure there is no accidental noindex rule."
            ),

            reason=(
                "No robots meta tag was detected. "
                "The absence of this tag is not automatically "
                "an SEO problem."
            )

        )

        return


    robots_lower = robots.lower()


    # ========================================================
    # NOINDEX
    # ========================================================

    if "noindex" in robots_lower:

        add_suggestion(

            suggestions=suggestions,

            category="Technical SEO",

            severity="critical",

            title="Page Contains NOINDEX",

            line=robots_line,

            current=robots,

            suggestion=(
                "If this page should appear in search results, "
                "remove the noindex directive."
            ),

            reason=(
                "The robots directive contains noindex."
            )

        )


    # ========================================================
    # INDEXABLE
    # ========================================================

    else:

        add_suggestion(

            suggestions=suggestions,

            category="Technical SEO",

            severity="good",

            title="Robots Directive Found",

            line=robots_line,

            current=robots,

            suggestion=(
                "Verify that the directive matches the "
                "intended indexing strategy."
            ),

            reason=(
                "A robots meta tag was detected without "
                "a noindex directive."
            )

        )


# ============================================================
# OPEN GRAPH ANALYSIS
# ============================================================

def analyze_og_tags(
    og_tags,
    suggestions
):

    required_og_tags = {

        "og:title": "Page title",

        "og:description": "Page description",

        "og:image": "Social sharing image",

        "og:url": "Canonical page URL",

    }


    existing_properties = {

        tag.get("property")

        for tag in og_tags

    }


    # ========================================================
    # CHECK REQUIRED OG TAGS
    # ========================================================

    for property_name, description in (
        required_og_tags.items()
    ):

        if property_name not in existing_properties:

            add_suggestion(

                suggestions=suggestions,

                category="Social SEO",

                severity="medium",

                title=f"Missing {property_name}",

                line="Not found",

                current=(
                    f"{property_name} is missing."
                ),

                suggestion=(
                    f"Add {property_name} for the "
                    f"{description.lower()}."
                ),

                reason=(
                    "Open Graph metadata improves how the "
                    "page is represented when shared on "
                    "social platforms."
                )

            )


    # ========================================================
    # ALL OG TAGS PRESENT
    # ========================================================

    if all(

        property_name in existing_properties

        for property_name in required_og_tags

    ):

        add_suggestion(

            suggestions=suggestions,

            category="Social SEO",

            severity="good",

            title="Open Graph Tags Found",

            line="Multiple",

            current=(
                "Required Open Graph tags are present."
            ),

            suggestion=(
                "Verify that og:title, og:description, "
                "og:image and og:url accurately represent "
                "the page."
            ),

            reason=(
                "The main Open Graph properties were detected."
            )

        )


# ============================================================
# TWITTER CARD ANALYSIS
# ============================================================

def analyze_twitter_tags(
    twitter_tags,
    suggestions
):

    existing_names = {

        tag.get("name")

        for tag in twitter_tags

    }


    # ========================================================
    # TWITTER CARD MISSING
    # ========================================================

    if "twitter:card" not in existing_names:

        add_suggestion(

            suggestions=suggestions,

            category="Social SEO",

            severity="low",

            title="Twitter Card Type Missing",

            line="Not found",

            current=(
                "twitter:card not found."
            ),

            suggestion=(
                "Add twitter:card, such as "
                "summary_large_image, according to "
                "the desired sharing format."
            ),

            reason=(
                "Twitter/X card metadata can control how "
                "shared links are presented."
            )

        )


    # ========================================================
    # TWITTER CARD FOUND
    # ========================================================

    else:

        card_tag = next(

            (
                tag
                for tag in twitter_tags
                if tag.get("name") == "twitter:card"
            ),

            None

        )


        add_suggestion(

            suggestions=suggestions,

            category="Social SEO",

            severity="good",

            title="Twitter Card Found",

            line=(

                card_tag.get("line")
                if card_tag
                else "Found"

            ),

            current=(

                card_tag.get("content")
                if card_tag
                else "twitter:card"

            ),

            suggestion=(
                "Verify that the selected card type "
                "matches the page content."
            ),

            reason=(
                "A Twitter/X card type was detected."
            )

        )


# ============================================================
# IMAGE ALT ANALYSIS
# ============================================================

def analyze_images(
    images,
    suggestions
):

    # ========================================================
    # NO IMAGES
    # ========================================================

    if not images:

        add_suggestion(

            suggestions=suggestions,

            category="Image SEO",

            severity="good",

            title="No Images Found",

            line="Page images",

            current=(
                "No image elements were detected."
            ),

            suggestion=(
                "If visual content is useful for the page, "
                "consider adding relevant optimized images."
            ),

            reason=(
                "No <img> elements were detected on the page."
            )

        )

        return


    missing_alt = []


    # ========================================================
    # FIND MISSING ALT
    # ========================================================

    for image in images:

        if not image.get(
            "has_alt"
        ):

            missing_alt.append(
                image
            )


    # ========================================================
    # MISSING ALT FOUND
    # ========================================================

    if missing_alt:

        lines = [

            str(
                image.get("line")
            )

            for image in missing_alt

            if image.get("line")

        ]


        add_suggestion(

            suggestions=suggestions,

            category="Image SEO",

            severity="high",

            title="Images Missing ALT Text",

            line=", ".join(lines),

            current=(

                f"{len(missing_alt)} image(s) "
                "without ALT text."

            ),

            suggestion=(
                "Add concise, descriptive ALT text that "
                "explains the image content. Avoid keyword "
                "stuffing."
            ),

            reason=(
                "ALT text improves image accessibility and "
                "helps search engines understand images."
            )

        )


    # ========================================================
    # ALL ALT PRESENT
    # ========================================================

    else:

        add_suggestion(

            suggestions=suggestions,

            category="Image SEO",

            severity="good",

            title="Image ALT Text Found",

            line="Multiple",

            current=(

                f"{len(images)} image(s) analyzed."

            ),

            suggestion=(
                "Continue using descriptive ALT text "
                "where appropriate."
            ),

            reason=(
                "The analyzed images contain ALT text."
            )

        )


# ============================================================
# CONTENT ANALYSIS
# ============================================================

def analyze_content(
    word_count,
    suggestions
):

    # ========================================================
    # VERY THIN CONTENT
    # ========================================================

    if word_count < 300:

        add_suggestion(

            suggestions=suggestions,

            category="Content SEO",

            severity="high",

            title="Page Content May Be Thin",

            line="Page content",

            current=(

                f"{word_count} words detected."

            ),

            suggestion=(
                "Review whether the page sufficiently "
                "answers the user's search intent. Add useful, "
                "original information where genuinely needed."
            ),

            reason=(
                "The extracted visible content is relatively short."
            )

        )


    # ========================================================
    # MODERATE CONTENT
    # ========================================================

    elif word_count < 600:

        add_suggestion(

            suggestions=suggestions,

            category="Content SEO",

            severity="medium",

            title="Content Depth Could Be Reviewed",

            line="Page content",

            current=(

                f"{word_count} words detected."

            ),

            suggestion=(
                "Check whether important subtopics, FAQs, "
                "benefits and supporting information are covered."
            ),

            reason=(
                "The page has moderate visible text content."
            )

        )


    # ========================================================
    # GOOD CONTENT
    # ========================================================

    else:

        add_suggestion(

            suggestions=suggestions,

            category="Content SEO",

            severity="good",

            title="Content Volume Looks Reasonable",

            line="Page content",

            current=(

                f"{word_count} words detected."

            ),

            suggestion=(
                "Focus on relevance, usefulness and search "
                "intent rather than adding text only to "
                "increase word count."
            ),

            reason=(
                "The page contains a substantial amount "
                "of visible text."
            )

        )


# ============================================================
# CATEGORY SCORE
# ============================================================

def calculate_category_scores(
    suggestions
):
    """
    Category-wise SEO score calculate karta hai.

    Har category 100 se start hoti hai.
    """

    categories = {}

    penalties = {

        "critical": 15,

        "high": 8,

        "medium": 4,

        "low": 2,

        "good": 0,

    }


    # ========================================================
    # COLLECT CATEGORIES
    # ========================================================

    for item in suggestions:

        category = item.get(
            "category",
            "Other"
        )

        if category not in categories:

            categories[category] = 100


    # ========================================================
    # APPLY PENALTIES
    # ========================================================

    for item in suggestions:

        category = item.get(
            "category",
            "Other"
        )

        severity = item.get(
            "severity",
            "low"
        )

        penalty = penalties.get(
            severity,
            0
        )

        categories[category] -= penalty


    # ========================================================
    # LIMIT CATEGORY SCORES
    # ========================================================

    for category in categories:

        if categories[category] < 0:

            categories[category] = 0


        if categories[category] > 100:

            categories[category] = 100


    return categories


# ============================================================
# MAIN SEO ANALYZER
# ============================================================

def generate_seo_suggestions(
    seo_data
):

    suggestions = []


    # ========================================================
    # TITLE
    # ========================================================

    analyze_title(

        seo_data.get(
            "title",
            ""
        ),

        seo_data.get(
            "title_line"
        ),

        suggestions

    )


    # ========================================================
    # META DESCRIPTION
    # ========================================================

    analyze_meta_description(

        seo_data.get(
            "meta_description",
            ""
        ),

        seo_data.get(
            "meta_description_line"
        ),

        suggestions

    )


    # ========================================================
    # HEADINGS
    # ========================================================

    analyze_headings(

        seo_data.get(
            "headings",
            {}
        ),

        suggestions

    )


    # ========================================================
    # CANONICAL
    # ========================================================

    analyze_canonical(

        seo_data.get(
            "canonical",
            ""
        ),

        seo_data.get(
            "canonical_line"
        ),

        suggestions

    )


    # ========================================================
    # ROBOTS
    # ========================================================

    analyze_robots(

        seo_data.get(
            "robots",
            ""
        ),

        seo_data.get(
            "robots_line"
        ),

        suggestions

    )


    # ========================================================
    # OPEN GRAPH
    # ========================================================

    analyze_og_tags(

        seo_data.get(
            "og_tags",
            []
        ),

        suggestions

    )


    # ========================================================
    # TWITTER
    # ========================================================

    analyze_twitter_tags(

        seo_data.get(
            "twitter_tags",
            []
        ),

        suggestions

    )


    # ========================================================
    # IMAGES
    # ========================================================

    analyze_images(

        seo_data.get(
            "images",
            []
        ),

        suggestions

    )


    # ========================================================
    # CONTENT
    # ========================================================

    analyze_content(

        seo_data.get(
            "word_count",
            0
        ),

        suggestions

    )


    # ========================================================
    # COUNTS
    # ========================================================

    total = len(
        suggestions
    )


    critical = len([

        item

        for item in suggestions

        if item.get(
            "severity"
        ) == "critical"

    ])


    high = len([

        item

        for item in suggestions

        if item.get(
            "severity"
        ) == "high"

    ])


    medium = len([

        item

        for item in suggestions

        if item.get(
            "severity"
        ) == "medium"

    ])


    low = len([

        item

        for item in suggestions

        if item.get(
            "severity"
        ) == "low"

    ])


    good = len([

        item

        for item in suggestions

        if item.get(
            "severity"
        ) == "good"

    ])


    # ========================================================
    # OVERALL SCORE
    # ========================================================

    score = calculate_seo_score(
        suggestions
    )


    # ========================================================
    # SCORE GRADE
    # ========================================================

    score_grade = get_score_grade(
        score
    )


    # ========================================================
    # CATEGORY SCORES
    # ========================================================

    category_scores = calculate_category_scores(
        suggestions
    )


    # ========================================================
    # RESULT
    # ========================================================

    return {

        "suggestions": suggestions,

        "score": score,

        "score_grade": score_grade,

        "total": total,

        "critical": critical,

        "high": high,

        "medium": medium,

        "low": low,

        "good": good,

        "category_scores": category_scores,

    }