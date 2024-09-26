# ※単位は全部mmとしています
# デモ：Pythonロゴを使ってコースターを作る
import cadquery as cq
from ocp_vscode import show_object

# コースターの半径 * 厚み 50mm x 3mm
coaster_size = 50
coaster_tickness = 3

# Python logoのデータを取得 svgから輪郭を取りdxfにしたファイルを呼び出す
# https://commons.wikimedia.org/wiki/File:Python-logo-notext.svg
# 縮小調整した結果、おおよそ縦横56mm、輪郭全体の中心が原点になるように調整済み
logo_size = 56

# ファイルを読み込む
python_logo_rinkaku = cq.importers.importDXF("asset/python-logo-only_rinkaku.dxf")
# show_object(python_logo_rinkaku, name="Python Logo")

# 輪郭のみを取り出して押し出し、中心位置に持ってくる
# DXFからワイヤーのみ(wires)を取り出す（toPending）、押し出す（extrude）
logo_obj = (
    cq.Workplane("XY")
    .add(python_logo_rinkaku)
    .wires()
    .toPending()
    .extrude(3)
    .translate((0, 0, 2))
)
# show_object(
#     logo_obj,
#     name="Python Logo model",
# )

# コースターの土台を作る。円筒を作り下面の外周にフィレットをかける
coaster_base = (
    cq.Workplane("XY")
    .cylinder(coaster_tickness, coaster_size)
    .translate(
        (
            0,
            0,
            coaster_tickness / 2,
        )
    )
    .faces(">X")
    .fillet(0.5)
)
# show_object(
#     coaster_base,
#     name="Coaster base",
# )

# 輪郭をコースターに切り抜く
coaster_result = coaster_base.cut(logo_obj)

# 対象を表示
show_object(
    coaster_result,
    name="Coaster with Python Logo",
)

# STLで書き出す: トレランスを細かくして輪郭を綺麗にする
cq.exporters.export(coaster_result, "exports/ex3_coster.stl", tolerance=0.001)
