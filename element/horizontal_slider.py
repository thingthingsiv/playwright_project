from playwright.sync_api import sync_playwright

def horizontal_slider():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  
        context = browser.new_context()
        page = context.new_page()

        # Navigate to horizontal slider page
        page.goto("https://the-internet.herokuapp.com/horizontal_slider")
        
        # Move slider to the right
        page.evaluate('document.querySelector(\'input[type="range"]\').value = "4"')
        
        print("Slider moved to the right")
        page.screenshot(path="screenshort/horizontal_slider.png")
        browser.close()

if __name__ == "__main__":
    horizontal_slider()

    