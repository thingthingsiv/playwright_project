from playwright.sync_api import sync_playwright

def test_addcart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  
        context = browser.new_context(storage_state="auth.json")  
        page = context.new_page()  
        
        page.goto("https://www.saucedemo.com/inventory.html")
    
        # Add to cart
        page.click('button[id="add-to-cart-sauce-labs-backpack"]')
        page.click('button[id="add-to-cart-sauce-labs-bike-light"]')
        page.click('button[id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        page.click('button[id="add-to-cart-sauce-labs-fleece-jacket"]')
        page.click('button[id="add-to-cart-sauce-labs-onesie"]')
        page.click('button[id="add-to-cart-test.allthethings()-t-shirt-(red)"]')

        # Verify cart
        page.click('a[class="shopping_cart_link"]')
        assert "cart.html" in page.url, "Cart empty"
        
        print("Cart not empty")
        browser.close()

if __name__ == "__main__":
    test_addcart()