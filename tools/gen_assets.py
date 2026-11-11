#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 www.xinmx.com / AT歌词识别 落地页的 SVG 素材（XM CYBERDECK 皮肤）。

产出：app-icon.svg、3 张教程封面、3 张软件界面示意图。
全部离线自包含，不引用外部字体或图片。改完运行：python3 tools/gen_assets.py
"""
import math
from pathlib import Path
from xml.etree import ElementTree as ET

OUT = Path(__file__).resolve().parent.parent / "assets"
assert OUT.is_dir(), OUT

VOID, CARD, SURFACE = "#05080F", "#0B1220", "#111C2F"
CYAN, MAGENTA, LIME = "#00E5FF", "#FF2E88", "#B8FF3C"
INK, SUB, MUTE = "#EAF7FF", "#7E9AB5", "#4F6B87"
SANS = "'PingFang SC','Microsoft YaHei',sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,monospace"


def e(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def T(x, y, s, size=16, fill=INK, weight=400, mono=False, anchor=None, spacing=None, opacity=None):
    a = ['x="%s"' % x, 'y="%s"' % y, 'font-size="%s"' % size, 'fill="%s"' % fill,
         'font-weight="%s"' % weight, 'font-family="%s"' % (MONO if mono else SANS)]
    if anchor:
        a.append('text-anchor="%s"' % anchor)
    if spacing is not None:
        a.append('letter-spacing="%s"' % spacing)
    if opacity is not None:
        a.append('opacity="%s"' % opacity)
    return "<text %s>%s</text>" % (" ".join(a), e(s))


def R(x, y, w, h, fill=CARD, stroke=CYAN, sw=1, so=.22, rx=0):
    return '<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" stroke-width="%s" stroke-opacity="%s"/>' % (
        x, y, w, h, rx, fill, stroke, sw, so)


def CUT(x, y, w, h, fill=CARD, stroke=CYAN, c=10, sw=1, so=.22):
    p = "M%s %s H%s V%s L%s %s H%s V%s Z" % (x + c, y, x + w, y + h - c, x + w - c, y + h, x, y + c)
    return '<path d="%s" fill="%s" stroke="%s" stroke-width="%s" stroke-opacity="%s"/>' % (p, fill, stroke, sw, so)


def LINE(x1, y1, x2, y2, stroke=CYAN, sw=1, so=.22):
    return '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" stroke-opacity="%s"/>' % (
        x1, y1, x2, y2, stroke, sw, so)


def DEFS(w, h):
    return """<defs>
  <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0 H0 V32" fill="none" stroke="#00E5FF" stroke-opacity=".035"/></pattern>
  <pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#000" fill-opacity=".14"/></pattern>
  <linearGradient id="tube" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4CE0FF"/><stop offset="1" stop-color="#FF2E88"/></linearGradient>
  <linearGradient id="bar" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#00E5FF"/><stop offset="1" stop-color="#FF2E88"/></linearGradient>
  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2.2"/></filter>
