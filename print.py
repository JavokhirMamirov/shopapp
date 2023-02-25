from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtPrintSupport import QPrintPreviewDialog, QPrinter
app = QApplication([])

# Create a QWebEngineView and load a web page
web_view = QWebEngineView()
html = """<html>
    <head>
        <style>
            .container{
                display: flex;
                flex-direction: column;
            }

            .header{
                display: flex;
                flex-direction: row;
                justify-content: space-between;
                margin-bottom: 15px;
                margin-left: 15px;
                margin-right: 15px;

            }

            table {
                width: 100%;
                border: 1px solid;
                border-collapse: collapse;
                
            }

            th, td {
                border: 1px solid;
                word-wrap: break-word;
                text-align: center;
                padding: 5px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="client-container">
                    <p>Мижоз</p>
                    <p>Name</p>
                    <p>phone</p>
                </div>
                <div class="chek">
                    <p>106</p>
                    <p>chek nomer: 800</p>
                </div>
                <div class="firma">
                    <p>Бизнинг фирма</p>
                    <p>106</p>
                    <p>+998901234578</p>
                </div>
            </div>
            <div class="content">
                <table style="width:100%">
                    <tr>
                        <th>№</th>
                        <th>Махсулот номи</th>
                        <th>Модел</th>
                        <th>Бренд</th>
                        <th>Ишлаб чиқарувчи</th>
                        <th>Бирлиги</th>
                        <th>Сони</th>
                        <th>Нархи</th>
                        <th>Сумма</th>
                    </tr>
                </table>
            </div>
        </div>
    </body>
</html>"""

web_view.setHtml(html)

# Create a QPrinter and a QPrintPreviewDialog
printer = QPrinter()
preview_dialog = QPrintPreviewDialog(printer)

# Connect the preview dialog's paintRequested signal to a function that will render the web page to the printer
def print_preview():
    web_page = web_view.page()
    web_page.print(printer, lambda result: preview_dialog.exec_())
preview_dialog.paintRequested.connect(print_preview)

# Show the QWebEngineView
web_view.show()

# Show the QPrintPreviewDialog
preview_dialog.exec_()

# Enter the main event loop
app.exec_()