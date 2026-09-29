# 仓库管理与外部材料

仓库：https://github.com/js110/Bpaper

main 是当前论文、代码、配置、最终实验依据和投稿包的唯一主线。已经淘汰的草稿、失败/中断运行、旧比较版本、构建日志和预览截图不继续保留在 main；如需追溯，使用 Git 历史恢复，不在当前树中维持重复副本。

## 版本管理范围

当前 main 保留：

- paper/：正式主稿、Supplement、最终上传文件和当前实际引用的图表/表格；
- src/、tests/、configs/：当前实现、测试和仍可执行的冻结配置；
- data/：预处理后的 GeoLife 拆分及 manifest；
- results/：正文与 Supplement 当前结论对应的冻结实验结果、分析和 provenance；
- literature/：可再分发的文献元数据、公开比较代码及许可证；
- research/：当前协议、进度、状态、内部审稿结论和必要研究说明。

不跟踪：

- Microsoft GeoLife 原始压缩包；
- 第三方论文 PDF、全文提取文本和网页副本；
- 虚拟环境、缓存、LaTeX 临时文件和 build/ 临时目录；
- 已被最终版本替代的中间草稿和失败运行副本。

## 获取 GeoLife 原包

~~~bash
python3 - <<'PY'
import hashlib, json, pathlib, urllib.request
manifest = json.loads(pathlib.Path('data/manifest.json').read_text())
target = pathlib.Path('data/geolife.zip')
if not target.exists():
    urllib.request.urlretrieve(manifest['source_url'], target)
assert hashlib.sha256(target.read_bytes()).hexdigest() == manifest['source_sha256']
PY
python3 -m src.prepare_data
~~~

原始数据的来源条款继续适用。本仓库不重新授予 GeoLife 数据许可。literature/recent/ 中保留的 PRIVIC 公开代码按其原许可证管理。

## 日常操作

~~~bash
git status --short
git add <files>
git commit -m "Describe the change"
git push origin main
~~~

较大的新实验或方法修改建议先建独立分支，再通过 PR 合入 main。不要强制推送改写 main 历史。每次影响正式稿或投稿包的修改都应重新运行测试和最终 package workflow。
