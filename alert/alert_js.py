from playwright.sync_api import sync_playwright

def alert_js():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  
        context = browser.new_context()
        page = context.new_page()

        # Navigate to alert page
        page.goto("https://the-internet.herokuapp.com/javascript_alerts")
        
        # Set up dialog event listener
        page.on("dialog", lambda dialog: dialog.accept())

        # Click on JS Alert button
        page.click("text=Click for JS Alert")
        print("JS Alert clicked")
        
        # Click on JS Confirm button
        page.click("text=Click for JS Confirm")
        print("JS Confirm clicked")
        
        # Click on JS Prompt button
        page.click("text=Click for JS Prompt")
        print("JS Prompt clicked")
        
        page.screenshot(path="screenshort/alert_js.png")
        browser.close()

if __name__ == "__main__":
    alert_js()