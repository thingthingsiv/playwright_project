from playwright.sync_api import sync_playwright

def entry_ad():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  
        context = browser.new_context()
        page = context.new_page()

        # Navigate to entry ad page
        page.goto("https://the-internet.herokuapp.com/entry_ad")
        
        # Close modal
        page.click("text=Close")
        print("Modal closed")
        
        page.screenshot(path="screenshort/entry_ad.png")
        browser.close()

if __name__ == "__main__":
    entry_ad()