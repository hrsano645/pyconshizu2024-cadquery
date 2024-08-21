import cadquery as cq
from ocp_vscode import show_object, show

# 単位は全部mmとしています

# 蓋付きの入れ物を作ってみよう

# まず下側から作る。円筒を作る。shellで壁を作る。
ex2_iremono = cq.Workplane("XY").circle(100).extrude(50).faces(">Z").shell(-4)

# ふたを作る
ex2_futa = (
    cq.Workplane("XY")
    .circle(100)
    .extrude(10)
    .faces(">Z")
    .workplane()
    .circle(92)
    .extrude(4)
)

# 蓋を取りやすい様に、蓋の中央に穴を開ける
ex2_futa = ex2_futa.faces(">Z").workplane().circle(10).cutThruAll()

# 最後に表示
show_object(ex2_iremono.translate((0, -120, 0)), name="ex2_iremono", measure_tools=True)
show_object(ex2_futa.translate((220, -120, 0)), name="ex2_futa", measure_tools=True)
