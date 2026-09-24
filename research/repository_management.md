# 仓库管理与外部材料

仓库：https://github.com/js110/Bpaper （公开）。本机项目根目录保持 `/Users/jiangsheng/Desktop/crowdsensing_task_privacy`。

纳入版本管理：英文 LaTeX 与 PDF、源码包、生成图表、生图提示词和出处、仿真与分析代码、配置、依赖清单、预处理窗口、所有已保存的实验日志和汇总、训练通道、研究与内部审稿记录。失败/中断/旧版本实验保持原有目录和排除说明，不混入最终比较。

不上传的本地材料：第三方论文 PDF 及全文提取文本/网页、GeoLife 原始压缩包、虚拟环境、缓存、临时编译产物、重复的源码解包编译目录。未为第三方全文取得再分发授权；原包超过 GitHub 单文件限制。保留文献元数据、DOI、来源清单、阅读笔记、哈希和本机获取记录。原始材料仍保留在本机。

## 获取 GeoLife 原包

在根目录执行：

```bash
python3 - <<'PY'
import hashlib, json, pathlib, urllib.request
manifest = json.loads(pathlib.Path('data/manifest.json').read_text())
target = pathlib.Path('data/geolife.zip')
if not target.exists():
    urllib.request.urlretrieve(manifest['source_url'], target)
assert hashlib.sha256(target.read_bytes()).hexdigest() == manifest['source_sha256']
PY
```

之后使用 README 的预处理、测试、审计和复现命令。GeoLife 来源条款和原始作者归属继续适用；本项目未另行授予原数据许可。`literature/recent/privic_*.py` 为作者公开 MIT 代码，许可证保留在同目录的 `PRIVIC_LICENSE`。Elsevier 模板文件保留其原始许可头。

## 后续日常操作

```bash
git status --short
git add <本次修改的文件>
git commit -m "Describe manuscript or experiment changes"
git push
```

首次初始化空仓库使用 `main`；后续需隔离的修改分支使用 `js/` 前缀。不要强制推送改写远端历史。每次改动稿件后重新编译，并同步源码包及交付清单。未提交的本机外部材料不会因忽略规则被删除。
