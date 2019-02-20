"""
API OpenfoodFacts management module
"""

import requests

from ._glob import Glob


class ApiRest:

    def __init__(self, log):
        """
        ## Initialize Class Apirest ##
        :param log:
            logging module
        """
        self.log = log
        info_api = Glob.infoApi
        self.tag_0 = (
            f"&tagtype_0={info_api['tagtype_0']}"
            f"&tag_contains_0={info_api['tag_contains_0']}"
            f"&tag_0="
        )
        self.cmdRequest = (
            f"{info_api['https']}&action={info_api['action']}"
            f"&sort_by={info_api['sort_by']}"
            f"&page_size={info_api['page_size']}"
            f"&json={info_api['json']}"
        )
        self.data = 'products'

    def get_request(self, tag):
        """
        ## Execute API request ##
        :param tag:
            value of the reseach
        :return:
            data in json format
        """
        r = requests.get(f"{self.cmdRequest}{self.tag_0}{tag}")
        self.log.debug("=============================================================\n"
                       "# Status Code: %s #\n"
                       "# Headers: %s #\n" % (r.status_code, r.headers['content-type']))
        return r.json()[self.data]

    def convert_data(self, result, data_name):
        """
        ## Conversion of values ##
        :param result:
            List of the different values
        :param data_name:
            Name of the values
        :return:
            List of values to be included in the table
        """
        val_product = []
        for nb in range(len(data_name)):
            try:
                case = result[data_name[nb]]
                if type(case) is not list:
                    rep_val = {"'": " ", '<span class="allergen">': '', '</span>': '', '\r': ' '}
                    if case != "" and case is not None:
                        for key, value in rep_val.items():
                            case = case.strip().replace(key, value)
                    else:
                        case = "NULL"
                else:
                    case = ", ".join(case)
            except KeyError as err:
                case = "NULL"
                self.log.debug("*** Valeur absente dans OFF: %s", err)
            val_product.append(case)
        return val_product
