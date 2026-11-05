#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 PrismNote 落地页的 SVG 素材：应用图标、教程封面、软件界面截图。

运行：python3 tools/gen_assets.py
产物写入 assets/。全部为矢量，不依赖外部图片。
"""
import os
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")
os.makedirs(ASSETS, exist_ok=True)

FONT = "-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,monospace"

BLUE = "#91c8f0"
PURPLE = "#b3a2f2"
GREEN = "#7ec9a2"
AMBER = "#e8c58a"
MUTED = "#9a9aa8"
TEXT = "#e8e8ee"


def save(name, parts):
    svg = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"%s\" width=\"%s\" height=\"%s\" "
           "font-family=\"%s\">\n" % (parts[0], parts[1], parts[2], FONT))
    svg += "\n".join(parts[3]) + "\n</svg>\n"
    with open(os.path.join(ASSETS, name), "w", encoding="utf-8") as fh:
        fh.write(svg)
    print("generated:", name)


def t(x, y, s, size=14, fill=TEXT, weight="400", anchor="start", opacity=None, spacing=None, family=FONT):
    op = ' opacity="%s"' % opacity if opacity else ""
    sp = ' letter-spacing="%s"' % spacing if spacing else ""
    return ('<text x="%s" y="%s" font-family="%s" font-size="%s" font-weight="%s" '
            'fill="%s" text-anchor="%s"%s%s>%s</text>' %
            (x, y, family, size, weight, fill, anchor, op, sp, escape(str(s))))


def r(x, y, w, h, fill, rx=0, stroke=None, sw=1, opacity=None):
    op = ' opacity="%s"' % opacity if opacity else ""
    st = ' stroke="%s" stroke-width="%s"' % (stroke, sw) if stroke else ""
    return '<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s"%s%s/>' % (
        x, y, w, h, rx, fill, st, op)


def line(x1, y1, x2, y2, stroke="#3a3a46", sw=1, opacity=None):
    op = ' opacity="%s"' % opacity if opacity else ""
    return '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>' % (
        x1, y1, x2, y2, stroke, sw, op)


def circle(cx, cy, rad, fill, stroke=None, sw=1, opacity=None):
    op = ' opacity="%s"' % opacity if opacity else ""
    st = ' stroke="%s" stroke-width="%s"' % (stroke, sw) if stroke else ""
    return '<circle cx="%s" cy="%s" r="%s" fill="%s"%s%s/>' % (cx, cy, rad, fill, st, op)


def bar(x, y, w, h=8, fill="#3a3a46", rx=4, opacity=None):
    return r(x, y, w, h, fill, rx=rx, opacity=opacity)


# ---------------------------------------------------------------- 应用图标
def gen_icon():
    d = [
        '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#5b83d6"/><stop offset="0.55" stop-color="#6d63bb"/>'
        '<stop offset="1" stop-color="#3c4d86"/></linearGradient></defs>',
        r(4, 4, 120, 120, "url(#g)", rx=28),
        r(5, 5, 118, 118, "none", rx=27, stroke="#ffffff30", sw=1.5),
        # 棱镜三角形
        '<path d="M64 30 L104 96 L24 96 Z" fill="none" stroke="#ffffff" stroke-opacity="0.92" '
        'stroke-width="4.5" stroke-linejoin="round"/>',
        # 入射光与色散
        line(14, 52, 58, 66, "#ffffff", 3, .85),
        line(66, 72, 116, 54, BLUE, 3, .95),
        line(66, 76, 116, 72, GREEN, 3, .95),
        line(66, 80, 116, 92, AMBER, 3, .95),
        circle(64, 63, 5, "#ffffff"),
    ]
    save("app-icon.svg", ("0 0 128 128", 128, 128, d))


# ---------------------------------------------------------------- 教程封面
def poster_window(x, y, w, h, accent, mode):
    """海报右侧的简化应用窗口"""
    d = [r(x, y, w, h, "#1e1e24", rx=14, stroke="#3d3d48", sw=1.5)]
    # 标题栏
    d.append(r(x, y, w, 34, "#26262d", rx=14))
    d.append(r(x, y + 20, w, 14, "#26262d"))
    for i, c in enumerate(["#d97b72", "#d9b46a", "#7bbf95"]):
        d.append(circle(x + 24 + i * 18, y + 17, 5, c, opacity=.85))
    d.append(t(x + w / 2, y + 22, "PrismNote · 笔记库", 12, MUTED, anchor="middle"))
    # 左侧导航
    side = 176
    d.append(r(x + 14, y + 34, side - 14, h - 48, "#1a1a20", rx=0))
    d.append(line(x + side, y + 34, x + side, y + h - 14, "#34343e", 1))
    d.append(r(x + 28, y + 52, side - 42, 26, "#2b2b34", rx=6))
    d.append(t(x + 38, y + 70, "搜索  ⌘K", 11, MUTED))
    items = ["每日笔记", "项目 / 落地页", "双向链接实践", "阅读清单", "灵感碎片"]
    for i, name in enumerate(items):
        yy = y + 102 + i * 34
        if i == 2:
            d.append(r(x + 20, yy - 15, side - 24, 28, "#33405e", rx=6))
            d.append(r(x + 20, yy - 15, 3, 28, accent, rx=2))
        d.append(t(x + 36, yy + 4, name, 12, TEXT if i == 2 else MUTED, weight="600" if i == 2 else "400"))
    # 主区域
    mx = x + side + 32
    d.append(t(mx, y + 76, "双向链接实践", 22, TEXT, weight="700"))
    d.append(t(mx, y + 100, "更新于 11 月 5 日 · 1,284 字", 11, MUTED))
    d.append(line(mx, y + 116, x + w - 28, y + 116, "#33333d", 1))
    widths = [400, 372, 418, 330, 390]
    for i, wd in enumerate(widths):
        d.append(bar(mx, y + 140 + i * 26, wd, 8, "#393943", rx=4))
    d.append(r(mx, y + 282, 116, 22, "#33405e", rx=6))
    d.append(t(mx + 10, y + 297, "[[知识图谱]]", 11, accent))
    d.append(bar(mx, y + 320, 356, 8, "#393943"))
    if mode == "graph":
        nodes = [(mx + 70, y + 400, 16, accent), (mx + 190, y + 366, 11, PURPLE),
                 (mx + 210, y + 448, 13, GREEN), (mx + 320, y + 392, 10, AMBER),
                 (mx + 150, y + 490, 9, MUTED)]
        d.append(r(mx, y + 346, 400, 176, "#16161c", rx=10))
        for a, b in [(0, 1), (0, 2), (1, 3), (2, 3), (0, 4), (2, 4)]:
            d.append(line(nodes[a][0], nodes[a][1], nodes[b][0], nodes[b][1], "#4a5776", 1.5))
        for nx, ny, rad, col in nodes:
            d.append(circle(nx, ny, rad, col, opacity=.9))
            d.append(circle(nx, ny, rad + 7, "none", stroke=col, sw=1, opacity=".35"))
    elif mode == "capture":
        d.append(r(x + side + 10, y + 46, w - side - 24, h - 60, "#0b0b0d", rx=0, opacity=.62))
        d.append(r(mx + 20, y + 330, 360, 190, "#2a2a33", rx=12, stroke="#50505e", sw=1))
        d.append(r(mx + 38, y + 348, 324, 34, "#1d1d24", rx=7))
        d.append(t(mx + 50, y + 370, "知识", 14, TEXT))
        d.append(r(mx + 118, y + 356, 2, 18, accent))
        for i, name in enumerate(["打开 知识图谱", "新建：知识卡片", "搜索 知识管理"]):
            yy = y + 404 + i * 34
            if i == 0:
                d.append(r(mx + 32, yy - 16, 336, 30, "#33405e", rx=6))
            d.append(t(mx + 48, yy + 4, name, 12, TEXT if i == 0 else MUTED))
    else:
        d.append(r(mx, y + 372, 172, 24, "#2f2f39", rx=6))
        d.append(t(mx + 12, y + 388, "# 本地优先", 11, MUTED))
        d.append(r(mx + 184, y + 372, 120, 24, "#2f2f39", rx=6))
        d.append(t(mx + 196, y + 388, "# 双链", 11, MUTED))
        d.append(line(mx, y + 424, x + w - 28, y + 424, "#33333d", 1))
        d.append(bar(mx, y + 444, 360, 8, "#393943"))
        d.append(bar(mx, y + 466, 300, 8, "#393943"))
    return d


def gen_poster(name, idx, kicker, title1, title2, subtitle, chips, duration, accent, mode):
    w, h = 1600, 900
    d = [
        '<defs>',
        '<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#1d2029"/><stop offset="0.6" stop-color="#1a1a20"/>'
        '<stop offset="1" stop-color="#252031"/></linearGradient>',
        '<radialGradient id="glow" cx="0.78" cy="0.32" r="0.55">'
        '<stop offset="0" stop-color="%s" stop-opacity="0.20"/>'
        '<stop offset="1" stop-color="%s" stop-opacity="0"/></radialGradient>' % (accent, accent),
        '<pattern id="dots" width="28" height="28" patternUnits="userSpaceOnUse">'
        '<circle cx="1.5" cy="1.5" r="1.2" fill="#ffffff" fill-opacity="0.055"/></pattern>',
        '</defs>',
        r(0, 0, w, h, "url(#bg)"),
        r(0, 0, w, h, "url(#dots)"),
        r(0, 0, w, h, "url(#glow)"),
        r(0, 0, 8, h, accent, opacity=.8),
        # 左侧文案
        r(92, 152, 208, 34, "#ffffff12", rx=17, stroke="#ffffff28", sw=1),
        t(112, 175, kicker, 15, accent, weight="600", spacing="1"),
        t(90, 320, title1, 72, TEXT, weight="700", spacing="-2"),
        t(90, 408, title2, 72, TEXT, weight="700", spacing="-2"),
        t(92, 474, subtitle, 24, MUTED),
        t(92, 512, "跟着真实软件演示，一步一步完成设置。", 19, "#85858f"),
    ]
    x = 92
    for chip in chips:
        cw = 30 + len(chip) * 17
        d.append(r(x, 574, cw, 40, "#ffffff0e", rx=20, stroke="#ffffff22", sw=1))
        d.append(t(x + 15, 600, chip, 15, "#c9c9d4"))
        x += cw + 12
    d.append(line(92, 720, 700, 720, "#ffffff1f", 1))
    d.append(t(92, 780, "PRISMNOTE · 官方视频教程", 17, "#b9b9c6", weight="600", spacing="1.4"))
    d.append(t(92, 812, "中文解说与字幕 · 桌面版 2.4.1", 15, "#7f7f8c"))
    d.append(r(620, 752, 120, 40, accent, rx=20, opacity=.16))
    d.append(t(680, 779, duration, 15, accent, weight="600", anchor="middle"))
    # 右侧应用窗口
    d += poster_window(790, 168, 740, 566, accent, mode)
    d.append(t(1560, 828, "0%s / 03" % idx, 15, "#7f7f8c", anchor="end"))
    save(name, ("0 0 %s %s" % (w, h), w, h, d))


# ---------------------------------------------------------------- 界面截图
LEFT_W = 248
RIGHT_X = 1280
CW, CH = 1600, 920


def chrome(title, active_index=2):
    d = [
        r(0, 0, CW, CH, "#17171b"),
        r(0, 0, CW, 44, "#202026"),
        line(0, 44, CW, 44, "#34343e", 1),
    ]
    for i, c in enumerate(["#d97b72", "#d9b46a", "#7bbf95"]):
        d.append(circle(26 + i * 20, 22, 6, c, opacity=.85))
    d.append(t(800, 28, title, 13, MUTED, anchor="middle"))
    for i in range(3):
        d.append(r(1490 + i * 30, 15, 18, 14, "#2f2f38", rx=4))
    # 左侧栏
    d.append(r(0, 44, LEFT_W, CH - 44, "#1b1b21"))
    d.append(line(LEFT_W, 44, LEFT_W, CH, "#33333d", 1))
    d.append(r(16, 62, 216, 36, "#26262e", rx=7, stroke="#383842", sw=1))
    d.append(circle(34, 80, 5, "none", stroke=MUTED, sw=1.5))
    d.append(line(38, 84, 43, 89, MUTED, 1.5))
    d.append(t(52, 86, "搜索笔记", 13, MUTED))
    d.append(r(190, 70, 32, 20, "#30303a", rx=5))
    d.append(t(206, 84, "⌘K", 10, MUTED, anchor="middle"))
    d.append(t(20, 132, "笔记库", 11, "#7c7c8a", weight="600", spacing="1.2"))
    items = ["每日笔记", "收件箱", "项目 / 落地页改版", "双向链接实践", "阅读清单", "灵感碎片"]
    for i, name in enumerate(items):
        yy = 158 + i * 36
        if i == active_index:
            d.append(r(10, yy - 20, 228, 32, "#30405e", rx=6))
            d.append(r(10, yy - 20, 3, 32, BLUE, rx=2))
        d.append(r(24, yy - 9, 11, 11, "#4a4a58" if i != active_index else BLUE, rx=3, opacity=".8"))
        d.append(t(46, yy + 3, name, 13, TEXT if i == active_index else "#a6a6b3",
                   weight="600" if i == active_index else "400"))
    d.append(t(20, 398, "最近", 11, "#7c7c8a", weight="600", spacing="1.2"))
    for i, name in enumerate(["2026-11-05", "2026-11-04", "知识图谱笔记"]):
        yy = 424 + i * 32
        d.append(r(24, yy - 9, 10, 10, "#3f3f4c", rx=3))
        d.append(t(46, yy + 3, name, 12.5, "#9a9aa8"))
    d.append(line(0, 856, LEFT_W, 856, "#33333d", 1))
    d.append(circle(30, 882, 8, "#3f3f4c"))
    d.append(t(48, 887, "本地笔记库 · 已同步", 12, MUTED))
    # 底部状态栏
    d.append(r(0, CH - 30, CW, 30, "#202026"))
    d.append(line(0, CH - 30, CW, CH - 30, "#33333d", 1))
    d.append(t(20, CH - 10, "PrismNote", 11, MUTED))
    d.append(t(264, CH - 10, "已保存 · 1,284 字 · 12 个链接", 11, MUTED))
    d.append(t(1580, CH - 10, "Markdown  ·  UTF-8", 11, MUTED, anchor="end"))
    return d


def right_panel_base(heading, count):
    d = [
        r(RIGHT_X, 44, CW - RIGHT_X, CH - 74, "#1b1b21"),
        line(RIGHT_X, 44, RIGHT_X, CH - 30, "#33333d", 1),
        t(RIGHT_X + 24, 84, heading, 14, TEXT, weight="600"),
        r(RIGHT_X + 246, 68, 38, 22, "#2e2e38", rx=11),
        t(RIGHT_X + 265, 83, count, 11, MUTED, anchor="middle"),
        line(RIGHT_X + 24, 100, CW - 24, 100, "#33333d", 1),
    ]
    return d


def editor_bg():
    return r(LEFT_W, 44, RIGHT_X - LEFT_W, CH - 74, "#1f1f25")


def gen_workspace():
    d = chrome("PrismNote — 双向链接实践")
    d.append(editor_bg())
    x = 304
    d.append(t(x, 104, "笔记库  /  项目  /  双向链接实践", 12, MUTED))
    d.append(t(x, 174, "双向链接实践", 38, TEXT, weight="700", spacing="-1"))
    d.append(t(x, 210, "更新于 11 月 5 日 · 1,284 字 · 12 个链接", 13, MUTED))
    d.append(line(x, 236, 1224, 236, "#34343e", 1))
    d.append(t(x, 284, "把笔记连起来，而不是把它们堆起来。", 18, TEXT, weight="600"))
    for i, wd in enumerate([824, 780, 846, 690]):
        d.append(bar(x, 314 + i * 30, wd, 9, "#3c3c48", rx=4))
    # 含链接胶囊的一行
    d.append(bar(x, 434, 226, 9, "#3c3c48"))
    d.append(r(x + 234, 426, 132, 24, "#33405e", rx=6))
    d.append(t(x + 244, 443, "[[知识图谱]]", 13, BLUE))
    d.append(bar(x + 374, 434, 190, 9, "#3c3c48"))
    d.append(r(x + 572, 426, 106, 24, "#3c3358", rx=6))
    d.append(t(x + 582, 443, "[[每日笔记]]", 13, PURPLE))
    d.append(bar(x, 464, 742, 9, "#3c3c48"))
    d.append(t(x, 534, "为什么用它", 22, TEXT, weight="700"))
    d.append(r(x, 560, 4, 68, GREEN, rx=2))
    d.append(t(x + 20, 588, "链接是双向的：写下一处引用，另一端自动生成反向链接。", 15, "#c2c2cd"))
    d.append(t(x + 20, 616, "所有内容都是本地 Markdown 文件，随时可以带走。", 15, "#c2c2cd"))
    d.append(bar(x, 656, 812, 9, "#3c3c48"))
    d.append(bar(x, 686, 640, 9, "#3c3c48"))
    d.append(r(x, 738, 132, 28, "#2f2f3a", rx=14))
    d.append(t(x + 66, 757, "# 本地优先", 12, MUTED, anchor="middle"))
    d.append(r(x + 144, 738, 108, 28, "#2f2f3a", rx=14))
    d.append(t(x + 198, 757, "# 双链", 12, MUTED, anchor="middle"))
    # 右栏：反向链接
    d += right_panel_base("反向链接", "12")
    cards = [
        ("知识图谱视图", "把散落的笔记看成一张网", "3 处引用"),
        ("每日笔记 / 11-04", "今天整理的项目结构", "2 处引用"),
        ("阅读清单", "关于链接思维的摘录", "1 处引用"),
    ]
    for i, (title, sub, badge) in enumerate(cards):
        yy = 122 + i * 122
        d.append(r(RIGHT_X + 22, yy, 276, 104, "#24242c", rx=9, stroke="#34343f", sw=1))
        d.append(r(RIGHT_X + 38, yy + 20, 12, 12, [BLUE, PURPLE, GREEN][i], rx=3))
        d.append(t(RIGHT_X + 58, yy + 32, title, 14, TEXT, weight="600"))
        d.append(t(RIGHT_X + 38, yy + 60, sub, 12, MUTED))
        d.append(bar(RIGHT_X + 38, yy + 76, 176, 7, "#3a3a46"))
        d.append(r(RIGHT_X + 214, yy + 70, 66, 20, "#2f3a52", rx=10))
        d.append(t(RIGHT_X + 247, yy + 84, badge, 10, BLUE, anchor="middle"))
    d.append(line(RIGHT_X + 24, 500, CW - 24, 500, "#33333d", 1))
    d.append(t(RIGHT_X + 24, 534, "本页大纲", 14, TEXT, weight="600"))
    for i, name in enumerate(["把笔记连起来", "为什么用它", "引用与标签", "下一步"]):
        yy = 570 + i * 38
        d.append(r(RIGHT_X + 26, yy - 6, 6, 6, "#4a4a58", rx=3))
        d.append(t(RIGHT_X + 44, yy + 3, name, 13, "#a6a6b3"))
    save("shot-workspace.svg", ("0 0 %s %s" % (CW, CH), CW, CH, d))


def gen_graph():
    d = chrome("PrismNote — 知识图谱", active_index=3)
    d.append(r(LEFT_W, 44, RIGHT_X - LEFT_W, CH - 74, "#15151b"))
    # 画布网格点
    d.append('<defs><pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">'
             '<circle cx="2" cy="2" r="1.1" fill="#ffffff" fill-opacity="0.07"/></pattern></defs>')
    d.append(r(LEFT_W, 44, RIGHT_X - LEFT_W, CH - 74, "url(#grid)"))
    # 顶部工具条
    d.append(r(280, 66, 356, 40, "#24242c", rx=9, stroke="#3a3a46", sw=1))
    d.append(t(300, 92, "图谱视图", 14, TEXT, weight="600"))
    d.append(line(372, 76, 372, 96, "#3a3a46", 1))
    d.append(t(388, 92, "全部笔记", 13, MUTED))
    d.append(line(470, 76, 470, 96, "#3a3a46", 1))
    d.append(t(486, 92, "筛选", 13, MUTED))
    d.append(r(1120, 66, 128, 40, "#24242c", rx=9, stroke="#3a3a46", sw=1))
    d.append(t(1140, 92, "−", 17, MUTED))
    d.append(line(1172, 76, 1172, 96, "#3a3a46", 1))
    d.append(t(1196, 92, "100%", 13, MUTED, anchor="middle"))
    d.append(line(1218, 76, 1218, 96, "#3a3a46", 1))
    d.append(t(1232, 92, "+", 17, MUTED))
    # 节点与连线
    nodes = [
        (740, 470, 34, BLUE, "双向链接实践"),
        (520, 320, 20, PURPLE, "每日笔记"),
        (960, 300, 18, GREEN, "知识图谱"),
        (500, 620, 16, AMBER, "阅读清单"),
        (1010, 630, 22, PURPLE, "项目 / 落地页"),
        (760, 210, 13, MUTED, "灵感碎片"),
        (340, 470, 12, MUTED, "收件箱"),
        (1150, 460, 14, GREEN, "模板"),
        (700, 720, 15, AMBER, "导出"),
        (900, 760, 11, MUTED, "标签"),
    ]
    edges = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 8), (0, 9),
             (1, 5), (2, 7), (4, 7), (3, 8), (2, 9), (1, 6)]
    for a, b in edges:
        d.append(line(nodes[a][0], nodes[a][1], nodes[b][0], nodes[b][1], "#46536f", 2, .85))
    for nx, ny, rad, col, label in nodes:
        d.append(circle(nx, ny, rad + 12, col, opacity=.10))
        d.append(circle(nx, ny, rad, "#1d2430", stroke=col, sw=2.5))
        d.append(circle(nx, ny, max(4, rad * .38), col))
        d.append(t(nx, ny + rad + 26, label, 12.5, "#c8c8d4", anchor="middle", weight="600" if rad > 25 else "400"))
    # 右栏：图谱设置
    d += right_panel_base("图谱设置", "10")
    d.append(t(RIGHT_X + 24, 138, "显示范围", 13, "#a6a6b3"))
    d.append(r(RIGHT_X + 24, 156, 272, 30, "#26262e", rx=7, stroke="#383842", sw=1))
    d.append(t(RIGHT_X + 38, 176, "全部笔记", 13, TEXT))
    d.append(t(RIGHT_X + 292, 176, "⌄", 13, MUTED))
    d.append(t(RIGHT_X + 24, 226, "节点引力", 13, "#a6a6b3"))
    d.append(t(RIGHT_X + 292, 226, "62", 13, BLUE, anchor="end"))
    d.append(r(RIGHT_X + 24, 244, 272, 6, "#3a3a46", rx=3))
    d.append(r(RIGHT_X + 24, 244, 168, 6, BLUE, rx=3))
    d.append(circle(RIGHT_X + 192, 247, 10, "#e8e8ee"))
    d.append(t(RIGHT_X + 24, 306, "连线距离", 13, "#a6a6b3"))
    d.append(t(RIGHT_X + 292, 306, "40", 13, BLUE, anchor="end"))
    d.append(r(RIGHT_X + 24, 324, 272, 6, "#3a3a46", rx=3))
    d.append(r(RIGHT_X + 24, 324, 110, 6, PURPLE, rx=3))
    d.append(circle(RIGHT_X + 134, 327, 10, "#e8e8ee"))
    for i, (label, on) in enumerate([("显示标签", True), ("显示未链接笔记", False), ("按文件夹着色", True)]):
        yy = 386 + i * 46
        d.append(t(RIGHT_X + 24, yy, label, 13, "#c2c2cd"))
        d.append(r(RIGHT_X + 244, yy - 16, 44, 24, "#3f6bb5" if on else "#3a3a46", rx=12))
        d.append(circle(RIGHT_X + (276 if on else 256), yy - 4, 9, "#ffffff"))
    d.append(line(RIGHT_X + 24, 546, CW - 24, 546, "#33333d", 1))
    d.append(t(RIGHT_X + 24, 582, "分组颜色", 14, TEXT, weight="600"))
    legend = [("项目", BLUE), ("笔记", PURPLE), ("摘录", GREEN), ("待整理", AMBER), ("其他", MUTED)]
    for i, (name, col) in enumerate(legend):
        yy = 616 + i * 36
        d.append(circle(RIGHT_X + 34, yy - 4, 6, col))
        d.append(t(RIGHT_X + 50, yy, name, 13, "#a6a6b3"))
    save("shot-graph.svg", ("0 0 %s %s" % (CW, CH), CW, CH, d))


def gen_capture():
    d = chrome("PrismNote — 快速捕获")
    d.append(editor_bg())
    x = 304
    d.append(t(x, 104, "笔记库  /  每日笔记  /  2026-11-05", 12, MUTED))
    d.append(t(x, 174, "2026-11-05 星期四", 36, TEXT, weight="700", spacing="-1"))
    d.append(line(x, 210, 1224, 210, "#34343e", 1))
    for i, wd in enumerate([780, 836, 640, 800, 712]):
        d.append(bar(x, 254 + i * 34, wd, 9, "#3c3c48"))
    d.append(r(x, 452, 118, 24, "#33405e", rx=6))
    d.append(t(x + 10, 469, "[[知识图谱]]", 12, BLUE))
    d.append(bar(x, 510, 690, 9, "#3c3c48"))
    d.append(bar(x, 544, 760, 9, "#3c3c48"))
    # 右栏（保留，稍后统一压暗）
    d += right_panel_base("反向链接", "8")
    for i, name in enumerate(["双向链接实践", "项目 / 落地页", "阅读清单", "灵感碎片"]):
        yy = 142 + i * 108
        d.append(r(RIGHT_X + 22, yy, 276, 88, "#24242c", rx=9, stroke="#34343f", sw=1))
        d.append(t(RIGHT_X + 40, yy + 30, name, 14, TEXT, weight="600"))
        d.append(bar(RIGHT_X + 40, yy + 50, 190, 7, "#3a3a46"))
        d.append(bar(RIGHT_X + 40, yy + 66, 140, 7, "#3a3a46"))
    # 遮罩
    d.append(r(LEFT_W, 44, CW - LEFT_W, CH - 74, "#0b0b0d", opacity=.66))
    # 命令面板
    px, py, pw, ph = 470, 190, 660, 470
    d.append(r(px + 4, py + 10, pw, ph, "#000000", rx=16, opacity=.35))
    d.append(r(px, py, pw, ph, "#27272f", rx=16, stroke="#55555f", sw=1.5))
    d.append(r(px + 20, py + 20, pw - 40, 52, "#1c1c23", rx=9, stroke="#3b3b46", sw=1))
    d.append(circle(px + 46, py + 46, 7, "none", stroke=BLUE, sw=2))
    d.append(line(px + 51, py + 51, px + 57, py + 57, BLUE, 2))
    d.append(t(px + 72, py + 54, "知识", 19, TEXT))
    d.append(r(px + 128, py + 36, 2, 24, BLUE))
    d.append(r(px + 20, py + 86, pw - 40, 1, "#3b3b46"))
    d.append(t(px + 24, py + 116, "建议", 11, "#8b8b99", weight="600", spacing="1.2"))
    results = [
        ("打开  知识图谱视图", "笔记库 / 项目", "↵"),
        ("新建  知识卡片", "模板 / 空白笔记", "⌘N"),
        ("搜索  知识管理", "全部笔记", "⌘F"),
        ("跳转  双向链接实践", "最近打开", "⌘1"),
        ("命令  重建图谱索引", "设置", "⌘R"),
    ]
    for i, (name, path, key) in enumerate(results):
        yy = py + 146 + i * 56
        if i == 0:
            d.append(r(px + 16, yy - 26, pw - 32, 48, "#3a4a68", rx=8))
            d.append(r(px + 16, yy - 26, 3, 48, BLUE, rx=2))
        d.append(r(px + 34, yy - 10, 16, 16, "#4a4a5a" if i else BLUE, rx=4, opacity=".9"))
        d.append(t(px + 62, yy + 3, name, 15, TEXT if i == 0 else "#c8c8d4", weight="600" if i == 0 else "400"))
        d.append(t(px + 62, yy + 22, path, 11, "#8b8b99"))
        d.append(r(px + pw - 78, yy - 14, 44, 24, "#ffffff12", rx=6))
        d.append(t(px + pw - 56, yy + 3, key, 12, "#a6a6b3", anchor="middle"))
    d.append(r(px + 1, py + ph - 46, pw - 2, 1, "#3b3b46"))
    d.append(t(px + 24, py + ph - 17, "↑ ↓ 选择     ↵ 打开     esc 关闭", 12, "#8b8b99"))
    d.append(t(px + pw - 24, py + ph - 17, "⌘K 命令面板", 12, BLUE, anchor="end"))
    save("shot-capture.svg", ("0 0 %s %s" % (CW, CH), CW, CH, d))


if __name__ == "__main__":
    gen_icon()
    gen_poster("poster-start.svg", 1, "教程 01 · 快速上手", "从第一篇笔记", "开始。",
               "安装、笔记库、Markdown 写作与每日笔记。",
               ["5 分 12 秒", "零基础", "中文解说"], "05:12", BLUE, "default")
    gen_poster("poster-links.svg", 2, "教程 02 · 连接与图谱", "把想法", "连成一张网。",
               "双向链接、反向链接面板与知识图谱视图。",
               ["8 分 03 秒", "双链", "图谱"], "08:03", PURPLE, "graph")
    gen_poster("poster-template.svg", 3, "教程 03 · 效率与导出", "更快一点，", "再快一点。",
               "命令面板、自定义模板与批量导出。",
               ["6 分 47 秒", "⌘K", "导出"], "06:47", GREEN, "capture")
    gen_workspace()
    gen_graph()
    gen_capture()
    print("all assets written to", ASSETS)
