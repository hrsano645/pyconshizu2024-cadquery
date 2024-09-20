# ※単位は全部mmとしています
# デモ：蓋付きの入れ物を作る
import cadquery as cq
from ocp_vscode import show_object

# まず下側から作る。円筒を作る。shellで壁を作る。
ex2_iremono = (
    cq.Workplane("XY")
    .circle(100)
    .extrude(50)
    .faces(">Z")
    .shell(-4)
    .faces("<Z")
    .fillet(6)
)

# ふたを作る
ex2_futa = (
    cq.Workplane("XY")
    .circle(100)
    .extrude(10)
    .faces(">Z")
    .workplane()
    .circle(92)
    .extrude(4)
    .faces("<Z")
    .fillet(6)
)

# 蓋を取りやすい様に、蓋の中央に穴を開ける
ex2_futa = ex2_futa.faces(">Z").workplane().circle(10).cutThruAll()

# 最後に表示
show_object(ex2_iremono, name="ex2_iremono")
show_object(ex2_futa.translate((220, 0, 0)), name="ex2_futa")

# show関数を使って表示する例(2つのオブジェクトを表示)
# show(
#     ex2_iremono,
#     ex2_futa.translate((220, 0, 0)),
#     names=["ex2_iremono", "ex2_futa"],
#     ,
# )

# STLで書き出す
cq.exporters.export(ex2_iremono, "exports/ex2_iremono.stl", tolerance=0.001)
cq.exporters.export(ex2_futa, "exports/ex2_futa.stl", tolerance=0.001)
