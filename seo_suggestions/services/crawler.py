from playwright.sync_api import sync_playwright


def crawl_page(url):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page(
            viewport={
                "width": 1440,
                "height": 900
            }
        )

        try:

            response = page.goto(

                url,

                wait_until="networkidle",

                timeout=60000
            )


        except Exception as e:

            browser.close()

            raise Exception(
                f"Unable to load URL: {str(e)}"
            )


        data = page.evaluate(
            """
            () => {

                const images =
                    [...document.images].map(
                        (img, index) => ({

                            index: index,

                            src:
                                img.currentSrc ||
                                img.src,

                            alt:
                                img.getAttribute(
                                    "alt"
                                ),

                            width:
                                img.getAttribute(
                                    "width"
                                ),

                            height:
                                img.getAttribute(
                                    "height"
                                ),

                            loading:
                                img.getAttribute(
                                    "loading"
                                ),

                            naturalWidth:
                                img.naturalWidth,

                            naturalHeight:
                                img.naturalHeight
                        })
                    );


                const links =
                    [
                        ...document.querySelectorAll("a")
                    ].map(a => ({

                        href:
                            a.href,

                        text:
                            a.innerText.trim(),

                        rel:
                            a.getAttribute("rel"),

                        target:
                            a.getAttribute("target")
                    }));


                const headings =
                    [
                        ...document.querySelectorAll(
                            "h1,h2,h3,h4,h5,h6"
                        )
                    ].map(h => ({

                        tag:
                            h.tagName.toLowerCase(),

                        text:
                            h.innerText.trim()
                    }));


                const jsonLd =
                    [
                        ...document.querySelectorAll(
                            'script[type="application/ld+json"]'
                        )
                    ].map(
                        script =>
                            script.textContent.trim()
                    );


                return {

                    url:
                        location.href,


                    title:
                        document.title || null,


                    meta_description:

                        document
                            .querySelector(
                                'meta[name="description"]'
                            )
                            ?.getAttribute(
                                "content"
                            ) || null,


                    canonical:

                        document
                            .querySelector(
                                'link[rel="canonical"]'
                            )
                            ?.getAttribute(
                                "href"
                            ) || null,


                    robots:

                        document
                            .querySelector(
                                'meta[name="robots"]'
                            )
                            ?.getAttribute(
                                "content"
                            ) || null,


                    viewport:

                        document
                            .querySelector(
                                'meta[name="viewport"]'
                            )
                            ?.getAttribute(
                                "content"
                            ) || null,


                    lang:

                        document.documentElement
                            .getAttribute("lang")
                            || null,


                    h1_count:

                        document.querySelectorAll(
                            "h1"
                        ).length,


                    h1_text:

                        [
                            ...document.querySelectorAll(
                                "h1"
                            )
                        ].map(
                            h =>
                                h.innerText.trim()
                        ),


                    headings,


                    images,


                    links,


                    json_ld:


                        jsonLd,


                    word_count:

                        (
                            document.body?.innerText
                            || ""
                        )
                        .trim()
                        .split(/\\s+/)
                        .filter(Boolean)
                        .length,


                    text_content:

                        document.body?.innerText
                        || "",


                    semantic: {

                        header:
                            !!document.querySelector(
                                "header"
                            ),

                        nav:
                            !!document.querySelector(
                                "nav"
                            ),

                        main:
                            !!document.querySelector(
                                "main"
                            ),

                        section:
                            !!document.querySelector(
                                "section"
                            ),

                        article:
                            !!document.querySelector(
                                "article"
                            ),

                        aside:
                            !!document.querySelector(
                                "aside"
                            ),

                        footer:
                            !!document.querySelector(
                                "footer"
                            )
                    },


                    open_graph: {

                        title:

                            document.querySelector(
                                'meta[property="og:title"]'
                            )?.content
                            || null,


                        description:

                            document.querySelector(
                                'meta[property="og:description"]'
                            )?.content
                            || null,


                        image:

                            document.querySelector(
                                'meta[property="og:image"]'
                            )?.content
                            || null,


                        url:

                            document.querySelector(
                                'meta[property="og:url"]'
                            )?.content
                            || null
                    },


                    twitter: {

                        card:

                            document.querySelector(
                                'meta[name="twitter:card"]'
                            )?.content
                            || null,


                        title:

                            document.querySelector(
                                'meta[name="twitter:title"]'
                            )?.content
                            || null
                    }
                }
            }
            """
        )


        html = page.content()


        status_code = (

            response.status

            if response

            else None
        )


        browser.close()


        return {

            "url": url,

            "http_status":
                status_code,

            "html":
                html,

            "data":
                data
        }