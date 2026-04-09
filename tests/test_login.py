

class TestLogin:


    def test_valid_login(self,login_page):
        login_page.login("standard_user","secret_sauce")
        assert "/inventory" in login_page.get_current_url()

    def test_invalid_login(self,login_page):
        login_page.login("wrong_user","wrong_password")
        assert "do not match" in login_page.get_error_messages()

    def test_both_blank_field(self,login_page):
        login_page.login("","")
        assert "required" in login_page.get_error_messages()

    def test_login_only_with_username(self,login_page):
        login_page.login("standard_user","")
        assert "required" in login_page.get_error_messages()

    def test_login_only_with_password(self,login_page):
        login_page.login("","secret_sauce")
        assert "required" in login_page.get_error_messages()

    def test_locked_user_attempt(self,login_page):
        login_page.login("locked_out_user", "secret_sauce")
        assert "locked" in login_page.get_error_messages()

    def test_protected_pages_requires_login(self,login_page):
        login_page.driver.get("https://www.saucedemo.com/inventory.html")
        assert login_page.get_unauthenticated_page() == "Swag Labs"

    def test_authentication_after_login(self,login_page):
        driver = login_page.driver
        login_page.login("standard_user","secret_sauce")
        driver.refresh()
        assert login_page.is_cart_visible()


    def test_logout(self,login_page):
        login_page.login("standard_user","secret_sauce")
        login_page.logout()
        assert login_page.get_unauthenticated_page() == "Swag Labs"
