from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem
from mainWindow import Ui_MainWindow
from tokenWindow import Ui_Dialog as ResultWindow

from filehandler import readFile
from lexical import analyze, lexycalAnalysis

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.btnAnalyze.clicked.connect(lambda:self.lexycalResult(lexycalAnalysis(self.txtOgText.toPlainText())))
        self.actionOpen.triggered.connect(lambda: self.openFile(QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "Archivos de texto (*.txt)")))

        self.tokensDialog = TokensDialog()

    def openFile(self, filepath:tuple[str]):
        resultText = readFile(filepath[0])
        if resultText[0]:
            self.txtOgText.setPlainText(resultText[0])
        else:
            self.txtOgText.setPlainText(resultText[1])

    def lexycalResult(self, result:list[tuple]):
        if result and len(result[0]) == 2:
            columns = ["Error", "Linea"]
        else :
            columns = ["Token", "Tipo", "Linea", "Columna", "#"]
        self.tokensDialog.setTable(result, columns)
        self.tokensDialog.show()

    def result(self, groups:tuple[list]):
        if len(groups[0]) == 0:
            fullList = []
            for tokens in groups[1:]:
                for token in tokens:
                    fullList.append(token)
#        import pandas
#        table = pandas.DataFrame(fullList, columns= ["Token", "Tipo", "Linea", "Columna", "#"])
#        print(table)
            self.tokensDialog.setTable(fullList, ["Token", "Tipo", "Linea", "Columna", "#"])
        else:
            self.tokensDialog.setTable(groups[0], ["Error", "Linea"])
        self.tokensDialog.show()


class TokensDialog(ResultWindow, QWidget):
    def __init__(self, parent = None) -> None:
        super(QWidget, self).__init__(parent)
        self.setupUi(self)
        

    def setTable(self,rows:list[list], columns:list[str]):
        tbl = self.tblTokens
        tbl.setColumnCount(len(columns))
        tbl.setHorizontalHeaderLabels(columns)
        tbl.clearContents()
        tbl.setRowCount(len(rows))
        for i in range(len(rows)):
            vals = rows[i]
            for j in range(len(vals)):
                tbl.setItem(i, j, QTableWidgetItem(str(vals[j])))
        tbl.resizeColumnsToContents()
        




def run():
    analizer = QApplication([])
    window = MainWindow()
    window.show()

    analizer.exec()

if __name__ == "__main__":
    run()