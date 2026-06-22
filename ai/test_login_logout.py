import time
from ai.pages.home_page import HomePage


def test_login_logout_flow(playwright):
    """Full login/logout flow on Demoblaze using POM and headed browser.

    Steps:
    - Open https://www.demoblaze.com/index.html
    - Click Log in, enter credentials, submit
    - Verify 'Log out' link visible and 'Welcome <user>' text appears
    - Click Log out
    - Verify 'Log in' link visible again
    """
    username = "pavanol"
    password = "test@123"

    # Launch headed browser so the flow is visible
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    home = HomePage(page)

    try:
        home.open()
        # ensure page loaded
        page.wait_for_load_state("domcontentloaded", timeout=10000)

        # Click Log in and perform login
        home.login(username, password)

        # Wait briefly for the login to process and UI to update
        # The site may take a moment to authenticate and update the top bar
        page.wait_for_selector(home.LOGOUT_LINK, timeout=10000)

        # Verify logout link visible
        assert page.is_visible(home.LOGOUT_LINK), "Logout link not visible after login"

        # Verify Welcome text
        page.wait_for_selector(home.NAME_OF_USER, timeout=10000)
        welcome_text = page.inner_text(home.NAME_OF_USER)
        assert username in welcome_text, f"Expected welcome text to include '{username}', got '{welcome_text}'"

        # Click logout
        home.click_logout()

        # Wait for login link to reappear
        page.wait_for_selector(home.LOGIN_LINK, timeout=10000)
        assert page.is_visible(home.LOGIN_LINK), "Login link not visible after logout"

    except Exception as e:
        # Save a screenshot for debugging
        page.screenshot(path="ai/login_logout_failure.png")
        raise
    finally:
        # keep the browser open a moment so user can see result, then close
        time.sleep(1.0)
        context.close()
        browser.close()

