from PIL import Image
from PIL import ImageDraw, ImageFont


def images(n, m):
    # 打开图像
    img = Image.open('1.png') # 'slidebg.png'
    img_d = ImageDraw.Draw(img)
    # 获取 图片的 x轴，y轴 像素
    x_len, y_len = img.size
    x_ = x_len // n
    y_ = y_len // m
    print(x_*y_)
    for x in range(0, x_len, x_):
        img_d.line(((x, 0), (x, y_len)), (0, 0, 180))
    for y in range(0, y_len, y_):
        img_d.line(((0, y), (x_len, y)), (0, 0, 180))
    # 保存图片

    fontSize = min(y_, x_)*3//4
    draw = ImageDraw.Draw(img)
    ttFont = ImageFont.truetype('simsunb.ttf', fontSize)
    data = dict()
    i = 1
    while i <= n*m:
        for yy in range(y_//2, y_len, y_):
            for xx in range(x_//2, x_len, x_):
                data[i] = (xx-fontSize*1.5/4, yy-fontSize*0.5)
                i += 1

    for key, value in data.items():
        draw.text(value, str(key), fill=(255, 0, 0),
                  font=ttFont)
    img.show()


    img.save('ii.png')


if __name__ == '__main__':
    images(16, 24)