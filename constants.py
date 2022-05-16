deviceModels = [
    [0x01, 0xf0], #LEFT_TABLE
    [0x01, 0xf1], #RIGHT_TABLE
    [0x01, 0xf2], #CONTROL_PANEL

    [0x02, 0xf0], #CURTAIN_REAR_LEFT
    [0x02, 0xf1], #CURTAIN_REAR_CENTER
    [0x02, 0xf2], #CURTAIN_REAR_RIGHT

    [0x03, 0xf0], #CURTAIN_FRONT_LEFT
    [0x03, 0xf1], #CURTAIN_FRONT_RIGHT
    [0x03, 0xf2], #TIVI

    [0x04, 0xf0], #LEFT_SEAT_A
    [0x04, 0xf1], #LEFT_SEAT_B
    [0x04, 0xf2], #LIGHT_4X

    [0x05, 0xf0], #RIGHT_SEAT_A
    [0x05, 0xf1], #RIGHT_SEAT_B
    [0x05, 0xf2], #LIGHT_SIDE

    [0x06, 0xf0], #LIGHT_CEILING
    [0x06, 0xf1], #LIGHT_DRAWERS
    [0x06, 0xf2]  #DO NOT USE
]

INDEX_LEFT_SEAT_A = 9
INDEX_LEFT_SEAT_B = 10
INDEX_RIGHT_SEAT_A = 12
INDEX_RIGHT_SEAT_B = 13

INDEX_LIGHT_SIDE = 14
INDEX_LIGHT_4X = 11
INDEX_LIGHT_CEILING = 15
INDEX_LIGHT_DRAWERS = 16

INDEX_CURTAIN_FRONT_LEFT = 6
INDEX_CURTAIN_FRONT_RIGHT = 7
INDEX_CURTAIN_REAR_LEFT = 3
INDEX_CURTAIN_REAR_RIGHT = 5
INDEX_CURTAIN_REAR_CENTER = 4

INDEX_LEFT_TABLE = 0
INDEX_RIGHT_TABLE = 1

INDEX_TV = 8
INDEX_CONTROL_PANEL = 2
INDEX_NOT_USE = 17