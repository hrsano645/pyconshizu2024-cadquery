# ※単位は全部mmとしています
# デモ：Pythonロゴを使ってコースターを作る
import cadquery as cq
from ocp_vscode import show_object

# コースターの半径 * 厚み 50mm x 6mm
coaster_size = 50
coaster_tickness = 6

# Python logoのデータを取得 svgから輪郭を取りdxfにしたファイルを呼び出す
# https://commons.wikimedia.org/wiki/File:Python-logo-notext.svg
# 縮小調整した結果、おおよそ縦横56mm、輪郭全体の中心が原点になるように調整済み
logo_size = 56

# ファイルを読み込む
python_logo_rinkaku = cq.importers.importDXF("asset/python-logo-only_rinkaku.dxf")
# show_object(python_logo_rinkaku, name="Python Logo", measure_tools=True)

# 輪郭のみを取り出して押し出し、中心位置に持ってくる
logo_obj = (
    cq.Workplane("XY")
    .add(python_logo_rinkaku)
    .wires()
    .toPending()
    .extrude(6)
    .translate((0, 0, 3))
)
# show_object(logo_obj, name="Python Logo model")

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
    .fillet(2)
)
# show_object(coaster_base, name="Coaster base")

# 輪郭をコースターに切り抜く
coaster_result = coaster_base.cut(logo_obj)

# 対象を表示
show_object(coaster_result, name="Coaster with Python Logo")

# STLで書き出す
cq.exporters.export(coaster_result, "exports/ex3_coster.stl")

# TODO, この先考えるべきところ（応用として）
# 1️. ロゴのサイズに合わせて位置の自動調整は、どうするか？
#  -> まずロゴのバウンディングボックス（BoundingBox）を作り、そこから正確な大きさを元に位置を調整する
# 2. コースターのサイズで、ロゴのサイズに合わせて拡大縮小する方法は？_
#  -> （BoundingBox）で大きさをとった後に適切な拡大率でスケールすればいい
