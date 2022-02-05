import pyedid

edid_txt = """
    0x00, // Header 
    0xFF, // 
    0xFF, // 
    0xFF, // 
    0xFF, // 
    0xFF, // 
    0xFF, // 
    0x00, // 
    0x06, // EISA Manuf. Code LSB 
    0xAF, // Compressed ASCII 
    0xD8, // 
    0x22, // 
    0x00, // 32-bit ser # 
    0x00, // 
    0x00, // 
    0x00, // 
    0x00, // Week of manufacture 
    0x16, // Year of manufacture 
    0x01, // EDID Structure Ver. 
    0x04, // EDID revision # 
    0xA0, // Video input def. (digital I/P, non-TMDS, CRGB) 
    0x16, // Max H image size (rounded to cm) 
    0x0E, // Max V image size (rounded to cm) 
    0x78, // Display Gamma (=(gamma*100)-100) 
    0x02, // Feature support (no DPMS, Active OFF, RGB, tmg Blk#1) 
    0x66, // Red/green low bits (Lower 2:2:2:2 bits) 
    0xF5, // Blue/white low bits (Lower 2:2:2:2 bits) 
    0xA2, // Red x (Upper 8 bits) 
    0x55, // Red y/ highER 8 bits 
    0x4F, // Green x 
    0x9A, // Green y 
    0x24, // Blue x 
    0x10, // Blue y 
    0x4F, // White x 
    0x54, // White y 
    0x00, // Established timing 1 
    0x00, // Established timing 2 
    0x00, // Established timing 3 
    0x01, // Standard timing #1 
    0x01, // 
    0x01, // Standard timing #2 
    0x01, // 
    0x01, // Standard timing #3 
    0x01, // 
    0x01, // Standard timing #4  
    0x01, // 
    0x01, // Standard timing #5 
    0x01, // 
    0x01, // Standard timing #6 
    0x01, // 
    0x01, // Standard timing #7 
    0x01, // 
    0x01, // Standard timing #8 
    0x01, // 
    0x90, // Pixel Clock/10000 LSB 
    0x3D, // Pixel Clock/10000 USB 
    0x80, // Horz active Lower 8bits 
    0xB4, // Horz blanking Lower 8bits 
    0x70, // HorzAct:HorzBlnk Upper 4:4 bits 
    0xB0, // Vertical Active Lower 8bits 
    0x32, // Vertical Blanking Lower 8bits 
    0x40, // Vert Act : Vertical Blanking (upper 4:4 bit) 
    0x3C, // HorzSync. Offset 
    0x3C, // HorzSync.Width 
    0xAA, // VertSync.Offset : VertSync.Width 
    0x00, // Horz&Vert Sync Offset/Width Upper 2bits 
    0xD8, // Horizontal Image Size Lower 8bits 
    0x88, // Vertical Image Size Lower 8bits 
    0x00, // Horizontal & Vertical Image Size (upper 4:4 bits) 
    0x00, // Horizontal Border (zero for internal LCD) 
    0x00, // Vertical Border (zero for internal LCD) 
    0x18, // Signal (non-intr, norm, no stero, sep sync, neg pol) 
    0x00, // Detailed timing/monitor 
    0x00, // descriptor #2 
    0x00, // 
    0x0F, // 
    0x00, // 
    0x00, // 
    0x00, // 
    0x00, // 
    0x00, // 
    0x00, // 
    0x00, // 
    0x00, // 
    0x00, // 
    0x00, // 
    0x00, // 
    0x00, // 
    0x00, // 
    0x20, // 
    0x00, // Detailed timing/monitor 
    0x00, // descriptor #3 
    0x00, // 
    0xFE, // 
    0x00, // 
    0x41, // Manufacture A
    0x55, // Manufacture U 
    0x4F, // Manufacture O
    0x0A, // 
    0x20, // 
    0x20, // 
    0x20, // 
    0x20, // 
    0x20, // 
    0x20, // 
    0x20, // 
    0x20, // 
    0x20, // 
    0x00, // Detailed timing/monitor 
    0x00, // descriptor #4 
    0x00, // 
    0xFE, // 
    0x00, // 
    0x42, // Manufacture P/N 
    0x31, // Manufacture P/N 
    0x30, // Manufacture P/N 
    0x31, // Manufacture P/N 
    0x55, // Manufacture P/N 
    0x41, // Manufacture P/N 
    0x54, // Manufacture P/N 
    0x30, // Manufacture P/N 
    0x32, // Manufacture P/N 
    0x2E, // Manufacture P/N 
    0x32, // Manufacture P/N 
    0x20, // 
    0x0A, // 
    0x00, // Extension Flag 
    0x00, // Checksum  """

edid_hex = ""
for line in edid_txt.split("\n"):
    hex = line.split(",")[0].replace(" ", "")
    # print(hex[2:])
    edid_hex += hex[2:]

edid_hex2 = (
    '00ffffffffffff000469982401010101'
    '1e1b01031e351e78ea9265a655559f28'
    '0d5054bfef00714f818081409500a940'
    'b300d1c00101023a801871382d40582c'
    '4500132b2100001e000000fd00324c1e'
    '5311000a202020202020000000fc0056'
    '533234380a20202020202020000000ff'
    '0048374c4d51533132323136310a0000'
)

edid_hex3 = (
    '00ffffffffffff0026CD684600000000'
    '230c010381241D78eF0DC2a057479827'
    '12484FBFEF008180818F614061594540'
    '455931403159BC34009851002A401090'
    '130068221100001e000000FF00300A20'
    '20202020202020202020000000FC0041'
    '533436333720202020202020000000FD'
    '00385518500E000A2020202020200006'
)


def print_edid(edid_str):
    edid_bytes = set_crc(edid_str)
    # returned Edid object, used the Default embedded registry
    edid = pyedid.parse_edid(edid_bytes)
    print("edid.name", edid.name)  # 'VS248'
    print("edid.manufacturer", edid.manufacturer)  # 'Ancor Communications Inc'
    print("edid.serial", edid.serial)  # 'H7LMQS122161'
    print("edid.year", edid.year)  # 2017 (year of manufacture)
    print("edid.week", edid.week)  # 30 (week of manufacture)
    print("edid.width", edid.width)  # 53.0 cm
    print("edid.height", edid.height)  # 30.0 cm
    print("edid.resolutions", edid.resolutions)  # list with resulutions (x, y, rate), ex (720, 400, 70.0)
    json_str = str(edid)  # making JSON string object
    print(json_str)


def check_crc(raw):
    if sum(raw) % 256 != 0:
        raise ValueError('Checksum mismatch')


def set_crc(edid_str: str) -> bytes:
    edid_bytes = bytes.fromhex(edid_str)
    print(edid_bytes)
    crc = sum(edid_bytes[:126]) % 256
    if crc != 0:
        crc = 256 - crc
    print("new crc:", crc, "old crc:", edid_bytes[127])
    edid_bytes = edid_bytes[:126] + bytes(crc)
    return edid_bytes


print_edid(edid_hex)
print_edid(edid_hex2)
print_edid(edid_hex3)

