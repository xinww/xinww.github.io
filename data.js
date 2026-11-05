/* ============================================================
 * PrismNote 站点内容配置
 * 换产品时只改这个文件：品牌名、标题、下载项、教程、截图、FAQ 都在这里。
 * 界面截图与教程封面由 tools/gen_assets.py 生成，改完文案可重新生成。
 * ============================================================ */
window.SITE = {
  // —— 全站文案（对应 index.html 里的 data-text）——
  text: {
    brandName: 'PrismNote',
    brandSub: '棱镜笔记',
    brandWord: 'PRISMNOTE',
    ribbonLead: '本地优先的 Markdown 双链笔记 · 把想法连成一张网',
    ribbonLink: '了解特性 ↗',
    eyebrow: '本地优先 · 离线可用 · v2.4.1',
    heroTitle: '把想法，连成一张网。',
    heroLead: '跟着真实软件演示，完成双向链接、知识图谱与每日笔记。',
    downloadTitle: '下载 PrismNote',
    releaseLine: '桌面版 2.4.1 · build 2026.11.02 · 11/05 更新',
    releaseBadge: '已签名并公证',
    packageNote: '打开 DMG 后将 PrismNote.app 拖入「应用程序」，再从应用程序打开使用和更新。',
    workspaceTitle: '写作、连接、回看，都在一个窗口。',
    workspaceLead: '左边是笔记树，中间是编辑器，右边是关系图谱与反向链接。',
    helpTitle: '安装与使用',
    footerNote: '数据留在你的电脑里。',
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
    { icon: '◈', label: '纯本地存储' },
    { icon: '⤳', label: '双向链接' },
    { icon: '✳', label: '知识图谱' },
    { icon: '↗', label: '导出 Markdown / PDF' }
  ],

  // —— 视频教程：填 src 即可播放真实 mp4；留空则显示章节导览 ——
  tutorials: [
    {
      id: 'start',
      label: '快速上手与第一篇笔记',
      duration: '5 分 12 秒',
      caption: '快速上手与第一篇笔记 · 5 分 12 秒 · 中文解说与字幕',
      poster: 'assets/poster-start.svg',
      src: '',
      chapters: [
        { time: '00:00', title: '安装后第一次打开' },
        { time: '00:48', title: '建立笔记库与文件夹' },
        { time: '02:10', title: 'Markdown 写作与实时预览' },
        { time: '03:35', title: '每日笔记与模板' },
        { time: '04:26', title: '导出与备份' }
      ]
    },
    {
      id: 'links',
      label: '双向链接与知识图谱',
      duration: '8 分 03 秒',
      caption: '双向链接与知识图谱 · 8 分 03 秒 · 中文解说与字幕',
      poster: 'assets/poster-links.svg',
      src: '',
      chapters: [
        { time: '00:00', title: '用 [[链接]] 连接两篇笔记' },
        { time: '01:32', title: '反向链接面板怎么用' },
        { time: '03:04', title: '打开图谱视图' },
        { time: '05:20', title: '分组、筛选与聚焦' },
        { time: '07:11', title: '把图谱导出为图片' }
      ]
    },
    {
      id: 'template',
      label: '命令面板、模板与导出',
      duration: '6 分 47 秒',
      caption: '命令面板、模板与导出 · 6 分 47 秒 · 中文解说与字幕',
      poster: 'assets/poster-template.svg',
      src: '',
      chapters: [
        { time: '00:00', title: '⌘K 命令面板' },
        { time: '01:20', title: '快速捕获与跳转' },
        { time: '02:45', title: '自定义模板变量' },
        { time: '04:30', title: '批量导出 Markdown 与 PDF' },
        { time: '05:52', title: '插件与快捷键' }
      ]
    }
  ],

  // —— 下载项：platform 用于自动推荐（mac / mac-intel / windows / linux）——
  downloads: [
    {
      label: '下载 M 系列版',
      detail: 'Apple Silicon · macOS 12 及以上 · DMG 148.6 MiB',
      href: '#download',
      primary: true,
      platform: 'mac',
      recommendLabel: '推荐'
    },
    {
      label: '下载 Intel 版',
      detail: 'Intel · macOS 12 及以上 · DMG 156.2 MiB',
      href: '#download',
      platform: 'mac-intel'
    },
    {
      label: '下载旧系统兼容版',
      detail: 'macOS 10.15 及以上 · 兼容版 2.2.8 · 不含本地 AI 摘要 · DMG 92.4 MiB',
      href: '#download',
      platform: 'mac-legacy'
    }
  ],

  otherPlatforms: [
    {
      title: 'Windows 下载',
      linkLabel: '下载 Windows 版 2.4.1 ↗',
      href: '#download',
      note: 'Windows 10 / 11，64 位。',
      integrityAnchor: '#windows-integrity'
    },
    {
      title: 'Linux 下载',
      linkLabel: '下载 Linux AppImage ↗',
      href: '#download',
      note: 'Ubuntu 22.04 及以上，x86_64。',
      integrityAnchor: '#windows-integrity'
    }
  ],

  // —— 界面截图画廊 ——
  shots: [
    { id: 'workspace', label: '写作工作台', image: 'assets/shot-workspace.svg', caption: '双栏编辑与反向链接同屏。' },
    { id: 'graph', label: '知识图谱', image: 'assets/shot-graph.svg', caption: '把散落的笔记看成一张网。' },
    { id: 'capture', label: '命令面板', image: 'assets/shot-capture.svg', caption: '⌘K 唤起，随手捕获与跳转。' }
  ],

  // —— 安装与使用（FAQ）——
  faqs: [
    {
      id: 'install',
      title: 'macOS 安装指南',
      paragraphs: [
        '在「关于本机」查看芯片。M 系列选 Apple Silicon 包；Intel 的 macOS 12 及以上选常规版，10.15 至 11 选兼容版。打开对应芯片的 DMG，将 PrismNote.app 拖入「Applications／应用程序」，再从应用程序打开。系统权限按正常提示由本人授予。',
        '更新前先保存笔记库、退出旧版并保留备份。兼容版最低目标为 macOS 10.15；旧系统的实际兼容性仍需实机核对。首次启动会让你选择一个文件夹作为笔记库，之后所有内容都以普通 Markdown 文件保存在这里。'
      ]
    },
    {
      id: 'windows-integrity',
      title: 'Windows / Linux 安装与文件校验',
      paragraphs: [
        'Windows 10 / 11 64 位双击安装包按向导安装到当前用户目录；Linux 下载 AppImage 后赋予可执行权限即可运行。两个平台都不需要联网激活，本地写作、搜索与图谱完全离线可用。',
        '安装包的发布校验值（SHA-256）：'
      ],
      checksums: [
        { label: 'Windows 2.4.1 安装包', value: '8c2f41de9b7a0536f1e4d89c20ab5e7f361d940cb28ea6f3d5170b8c9e4a26' },
        { label: 'Linux AppImage', value: '3b7e09ac51d8462f0e9a7c3b18d5f260e4c8179ab03d65f2c4e918a0d7b3c6' }
      ],
      paragraphsAfter: [
        '若系统安全软件提示风险，请先暂停安装并联系发布者核实，不要关闭系统安全保护。校验一致不等于绝对安全保证。历史版本的第三方对应源码与许可证可在发布者站点获取。'
      ]
    },
    {
      id: 'storage',
      title: '我的笔记存在哪里？会不会上传？',
      paragraphs: [
        '笔记库是你电脑上的一个普通文件夹，每篇笔记都是一个 .md 文件，图片和附件放在同级的 assets 目录。不登录也能用，软件不会把笔记内容上传到服务器。',
        '想多设备使用时，把笔记库放进你自己的同步盘（iCloud Drive、Dropbox、Syncthing 等）即可；软件只读写文件，不接管同步。'
      ]
    },
    {
      id: 'migrate',
      title: '怎么从其他笔记软件迁移？',
      paragraphs: [
        '在「文件 → 导入笔记库」选择原有文件夹，支持直接导入 Markdown、纯文本与 HTML；Front Matter 会保留为笔记属性。来自 Notion、Obsidian、语雀的导出包可先解压后再导入。',
        '导入前建议先复制一份原文件夹。导入是复制而非移动，原数据不会被修改。'
      ]
    },
    {
      id: 'license',
      title: '激活码、AI 摘要和导出有什么区别？',
      paragraphs: [
        '本地写作、搜索、双向链接与图谱都是免费功能，不需要激活码。导出 Markdown、PDF 与图片同样免费。',
        '可选的「本地 AI 摘要」使用设备端模型，需要单独下载模型包，不消耗额度；在线 AI 扩写为订阅功能，在「帮助 → 我的订阅」查看状态。激活码绑定设备，换机请联系发布者。'
      ]
    },
    {
      id: 'integrity',
      title: '文件校验与第三方许可证',
      paragraphs: ['正式发布包的 SHA-256（点击右侧可复制）：'],
      checksums: [
        { label: 'M 系列 DMG', value: '004c10e76965d987aa8773be102bfba8f39547fe46712cc90f8ec3e05569daf9' },
        { label: 'Intel DMG', value: '7a47e11af9d4b8e3eb5bbc0b895c7c35e8d8973d67462e377d17dc7ea56f70f0' },
        { label: '旧系统兼容版 DMG', value: 'c72351c165494a6ee901f76bf31c10549e4dd7b229dcce8d211d4a000197f884' }
      ],
      paragraphsAfter: [
        '第三方组件包括 CodeMirror 6、Mermaid、Lucide 图标与 Qt 6.8，各自许可证保留在 App 内「帮助 → 关于」中。对应源码与重新链接说明可向发布者索取。'
      ]
    }
  ]
};
