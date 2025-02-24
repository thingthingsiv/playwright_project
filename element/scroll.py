from playwright.async_api import async_playwright

async def scroll():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate to scroll page
        await page.goto("https://the-internet.herokuapp.com/infinite_scroll")

        # Scroll to the bottom of the page
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

        # Scroll to the top of the page
        await page.evaluate("window.scrollTo(0, 0)")

        print("Scroll successful")
        await page.screenshot(path="screenshort/scroll.png")
        await browser.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(scroll()) 