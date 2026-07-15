from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


OUT_DIR = Path(__file__).resolve().parent
ROOT = OUT_DIR.parents[1]
SOURCE_SCREENSHOT = ROOT / "zend-framework-1-crud-master" / "other_example" / "crud_picture.jpg"

W = 1200
H = 850


def font(size, bold=False):
    candidates = [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


F_NAV = font(18, True)
F_TEXT = font(17)
F_SMALL = font(15)
F_H1 = font(42)
F_H2 = font(32)
F_LABEL = font(17)
F_BTN = font(16)


def text(draw, xy, value, fill=(51, 51, 51), fnt=F_TEXT):
    draw.text(xy, value, fill=fill, font=fnt)


def rect(draw, xy, fill, outline=None, width=1):
    draw.rectangle(xy, fill=fill, outline=outline, width=width)


def rounded(draw, xy, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def make_canvas(height=H):
    img = Image.new("RGB", (W, height), "white")
    draw = ImageDraw.Draw(img)
    draw_nav(draw)
    return img, draw


def draw_nav(draw):
    rect(draw, (0, 0, W, 72), (248, 248, 248), (231, 231, 231))
    text(draw, (24, 22), "Zend Framework 1 CRUD EXAMPLE", (90, 90, 90), F_NAV)
    rounded(draw, (895, 18, 1026, 54), 5, (92, 184, 92), (76, 174, 76))
    text(draw, (920, 27), "Add Ticket", "white", F_BTN)
    rounded(draw, (1036, 18, 1168, 54), 5, (92, 184, 92), (76, 174, 76))
    text(draw, (1060, 27), "CVS export", "white", F_BTN)


def draw_table(draw, x, y, rows):
    widths = [110, 720, 90, 150]
    headers = ["Title", "Notes", "Date", "Action"]
    row_h = 112
    header_h = 54
    cur_x = x
    for width, header in zip(widths, headers):
        rect(draw, (cur_x, y, cur_x + width, y + header_h), (255, 255, 255), (221, 221, 221))
        text(draw, (cur_x + 14, y + 17), header, (51, 51, 51), font(17, True))
        cur_x += width
    yy = y + header_h
    for title, notes, date in rows:
        cur_x = x
        values = [title, notes, date]
        for i, width in enumerate(widths):
            rect(draw, (cur_x, yy, cur_x + width, yy + row_h), (255, 255, 255), (221, 221, 221))
            if i < 3:
                draw_multiline(draw, (cur_x + 14, yy + 15), values[i], width - 24, F_TEXT, (85, 85, 85), 23, max_lines=4)
            cur_x += width
        btn_x = x + sum(widths[:-1]) + 24
        rounded(draw, (btn_x, yy + 18, btn_x + 78, yy + 58), 5, (92, 184, 92), (76, 174, 76))
        text(draw, (btn_x + 24, yy + 27), "Edit", "white", F_BTN)
        rounded(draw, (btn_x, yy + 65, btn_x + 96, yy + 105), 5, (217, 83, 79), (212, 63, 58))
        text(draw, (btn_x + 22, yy + 74), "Delete", "white", F_BTN)
        yy += row_h


def draw_multiline(draw, xy, value, max_width, fnt, fill, line_h, max_lines=None):
    words = value.split()
    lines = []
    current = ""
    for word in words:
        test = word if not current else current + " " + word
        if draw.textlength(test, font=fnt) <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    if max_lines is not None:
        lines = lines[:max_lines]
    x, y = xy
    for line in lines:
        text(draw, (x, y), line, fill, fnt)
        y += line_h


def draw_form_group(draw, y, label, kind="text", value="", required=False):
    label_x = 112
    field_x = 260
    text(draw, (label_x, y + 8), label + (":" if label else ""), (51, 51, 51), F_LABEL)
    if kind == "textarea":
        rect(draw, (field_x, y, 1000, y + 148), (255, 255, 255), (204, 204, 204))
        if value:
            draw_multiline(draw, (field_x + 12, y + 11), value, 700, F_TEXT, (85, 85, 85), 24, max_lines=5)
        return y + 172
    if kind == "select":
        rect(draw, (field_x, y, 1000, y + 38), (255, 255, 255), (204, 204, 204))
        text(draw, (field_x + 12, y + 8), value or "Low", (85, 85, 85), F_TEXT)
        text(draw, (974, y + 8), "▼", (85, 85, 85), F_SMALL)
        return y + 65
    if kind == "file":
        rect(draw, (field_x, y, 625, y + 38), (255, 255, 255), (204, 204, 204))
        rounded(draw, (260, y, 370, y + 38), 3, (238, 238, 238), (204, 204, 204))
        text(draw, (281, y + 8), "Choose File", (51, 51, 51), F_SMALL)
        text(draw, (386, y + 8), value or "No file chosen", (85, 85, 85), F_SMALL)
        return y + 70
    rect(draw, (field_x, y, 1000, y + 38), (255, 255, 255), (204, 204, 204))
    if value:
        text(draw, (field_x + 12, y + 8), value, (85, 85, 85), F_TEXT)
    return y + 65


def make_list_png():
    if SOURCE_SCREENSHOT.exists():
        img = Image.open(SOURCE_SCREENSHOT).convert("RGB")
        img = img.resize((900, 956))
        canvas = Image.new("RGB", (980, 1040), "white")
        canvas.paste(img, (40, 35))
        canvas.save(OUT_DIR / "01_チケット一覧.png")
        return
    img, draw = make_canvas(900)
    x = 38
    text(draw, (38, 150), "Ticket System v 0.1", (33, 37, 41), F_H1)
    text(draw, (38, 208), "The zend framework crud operation tutorial (extra upload,pagination,cvs export)", (85, 85, 85), F_TEXT)
    text(draw, (38, 250), "1 - 5 of 12", (85, 85, 85), F_TEXT)
    text(draw, (875, 250), "First Previous 1 2 3 Next Last", (85, 85, 85), F_TEXT)
    notes = "Iners lacusque securae rudis fidem undas capacius surgere! Norant nuper mundi. Hominum distinxit litora bene pinus."
    rows = [
        ("lorem impsum 10", notes, "10 Mayis 2017"),
        ("lorem impsum 9", notes, "09 Mayis 2017"),
        ("lorem impsum 8", notes, "30 Nisan 2015"),
        ("lorem impsum 7", notes, "27 Mart 2015"),
        ("lorem impsum 6", notes, "09 Subat 2013"),
    ]
    draw_table(draw, x, 300, rows)
    img.save(OUT_DIR / "01_チケット一覧.png")


def make_create_png():
    img, draw = make_canvas(760)
    text(draw, (185, 122), "Add ticket", (33, 37, 41), F_H2)
    y = 190
    y = draw_form_group(draw, y, "", "text", "")
    y = draw_form_group(draw, y, "Title", "text", "")
    y = draw_form_group(draw, y, "Notes", "textarea", "")
    y = draw_form_group(draw, y, "priority", "select", "Low")
    y = draw_form_group(draw, y, "files", "file", "No file chosen")
    rounded(draw, (260, y + 10, 365, y + 50), 5, (92, 184, 92), (76, 174, 76))
    text(draw, (280, y + 19), "Post Topic", "white", F_BTN)
    img.save(OUT_DIR / "02_チケット新規登録.png")


def make_edit_png():
    img, draw = make_canvas(780)
    text(draw, (185, 122), "Edit ticket", (33, 37, 41), F_H2)
    y = 190
    y = draw_form_group(draw, y, "", "text", "127")
    y = draw_form_group(draw, y, "Title", "text", "lorem impsum 10")
    y = draw_form_group(
        draw,
        y,
        "Notes",
        "textarea",
        "Iners lacusque securae rudis fidem undas capacius surgere! Norant nuper mundi. Hominum distinxit litora bene pinus.",
    )
    y = draw_form_group(draw, y, "priority", "select", "Low")
    y = draw_form_group(draw, y, "files", "file", "avatar92.jpg")
    rounded(draw, (260, y + 10, 390, y + 50), 5, (92, 184, 92), (76, 174, 76))
    text(draw, (280, y + 19), "Update Ticket", "white", F_BTN)
    img.save(OUT_DIR / "03_チケット編集.png")


def make_error_png():
    img = Image.new("RGB", (900, 520), "white")
    draw = ImageDraw.Draw(img)
    text(draw, (26, 25), "An error occurred", (33, 37, 41), F_H1)
    text(draw, (26, 92), "Page not found", (33, 37, 41), F_H2)
    text(draw, (26, 158), "Exception information:", (33, 37, 41), font(22, True))
    text(draw, (26, 205), "Message: Invalid controller specified", (51, 51, 51), F_TEXT)
    text(draw, (26, 260), "Stack trace:", (33, 37, 41), font(22, True))
    rect(draw, (26, 302, 870, 465), (248, 248, 248), (230, 230, 230))
    text(draw, (42, 322), "#0 Zend_Controller_Dispatcher_Standard->dispatch()", (51, 51, 51), F_SMALL)
    text(draw, (42, 350), "#1 Zend_Controller_Front->dispatch()", (51, 51, 51), F_SMALL)
    text(draw, (42, 378), "#2 Zend_Application_Bootstrap_Bootstrap->run()", (51, 51, 51), F_SMALL)
    img.save(OUT_DIR / "04_エラー画面.png")


def main():
    make_list_png()
    make_create_png()
    make_edit_png()
    make_error_png()


if __name__ == "__main__":
    main()
