from playwright.sync_api import sync_playwright

def file_upload():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  
        context = browser.new_context()
        page = context.new_page()

        # Navigate to file upload page
        page.goto("https://the-internet.herokuapp.com/upload")
        
        # Upload file
        page.set_input_files('input[type="file"]', ["/Users/lychandy/Downloads/sunpaylogo.png"])

        print("File uploaded successfully")

        page.screenshot(path="screenshort/file_upload.png")
        browser.close()

if __name__ == "__main__":
    file_upload()