from playwright.sync_api import sync_playwright

def sort_table():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  
        context = browser.new_context()
        page = context.new_page()

        # Navigate to sort table page
        page.goto("https://the-internet.herokuapp.com/tables")
        
        # Sort table by last name
        page.click("text=Last Name")
        print("Table sorted by last name")

        page.click("text=First Name")
        print("Table sorted by first name")

        page.click("text=Email")
        print("Table sorted by email")


        
        print("Table sorted by last name")
        page.screenshot(path="screenshort/sort_table.png")
        browser.close()

if __name__ == "__main__":
    sort_table()