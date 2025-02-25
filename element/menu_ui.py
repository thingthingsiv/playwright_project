from playwright.sync_api import sync_playwright

def menu_ui():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  
        context = browser.new_context()
        page = context.new_page()

        # Navigate to menu ui page
        page.goto("https://the-internet.herokuapp.com/jqueryui/menu")

        # Hover over enabled menu item
        page.hover("text=Enabled")
        print("Hovered over enabled menu item")

        # Hover over downloads menu item
        page.hover("text=Downloads")
        print("Hovered over downloads menu item")   

        # Hover over pdf menu item  
        page.hover("text=PDF")
        print("Hovered over pdf menu item")

        page.screenshot(path="screenshort/menu_ui.png") 
        browser.close()

if __name__ == "__main__":
    menu_ui()