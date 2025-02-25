from playwright.sync_api import sync_playwright

def exit_intent():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  
        context = browser.new_context()
        page = context.new_page()

        # Navigate to exit intent page
        page.goto("https://the-internet.herokuapp.com/exit_intent")
        
        # Move mouse to the top of the page
        page.mouse.move(0, 0)
        print("Mouse moved to the top of the page")
        
        page.screenshot(path="screenshort/exit_intent.png")
        browser.close()

if __name__ == "__main__":  
    exit_intent()