from playwright.sync_api import sync_playwright

URL = "https://www.tudogostoso.com.br/sitemap-1.xml"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  #debug
    context = browser.new_context()
    page = context.new_page()

    page.goto(URL, timeout=60000)

    page.wait_for_load_state("networkidle")

    content = page.inner_text("body")

    with open("resultado.html", "w", encoding="utf-8") as f:
        f.write(content)

    print("200 ok")

    browser.close()
