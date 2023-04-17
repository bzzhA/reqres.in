from selenium.webdriver.common.by import By


class MainPageLocators:
    GET_LIST_USERS_BUTTON = (By.XPATH, "//li[@data-id='users']")
    GET_SINGLE_USER_BUTTON = (By.XPATH, "//li[@data-id='users-single']")
    GET_USER_SINGLE_NOT_FOUND_BUTTON = (By.XPATH, "//li[@data-id='users-single-not-found']")
    GET_LIST_RESOURCE_BUTTON = (By.XPATH, "//li[@data-id='unknown']")
    GET_SINGLE_RESOURCE_BUTTON = (By.XPATH, "//li[@data-id='unknown-single']")
    GET_SINGLE_RESOURCE_NOT_FOUND_BUTTON = (By.XPATH, "//li[@data-id='unknown-single-not-found']")
    POST_CREATE_BUTTON = (By.XPATH, "//li[@data-id='post']")
    PUT_UPDATE_BUTTON = (By.XPATH, "//li[@data-id='put']")
    PATCH_UPDATE_BUTTON = (By.XPATH, "//li[@data-id='patch']")
    DELETE_BUTTON = (By.XPATH, "//li[@data-id='delete']")
    POST_REGISTER_SUCCESSFUL_BUTTON = (By.XPATH, "//li[@data-id='register-successful']")
    POST_REGISTER_UNSUCCESSFUL_BUTTON = (By.XPATH, "//li[@data-id='register-unsuccessful']")
    POST_LOGIN_SUCCESSFUL_BUTTON = (By.XPATH, "//li[@data-id='login-successful']")
    POST_LOGIN_UNSUCCESSFUL_BUTTON = (By.XPATH, "//li[@data-id='login-unsuccessful']")
    GET_DELAYED_RESPONSE_BUTTON = (By.XPATH, "//li[@data-id='delay']")

    RESPONSE_CODE = (By.XPATH, "//span[@class='response-code']")
    RESPONSE_CODE_BAD = (By.XPATH, "//span[@class='response-code bad']")
    OUTPUT_RESPONSE = (By.XPATH, "//pre[@data-key='output-response']")


