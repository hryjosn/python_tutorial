import asyncio
from pyppeteer import launch

async def main():
    # browser = await launch(headless=False)
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://24h.pchome.com.tw/prod/DMABIX-A900DZR7B')
    page_text = await page.content()
    print(page_text)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())