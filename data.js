/* ============================================================
 * www.xinmx.com 站点内容配置 —— 产品：AT歌词识别
 * 换产品时只改这个文件：品牌、标题、下载项、教程、截图、FAQ 都在这里。
 * 界面截图与教程封面由 tools/gen_assets.py 生成。
 * ============================================================ */
window.SITE = {
  // —— 全站文案（对应 index.html 里的 data-text）——
  text: {
    brandName: 'XINMX.COM',
    brandSub: 'AT歌词识别',
    brandWord: 'XINMX.COM',
    documentTitle: 'www.xinmx.com | AT歌词识别 · 离线歌词识别与自动打轴',
    ribbonLead: '拖入一首歌 · 四个离线引擎 · 自动打轴 · 同名 LRC 落盘',
    ribbonLink: '了解引擎 ↗',
    eyebrow: 'AT歌词识别 1.1.0 · 四个离线 ASR 引擎 · 100% 本机',
    heroTitle: '把一首歌，变成带时间轴的歌词。',
    heroLead: '拖入音频或整个文件夹，四个离线引擎任选其一；自动识别、起振点对齐、逐行打轴，识别完就在歌曲同目录写一份 LRC。',
    downloadTitle: '下载 AT歌词识别',
    releaseLine: 'macOS 版 1.1.0 · 2026-11-12 更新 · 原生 AppKit 单窗口',
    releaseBadge: '全程离线 · 零上传',
    packageNote: '打开 DMG 后将 AT歌词识别.app 拖入「应用程序」。首次启动会自动拉起本机服务（仅监听 127.0.0.1:8898），音频与模型都不出本机。',
    workspaceTitle: '识别、校对、导出，都在一个窗口。',
    workspaceLead: '左栏是批量队列，右栏是播放条、可编辑时间轴与导出工具条。',
    helpTitle: '安装与使用',
    footerNote: '音频不出本机 · 服务只监听 127.0.0.1',
    publisher: '联系发布者 ↗'
  },

  // —— 顶部导航 ——
  nav: [
    { label: '视频教程', href: '#tutorial' },
    { label: '软件界面', href: '#workspace' },
    { label: '功能特性', href: '#features' },
    { label: '安装指南', href: '#help' },
    { label: '联系发布者 ↗', href: '#contact' }
  ],

  // —— 特性条 ——
  features: [
    { icon: '◈', label: '四个离线 ASR 引擎' },
    { icon: '⌁', label: '100% 本机 · 零上传' },
    { icon: '≡', label: '起振点对齐 · 逐字 LRC' },
    { icon: '↗', label: 'LRC / SRT / JSON 导出' }
  ],

  // —— 视频教程：填 src 即可播放真实 mp4；留空则显示章节导览 ——
  tutorials: [
    {
      id: 'start',
      label: '拖入歌曲与首次识别',
      duration: '5 分 12 秒',
      caption: '拖入歌曲与首次识别 · 5 分 12 秒 · 中文解说与字幕',
      poster: 'assets/poster-start.svg',
      src: '',
      chapters: [
        { time: '00:00', title: '安装与第一次打开' },
        { time: '00:42', title: '把音频或整个文件夹拖进队列' },
        { time: '01:38', title: '四个引擎怎么选、场景与范围' },
        { time: '02:55', title: '开始识别与进度条' },
        { time: '04:10', title: '同名 LRC 自动写到歌曲目录' }
      ]
    },
    {
      id: 'timeline',
      label: '时间轴校对与写回',
      duration: '8 分 03 秒',
      caption: '时间轴校对与写回 · 8 分 03 秒 · 中文解说与字幕',
      poster: 'assets/poster-links.svg',
      src: '',
      chapters: [
        { time: '00:00', title: '播放条、声纹与播放头' },
        { time: '01:26', title: '当前行高亮，边听边核对' },
        { time: '03:04', title: '双击修改时间码与文字' },
        { time: '05:12', title: '写回 LRC 与 ⌘S' },
        { time: '06:48', title: '切到队列里下一首，改动不丢' }
      ]
    },
    {
      id: 'engines',
      label: '引擎管理与命令行',
      duration: '6 分 47 秒',
      caption: '引擎管理与命令行 · 6 分 47 秒 · 中文解说与字幕',
      poster: 'assets/poster-template.svg',
      src: '',
      chapters: [
        { time: '00:00', title: '四款 ONNX 权重的差别' },
        { time: '01:32', title: '⌘E 引擎管理：在线下载与断点续传' },
        { time: '03:10', title: '识别设置：切窗、缝合、双引擎复核' },
        { time: '04:36', title: 'cli.sh：transcribe / align / models' },
        { time: '05:40', title: '导出 SRT、JSON 与逐字证据' }
      ]
    }
  ],

  // —— 下载项：platform 用于自动推荐 ——
  // href 为占位；填真实 DMG 地址后即可直接下载。
  downloads: [
    {
      label: '下载 Apple Silicon 版',
      detail: 'M 系列 · macOS 12 及以上 · 内置 SenseVoiceSmall 默认引擎 · DMG',
      href: '#download',
      primary: true,
      platform: 'mac',
      recommendLabel: '推荐'
    },
    {
      label: '下载 Intel 版',
      detail: 'Intel · macOS 12 及以上 · 同一套四引擎 · DMG',
      href: '#download',
      platform: 'mac-intel'
    },
    {
      label: '下载精简版（不含模型）',
      detail: '体积更小 · 启动后在「引擎管理」里按需下载四款权重',
      href: '#download',
      platform: 'mac-legacy'
    }
  ],

  // 产品目前仅提供 macOS 版，不列虚构的 Windows / Linux 包。
  otherPlatforms: [],

  // —— 界面截图画廊 ——
  shots: [
    { id: 'workspace', label: '识别工作台', image: 'assets/shot-workspace.svg', caption: '四引擎切换条、批量队列与结果卡同屏。' },
    { id: 'timeline', label: '时间轴校对', image: 'assets/shot-graph.svg', caption: '声纹播放头 + 当前行高亮，时间码可直接改。' },
    { id: 'engines', label: '引擎管理', image: 'assets/shot-capture.svg', caption: '四款 ONNX 权重的体积、状态与在线下载。' }
  ],

  // —— 安装与使用（FAQ）——
  faqs: [
    {
      id: 'install',
      title: 'macOS 安装与首次打开',
      paragraphs: [
        '打开对应芯片的 DMG，把 AT歌词识别.app 拖入「应用程序」再从那里启动。App 是原生 AppKit 单窗口，没有 WebView、没有账号，首次启动会自动拉起包内 Python 服务，服务只绑定 127.0.0.1:8898，退出时回收端口。',
        '把一首歌拖进左栏队列即可开始识别，也可以一次拖多首或整个文件夹，按文件名顺序逐首处理。默认引擎是 SenseVoiceSmall（最快），想换引擎在顶部切换条或「识别设置」里选。'
      ]
    },
    {
      id: 'engines',
      title: '四个离线引擎怎么选？',
      paragraphs: [
        'Qwen3-ASR 0.6B：52 语言 / 22 方言，说唱、方言与噪声最强；Fun-ASR-Nano：中英日 + 中文方言，长句稳定且带标点；SenseVoiceSmall：中英日韩粤，最快，默认引擎；Paraformer-Large：中文高精度，带 token 级时间戳。',
        '四款都是 sherpa-onnx 官方导出的 ONNX 权重，由包内的 ONNX Runtime 在 CPU 上推理，不依赖 torch / funasr / modelscope，也不需要联网。缺哪个引擎，用菜单「AT歌词识别 → 引擎管理…」（⌘E）在线下载，支持多线程分片、断点续传与备源自动切换；下载的模型放在 ~/Library/Application Support/AT歌词识别/models/，不写进已签名的 App 包。'
      ]
    },
    {
      id: 'align',
      title: '时间轴是怎么打出来的？已有歌词呢？',
      paragraphs: [
        '先按静音切窗（不做等长硬切），窗口边界截断的半句做字符级缝合；默认开启双引擎复核，正文逐字相同只差标点时不改判。起振点对齐检测全曲音节能量上升沿，按整窗字符数等比取点，每个字的起点都是真实声学事件，不依赖模型返回的 token 时间戳。之后做幻听过滤、口头噪声清理、标点分行，逐字 <mm:ss.xx> 可选。',
        '如果已经有准确歌词，走「能量打轴」：按行字数对累积人声能量取分位点，全程不经过 ASR。'
      ]
    },
    {
      id: 'export',
      title: '导出格式与写回',
      paragraphs: [
        'LRC 是默认主格式（可开逐字 LRC）；SRT 为 25fps 帧网格、首条从零、相邻零间隙；JSON 含 format / meta / 逐行 start-end 与逐字数组。三种格式共用同一个渲染入口，改完歌词再导出不会丢时间码。',
        '识别完恒在音频同目录写一份 <歌名>.lrc；表格里改完点「写回」或 ⌘S 覆盖同一个文件，不会另存副本。一首歌始终只有一份主歌词，重跑覆盖、换格式时只清理自己生成的旧格式，别人的 .lrc 不会被误删。'
      ]
    },
    {
      id: 'privacy',
      title: '离线与隐私',
      paragraphs: [
        '模型、解码器、运行时与界面全在 App 包内；界面没有 CDN、在线字体或统计脚本。Info.plist 只声明 NSAllowsLocalNetworking，服务只绑定 127.0.0.1。不写系统目录：运行日志在 ~/Library/Logs/AT歌词识别.log，配置在 ~/Library/Application Support/AT歌词识别/。',
        '音频不出本机；主歌词写到音频同目录，其余格式写进本机歌词缓存（加密文件名），从不上传。'
      ]
    },
    {
      id: 'integrity',
      title: '文件校验与第三方许可证',
      paragraphs: [
        '正式发布包的 SHA-256 与第三方组件许可证随发布页 / App 内「关于」提供；本站不内联校验值，请以实际下载到的文件为准自行核对。',
        '运行时包含 sherpa-onnx 2.0.1、ONNX Runtime 与包内 ffmpeg，各组件许可证保留在 App 内。'
      ]
    }
  ]
};
