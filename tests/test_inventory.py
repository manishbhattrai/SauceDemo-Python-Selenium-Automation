from pages.inventory_page import InventoryPage

class TestInventory:

    def test_product_link(self,logged_in_page):
        inventory = InventoryPage(logged_in_page.driver)
        inventory.click_product_title()
        path = inventory.get_current_path()

        assert "inventory-item" in path

    def test_sort_name_az(self,logged_in_page):
        inventory = InventoryPage(logged_in_page.driver)
        inventory.dropdown_for_ascending_alphabet()

        assert inventory.is_sorted_by_name_asc()

    def test_sort_name_za(self,logged_in_page):
        inventory = InventoryPage(logged_in_page.driver)
        inventory.dropdown_for_descending_alphabet()

        assert inventory.is_sorted_by_name_desc()

    def test_sort_price_high_low(self,logged_in_page):
        inventory = InventoryPage(logged_in_page.driver)
        inventory.dropdown_for_high_price()

        assert inventory.is_sorted_by_price_high_low()

    def test_sort_price_low_high(self,logged_in_page):
        inventory = InventoryPage(logged_in_page.driver)
        inventory.dropdown_for_low_price()

        assert inventory.is_sorted_by_price_low_high()