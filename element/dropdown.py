from playwright.sync_api import sync_playwright

def dropdown():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  
        context = browser.new_context()
        page = context.new_page()

        # Navigate to dropdown page
        page.goto("https://the-internet.herokuapp.com/dropdown")
        
        # Select option 1
        page.select_option('select[id="dropdown"]', "2")

        
        page.screenshot(path="screenshort/dropdown.png")
        browser.close()

if __name__ == "__main__":
    dropdown()