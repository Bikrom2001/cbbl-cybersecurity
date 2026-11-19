import struct
import zlib

with open('C:/Users/Bikrom/.gemini/antigravity/brain/a8dff2e4-3d1c-4623-bb86-445802189bd4/.user_uploaded/media_1795080997248_68f3a36f.png', 'rb') as f:
    data = f.read()

# Extract IDAT
idat = b''
pos = 8
while pos < len(data):
    length, chunk_type = struct.unpack('>I4s', data[pos:pos+8])
    pos += 8
    if chunk_type == b'IDAT':
        idat += data[pos:pos+length]
    pos += length + 4

raw = zlib.decompress(idat)
w, h = 237, 50
stride = 1 + w * 4
pixels = []
for y in range(h):
    row = raw[y*stride + 1 : (y+1)*stride]
    for x in range(w):
        r, g, b, a = row[x*4:(x+1)*4]
        if a > 200:
            pixels.append((r, g, b))

from collections import Counter
print("Dominant colors (RGB):")
for rgb, count in Counter(pixels).most_common(12):
    print(f"  #{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}: {count}")
