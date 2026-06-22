from playwright.sync_api import Page, expect


def test_verify_page_url(page: Page):
    page.goto("https://www.osprey.com/")
    expect(page).to_have_url("https://www.osprey.com/")
    assert page.title() == (
        "Osprey Packs | Backpacks, Travel Bags, Hydration Packs & More"
    ), f"Expected title to be 'Osprey Packs | Backpacks, Travel Bags, Hydration Packs & More' but got '{page.title()}'"
    page.fill("input[name='q']", "backpacks")
    assert page.url == "https://www.osprey.com/", f"Expected URL to be 'https://www.osprey.com/' but got '{page.url}'"


def test_page_navigates_to_osprey_domain(page: Page):
    page.goto("https://www.osprey.com/")
    assert page.url == "https://www.osprey.com/"


def test_page_title_matches_expected_value(page: Page):
    page.goto("https://www.osprey.com/")
    assert page.title() == "Osprey Packs | Backpacks, Travel Bags, Hydration Packs & More"


def test_search_field_exists_and_is_fillable(page: Page):
    page.goto("https://www.osprey.com/")
    page.fill("input[name='q']", "backpacks")
    search_input = page.query_selector("input[name='q']")
    assert search_input is not None
    assert search_input.input_value() == "backpacks"


def test_url_remains_unchanged_after_filling_search(page: Page):
    page.goto("https://www.osprey.com/")
    original_url = page.url
    page.fill("input[name='q']", "backpacks")
    assert page.url == original_url


def test_search_field_accepts_multiple_character_types(page: Page):
    page.goto("https://www.osprey.com/")
    search_term = "hiking & travel gear"
    page.fill("input[name='q']", search_term)
    search_input = page.query_selector("input[name='q']")
    assert search_input is not None
    assert search_input.input_value() == search_term


def test_search_field_accepts_empty_string(page: Page):
    page.goto("https://www.osprey.com/")
    page.fill("input[name='q']", "")
    search_input = page.query_selector("input[name='q']")
    assert search_input is not None
    assert search_input.input_value() == ""


def test_page_url_verification_with_expect_api(page: Page):
    page.goto("https://www.osprey.com/")
    expect(page).to_have_url("https://www.osprey.com/")


def test_sequential_searches_maintain_url_stability(page: Page):
    page.goto("https://www.osprey.com/")
    page.fill("input[name='q']", "backpacks")
    page.fill("input[name='q']", "daypacks")
    assert page.url == "https://www.osprey.com/"


def test_page_title_remains_unchanged_during_search_interaction(page: Page):
    page.goto("https://www.osprey.com/")
    expected_title = page.title()
    page.fill("input[name='q']", "backpacks")
    assert page.title() == expected_title


def test_search_input_field_is_visible_and_accessible(page: Page):
    page.goto("https://www.osprey.com/")
    search_input = page.query_selector("input[name='q']")
    assert search_input is not None
    assert search_input.is_visible()

