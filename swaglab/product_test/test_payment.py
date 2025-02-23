from playwright.sync_api import sync_playwright

def test_payment():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  
        context = browser.new_context(storage_state="auth.json")  
        page = context.new_page()  
        
        page.goto("https://www.saucedemo.com/cart.html")
    
        # Checkout
        page.click('button[id="checkout"]')
        
        # Enter shipping details
        page.fill('input[placeholder="First Name"]', "John")
        page.fill('input[placeholder="Last Name"]', "Doe")
        page.fill('input[placeholder="Zip/Postal Code"]', "12345")
        page.click('input[type="submit"]')
        
        # Verify payment page
        assert "checkout-step-two.html" in page.url, "Checkout failed"
        
        print("Checkout successful")
        page.screenshot(path="checkout:payment" + ".png")
        browser.close()

if __name__ == "__main__":
    test_payment()