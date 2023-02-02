from Settings.settings import *



gameChoosingButtons = [
    [
        types.InlineKeyboardButton(text="Thief", callback_data="thief"),
        types.InlineKeyboardButton(text="TicTacToe", callback_data="tic")
    ]
]

gameChoosingMenu = types.InlineKeyboardMarkup(inline_keyboard = gameChoosingButtons)

characterChoosingButtons = [
    [
        types.InlineKeyboardButton(text="X", callback_data="X"),
        types.InlineKeyboardButton(text="0", callback_data="0")
    ]
]




parsingButtons = [
    [types.InlineKeyboardButton(text="Parse/Спарсить", callback_data="parse")]
]
parseMenu = types.InlineKeyboardMarkup(inline_keyboard = parsingButtons)

languages = [
    [
        types.InlineKeyboardButton(text="Русский перевод", callback_data="russian"),
        types.InlineKeyboardButton(text="Анлийский", callback_data="english")
    ]
]

translations = types.InlineKeyboardMarkup(inline_keyboard = languages)

englishAuthors = [
    [
        types.InlineKeyboardButton(text="Pantera", callback_data="pantera"),
        types.InlineKeyboardButton(text="Metallica", callback_data="metallica")
    ]
]
englishBandsMenu = types.InlineKeyboardMarkup(inline_keyboard = englishAuthors)

lyricsPantera = [
        [
            types.InlineKeyboardButton(text="Walk", callback_data="walk"),
            types.InlineKeyboardButton(text="i'm Broken", callback_data="im-broken"),
            types.InlineKeyboardButton(text="10's", callback_data="10s"),
        ],
        [
            types.InlineKeyboardButton(text="13 Steps Nowhere", callback_data="13-steps-nowhere"),
            types.InlineKeyboardButton(text="25 Years", callback_data="25-years"),
            types.InlineKeyboardButton(text="5 Minutes Alone", callback_data="5-minutes-alone"),
        ],
        [
            types.InlineKeyboardButton(text="A New Level", callback_data="new-level"),
            types.InlineKeyboardButton(text="All over Tonight", callback_data="all-over-tonight"),
            types.InlineKeyboardButton(text="Avoid The Light", callback_data="avoid-light"),
        ],
        [
             types.InlineKeyboardButton(text="Becoming", callback_data="becoming"),
             types.InlineKeyboardButton(text="Biggest Part Me", callback_data="biggest-part-me"),
            types.InlineKeyboardButton(text="Burnnn", callback_data="burnnn"),
        ],
        [
            types.InlineKeyboardButton(text="By Demons Be Driven", callback_data="demons-be-driven"),
            types.InlineKeyboardButton(text="Cat Scratch Fever", callback_data="cat-scratch-fever"),
            types.InlineKeyboardButton(text="Cemetery Gates", callback_data="cemetery-gates"),
        ],
        [
            types.InlineKeyboardButton(text="Clash With Reality", callback_data="clash-reality"),
            types.InlineKeyboardButton(text="Come-on Eyes", callback_data="come-eyes"),
            types.InlineKeyboardButton(text="D*G*T*T*M", callback_data="dgttm"),
        ],


    ]

lyricsMenuPantera = types.InlineKeyboardMarkup(inline_keyboard=lyricsPantera)
lyricsMetallica = [
        [
            types.InlineKeyboardButton(text="Enter Sandman", callback_data="enter-sandman"),
            types.InlineKeyboardButton(text="Master Of Puppets ", callback_data="Metallica-Master-Puppets"),
            types.InlineKeyboardButton(text="Nothing Else Matters ", callback_data="Metallica-Nothing-else-matters"),
        ],
        [
            types.InlineKeyboardButton(text="Unforgiven", callback_data="unforgiven"),
            types.InlineKeyboardButton(text="The Unforgiven 2", callback_data="Metallica-Unforgiven-2"),
            types.InlineKeyboardButton(text="The Unforgiven 3", callback_data="Metallica-Unforgiven-III"),
        ],
        [
            types.InlineKeyboardButton(text="...And Justice For All", callback_data="Metallica-One"),
            types.InlineKeyboardButton(text="One", callback_data="and-justice-all"),

        ],

    ]

lyricsMenuMetallica = types.InlineKeyboardMarkup(inline_keyboard=lyricsMetallica)

gameButtons = [
    [
        types.InlineKeyboardButton(text = "10000", callback_data = "set_10000"),
        types.InlineKeyboardButton(text = "100000", callback_data = "set_100000"),
        types.InlineKeyboardButton(text = "1000000", callback_data = "set_1000000")
    ]
]
thiefMenuButtons = [
    [
        types.InlineKeyboardButton(text = "10", callback_data = "theft_10"),
        types.InlineKeyboardButton(text = "100", callback_data = "theft_100"),
        types.InlineKeyboardButton(text = "1000", callback_data = "theft_1000"),
        types.InlineKeyboardButton(text = "10000", callback_data = "theft_10000")
    ]
]

theftMenu = types.InlineKeyboardMarkup(inline_keyboard = thiefMenuButtons)


schekelsgameKeyBoard = types.InlineKeyboardMarkup(inline_keyboard = gameButtons)