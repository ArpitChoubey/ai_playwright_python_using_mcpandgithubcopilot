import time
from playwright.sync_api import TimeoutError


def test_search_product(playwright):
    """Search for 'T-shirts' on the automationpractice site and verify the product appears.

    This version uses the pytest-playwright `playwright` fixture and launches a headed
    Chromium browser so the run is visible.
    """
    # Launch headed browser so the run is visible
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    try:
        print("Navigating to the site...")
        page.goto("http://www.automationpractice.pl/index.php", timeout=30000)

        # Wait for the search input to be ready
        print("Waiting for search input...")
        page.wait_for_selector('input#search_query_top', timeout=15000)

        print("Entering search term and submitting...")
        page.fill('input#search_query_top', 'T-shirts')
        page.click('button[name="submit_search"]')

        # Wait for results to load and check for the expected product
        expected = 'Faded Short Sleeve T-shirts'
        print(f"Waiting for product '{expected}' in results...")

        # Use a locator that targets product names and look for the expected text
        product_locator = page.locator('a.product-name', has_text=expected)
        product_locator.wait_for(timeout=15000)

        # Verify it's visible
        visible_count = product_locator.count()
        print(f"Found {visible_count} matching product(s)")
        assert visible_count > 0, f"Product '{expected}' not found in search results"

        print("Test passed: product found in search results")

    except TimeoutError as e:
        # Surface helpful debugging information on timeout
        page.screenshot(path="AITesting/search_failure_screenshot.png")
        raise AssertionError(f"Timeout waiting for element: {e}") from e
    finally:
        # Keep browser open briefly so tester can see final state, then close
        time.sleep(1.0)
        context.close()
        browser.close()

