# ※単位は全部mmとしています
# デモ：蓋付きの入れ物を作る
import cadquery as cq
from ocp_vscode import show_object

# まず下側から作る。
# 円筒を作る -> shellで壁を作る -> 下側（Zのマイナス側）の面にフィレット処理
#
ex2_iremono = (
    cq.Workplane("XY")
    .circle(50)
    .extrude(50)  # 高さ50mmの円筒を作る
    .faces(">Z")
    .shell(-4)  # 壁の厚み4mm
    .faces("<Z")
    .edges()  # 下側の面からエッジを取得
    .fillet(6)  # フィレット処理
)

# ふたを作る
# 円筒を作る -> 作った円筒の上にまた円筒を作る -> 下側の面にフィレット処理
ex2_futa = (
    cq.Workplane("XY")
    .circle(50)
    .extrude(10)  # 高さ10mmの円筒を作る
    .faces(">Z")
    .workplane()  # 作った円筒の上に新しいワークプレーンを作る
    .circle(50 - 6)
    .extrude(4)  # 径を小さくした高さ4mmの円筒を作る
    .faces("<Z")
    .edges()  # 下側の面からエッジを取得
    .fillet(6)  # フィレット処理
)

# 蓋を取りやすい様に、蓋の中央に穴を開ける
ex2_futa = ex2_futa.faces(">Z").workplane().circle(10).cutThruAll()

# 最後に表示
show_object(ex2_iremono, name="ex2_iremono")
show_object(ex2_futa.translate((120, 0, 0)), name="ex2_futa")

# show関数を使って表示する例(2つのオブジェクトを表示)
# show(
#     ex2_iremono,
#     ex2_futa.translate((120, 0, 0)),
#     names=["ex2_iremono", "ex2_futa"],
# )

# STLで書き出す：torelanceでメッシュの精度を細かくする
cq.exporters.export(ex2_iremono, "exports/ex2_iremono.stl", tolerance=0.001)
cq.exporters.export(ex2_futa, "exports/ex2_futa.stl", tolerance=0.001)
