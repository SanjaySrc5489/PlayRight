from flask import Flask, jsonify, request
from playwright.sync_api import sync_playwright

app = Flask(__name__)

def scrape_content(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        
        # Wait for the page to load fully (including JS)
        page.wait_for_load_state("networkidle")
        
        # Extract dynamic content using JS selector
        content = page.eval_on_selector("h1", "el => el.innerText")
        
        browser.close()
        return content

@app.route('/scrape', methods=['GET'])
def scrape():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "Please provide a URL parameter."}), 400
    
    try:
        content = scrape_content(url)
        return jsonify({"content": content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return "Playwright Flask App is running!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
