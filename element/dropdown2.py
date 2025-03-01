from playwright.sync_api import sync_playwright

def test_dropdown2():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://qa-practice.netlify.app/dropdowns")
        page.wait_for_load_state("load") 
        

        try:
         
            dropdown = page.locator('select[name="country"]')
            dropdown.wait_for(state="visible", timeout=60000)  


            dropdown.select_option(value="Cambodia")
            print("Country selected successfully.")
        
        except Exception as e:
            print("Error:", e)

            page.screenshot(path="error_screenshot.png")
        
        finally:
            browser.close()

if __name__ == "__main__":
    test_dropdown2()
