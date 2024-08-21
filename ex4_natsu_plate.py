# %%
import cadquery as cq
from ocp_vscode import show_object, show

# フォントの設定(Macだとフォントパスの方が設定しやすそう？)
fontpath = "/Users/hiroshi/Library/Fonts/BIZUDGothic-Regular.ttf"


src_text = "25°　夏日\n30°真夏日"


## プレートを１枚作り、z軸上にテキストを配置する
# プレートの作成
plate = cq.Workplane("XY").box(100, 50, 5)

# プレートにテキストを配置
text_3d = (
    cq.Workplane("XY")
    .text(
        src_text,
        14,
        3,
        fontPath=fontpath,
    )
    .translate((0, 0, 2.5))
)

# プレートにテキストを配置
text_plate = plate.union(text_3d)

# 結果を表示
show(text_plate, measure_tools=True, axes=True, grid=True)

# %%
# 3DオブジェクトをSTLファイルとして保存
cq.exporters.export(text_plate, "text_plate.stl")

# %%
