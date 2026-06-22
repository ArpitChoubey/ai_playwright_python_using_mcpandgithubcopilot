def test_fakestore_product_api(playwright):
    """Send GET to fakestoreapi product 1 and validate response keys and values.

    Uses the pytest-playwright `playwright` fixture and the Playwright APIRequestContext.
    """
    url = "https://fakestoreapi.com/products/1"
    expected_values = {
        "id": 1,
        "price": 109.95,
        "category": "men's clothing",
    }

    # Create an API request context
    request_context = playwright.request.new_context()
    try:
        print(f"Sending GET request to: {url}")
        response = request_context.get(url, timeout=30000)

        # Log complete response body to console (as text)
        try:
            body = response.text()
        except Exception:
            body = "<unable to read body as text>"
        print("Response body:\n", body)

        # Validate status code
        status = response.status
        assert status == 200, f"Expected status 200, got {status}"

        # Parse JSON and validate keys and expected values
        data = response.json()
        # Ensure required keys exist
        required_keys = ["id", "title", "price", "category", "description"]
        for k in required_keys:
            assert k in data, f"Key '{k}' not present in response JSON"

        # Validate expected values (numeric comparison tolerant for floats)
        assert int(data.get("id", -1)) == expected_values["id"], (
            f"Expected id {expected_values['id']}, got {data.get('id')}"
        )

        # Price float comparison with small tolerance
        price = float(data.get("price", -1))
        assert abs(price - expected_values["price"]) < 1e-6, (
            f"Expected price {expected_values['price']}, got {price}"
        )

        category = data.get("category", "")
        assert category == expected_values["category"], (
            f"Expected category '{expected_values['category']}', got '{category}'"
        )
    finally:
        # Clean up the request context
        try:
            request_context.dispose()
        except Exception:
            # Best-effort cleanup
            pass

