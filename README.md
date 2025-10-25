# 🕸️ Web Scraper — Image + Class Collector

This small scraper collects image URLs and DOM class names from a webpage and can (optionally) download images into training/validation folders. It uses **Selenium** to render pages (so it can handle JavaScript-injected content) and falls back to **requests + BeautifulSoup** for simple parsing where appropriate.

> ⚠️ **Important:** This scraper does **not** work reliably on regular **Google Search results pages**. Google aggressively blocks automated scraping and often serves images through dynamic blobs, lazy-loading, or via CDNs that require a browser session. Use the scraper on website URLs without CAPTCHAs you control or on sites that allow scraping.

---

## ✨ Features

- ✅ Render pages with Selenium (Chrome) to capture JS-generated `<img>` elements and class attributes  
- 🧠 Heuristic to find the **dominant image class** in a page and collect image `src`s  
- 💾 Save images into `assets/images/training` and `assets/images/validation` with indexed filenames  
- 🧪 Optionally validate images with **Pillow** before saving  
- 📊 Produces **class-frequency counts** (useful for debugging and building selectors)

---

## 📦 Requirements

- Python 3.8+
- Install dependencies with `pip`:

```bash
git clone https://github.com/anthonycradockwatson/web_scraper.git
pip -m venv .venv
pip install -r requirements.txt
````
Then simply activate the venv and run the function, inputting whichever URL you want to scrape as the argument, ie:
````python
web_scraper("https://www.pexels.com/search/car%20rears/")
````

