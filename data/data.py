import requests
class Data:
    GET_LIST_USERS = requests.get('https://reqres.in/api/users?page=2').json()
    GET_SINGLE_USER = requests.get('https://reqres.in/api/users/2').json()
    GET_USER_SINGLE_NOT_FOUND = requests.get('https://reqres.in/api/users/23').json()
    GET_LIST_RESOURCE = requests.get('https://reqres.in/api/unknown').json()
    GET_SINGLE_RESOURCE = requests.get('https://reqres.in/api/unknown/2').json()
    GET_SINGLE_RESOURCE_NOT_FOUND = requests.get('https://reqres.in/api/unknown/23').json()
    POST_CREATE = '"name":"morpheus","job":"leader"'
    PUT_UPDATE = '"name":"morpheus","job":"zionresident","'
    PATCH_UPDATE = '"name":"morpheus","job":"zionresident","'
    DELETE = ""
    POST_REGISTER_SUCCESSFUL = '"id":4,"token":"QpwL5tke4Pnpja7X4"'
    POST_REGISTER_UNSUCCESSFUL = '"error":"Missingpassword"'
    POST_LOGIN_SUCCESSFUL = '"token":"QpwL5tke4Pnpja7X4"'
    POST_LOGIN_UNSUCCESSFUL = '"error":"Missingpassword"'
