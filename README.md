# pyconshizu2024-cadquery

PyCon mini Shizuoka 2024で利用するCadQueryのサンプルコード

## 環境の用意

### 検証した環境

* Python 3.11
* VSCode（説明でvscodeの拡張機能を利用します）
* [OCP CAD Viewer](https://marketplace.visualstudio.com/items?itemName=bernhard-42.ocp-cad-viewer)
* Apple Silicon Macでは conda環境が必要です。（miniforge + mambaにてテスト済み）
* Windowsの場合はpip + venvが利用できます。

### Mシリーズ Mac

※基本的に ocp-cad-viewerのREDAMEの手順に従ってください。簡易的な手順を残します。
<https://github.com/bernhard-42/vscode-ocp-cad-viewer?tab=readme-ov-file#installation-1:~:text=On%20Silicon%20Macs%20(ARM%20CPU)>

mambaの環境構築時の名称は `pyconshizu2024-cq` としていますが、任意の名称で構いません。

* `brew install miniforge`
* `mamba init $(basename "$SHELL")`
* `mamba create -n pyconshizu2024-cq python=3.10`
* `mamba activate pyconshizu2024-cq`
* vscodeのPythonインタープリターで、作成した環境を指定します。
* OCP CAD Viewerのインストール
* OCP CAD Viewerのサイドバーから `Quickstart CadQuery` を選択して、mamba環境を指定してインストールを進めます。
* （mambaのインストールが流れていれば問題ないと思います）
* OCP CAD ViewerのサイドバーでVIEWER MANAGERにパッケージのインストールがされていればOKです。

### Windows

* python -m venv .venv
* vscodeのPythonインタープリターで、作成した環境を指定します。
* OCP CAD Viewerのインストール
* OCP CAD Viewerのサイドバーから `Quickstart CadQuery` を選択して、インストールを進めます。
* OCP CAD ViewerのサイドバーでVIEWER MANAGERにパッケージのインストールがされていればOKです。
