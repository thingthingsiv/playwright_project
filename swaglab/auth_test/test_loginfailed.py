from playwright.sync_api import sync_playwright

def test_loginfailed():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  
        context = browser.new_context()  
        page = context.new_page()  
        
        page.goto("https://www.saucedemo.com/")
    
        # Enter credentials
        page.fill('input[placeholder="Username"]', "locked_out_user")
        page.fill('input[placeholder="Password"]', "secret_sauce")
        page.click('input[type="submit"]')

        # Verify login failed
        assert "inventory.html" not in page.url, "Login successful"

        print("Login failed",)
        browser.close()

if __name__ == "__main__":
    test_loginfailed()