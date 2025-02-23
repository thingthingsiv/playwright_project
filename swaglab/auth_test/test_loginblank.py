from playwright.sync_api import sync_playwright

def test_loginblank():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  
        context = browser.new_context()  
        page = context.new_page()  
        
        page.goto("https://www.saucedemo.com/")
    
        # Enter credentials
        page.fill('input[placeholder="Username"]', "")
        page.fill('input[placeholder="Password"]', "")
        page.click('input[type="submit"]')

        # Verify login failed
        assert "inventory.html" not in page.url, "Login successful"

        print("Login failed please input the credentials",)
        browser.close()

if __name__ == "__main__":  
    test_loginblank()