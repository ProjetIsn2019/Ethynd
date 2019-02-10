# -*- coding: utf-8 -*-
"""Les listes constantes tuiles
Tuiles avec interaction
Tuiles avec collision
Tuiles d'eau
Etc.
(A IMPORTER)
"""
tuiles = {}  # Dictionnaire des tuiles. "numero: image", sera défini plus tard
tuiles_collisions = (  # Liste des blocs sur lesquels on ne peux pas aller
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
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    ""
)

eau = (
    "283",
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
    "165"
)
