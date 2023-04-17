from pom.pages.main_page_ui import MainPage
from data.data import Data


class TestReqresIn:
    def test_list_users_button(self, driver_factory):
        main_page = MainPage(driver_factory)
        output_data = Data
        main_page.open()
        main_page.list_users()
        assert main_page.list_users_response_code() == '200', "Status code doesn't match"
        assert output_data.GET_LIST_USERS == main_page.list_users_data(), "JSON data doesn't match"

    def test_single_user_button(self, driver_factory):
        main_page = MainPage(driver_factory)
        output_data = Data
        main_page.single_user()
        assert main_page.single_user_response_code() == '200', "Status code doesn't match"
        assert output_data.GET_SINGLE_USER == main_page.single_user_data(), "JSON data doesn't match"

    def test_single_user_not_found_button(self, driver_factory):
        main_page = MainPage(driver_factory)
        output_data = Data
        main_page.single_user_not_found()
        assert main_page.single_user_not_found_response_code() == '404', "Status code doesn't match"
        assert output_data.GET_USER_SINGLE_NOT_FOUND == main_page.single_user_not_found_data(), "JSON data doesn't match"

    def test_list_resource_button(self, driver_factory):
        main_page = MainPage(driver_factory)
        output_data = Data
        main_page.list_resource()
        assert main_page.list_resource_response_code() == '200', "Status code doesn't match"
        assert output_data.GET_LIST_RESOURCE == main_page.list_resource_data(), "JSON data doesn't match"

    def test_single_resource_button(self, driver_factory):
        main_page = MainPage(driver_factory)
        output_data = Data
        main_page.single_resource()
        assert main_page.single_resource_response_code() == '200', "Status code doesn't match"
        assert output_data.GET_SINGLE_RESOURCE == main_page.single_resource_data(), "JSON data doesn't match"

    def test_single_resource_not_found_button(self, driver_factory):
        main_page = MainPage(driver_factory)
        output_data = Data
        main_page.single_resource_not_found()
        assert main_page.single_resource_not_found_response_code() == '404', "Status code doesn't match"
        assert output_data.GET_SINGLE_RESOURCE_NOT_FOUND == main_page.single_resource_not_found_data(), "JSON data doesn't match"

    def test_create_button(self, driver_factory):
        main_page = MainPage(driver_factory)
        output_data = Data
        main_page.create()
        assert main_page.create_response_code() == '201', "Status code doesn't match"
        assert output_data.POST_CREATE in main_page.create_data(), "JSON data doesn't match"

    def test_update_button(self, driver_factory):
        main_page = MainPage(driver_factory)
        output_data = Data
        main_page.update()
        assert main_page.update_response_code() == '200', "Status code doesn't match"
        assert output_data.PUT_UPDATE in main_page.update_data(), "JSON data doesn't match"

    def test_patch_update_button(self, driver_factory):
        main_page = MainPage(driver_factory)
        output_data = Data
        main_page.patch_update()
        assert main_page.patch_update_response_code() == '200', "Status code doesn't match"
        assert output_data.PUT_UPDATE in main_page.patch_update_data(), "JSON data doesn't match"

    def test_delete_button(self, driver_factory):
        main_page = MainPage(driver_factory)
        output_data = Data
        main_page.delete()
        assert main_page.delete_response_code() == '204', "Status code doesn't match"
        assert output_data.DELETE in main_page.delete_data(), "JSON data doesn't match"

    def test_register_successful_button(self, driver_factory):
        main_page = MainPage(driver_factory)
        output_data = Data
        main_page.register_successful()
        assert main_page.register_successful_response_code() == '200', "Status code doesn't match"
        assert output_data.POST_REGISTER_SUCCESSFUL in main_page.register_successful_data(), "JSON data doesn't match"

    def test_register_unsuccessful_button(self, driver_factory):
        main_page = MainPage(driver_factory)
        output_data = Data
        main_page.register_unsuccessful()
        assert main_page.register_unsuccessful_response_code() == '400', "Status code doesn't match"
        assert output_data.POST_REGISTER_UNSUCCESSFUL in main_page.register_unsuccessful_data(), "JSON data doesn't match"

    def test_login_successful_button(self, driver_factory):
        main_page = MainPage(driver_factory)
        output_data = Data
        main_page.login_successful()
        assert main_page.login_successful_response_code() == '200', "Status code doesn't match"
        assert output_data.POST_LOGIN_SUCCESSFUL in main_page.login_successful_data(), "JSON data doesn't match"

    def test_login_unsuccessful_button(self, driver_factory):
        main_page = MainPage(driver_factory)
        output_data = Data
        main_page.login_unsuccessful()
        assert main_page.login_unsuccessful_response_code() == '400', "Status code doesn't match"
        assert output_data.POST_LOGIN_UNSUCCESSFUL in main_page.login_unsuccessful_data(), "JSON data doesn't match"

