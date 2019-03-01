from PIL import Image
from PIL import ImageDraw, ImageFont


def images(file, n, m):

    img = Image.open(file)
    img_d = ImageDraw.Draw(img)
    x_len, y_len = img.size
    x_ = x_len // n
    y_ = y_len // m
    print(x_*y_)
    for x in range(0, x_len, x_):
        img_d.line(((x, 0), (x, y_len)), (0, 0, 180))
    for y in range(0, y_len, y_):
        img_d.line(((0, y), (x_len, y)), (0, 0, 180))
    fontsize = min(y_, x_)*3//4
    draw = ImageDraw.Draw(img)
    ttfont = ImageFont.truetype('simsunb.ttf', fontsize)
    data = dict()
    i = 1
    while i <= n*m:
        for yy in range(y_//2, y_len, y_):
            for xx in range(x_//2, x_len, x_):
                data[i] = (xx, yy)
                i += 1

    for key, value in data.items():
        xx, yy = value
        draw.text((xx-fontsize*1.5/4, yy-fontsize*0.5), str(key), fill=(255, 0, 0),
                  font=ttfont)
        img_d.line(((xx-2, yy), (xx+2, yy)), (0, 0, 180))
        img_d.line(((xx, yy-2), (xx, yy+2)), (0, 0, 180))

    img.show()
    img.save('ii.png')


if __name__ == '__main__':
    images('1.png', 15, 12)