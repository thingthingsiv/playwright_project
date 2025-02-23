from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  
        context = browser.new_context()  
        page = context.new_page()  
        
        page.goto("https://www.saucedemo.com/")
    
        # Enter credentials
        page.fill('input[placeholder="Username"]', "standard_user")
        page.fill('input[placeholder="Password"]', "secret_sauce")
        page.click('input[type="submit"]')

        # Verify login successful
        assert "inventory.html" in page.url, "Login failed"

        # Save session state
        context.storage_state(path="auth.json")

        print("Login successful")
        browser.close()

if __name__ == "__main__":
    test_login()
