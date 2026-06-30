# OmegA Computer Education — Website (Streamlit)

## Run locally
```
pip install -r requirements.txt
streamlit run app.py
```

## Deploy (Streamlit Community Cloud — free)
1. Push this folder (`app.py`, `requirements.txt`, `assets/logo.png`) to a GitHub repo.
2. Go to share.streamlit.io, sign in, click "New app".
3. Point it at the repo and set the main file to `app.py`.
4. Deploy — you'll get a public `*.streamlit.app` link.

## Structure
- `app.py` — entire site (single page: hero, courses, languages, emerging tech,
  why-us, CTA, contact form, footer)
- `assets/logo.png` — your OmegA logo, embedded into the page
- `requirements.txt` — just Streamlit

## Customizing
- Course/language/tech lists live near the top of `app.py` as plain Python
  lists/dicts — edit those to add or change content, no HTML knowledge needed.
- Colors and fonts are defined as CSS variables at the top of the `CSS` string
  (`--c1`, `--c2`, `--c3`, `--cyan`, fonts) if you want to retheme.
- The contact form at the bottom currently shows a success message on submit;
  wire it to an email service (e.g. Formspree, SMTP, Google Sheets) when ready
  to receive real leads.
