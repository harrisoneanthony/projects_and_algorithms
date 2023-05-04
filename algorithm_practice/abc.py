from TikTokApi import TikTokApi
from TikTokApi.browser import set_async_browser
import asyncio

# Create and configure browser instance
async def browser_instance():
    browser = await set_async_browser(headless=True)
    return browser

# Get cookie data
verifyFp = "verify_kx2ee558_BH6fvQVi_cXHF_4lfK_Bimg_hH0lYMCV6Vm6"

# Setup instance
loop = asyncio.get_event_loop()
browser = loop.run_until_complete(browser_instance())
api = TikTokApi(custom_verifyFp=verifyFp, browser=browser, use_test_endpoints=True)

# Get data by hashtag
trending = api.byHashtag('bitcoin')
print(trending)
