import requests

from bs4 import BeautifulSoup
from django.shortcuts import render
from urllib.parse import urlparse, urljoin

from .seo_engine import generate_seo_suggestions

from .services.gemini import analyze_with_gemini





from django.views import View


from .services.crawler import crawl_page
from .services.seo_analyzer import calculate_seo_score



# ============================================================
# FIND HTML LINE NUMBER
# ============================================================

def find_html_line(
    html,
    search_text,
    start_line=1
):
    """
    HTML source ke andar search_text ki line number find karta hai.
    """

    if not search_text:
        return None

    lines = html.splitlines()

    for index in range(
        start_line - 1,
        len(lines)
    ):

        if search_text in lines[index]:

            return index + 1

    return None


# ============================================================
# SEO HOME
# ============================================================

def seo_home(request):

    context = {}

    # ========================================================
    # POST REQUEST
    # ========================================================

    if request.method == "POST":

        website_url = request.POST.get(
            "website_url",
            ""
        ).strip()

        context["website_url"] = website_url

        # ====================================================
        # BASIC URL VALIDATION
        # ====================================================

        if not website_url.startswith(
            (
                "http://",
                "https://"
            )
        ):

            context["error"] = (
                "Please enter a valid URL starting with "
                "http:// or https://"
            )

            return render(
                request,
                "seo_suggestions/index.html",
                context
            )

        try:

            # =================================================
            # FETCH WEBSITE
            # =================================================

            response = requests.get(

                website_url,

                timeout=20,

                headers={

                    "User-Agent": (
                        "Mozilla/5.0 "
                        "(Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 "
                        "(KHTML, like Gecko) "
                        "Chrome/151.0.0.0 Safari/537.36"
                    )

                }

            )

            response.raise_for_status()

            html = response.text


            # =================================================
            # PARSE HTML
            # =================================================

            soup = BeautifulSoup(

                html,

                "html.parser"

            )


            # =================================================
            # PAGE TITLE
            # =================================================

            title = ""

            title_line = None

            if soup.title:

                title = soup.title.get_text(

                    " ",

                    strip=True

                )

                title_line = find_html_line(

                    html,

                    "<title"

                )


            # =================================================
            # META DESCRIPTION
            # =================================================

            meta_description = ""

            meta_description_line = None

            meta_description_tag = soup.find(

                "meta",

                attrs={
                    "name": "description"
                }

            )

            if meta_description_tag:

                meta_description = (

                    meta_description_tag
                    .get(
                        "content",
                        ""
                    )
                    .strip()

                )

                meta_description_line = (
                    find_html_line(
                        html,
                        str(
                            meta_description_tag
                        )
                    )
                )


            # =================================================
            # META KEYWORDS
            # =================================================

            meta_keywords = ""

            meta_keywords_line = None

            meta_keywords_tag = soup.find(

                "meta",

                attrs={
                    "name": "keywords"
                }

            )

            if meta_keywords_tag:

                meta_keywords = (

                    meta_keywords_tag
                    .get(
                        "content",
                        ""
                    )
                    .strip()

                )

                meta_keywords_line = (
                    find_html_line(
                        html,
                        str(
                            meta_keywords_tag
                        )
                    )
                )


            # =================================================
            # CANONICAL
            # =================================================

            canonical = ""

            canonical_line = None

            canonical_tag = soup.find(

                "link",

                attrs={
                    "rel": "canonical"
                }

            )

            if canonical_tag:

                canonical = (

                    canonical_tag
                    .get(
                        "href",
                        ""
                    )
                    .strip()

                )

                canonical_line = (
                    find_html_line(
                        html,
                        str(
                            canonical_tag
                        )
                    )
                )


            # =================================================
            # ROBOTS
            # =================================================

            robots = ""

            robots_line = None

            robots_tag = soup.find(

                "meta",

                attrs={
                    "name": "robots"
                }

            )

            if robots_tag:

                robots = (

                    robots_tag
                    .get(
                        "content",
                        ""
                    )
                    .strip()

                )

                robots_line = (
                    find_html_line(
                        html,
                        str(
                            robots_tag
                        )
                    )
                )


            # =================================================
            # HEADINGS H1 - H6
            # =================================================

            headings = {}

            for level in range(
                1,
                7
            ):

                tag_name = f"h{level}"

                tags = soup.find_all(
                    tag_name
                )

                heading_data = []

                for tag in tags:

                    heading_text = tag.get_text(

                        " ",

                        strip=True

                    )

                    heading_line = (
                        find_html_line(
                            html,
                            str(tag)
                        )
                    )

                    heading_data.append({

                        "text": heading_text,

                        "line": heading_line,

                    })

                headings[tag_name] = (
                    heading_data
                )


            # =================================================
            # OPEN GRAPH TAGS
            # =================================================

            og_tags = []

            for tag in soup.find_all(

                "meta",

                attrs={
                    "property": True
                }

            ):

                property_name = tag.get(

                    "property",

                    ""

                ).strip()


                if property_name.startswith(
                    "og:"
                ):

                    og_line = find_html_line(

                        html,

                        str(tag)

                    )

                    og_tags.append({

                        "property": (
                            property_name
                        ),

                        "content": tag.get(

                            "content",

                            ""

                        ).strip(),

                        "line": og_line,

                    })


            # =================================================
            # TWITTER CARD TAGS
            # =================================================

            twitter_tags = []

            for tag in soup.find_all(

                "meta",

                attrs={
                    "name": True
                }

            ):

                tag_name = tag.get(

                    "name",

                    ""

                ).strip()


                if tag_name.startswith(
                    "twitter:"
                ):

                    twitter_line = (
                        find_html_line(
                            html,
                            str(tag)
                        )
                    )

                    twitter_tags.append({

                        "name": tag_name,

                        "content": tag.get(

                            "content",

                            ""

                        ).strip(),

                        "line": twitter_line,

                    })


            # =================================================
            # IMAGES
            # =================================================

            images = []

            for img in soup.find_all(
                "img"
            ):

                src = img.get(

                    "src",

                    ""

                ).strip()


                alt = img.get(
                    "alt"
                )


                absolute_src = urljoin(

                    website_url,

                    src

                )


                image_line = find_html_line(

                    html,

                    str(img)

                )


                images.append({

                    "src": absolute_src,

                    "alt": alt,

                    "has_alt": bool(

                        alt

                        and

                        alt.strip()

                    ),

                    "line": image_line,

                })


            # =================================================
            # LINKS
            # =================================================

            internal_links = []

            external_links = []


            parsed_website_url = urlparse(

                website_url

            )


            base_domain = (

                parsed_website_url.netloc
                .lower()
                .replace(
                    "www.",
                    ""
                )

            )


            for link in soup.find_all(

                "a",

                href=True

            ):

                href = link.get(

                    "href",

                    ""

                ).strip()


                # ------------------------------------------------
                # EMPTY LINK
                # ------------------------------------------------

                if not href:

                    continue


                # ------------------------------------------------
                # SKIP ANCHORS
                # ------------------------------------------------

                if href.startswith(
                    "#"
                ):

                    continue


                # ------------------------------------------------
                # SKIP JAVASCRIPT
                # ------------------------------------------------

                if href.startswith(
                    "javascript:"
                ):

                    continue


                # ------------------------------------------------
                # MAKE ABSOLUTE URL
                # ------------------------------------------------

                absolute_url = urljoin(

                    website_url,

                    href

                )


                parsed_link = urlparse(

                    absolute_url

                )


                # ------------------------------------------------
                # ONLY HTTP / HTTPS
                # ------------------------------------------------

                if parsed_link.scheme not in (

                    "http",

                    "https"

                ):

                    continue


                link_domain = (

                    parsed_link.netloc
                    .lower()
                    .replace(
                        "www.",
                        ""
                    )

                )


                link_text = link.get_text(

                    " ",

                    strip=True

                )


                link_line = find_html_line(

                    html,

                    str(link)

                )


                link_data = {

                    "url": absolute_url,

                    "text": link_text,

                    "line": link_line,

                }


                # ------------------------------------------------
                # INTERNAL / EXTERNAL
                # ------------------------------------------------

                if link_domain == base_domain:

                    internal_links.append(

                        link_data

                    )

                else:

                    external_links.append(

                        link_data

                    )


            # =================================================
            # REMOVE NON-CONTENT ELEMENTS
            # =================================================

            for unwanted in soup([

                "script",

                "style",

                "noscript",

                "svg"

            ]):

                unwanted.decompose()


            # =================================================
            # PAGE TEXT
            # =================================================

            page_text = soup.get_text(

                " ",

                strip=True

            )


            words = page_text.split()


            word_count = len(
                words
            )


            # =================================================
            # SEO DATA
            # =================================================

            seo_data = {

                # ---------------------------------------------
                # BASIC
                # ---------------------------------------------

                "title": title,

                "title_line": title_line,


                "meta_description": (
                    meta_description
                ),

                "meta_description_line": (
                    meta_description_line
                ),


                "meta_keywords": (
                    meta_keywords
                ),

                "meta_keywords_line": (
                    meta_keywords_line
                ),


                "canonical": canonical,

                "canonical_line": (
                    canonical_line
                ),


                "robots": robots,

                "robots_line": (
                    robots_line
                ),


                # ---------------------------------------------
                # HEADINGS
                # ---------------------------------------------

                "headings": headings,


                # ---------------------------------------------
                # SOCIAL
                # ---------------------------------------------

                "og_tags": og_tags,

                "twitter_tags": (
                    twitter_tags
                ),


                # ---------------------------------------------
                # IMAGES
                # ---------------------------------------------

                "images": images,


                # ---------------------------------------------
                # LINKS
                # ---------------------------------------------

                "internal_links": (
                    internal_links
                ),

                "external_links": (
                    external_links
                ),


                # ---------------------------------------------
                # CONTENT
                # ---------------------------------------------

                "word_count": word_count,

            }


            # =================================================
            # GENERATE SEO SUGGESTIONS
            # =================================================

            seo_report = (
                generate_seo_suggestions(
                    seo_data
                )
            )


            # =================================================
            # SUCCESS
            # =================================================

            context.update({

                "success": True,

                "status_code": (
                    response.status_code
                ),

                "seo_data": seo_data,

                "seo_report": seo_report,

            })


        # =====================================================
        # REQUEST TIMEOUT ERROR
        # =====================================================

        except requests.exceptions.Timeout:

            context["error"] = (

                "Website response timeout ho gaya. "
                "Please try again."

            )


        # =====================================================
        # CONNECTION ERROR
        # =====================================================

        except requests.exceptions.ConnectionError:

            context["error"] = (

                "Website se connection establish "
                "nahi ho saka."

            )


        # =====================================================
        # HTTP ERROR
        # =====================================================

        except requests.exceptions.HTTPError as e:

            context["error"] = (

                f"Website HTTP error: {str(e)}"

            )


        # =====================================================
        # REQUEST ERROR
        # =====================================================

        except requests.exceptions.RequestException as e:

            context["error"] = (

                f"Website fetch nahi ho payi: {str(e)}"

            )


        # =====================================================
        # GENERAL ERROR
        # =====================================================

        except Exception as e:

            context["error"] = (

                f"Analysis ke time error aaya: {str(e)}"

            )


    # =========================================================
    # RENDER PAGE
    # =========================================================

    return render(

        request,

        "seo_suggestions/index.html",

        context

    )





