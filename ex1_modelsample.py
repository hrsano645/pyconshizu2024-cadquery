# ※単位は全部mmとしています
# デモ：基本的なモデルの作成
import cadquery as cq
from ocp_vscode import show_object

# 四角形の箱、サイズは 10x10x10mm
ex1_box = cq.Workplane("XY").box(10, 10, 10)
show_object(
    ex1_box,
    name="ex1_box",
)

# 球体 半径10mm
ex1_sphere = cq.Workplane("XY").sphere(10)
show_object(
    ex1_sphere.translate((20, 0, 0)),  # translateで移動 20mm右に移動
    name="ex1_sphere",
)

# 円筒2種類の作り方
# 2Dで円を書いてから押し出す方法
ex1_cylinder_2d = cq.Workplane("XY").circle(6).extrude(10)
show_object(
    ex1_cylinder_2d.translate((40, 0, 0)),
    name="ex1_cylinder_2d",
)
# 3Dのcylinderを使う方法
ex1_cylinder_3d = cq.Workplane("XY").cylinder(10, 6)
show_object(
    ex1_cylinder_3d.translate((60, 0, 0)),
    name="ex1_cylinder_3d",
)

# 多角形：5角形で例。最初に2Dで図形を書いて押し出している。5角形
ex1_pentagon = cq.Workplane("XY").polygon(5, 10).extrude(10)
show_object(
    ex1_pentagon.translate((80, 0, 0)),
    name="ex1_pentagon",
)

# 内側をくりぬいていく。壁の厚みは 1mm
# まず立方体を作り壁を作る。shellを使いくり抜く
ex1_hako = (
    cq.Workplane("XY")
    .box(10, 10, 10)
    .faces(">Z")
    .shell(-1)  # Z方向のfaces（面）を指示すると、その面を基準に空洞が作られる
)
show_object(
    ex1_hako.translate((100, 0, 0)),
    name="ex1_hako",
)
# ref: https://cadquery.readthedocs.io/en/latest/examples.html#shelling-to-create-thin-features
