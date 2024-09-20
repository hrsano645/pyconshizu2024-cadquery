# ※単位は全部mmとしています
# デモ：基本的なモデルの作成
import cadquery as cq
from ocp_vscode import show_object

# 四角形の箱、サイズは 10x10x10mm
ex1_box = cq.Workplane("XY").box(10, 10, 10)
show_object(ex1_box, name="ex1_box", measure_tools=True)

# 多角形もできる：5角形で例。最初に2Dで図形を書いて押し出している。直径10mmの5角形
ex1_pentagon = cq.Workplane("XY").polygon(5, 10).extrude(10)
show_object(ex1_pentagon.translate((20, 0, 0)), name="ex1_pentagon")

# 球体
ex1_sphere = cq.Workplane("XY").sphere(4)
show_object(ex1_sphere.translate((40, 0, 0)), name="ex1_sphere", measure_tools=True)

# 円筒
ex1_cylinder = cq.Workplane("XY").circle(10).extrude(10)
show_object(ex1_cylinder.translate((60, 0, 0)), name="ex1_cylinder", measure_tools=True)

# 内側をくりぬいていく。壁の厚みは 2mm
# まず立方体を作り壁を作る。shellを使いくり抜く
# Z方向のfaces（面）を指示すると、その面を基準に空洞が作られる
# ref: https://cadquery.readthedocs.io/en/latest/examples.html#shelling-to-create-thin-features
ex1_hako = cq.Workplane("XY").box(10, 10, 10).faces(">Z").shell(-1)
# translateで移動させる
show_object(ex1_hako.translate((80, 0, 0)), name="ex1_hako", measure_tools=True)
