from playwright.sync_api import sync_playwright

def form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  
        context = browser.new_context()
        page = context.new_page()

        # Navigate to login page
        page.goto("https://the-internet.herokuapp.com/login")
        
        # Enter credentials
        page.fill('input[name="username"]', "tomsmith")
        page.fill('input[name="password"]', "SuperSecretPassword!")
        page.click('button[type="submit"]')

        # Verify login successful
        assert "secure" in page.url, "Login failed"
        print("Login successful")

        page.screenshot(path="screnshort/login.png")
        browser.close()

        
if __name__ == "__main__":
    form()
