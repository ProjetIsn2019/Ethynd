# -*- coding: utf-8 -*-
"""Les listes constantes tuiles
Tuiles avec interaction
Tuiles avec collision
Tuiles d'eau
Etc.
(A IMPORTER)
"""
tuiles = {}  # Dictionnaire des tuiles. "numero: image", sera défini plus tard dans une fonction de chargement (charger.py)
animations = {  # Sert a mettre en place les animations de tuiles. Défini par "numéro_tuile" : "numéro_tuile_suivante"
    "40": "41",
    "41": "42",
    "42": "43",
    "43": "40",
    # Toutes les animations sont séparés par un commentaire vide
    "80": "81",
    "81": "82",
    "82": "83",
    "83": "80",
    #
    "163": "164",
    "164": "165",
    "165": "123",
    "123": "124",
    "124": "125",
    "125": "123",
    #
    "96": "98",
    "98": "100",
    "100": "16",
    "16": "18",
    "18": "20",
    "20": "96",
    #
    "97": "99",
    "99": "101",
    "101": "17",
    "17": "19",
    "19": "21",
    "21": "97",
    #
    "136": "168",
    "138": "140",
    "140": "56",
    "56": "58",
    "58": "60",
    "60": "136",
    #
    "137": "169",
    "139": "141",
    "141": "57",
    "57": "59",
    "59": "61",
    "61": "137",
    #
    "258": "259",
    "259": "260",
    "260": "258",
    #
    "298": "299",
    "299": "300",
    "300": "298",
    #
    "338": "339",
    "339": "340",
    "340": "338",
    #
    "378": "418",
    "418": "459",
    "459": "378",
    #
    "379": "419",
    "419": "460",
    "460": "379",
    #
    "377": "417",
    "417": "458",
    "458": "377",
    #
    "382": "385",
    "385": "388",
    "388": "382",
    #
    "383": "386",
    "386": "389",
    "389": "383",
    #
    "384": "387",
    "387": "390",
    "390": "384",
    #
    "422": "425",
    "425": "428",
    "428": "422",
    #
    "423": "426",
    "426": "429",
    "429": "423",
    #
    "424": "427",
    "427": "430",
    "430": "424",
    #
    "462": "465",
    "465": "468",
    "468": "462",
    #
    "463": "466",
    "466": "469",
    "469": "463",
    #
    "464": "467",
    "467": "470",
    "470": "464",
    #
    "1163": "1165",
    "1165": "1167",
    "1167": "1169",
    "1169": "1171",
    "1171": "1163",
    #
    "1164": "1166",
    "1166": "1168",
    "1168": "1170",
    "1170": "1172",
    "1172": "1164",
    #
    "1203": "1205",
    "1205": "1207",
    "1207": "1209",
    "1209": "1211",
    "1211": "1203",
    #
    "1204": "1206",
    "1206": "1208",
    "1208": "1210",
    "1210": "1212",
    "1212": "1204"
}
collisions = (  # Liste des blocs sur lesquels on ne peux pas aller
    "32",
    "35",
    "37"
    "44",
    "45",
    "70",
    "71",
    "73",
    "74",
    "75",
    "84",
    "85",
    "111",
    "112",
    "114",
    "115",
    "116",
    "76",
    "36",
    "126",
    "127",
    "128",
    "129",
    "130",
    "131",
    "132",
    "133",
    "134",
    "135",
    "102",
    "103",
    "104",
    "142",
    "143",
    "144",
    "151",
    "152",
    "191",
    "192",
    "157",
    "158",
    "197",
    "198",
    "126",
    "127",
    "166",
    "167",
    "168",
    "169",
    "170",
    "171",
    "172",
    "173",
    "174",
    "175",
    "176",
    "177",
    "178",
    "179",
    "180",
    "181",
    "182",
    "183",
    "184",
    "203",
    "204",
    "205",
    "207",
    "208",
    "209",
    "216",
    "217",
    "218",
    "219",
    "220",
    "221",
    "222",
    "223",
    "224",
    "226",
    "227",
    "228",
    "229",
    "230",
    "231",
    "232",
    "235",
    "236",
    "237",
    "238",
    "239",
    "261",
    "266",
    "267",
    "268",
    "269",
    "270",
    "271",
    "272",
    "275",
    "276",
    "277",
    "278",
    "279",
    "315",
    "316",
    "317",
    "318",
    "319",
    "293",
    "294",
    "306",
    "307",
    "308",
    "309",
    "310",
    "333",
    "334",
    "373",
    "374",
    "382",
    "383",
    "384",
    "385",
    "386",
    "387",
    "388",
    "389",
    "390",
    "395",
    "396",
    "397",
    "357",
    "358",
    "351",
    "352",
    "353",
    "371",
    "372",
    "373",
    "374",
    "422",
    "423",
    "424",
    "425",
    "426",
    "427",
    "428",
    "429",
    "430",
    "462",
    "463",
    "464",
    "465",
    "466",
    "467",
    "468",
    "469",
    "470",
    "476",
    "516",
    "484",
    "485",
    "486",
    "409",
    "410",
    "411",
    "412",
    "413",
    "449",
    "450",
    "451",
    "452",
    "453",
    "484",
    "485",
    "486",
    "524",
    "525",
    "526",
    "564",
    "565",
    "566",
    "489",
    "490",
    "491",
    "492",
    "493",
    "532",
    "533",
    "534",
    "572",
    "573",
    "574",
    "521",
    "522",
    "523",
    "560",
    "561",
    "562",
    "563",
    "600",
    "601",
    "602",
    "603",
    "608",
    "609",
    "611",
    "612",
    "640",
    "641",
    "642",
    "643",
    "644",
    "685",
    "686",
    "647",
    "687",
    "651",
    "652",
    "680",
    "682",
    "683",
    "684",
    "720",
    "722",
    "723",
    "724",
    "760",
    "761",
    "725",
    "726",
    "727",
    "763",
    "764",
    "765",
    "766",
    "767",
    "768",
    "729",
    "730",
    "769",
    "770",
    "809",
    "810",
    "803",
    "804",
    "805",
    "806",
    "807",
    "844",
    "845",
    "846",
    "847",
    "815",
    "816",
    "817",
    "855",
    "856",
    "857",
    "895",
    "896",
    "897",
    "861",
    "862",
    "863",
    "864",
    "865",
    "824",
    "826",
    "827",
    "828",
    "829",
    "866",
    "867",
    "868",
    "869",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "86",
    "87",
    "88",
    "89",
    "90",
    "91",
    "92",
    "93",
    "94",
    "95",
    "33",
    "34",
    "355",
    "356",
    "840",
    "841",
    "842",
    "880",
    "881",
    "882",
    "920",
    "921",
    "922",
    "960",
    "961",
    "962",
    "1000",
    "1001",
    "1002",
    "1040",
    "1041",
    "1042",
    "1080",
    "1081",
    "1082",
    "821",
    "822",
    "22",
    "23",
    "24",
    "62",
    "63",
    "64",
    "253",
    "254",
    "898",
    "938",
    "978",
    "1018",
    "1058",
    "1059",
    "1060",
    "1061",
    "1062",
    "1022",
    "982",
    "1098",
    "1099",
    "1100",
    "1101",
    "1102",
    "1328",
    "1329",
    "1248",
    "1249",
    "1288",
    "1289",
    "1283",
    # CI DESSOUS => LES TUILES D'EAU
    "40",
    "41",
    "42",
    "43",
    "80",
    "81",
    "82",
    "83",
    "123",
    "124",
    "125",
    "163",
    "164",
    "165",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "56",
    "57",
    "58",
    "59",
    "61",
    "96",
    "97",
    "98",
    "99",
    "100",
    "101",
    "136",
    "137",
    "138",
    "139",
    "140",
    "141",
    "377",
    "378",
    "379",
    "417",
    "418",
    "419",
    "458",
    "459",
    "460",
    "1761",
    "283",
    "1725",
    "1726",
    "1727",
    "1728",
    "1765",
    "1766",
    "1767",
    "1768"
)
