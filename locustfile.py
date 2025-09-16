from locust.clients import HttpSession


def test_task(session: HttpSession):
    session.base_url = "https://mock-test-target.eu-north-1.locust.cloud"

    session.post("/authenticate", json={"username": "foo", "password": "bar"})

    for product_id in [1, 2, 42, 4711]:
        session.post("/cart/add", json={"productId": product_id})

    with session.post("/checkout/confirm", catch_response=True) as resp:
        if not resp.json().get("orderId"):
            resp.failure("orderId missing")
    resp.raise_for_status()
