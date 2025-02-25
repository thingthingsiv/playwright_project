from playwright.sync_api import sync_playwright

def dynamic_loading():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  
        context = browser.new_context()
        page = context.new_page()

        # Navigate to dynamic loading page
        page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
        
        # Click on start button
        page.click("text=Start")
        print("Start button clicked")
        
        # Wait for loading to complete
        page.wait_for_selector("text=Hello World!")
        print("Loading complete")
        
        page.screenshot(path="screenshort/dynamic_loading.png")
        browser.close()

if __name__ == "__main__":
    dynamic_loading()