from pages.checkout_step_two_page import CheckoutStepTwoPage

class TestCart:

    def test_checkout_btn(self,loaded_cart):
        checkout = loaded_cart.click_checkout_btn()

        assert "/checkout-step-one" in checkout.driver.current_url

    def test_valid_checkout_info(self,loaded_cart):
        checkout = loaded_cart.click_checkout_btn()
        checkout.enter_info("john", "doe", "12345")

        assert "/checkout-step-two" in checkout.driver.current_url

    def test_checkout_without_firstname(self,loaded_cart):
        checkout = loaded_cart.click_checkout_btn()
        result = checkout.enter_info("", "doe", "12345")

        assert result.is_error_displayed()
        assert "First Name is required" in result.get_error_messages()

    def test_checkout_without_lastname(self,loaded_cart):
        checkout = loaded_cart.click_checkout_btn()
        checkout.enter_info("john", "", "12345")

        assert "required" in checkout.get_error_messages()

    def test_checkout_without_postal_code(self,loaded_cart):
        checkout = loaded_cart.click_checkout_btn()
        checkout.enter_info("john", "doe", "")

        assert "required" in checkout.get_error_messages()

    def test_checkout_step_two_finish_btn(self,loaded_cart):
        checkout_one = loaded_cart.click_checkout_btn()
        checkout_one.enter_info("john", "doe", "12345")

        checkout_two = CheckoutStepTwoPage(checkout_one.driver)
        checkout_two.click_finish_btn()

        assert "/checkout-complete" in checkout_two.driver.current_url