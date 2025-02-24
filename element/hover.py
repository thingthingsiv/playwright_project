from playwright.sync_api import sync_playwright 


def hover():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  
        context = browser.new_context()
        page = context.new_page()

        # Navigate to hover page
        page.goto("https://the-internet.herokuapp.com/hovers")
        
        # Hover over first image
        page.hover('div.figure:nth-child(3) img')
        # verify hover1
        assert "user1" in page.inner_text('div.figure:nth-child(3) h5')

        # Hover over second image
        page.hover('div.figure:nth-child(4) img')  
        # verify hover2
        assert "user2" in page.inner_text('div.figure:nth-child(4) h5')
        
        print("Hover successful")
        page.screenshot(path="screenshort/hover.png")
        browser.close()

if __name__ == "__main__":
    hover()