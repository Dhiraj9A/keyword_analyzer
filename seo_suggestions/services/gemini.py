import os
import json
import requests


GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.6-flash"
)


def analyze_with_gemini(
    page_data,
    seo_result
):

    # ==========================================
    # API KEY CHECK
    # ==========================================

    if not GEMINI_API_KEY:

        raise Exception(
            "GEMINI_API_KEY is not configured."
        )


    # ==========================================
    # GEMINI API URL
    # ==========================================

    url = (
        "https://generativelanguage.googleapis.com/"
        "v1beta/models/"
        f"{GEMINI_MODEL}:generateContent"
        f"?key={GEMINI_API_KEY}"
    )


    # ==========================================
    # SEO DATA
    # ==========================================

    current_score = seo_result.get(
        "current_score",
        0
    )

    issues = seo_result.get(
        "issues",
        []
    )


    # ==========================================
    # PROMPT
    # ==========================================

    prompt = f"""
Analyze the SEO of the webpage using the supplied
page data and deterministic SEO analysis.

PAGE DATA:
{json.dumps(
    page_data,
    indent=2,
    ensure_ascii=False
)}

CURRENT SEO SCORE:
{current_score}/100

DETECTED SEO ISSUES:
{json.dumps(
    issues,
    indent=2,
    ensure_ascii=False
)}


Your job is to provide professional,
developer-ready SEO recommendations.

For EVERY important issue provide:

1. Exact issue
2. Why it matters
3. HTML/code location
4. Before code
5. After code
6. Current score
7. Expected score after the fix
8. Score gain
9. Developer action
10. Validation instructions


IMPORTANT RULES:

- Return valid JSON only.
- Do not return Markdown.
- Do not use ```json.
- Do not invent issues that are not supported by
  the supplied webpage data.
- current_score must be {current_score}.
- expected_score must be realistic.
- score_gain must be realistic.
- expected_score cannot exceed 100.
- Keep recommendations actionable for developers.
- If an issue does not require code, explain the
  exact developer action.
- Use high, medium or low priority.
"""


    # ==========================================
    # REQUEST BODY
    # ==========================================

    payload = {

        "contents": [

            {

                "role": "user",

                "parts": [

                    {
                        "text": prompt
                    }

                ]

            }

        ],


        "systemInstruction": {

            "parts": [

                {

                    "text":
                    """
You are a professional technical SEO
analyzer and senior web developer.

Analyze supplied webpage SEO data.

Return ONLY valid JSON.

Never return Markdown.

Your recommendations must be:
- technically accurate
- developer-friendly
- based on supplied data
- realistic regarding SEO score improvement

Each recommendation should clearly explain
what the developer needs to change.
"""
                }

            ]

        },


        "generationConfig": {

            "responseMimeType":
                "application/json",

            "temperature":
                0.2

        }

    }


    # ==========================================
    # SEND REQUEST
    # ==========================================

    try:

        response = requests.post(

            url,

            headers={
                "Content-Type":
                    "application/json"
            },

            json=payload,

            timeout=90
        )


    except requests.exceptions.Timeout:

        raise Exception(
            "Gemini API request timed out."
        )


    except requests.exceptions.RequestException as e:

        raise Exception(
            f"Gemini API connection failed: {str(e)}"
        )


    # ==========================================
    # HTTP ERROR
    # ==========================================

    if response.status_code != 200:

        try:

            error_data = response.json()

        except ValueError:

            error_data = response.text


        raise Exception(

            f"Gemini API error "
            f"{response.status_code}: "
            f"{error_data}"

        )


    # ==========================================
    # PARSE RESPONSE
    # ==========================================

    try:

        response_data = response.json()

    except ValueError:

        raise Exception(
            "Gemini returned invalid HTTP JSON."
        )


    # ==========================================
    # GET GENERATED TEXT
    # ==========================================

    try:

        text = (
            response_data
            ["candidates"][0]
            ["content"]
            ["parts"][0]
            ["text"]
        )

    except (
        KeyError,
        IndexError,
        TypeError
    ):

        raise Exception(

            "Unexpected Gemini response format: "
            + json.dumps(
                response_data,
                ensure_ascii=False
            )

        )


    # ==========================================
    # PARSE AI JSON
    # ==========================================

    try:

        return json.loads(text)

    except json.JSONDecodeError:

        raise Exception(

            "Gemini did not return valid JSON: "
            + text

        )