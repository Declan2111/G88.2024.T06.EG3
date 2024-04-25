


class AccessManager:
    def __init__(self):
        class __AccessManager:
            def __init__(self):
                pass
            def request_access_code(self, id_card, name_surname, access_type, email_address, days):
                pass
            def get_access_key(self, keyfile):
                pass

            def open_door(self, key):
                pass

    __instance = None

    def __new__(_cls_):
        if not AccessManager.__instance:
            AccessManager.__instance = AccessManager.__AccessManager()
        return AccessManager.__instance



