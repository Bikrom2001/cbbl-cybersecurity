import struct
import zlib

with open('C:/Users/Bikrom/.gemini/antigravity/brain/a8dff2e4-3d1c-4623-bb86-445802189bd4/.user_uploaded/media_1795080997248_68f3a36f.png', 'rb') as f:
    data = f.read()

# Parse PNG header
w, h, bitd, colort = struct.unpack('>IIBB', data[16:26])
print(f"PNG: width={w}, height={h}, bitdepth={bitd}, colortype={colort}")
