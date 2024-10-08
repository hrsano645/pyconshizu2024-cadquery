# ※単位は全部mmとしています
# デモ：夏の気温表示プレートを作る
import cadquery as cq
from ocp_vscode import show_object

# 各種設定
# フォントの設定(Macだとフォントパスの方が設定しやすそう？)
fontpath = ""

# モデルのサイズ
base_plate_width = 150
base_plate_height = 100
base_plate_thickness = 5

# 窪みのサイズとクリアランス
kubomi_width = 68
kubomi_height = 82
kubomi_thickness = 2
kubomi_clearance = 2

# 表示するテキスト
src_text = "【危険温度】\n25:　夏日\n30:真夏日\n35:猛暑日"

# プレート全体の作成
base_plate = (
    cq.Workplane("XY")
    .box(base_plate_width, base_plate_height, base_plate_thickness)
    .edges("|Z")
    .fillet(2)
)
show_object(
    base_plate,
    name="base_plate",
)

# 右側に温湿度計を乗せる窪みを作る
# 窪み用モデルを作る: 82 x 68 で2mm窪ませる。
kubomi = (
    cq.Workplane("XY")
    .box(kubomi_width, kubomi_height, kubomi_thickness)
    .edges("|Z")
    .fillet(1.8)
)
# 窪み用モデルを移動させる。左側に寄せる。クリアランスは 上と左が2mmになる様にする
# 左なので-方向に移動させる
move_x = -(base_plate_width - kubomi_width) / 2 + kubomi_clearance
# 上からなので+方向に移動させる
move_y = (base_plate_height - kubomi_height) / 2 - kubomi_clearance
print(f"窪みの移動量: {move_x=}, {move_y=}")
kubomi = kubomi.translate((move_x, move_y, 2))

# 窪みをプレートから切り抜く
show_object(
    kubomi,
    name="kubomi",
)
base_plate = base_plate.cut(kubomi)
show_object(
    base_plate,
    name="cut base_plate",
)

# プレートにテキストを配置
text_3d = (
    cq.Workplane("XY")
    .text(
        src_text,
        14,
        2,
        fontPath=fontpath,
    )
    .translate((38, 0, 2.5))
)
text_base_plate = base_plate.union(text_3d)

# 結果を表示
show_object(
    text_base_plate,
    name="text_base_plate",
)

# 3DオブジェクトをSTLファイルとして保存
cq.exporters.export(text_base_plate, "exports/natsu_plate.stl")
# stepファイルとして保存
cq.exporters.export(text_base_plate, "exports/natsu_plate.step")
