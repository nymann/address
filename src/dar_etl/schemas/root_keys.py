from enum import Enum


class Root(Enum):
    addresses = "AdresseList"
    address_points = "AdressepunktList"
    house_numbers = "HusnummerList"
    named_roads = "NavngivenVejList"
    q1 = "NavngivenVejKommunedelList"
    q2 = "NavngivenVejPostnummerList"
    q3 = "NavngivenVejSupplerendeBynavnList"
    postal_codes = "PostnummerList"
    q4 = "SupplerendeBynavnList"
