# Digital Inker (MVP)

これはDigital InkerアプリケーションのMVP（Minimum Viable Product）版です。ユーザーは手書きの日本語/英語テキストを含む単一のPNGファイルを選択し、OCRを使用して機械が読み取り可能なテキストに変換することができます。

## 事前準備

このアプリケーションを実行するには、お使いのシステムにTesseract OCRエンジンがインストールされている必要があります。

### Ubuntu Linux の場合

ターミナルを開き、以下のコマンドを実行してTesseractと日本語言語パックをインストールします。

```bash
sudo apt-get update
sudo apt-get install tesseract-ocr tesseract-ocr-jpn
```

### Windows の場合

1.  **Tesseract インストーラーのダウンロード**:
    *   [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki) のページから、Windows用の公式Tesseractインストーラーをダウンロードします。最新の安定版をダウンロードすることをお勧めします。

2.  **インストーラーの実行**:
    *   ダウンロードした `.exe` ファイルを実行します。
    *   インストールの際、日本語OCRのサポートを有効にするために、必ず「Japanese」言語データコンポーネントを選択してください。

3.  **Tesseract を PATH に追加**:
    *   インストール後、Tesseractのインストールフォルダ（例: `C:\Program Files\Tesseract-OCR`）をシステムの `PATH` 環境変数に追加する必要があります。これにより、アプリケーションがTesseractの実行ファイルを見つけられるようになります。
    *   PATHにディレクトリを追加する方法については、「Windows 環境変数の編集」などで検索して手順をご確認ください。

## インストール

事前準備が完了したら、以下の手順でアプリケーションをセットアップします。

1.  **リポジトリのクローン（またはファイルのダウンロード）**:
    *   プロジェクトファイルをお使いのローカルマシンに取得します。

2.  **仮想環境の作成（推奨）**:
    *   他のプロジェクトとの競合を避けるため、Pythonの仮想環境を使用することを強くお勧めします。
    ```bash
    python -m venv venv
    # Windowsの場合
    venv\Scripts\activate
    # macOS/Linuxの場合
    source venv/bin/activate
    ```

3.  **依存関係のインストール**:
    *   `requirements.txt` ファイルを使って、必要なすべてのPythonライブラリをインストールします。
    ```bash
    pip install -r requirements.txt
    ```

## 使い方

アプリケーションを実行するには、ターミナルから `main.py` スクリプトを実行します。

```bash
python main.py
```

これによりGUIが起動します。GUIからは以下の操作が可能です:
1.  「PNGファイルを選択」をクリックして画像を選びます。
2.  「変換開始」をクリックしてOCR処理を実行します。
3.  結果はテキストエリアに表示され、同時に画像と同じディレクトリに `_output.txt` ファイルとして保存されます。
4.  「結果をクリップボードにコピー」をクリックして結果をコピーします。
