import cadquery as cq
from ocp_vscode import show_object, show

# 単位は全部mm

# 四角形の箱、サイズは 10x10x10
box = cq.Workplane("XY").box(10, 10, 10)


# 次に 内側をくりぬいていく。壁の厚みは 2mm
## まずは、外側の壁を作る
box = cq.Workplane("XY").box(10, 10, 10)


# 多角形もできる。（5角形で例

# 円筒も

# とりあえず箱的な物はこうやってできるよ

ふたを作ってみよう

#
