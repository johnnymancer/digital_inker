import sys
import os
import cv2
import pytesseract
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QTextEdit, QLabel, QFileDialog, QMessageBox
)
from PyQt6.QtGui import QGuiApplication

class DigitalInkerApp(QMainWindow):
    """
    Digital Inker MVPのメインアプリケーションクラス。
    PyQt6を使用してGUIを構築し、手書きPNG画像のOCR処理機能を提供します。
    """
    def __init__(self):
        """
        アプリケーションの初期化、UIのセットアップ、シグナルとスロットの接続を行います。
        """
        super().__init__()
        self.setWindowTitle("Digital Inker MVP")
        self.setGeometry(100, 100, 600, 500)

        # 現在選択されているファイルパスを保持する変数
        self.selected_file_path = None

        # --- UI要素のセットアップ ---
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # ファイル選択ボタンと選択されたファイル名を表示するラベル
        self.select_file_button = QPushButton("PNGファイルを選択 (Select PNG File)")
        self.file_path_label = QLabel("選択されたファイル: なし (No file selected)")

        # OCR変換を開始するボタン
        self.start_conversion_button = QPushButton("変換開始 (Start Conversion)")

        # OCR結果を表示するテキストエリア
        self.result_text_area = QTextEdit()
        self.result_text_area.setPlaceholderText("ここに変換結果が表示されます。 (Conversion result will be displayed here.)")

        # 結果をクリップボードにコピーするボタン
        self.copy_button = QPushButton("結果をクリップボードにコピー (Copy to Clipboard)")

        # --- UIレイアウトへのウィジェット配置 ---
        self.layout.addWidget(self.select_file_button)
        self.layout.addWidget(self.file_path_label)
        self.layout.addSpacing(20)
        self.layout.addWidget(self.start_conversion_button)
        self.layout.addWidget(self.result_text_area)
        self.layout.addWidget(self.copy_button)

        # --- シグナルとスロットの接続 ---
        # 各ボタンのクリックイベントに対応するメソッドを接続します。
        self.select_file_button.clicked.connect(self.select_file)
        self.start_conversion_button.clicked.connect(self.start_conversion)
        self.copy_button.clicked.connect(self.copy_to_clipboard)

    def select_file(self):
        """
        「PNGファイルを選択」ボタンがクリックされたときに呼び出されます。
        ファイルダイアログを開き、ユーザーが選択したPNGファイルのパスを取得して保持します。
        """
        # QFileDialogを開いてユーザーにファイルを選択させる
        file_path, _ = QFileDialog.getOpenFileName(self, "PNGファイルを選択", "", "PNG Files (*.png)")
        if file_path:
            self.selected_file_path = file_path
            # ラベルに選択されたファイル名を表示
            self.file_path_label.setText(f"選択されたファイル: {os.path.basename(file_path)}")
            self.result_text_area.clear()

    def start_conversion(self):
        """
        「変換開始」ボタンがクリックされたときに呼び出されます。
        選択された画像をOCR処理し、結果をテキストエリアに表示し、ファイルにも保存します。
        """
        # ファイルが選択されているかチェック
        if not self.selected_file_path:
            QMessageBox.warning(self, "注意", "まずPNGファイルを選択してください。")
            return

        try:
            # 処理中であることをユーザーに通知
            self.result_text_area.setText("変換中... (Converting...)")
            QApplication.processEvents() # GUIの表示を強制的に更新

            # OpenCVで画像を読み込む
            image = cv2.imread(self.selected_file_path)

            # Tesseract OCRを実行
            # 日本語と英語の言語モデルを指定
            recognized_text = pytesseract.image_to_string(image, lang='jpn+eng')

            # 結果をテキストエリアに表示
            self.result_text_area.setText(recognized_text)

            # 結果をテキストファイルとして保存
            self.save_output_to_file(recognized_text)

        except Exception as e:
            # エラーハンドリング
            self.result_text_area.setText(f"エラーが発生しました: {e}")
            QMessageBox.critical(self, "エラー", f"OCR処理中にエラーが発生しました:\n{e}")

    def save_output_to_file(self, text):
        """
        OCR結果のテキストを指定された命名規則でファイルに保存します。
        ファイル名は `[元のファイル名]_output.txt` となります。
        """
        if not self.selected_file_path:
            return

        # 出力用のファイルパスを生成
        directory, filename = os.path.split(self.selected_file_path)
        base_filename, _ = os.path.splitext(filename)
        output_filename = f"{base_filename}_output.txt"
        output_filepath = os.path.join(directory, output_filename)

        try:
            # UTF-8エンコーディングでファイルに書き込み
            with open(output_filepath, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Output saved to {output_filepath}") # コンソールへの保存通知
        except Exception as e:
            # エラーハンドリング
            QMessageBox.critical(self, "エラー", f"ファイル保存中にエラーが発生しました:\n{e}")

    def copy_to_clipboard(self):
        """
        「結果をクリップボードにコピー」ボタンがクリックされたときに呼び出されます。
        テキストエリアの内容をシステムのクリップボードにコピーします。
        """
        clipboard = QGuiApplication.clipboard()
        text_to_copy = self.result_text_area.toPlainText()
        if text_to_copy:
            clipboard.setText(text_to_copy)
            QMessageBox.information(self, "成功", "結果をクリップボードにコピーしました。")
        else:
            QMessageBox.warning(self, "注意", "コピーするテキストがありません。")


if __name__ == "__main__":
    # アプリケーションのエントリポイント
    app = QApplication(sys.argv)
    main_window = DigitalInkerApp()
    main_window.show()
    sys.exit(app.exec())
