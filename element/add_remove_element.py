from playwright.sync_api import sync_playwright

def add_remove_element():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  
        context = browser.new_context()
        page = context.new_page()

        # Navigate to add remove element page
        page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
        
        # Add element
        page.click("text=Add Element")
        print("Element added")
        
        # Remove element
        page.click("text=Delete")
        print("Element removed")
        
        page.screenshot(path="screenshort/add_remove_element.png")
        browser.close()

if __name__ == "__main__":
    add_remove_element()

    