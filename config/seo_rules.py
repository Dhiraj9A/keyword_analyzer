SEO_CATEGORIES = {
    "technical_seo": {
        "max": 20
    },
    "on_page_seo": {
        "max": 25
    },
    "content_quality": {
        "max": 15
    },
    "semantic_html": {
        "max": 10
    },
    "links": {
        "max": 10
    },
    "images": {
        "max": 5
    },
    "structured_data": {
        "max": 5
    },
    "mobile_ux": {
        "max": 5
    },
    "performance": {
        "max": 5
    }
}


SEO_RULES = {

    "title_missing": {
        "category": "on_page_seo",
        "penalty": 7,
        "priority": "P0"
    },

    "title_too_short": {
        "category": "on_page_seo",
        "penalty": 2,
        "priority": "P2"
    },

    "meta_description_missing": {
        "category": "on_page_seo",
        "penalty": 4,
        "priority": "P1"
    },

    "canonical_missing": {
        "category": "technical_seo",
        "penalty": 4,
        "priority": "P1"
    },

    "h1_missing": {
        "category": "on_page_seo",
        "penalty": 5,
        "priority": "P1"
    },

    "multiple_h1": {
        "category": "on_page_seo",
        "penalty": 2,
        "priority": "P2"
    },

    "images_missing_alt": {
        "category": "images",
        "penalty": 1,
        "priority": "P2"
    },

    "images_missing_dimensions": {
        "category": "images",
        "penalty": 0.5,
        "priority": "P3"
    },

    "viewport_missing": {
        "category": "mobile_ux",
        "penalty": 3,
        "priority": "P1"
    },

    "lang_missing": {
        "category": "technical_seo",
        "penalty": 1,
        "priority": "P2"
    },

    "main_missing": {
        "category": "semantic_html",
        "penalty": 2,
        "priority": "P2"
    },

    "internal_links_low": {
        "category": "links",
        "penalty": 2,
        "priority": "P2"
    },

    "generic_anchor_text": {
        "category": "links",
        "penalty": 1,
        "priority": "P3"
    },

    "structured_data_missing": {
        "category": "structured_data",
        "penalty": 2,
        "priority": "P2"
    }
}