# =========================================================
# HOME VIEW
# =========================================================

class HomeView(View):

    template_name = "seo_suggestions/home.html"
    def get(self, request):

        return render(
            request,
            self.template_name,
            {
                "success": True,
                "message":
                    "AI SEO Analyzer is ready."
            }
        )

# =========================================================
# SEO ANALYZER VIEW
# =========================================================

class AnalyzeSEOView(View):

    template_name = "seo_suggestions/analyze.html"

    def get(self, request):

        return render(
            request,
            self.template_name,
            {
                "success": None,
                "url": ""
            }
        )


    def post(self, request):

        # =================================================
        # GET URL FROM HTML FORM
        # =================================================

        url = request.POST.get(
            "url",
            ""
        ).strip()


        # =================================================
        # URL VALIDATION
        # =================================================

        if not url:

            return render(

                request,

                self.template_name,

                {
                    "success": False,

                    "message":
                        "Please enter a website URL.",

                    "url":
                        url
                }
            )


        # =================================================
        # SEO ANALYSIS
        # =================================================

        try:

            # ---------------------------------------------
            # 1. Crawl Website
            # ---------------------------------------------

            page = crawl_page(
                url

            )
            print("page result =================================================")
            print(page)
            print("page result =================================================")

            # ---------------------------------------------
            # 2. Calculate SEO Score
            # ---------------------------------------------

            seo_result = calculate_seo_score(
                page
            )
            print("seo result =================================================")
            print(seo_result)
            print("seo result =================================================")

            # ---------------------------------------------
            # 3. Gemini AI Analysis
            # ---------------------------------------------

            ai_result = analyze_with_gemini(

                page["data"],

                seo_result
            )
            print("ai result =================================================")
            print(ai_result)
            print("ai result =================================================")

            # =================================================
            # TEMPLATE CONTEXT
            # =================================================

            context = {

                "success": True,

                "url": url,


                # -----------------------------------------
                # SEO SCORE
                # -----------------------------------------

                "current_score":
                    seo_result[
                        "current_score"
                    ],


                # -----------------------------------------
                # CATEGORY SCORES
                # -----------------------------------------

                "category_scores":
                    seo_result[
                        "category_scores"
                    ],


                # -----------------------------------------
                # DETECTED ISSUES
                # -----------------------------------------

                "detected_issues":
                    seo_result[
                        "issues"
                    ],


                # -----------------------------------------
                # GEMINI AI
                # -----------------------------------------

                "ai_analysis":
                    ai_result,


                # -----------------------------------------
                # CRAWL INFORMATION
                # -----------------------------------------

                "crawl": {

                    "http_status":
                        page[
                            "http_status"
                        ],

                    "word_count":
                        page[
                            "data"
                        ].get(
                            "word_count",
                            0
                        )
                }

            }


            # =================================================
            # RENDER HTML TEMPLATE
            # =================================================

            return render(

                request,

                self.template_name,

                context
            )


        # =================================================
        # ERROR
        # =================================================

        except Exception as e:

            return render(

                request,

                self.template_name,

                {

                    "success": False,

                    "message":
                        str(e),

                    "url":
                        url
                }
            )