</defs>"""


def BG(w, h):
    return [DEFS(w, h), '<rect width="%s" height="%s" fill="%s"/>' % (w, h, VOID),
            '<rect width="%s" height="%s" fill="url(#grid)"/>' % (w, h),
            '<rect width="%s" height="%s" fill="url(#scan)"/>' % (w, h)]


def svg(name, w, h, body):
    doc = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %s %s" width="%s" height="%s" role="img">\n'
           % (w, h, w, h)) + "\n".join(BG(w, h) + body) + "\n</svg>\n"
    ET.fromstring(doc)  # 自检：XML 必须合法
    (OUT / name).write_text(doc, encoding="utf-8")
    print("OK  %-24s %6d B" % (name, len(doc.encode("utf-8"))))


def wave(x, y, w, h, n=64, base=CYAN, hi=MAGENTA, seed=0.0, head=None):
    d = []
    bw = w / n
    for i in range(n):
        v = (math.sin(i * .47 + seed) + math.sin(i * 1.31 + seed * 2) * .6 + math.sin(i * .19 + seed) * .9)
        bh = max(4, (v + 2.4) / 4.8 * h)
        col = hi if (i % 17 == 0) else base
        op = ".95" if (head is not None and abs(i - head) < 1.5) else ".55"
        d.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" opacity="%s"/>'
                 % (x + i * bw, y + (h - bh) / 2, max(1.5, bw - 1.5), bh, col, op))
    if head is not None:
        hx = x + head * bw
        d.append(LINE(hx, y - 10, hx, y + h + 10, MAGENTA, 2, .95))
    return d


def tag(x, y, label, col=CYAN, w=None):
    w = w or (len(label) * 13 + 28)
    return [CUT(x, y, w, 38, fill=SURFACE, stroke=col, c=7, so=.55), T(x + 14, y + 25, label, 14, col, 600, True)]


# ---------- XM 霓虹徽标（favicon，与页头内联徽标同一几何） ----------
def app_icon():
    d = ['<path d="M10 2 H62 V54 L54 62 H2 V10 Z" fill="#0B1524" stroke="#00E5FF" stroke-opacity=".35" stroke-width="1"/>']
    paths = ['<path d="M10 16 L27 48 M27 16 L10 48"/>', '<path d="M36 48 V16 L47 36 L58 16 V48"/>']
    d.append('<g fill="none" stroke="url(#tube)" stroke-width="7" stroke-linecap="round" opacity=".55" filter="url(#glow)">%s</g>' % "".join(paths))
    d.append('<g fill="none" stroke="url(#tube)" stroke-width="4.2" stroke-linecap="round">%s</g>' % "".join(paths))
    d.append('<g fill="none" stroke="#FFFFFF" stroke-opacity=".72" stroke-width="1.1" stroke-linecap="round">%s</g>' % "".join(paths))
    doc = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64" role="img">\n'
           + DEFS(64, 64) + "\n" + "\n".join(d) + "\n</svg>\n")
    ET.fromstring(doc)
    (OUT / "app-icon.svg").write_text(doc, encoding="utf-8")
    print("OK  %-24s %6d B" % ("app-icon.svg", len(doc.encode("utf-8"))))


# ---------- 教程封面 ----------
def poster(name, idx, kicker, line1, line2, desc, tags, time, accent, motif):
    w, h = 1600, 900
    d = [CUT(48, 48, 1504, 804, fill=CARD, so=.18),
         T(100, 128, kicker, 18, CYAN, 600, True, spacing="2"),
         LINE(100, 156, 1500, 156, CYAN, 1, .22),
         T(100, 300, line1, 62, INK, 700),
         T(100, 382, line2, 62, accent, 700),
         T(100, 462, desc, 22, SUB, 400)]
    x = 100
    for t in tags:
        d += tag(x, 520, t, CYAN)
        x += len(t) * 13 + 42
    d += [LINE(100, 742, 1500, 742, CYAN, 1, .18),
          T(100, 800, "XINMX.COM  //  AT歌词识别", 18, SUB, 500, True, spacing="1"),
          T(1500, 800, time, 22, accent, 600, True, anchor="end")]

    if motif == "wave":
        d += [CUT(980, 210, 520, 420, fill=SURFACE, so=.3),
              T(1010, 258, "WAVEFORM / 声纹", 15, CYAN, 600, True)]
        d += wave(1010, 300, 460, 230, 52, seed=.7, head=24)
        d += [LINE(1010, 570, 1470, 570, CYAN, 1, .3),
              T(1010, 606, "00:00", 14, SUB, 500, True), T(1470, 606, time, 14, SUB, 500, True, anchor="end")]
    elif motif == "timeline":
        d += [CUT(980, 210, 520, 420, fill=SURFACE, so=.3),
              T(1010, 258, "TIMELINE / 时间轴", 15, CYAN, 600, True)]
        rows = [("00:12.40", "折一只纸月亮挂在窗前"), ("00:18.96", "风把旧信件吹成了帆"),
                ("00:25.31", "你说远方有灯"), ("00:31.08", "我们就往那边走")]
        for i, (tc, lyric) in enumerate(rows):
            yy = 300 + i * 76
            on = i == 1
            d += [R(1006, yy, 468, 62, fill=VOID if on else CARD, stroke=CYAN if on else MUTE, so=.75 if on else .18),
                  T(1022, yy + 39, tc, 17, MAGENTA if on else SUB, 600, True),
                  T(1132, yy + 39, lyric, 19, INK if on else SUB, 500)]
    else:
        d += [CUT(980, 210, 520, 420, fill=SURFACE, so=.3),
              T(1010, 258, "ENGINES / 四引擎", 15, CYAN, 600, True)]
        names = ["Qwen3-ASR 0.6B", "Fun-ASR-Nano", "SenseVoiceSmall", "Paraformer-Large"]
        for i, n in enumerate(names):
            yy = 292 + i * 80
            on = i == 2
            d += [R(1006, yy, 468, 64, fill=VOID if on else CARD, stroke=CYAN if on else MUTE, so=.7 if on else .18),
                  T(1024, yy + 40, n, 19, INK if on else SUB, 600, True),
                  T(1456, yy + 40, "已安装" if on else "在线下载", 14, LIME if on else CYAN, 600, True, anchor="end")]
    svg(name, w, h, d)


# ---------- 软件界面：识别工作台 ----------
def shot_workspace():
    w, h = 1600, 920
    d = [CUT(28, 28, 1544, 864, fill=CARD, so=.28),
         R(28, 28, 1544, 62, fill=SURFACE, so=.18),
         *[f'<circle cx="{60 + i * 26}" cy="59" r="6" fill="{c}"/>' for i, c in enumerate([MAGENTA, "#FFB347", LIME])],
         T(180, 68, "AT歌词识别 1.1.0", 20, INK, 600, True),
         T(1552, 68, "100% 离线 · 零上传", 15, LIME, 600, True, anchor="end"),
         T(60, 132, "识别引擎 / ENGINE SELECT", 14, MAGENTA, 600, True, spacing="1")]

    engines = ["Qwen3-ASR", "Fun-ASR-Nano", "SenseVoiceSmall", "Paraformer-Large"]
    for i, n in enumerate(engines):
        x = 60 + i * 374
        on = i == 2
        d += [CUT(x, 150, 358, 74, fill=VOID if on else SURFACE, stroke=CYAN if on else MUTE, c=8, so=.85 if on else .2)]
        if on:
            d.append(R(x, 150, 4, 74, fill=CYAN, stroke=CYAN, so=0))
        d += [T(x + 20, 180, n, 17, CYAN if on else SUB, 600, True),
              T(x + 20, 206, ["52 语言 · 最强", "长句稳定", "最快 · 默认", "中文高精度"][i], 13, SUB, 400)]

    d += [CUT(60, 252, 440, 560, fill=SURFACE, so=.25),
          T(84, 292, "识别队列 / QUEUE", 15, CYAN, 600, True, spacing="1"),
          LINE(84, 308, 476, 308, CYAN, 1, .18)]
    queue = [("折一只纸月亮.mp3", "已识别", LIME), ("旧信件.mp3", "已识别", LIME),
             ("远方有灯.flac", "识别中", CYAN), ("往那边走.m4a", "待识别", SUB), ("潮汐.wav", "待识别", SUB)]
    for i, (name, state, col) in enumerate(queue):
        yy = 330 + i * 92
        d += [R(84, yy, 392, 78, fill=VOID, stroke=col if state != "待识别" else MUTE, so=.45),
              T(102, yy + 32, name, 17, INK, 500),
              T(102, yy + 60, "19s · 44.1kHz", 13, SUB, 400, True),
              T(458, yy + 60, state, 13, col, 600, True, anchor="end")]
    d += [T(84, 790, "拖入音频或文件夹 · 按文件名顺序逐首", 13, SUB, 400)]

    d += [CUT(524, 252, 1016, 560, fill=SURFACE, so=.25),
          T(548, 292, "折一只纸月亮.mp3", 20, INK, 600),
          T(1516, 292, "SenseVoiceSmall · 2.05s", 14, CYAN, 600, True, anchor="end")]
    d += wave(548, 320, 968, 92, 84, seed=1.3, head=41)
    d += [T(548, 442, "00:41.20", 14, MAGENTA, 600, True), T(1516, 442, "03:12.00", 14, SUB, 600, True, anchor="end")]
    d += [CUT(548, 462, 968, 74, fill=VOID, stroke=LIME, c=8, so=.55),
          T(568, 492, "已写入同名 LRC", 17, LIME, 600),
          T(568, 518, "~/Music/折一只纸月亮.lrc", 14, SUB, 400, True)]
    d += [T(548, 568, "歌词时间轴 / TIMELINE · 4 行", 14, CYAN, 600, True, spacing="1")]
    rows = [("00:12.40", "折一只纸月亮挂在窗前"), ("00:18.96", "风把旧信件吹成了帆"),
            ("00:25.31", "你说远方有灯"), ("00:31.08", "我们就往那边走")]
    for i, (tc, lyric) in enumerate(rows):
        yy = 586 + i * 48
        on = i == 1
        d += [R(548, yy, 968, 44, fill=VOID if on else CARD, stroke=CYAN if on else MUTE, so=.6 if on else .14),
              T(564, yy + 30, tc, 15, MAGENTA if on else SUB, 600, True),
              T(700, yy + 30, lyric, 16, INK if on else SUB, 500)]
    d += [LINE(548, 790, 1516, 790, CYAN, 1, .18),
          T(548, 838, "导出 LRC", 15, CYAN, 600, True), T(700, 838, "写回 ⌘S", 15, CYAN, 600, True),
          T(852, 838, "导出 SRT", 15, CYAN, 600, True), T(1516, 838, "设置…", 15, SUB, 600, True, anchor="end")]
    d += [T(60, 872, "127.0.0.1:8898 · 4/4 模型就绪 · 音频不出本机", 13, SUB, 400, True)]
    svg("shot-workspace.svg", w, h, d)


# ---------- 软件界面：时间轴校对 ----------
def shot_timeline():
    w, h = 1600, 920
    d = [CUT(28, 28, 1544, 864, fill=CARD, so=.28),
         R(28, 28, 1544, 62, fill=SURFACE, so=.18),
         T(60, 68, "AT歌词识别 — 时间轴校对", 20, INK, 600, True),
         T(1552, 68, "起振点对齐 · 逐字证据", 15, CYAN, 600, True, anchor="end"),
         T(60, 132, "PLAYHEAD 00:18.96  /  当前行 02", 14, MAGENTA, 600, True, spacing="1")]
    d += [CUT(60, 152, 1080, 300, fill=SURFACE, so=.3)]
    d += wave(84, 196, 1032, 220, 116, seed=2.1, head=52)
    d += [T(84, 438, "00:00", 13, SUB, 500, True), T(600, 438, "01:36", 13, SUB, 500, True),
          T(1116, 438, "03:12", 13, SUB, 500, True, anchor="end")]
    d += [CUT(1164, 152, 376, 300, fill=SURFACE, stroke=CYAN, c=10, so=.55),
          T(1188, 194, "对齐证据 / EVIDENCE", 14, CYAN, 600, True),
          LINE(1188, 210, 1516, 210, CYAN, 1, .22)]
    ev = [("起振点", "142 个"), ("置信度", "0.94"), ("命中率", "96%"), ("对齐引擎", "xm-fa 1.1.0")]
    for i, (k, v) in enumerate(ev):
        yy = 250 + i * 48
        d += [T(1188, yy, k, 14, SUB, 400), T(1516, yy, v, 15, LIME if i == 2 else INK, 600, True, anchor="end")]
    d += [T(1188, 428, "正文逐字相同、只差标点时不改判", 12, SUB, 400)]

    d += [CUT(60, 476, 1080, 336, fill=SURFACE, so=.25),
          T(84, 514, "可编辑时间轴 / TIMELINE", 15, CYAN, 600, True, spacing="1"),
          R(84, 532, 1032, 38, fill="#0E1728", stroke=CYAN, so=.35),
          T(100, 558, "时间码", 13, CYAN, 600, True), T(280, 558, "歌词（双击可改）", 13, CYAN, 600, True)]
    rows = [("00:06.12", "夜色落在窗台"), ("00:12.40", "折一只纸月亮挂在窗前"),
            ("00:18.96", "风把旧信件吹成了帆"), ("00:25.31", "你说远方有灯"),
            ("00:31.08", "我们就往那边走")]
    for i, (tc, lyric) in enumerate(rows):
        yy = 574 + i * 46
        on = i == 2
        d += [R(84, yy, 1032, 42, fill=VOID if on else CARD, stroke=CYAN if on else MUTE, so=.7 if on else .14),
              T(100, yy + 28, tc, 14, MAGENTA if on else SUB, 600, True),
              T(280, yy + 28, lyric, 16, INK if on else SUB, 500)]
    d += [CUT(1164, 476, 376, 336, fill=SURFACE, so=.25),
          T(1188, 514, "当前行 / NOW", 15, MAGENTA, 600, True),
          T(1188, 574, "00:18.96", 26, CYAN, 600, True),
          T(1188, 620, "风把旧信件吹成了帆", 19, INK, 500),
          LINE(1188, 646, 1516, 646, CYAN, 1, .22),
          T(1188, 684, "逐字 <mm:ss.xx>", 14, SUB, 400, True),
          T(1188, 720, "25fps 标准 SRT", 14, SUB, 400, True),
          T(1188, 756, "同名 LRC 写回", 14, LIME, 600, True),
          T(1188, 792, "拖动播放头边听边核对", 12, SUB, 400)]
    d += [T(60, 872, "双引擎复核 · 跨窗缝合 · 幻听过滤 · 标点分行", 13, SUB, 400, True)]
    svg("shot-graph.svg", w, h, d)


# ---------- 软件界面：引擎管理 ----------
def shot_engines():
    w, h = 1600, 920
    d = [CUT(28, 28, 1544, 864, fill=CARD, so=.28),
         R(28, 28, 1544, 62, fill=SURFACE, so=.18),
         T(60, 68, "引擎管理 / ENGINE MANAGER  ⌘E", 20, INK, 600, True),
         T(1552, 68, "4 / 4 模型就绪", 15, LIME, 600, True, anchor="end"),
         T(60, 132, "OFFLINE ONNX WEIGHTS / 全程本机 CPU 推理", 14, CYAN, 600, True, spacing="1")]
    cards = [("Qwen3-ASR 0.6B", "0.6B · INT8", "941 MB", "52 语言 / 22 方言", True),
             ("Fun-ASR-Nano 2512", "端到端 LLM-ASR · INT8", "963 MB", "中英日 + 中文方言", True),
             ("SenseVoiceSmall", "234M · INT8", "228 MB", "中英日韩粤 · 最快", True),
             ("Paraformer-Large", "220M · INT8", "217 MB", "中文高精度 · token 时间戳", True)]
    for i, (name, param, size, feat, ready) in enumerate(cards):
        x = 60 + (i % 2) * 760
        y = 158 + (i // 2) * 250
        d += [CUT(x, y, 728, 226, fill=SURFACE, stroke=CYAN if i == 2 else MUTE, c=10, so=.7 if i == 2 else .2),
              T(x + 24, y + 46, name, 22, INK, 600, True),
              T(x + 24, y + 82, param, 15, SUB, 400, True),
              T(x + 24, y + 116, size, 18, CYAN, 600, True),
              T(x + 24, y + 152, feat, 16, SUB, 400),
              LINE(x + 24, y + 170, x + 704, y + 170, CYAN, 1, .18),
              T(x + 24, y + 204, "已安装" if ready else "在线下载", 15, LIME if ready else CYAN, 600, True),
              T(x + 704, y + 204, "官方源 ↗", 14, SUB, 500, True, anchor="end")]
    d += [CUT(60, 668, 1488, 158, fill=SURFACE, so=.25),
          T(84, 706, "下载进度 / DOWNLOAD", 15, CYAN, 600, True, spacing="1"),
          T(1524, 706, "68%  ·  断点续传 / 备源自动切换", 14, SUB, 500, True, anchor="end"),
          R(84, 730, 1440, 16, fill=VOID, stroke=CYAN, so=.3),
          R(84, 730, 979, 16, fill="url(#bar)", stroke=CYAN, so=0),
          T(84, 786, "写入 ~/Library/Application Support/AT歌词识别/models/ · 不写入已签名的 App 包", 13, SUB, 400, True)]
    d += [T(60, 872, "sherpa-onnx 2.0.1 · ONNX Runtime · 不依赖 torch / funasr / 联网", 13, SUB, 400, True)]
    svg("shot-capture.svg", w, h, d)


if __name__ == "__main__":
    app_icon()
    poster("poster-start.svg", 1, "TUTORIAL 01  //  快速上手", "拖入一首歌，", "歌词自动就位。",
           "安装、批量队列、四引擎选择与同名 LRC 落盘。",
           ["05:12", "拖放", "四引擎"], "05:12", CYAN, "wave")
    poster("poster-links.svg", 2, "TUTORIAL 02  //  时间轴校对", "边听边改，", "每一行都对得上。",
           "声纹播放头、当前行高亮、可编辑时间码与写回。",
           ["08:03", "声纹", "逐字 LRC"], "08:03", MAGENTA, "timeline")
    poster("poster-template.svg", 3, "TUTORIAL 03  //  引擎与命令行", "四个引擎，", "按需装、按需换。",
           "引擎管理在线下载、识别设置与 cli.sh 用法。",
           ["06:47", "ONNX", "CLI"], "06:47", LIME, "engines")
    shot_workspace()
    shot_timeline()
    shot_engines()
    print("全部素材生成并通过 XML 校验")
