# Playwright search_product test

This project contains a pytest-style Playwright test that searches for "T-shirts" on
http://www.automationpractice.pl/index.php and asserts the product "Faded Short Sleeve T-shirts"
is present in the search results.

Files:
- `AITesting/search_product.py` - test script using Playwright sync API (headed mode)
- `requirements.txt` - packages to install (playwright, pytest)

Quick start (PowerShell):

```powershell
# from project root
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m pytest -q AITesting\search_product.py -s
```

If the test times out, a screenshot will be saved to `AITesting/search_failure_screenshot.png`.

