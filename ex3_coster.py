import cadquery as cq
from ocp_vscode import show_object

# Python logoを使ってコースターを作ってみる

# Python logoのデータを取得 svgから輪郭を取りdxfにしたファイルを呼び出す
# https://commons.wikimedia.org/wiki/File:Python-logo-notext.svg

# ファイルを読み込む
python_logo_rinkaku = cq.importers.importDXF("asset/python-logo-only_rinkaku.dxf")
# show_object(python_logo_rinkaku, name="Python Logo", measure_tools=True)

# 輪郭のみを取り出して押し出し
logo_obj = cq.Workplane("XY").add(python_logo_rinkaku).wires().toPending().extrude(4)

show_object(logo_obj, name="Python Logo model")

# コースターのサイズ 100mm x 6mm
coaster_size = 100

# 輪郭から切り抜き対象の面を作成

# コースターの周りの壁を作成

# 対象を表示

# STLで書き出す
