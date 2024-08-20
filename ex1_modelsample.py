import cadquery as cq
from ocp_vscode import show_object

# 単位は全部mmとしています

# 四角形の箱、サイズは 10x10x10mm
ex1_box = cq.Workplane("XY").box(10, 10, 10)
show_object(ex1_box, name="ex1_box", measure_tools=True)

# 次に 内側をくりぬいていく。壁の厚みは 2mm
# まずは、外側の壁を作る,  次に内側の壁を作る: shellで内部をくりぬく
ex1_hako = cq.Workplane("XY").box(10, 10, 10).faces(">Z").workplane().shell(-2)
# translateで移動させる
show_object(ex1_hako.translate((20, 0, 0)), name="ex1_hako", measure_tools=True)

# 多角形もできる：5角形で例。最初に2Dで図形を書いて押し出している。直径10mmの5角形
ex1_pentagon = cq.Workplane("XY").polygon(5, 10).extrude(10)
show_object(ex1_pentagon.translate((40, 0, 0)), name="ex1_pentagon", measure_tools=True)

# 球体
ex1_sphere = cq.Workplane("XY").sphere(4)
show_object(ex1_sphere.translate((60, 0, 0)), name="ex1_sphere", measure_tools=True)

# 円筒
ex1_cylinder = cq.Workplane("XY").circle(10).extrude(10)
show_object(ex1_cylinder.translate((80, 0, 0)), name="ex1_cylinder", measure_tools=True)
