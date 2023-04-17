import json
import time

from base.base import Base
from pom.locators.main_page_locators import MainPageLocators


class MainPage(Base):
    main_locators = MainPageLocators

    def list_users(self):
        self.element_is_visible(self.main_locators.GET_LIST_USERS_BUTTON).click()

    def list_users_data(self):
        data = self.get_text(self.main_locators.OUTPUT_RESPONSE)
        return json.loads(data)

    def list_users_response_code(self):
        return self.get_text(self.main_locators.RESPONSE_CODE)

    def single_user(self):
        self.element_is_visible(self.main_locators.GET_SINGLE_USER_BUTTON).click()

    def single_user_response_code(self):
        return self.get_text(self.main_locators.RESPONSE_CODE)

    def single_user_data(self):
        data = self.get_text(self.main_locators.OUTPUT_RESPONSE)
        return json.loads(data)

    def single_user_not_found(self):
        self.element_is_visible(self.main_locators.GET_USER_SINGLE_NOT_FOUND_BUTTON).click()

    def single_user_not_found_response_code(self):
        return self.get_text(self.main_locators.RESPONSE_CODE_BAD)

    def single_user_not_found_data(self):
        data = self.get_text(self.main_locators.OUTPUT_RESPONSE)
        return json.loads(data)

    def list_resource(self):
        self.element_is_visible(self.main_locators.GET_LIST_RESOURCE_BUTTON).click()

    def list_resource_response_code(self):
        return self.get_text(self.main_locators.RESPONSE_CODE)

    def list_resource_data(self):
        data = self.get_text(self.main_locators.OUTPUT_RESPONSE)
        return json.loads(data)

    def single_resource(self):
        self.element_is_visible(self.main_locators.GET_SINGLE_RESOURCE_BUTTON).click()

    def single_resource_response_code(self):
        return self.get_text(self.main_locators.RESPONSE_CODE)

    def single_resource_data(self):
        data = self.get_text(self.main_locators.OUTPUT_RESPONSE)
        return json.loads(data)

    def single_resource_not_found(self):
        self.element_is_visible(self.main_locators.GET_SINGLE_RESOURCE_NOT_FOUND_BUTTON).click()

    def single_resource_not_found_response_code(self):
        return self.get_text(self.main_locators.RESPONSE_CODE_BAD)

    def single_resource_not_found_data(self):
        data = self.get_text(self.main_locators.OUTPUT_RESPONSE)
        return json.loads(data)

    def create(self):
        self.element_is_visible(self.main_locators.POST_CREATE_BUTTON).click()

    def create_response_code(self):
        return self.get_text(self.main_locators.RESPONSE_CODE)

    def create_data(self):
        return str(self.get_text(self.main_locators.OUTPUT_RESPONSE)).replace('\n', '').replace(' ', '')

    def update(self):
        self.element_is_visible(self.main_locators.PUT_UPDATE_BUTTON).click()

    def update_response_code(self):
        time.sleep(1)
        return self.get_text(self.main_locators.RESPONSE_CODE)

    def update_data(self):
        return str(self.get_text(self.main_locators.OUTPUT_RESPONSE)).replace('\n', '').replace(' ', '')

    def patch_update(self):
        self.element_is_visible(self.main_locators.PATCH_UPDATE_BUTTON).click()

    def patch_update_response_code(self):
        return self.get_text(self.main_locators.RESPONSE_CODE)

    def patch_update_data(self):
        return str(self.get_text(self.main_locators.OUTPUT_RESPONSE)).replace('\n', '').replace(' ', '')

    def delete(self):
        self.element_is_visible(self.main_locators.DELETE_BUTTON).click()

    def delete_response_code(self):
        return self.get_text(self.main_locators.RESPONSE_CODE_BAD)

    def delete_data(self):
        return str(self.get_text(self.main_locators.OUTPUT_RESPONSE))

    def register_successful(self):
        self.element_is_visible(self.main_locators.POST_REGISTER_SUCCESSFUL_BUTTON).click()

    def register_successful_response_code(self):
        return self.get_text(self.main_locators.RESPONSE_CODE)

    def register_successful_data(self):
        return str(self.get_text(self.main_locators.OUTPUT_RESPONSE)).replace('\n', '').replace(' ', '')

    def register_unsuccessful(self):
        self.element_is_visible(self.main_locators.POST_REGISTER_UNSUCCESSFUL_BUTTON).click()

    def register_unsuccessful_response_code(self):
        return self.get_text(self.main_locators.RESPONSE_CODE_BAD)

    def register_unsuccessful_data(self):
        return str(self.get_text(self.main_locators.OUTPUT_RESPONSE)).replace('\n', '').replace(' ', '')

    def login_successful(self):
        self.element_is_visible(self.main_locators.POST_LOGIN_SUCCESSFUL_BUTTON).click()

    def login_successful_response_code(self):
        return self.get_text(self.main_locators.RESPONSE_CODE)

    def login_successful_data(self):
        return str(self.get_text(self.main_locators.OUTPUT_RESPONSE)).replace('\n', '').replace(' ', '')

    def login_unsuccessful(self):
        self.element_is_visible(self.main_locators.POST_LOGIN_UNSUCCESSFUL_BUTTON).click()

    def login_unsuccessful_response_code(self):
        return self.get_text(self.main_locators.RESPONSE_CODE_BAD)

    def login_unsuccessful_data(self):
        return str(self.get_text(self.main_locators.OUTPUT_RESPONSE)).replace('\n', '').replace(' ', '')






