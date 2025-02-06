import sys
import coinProbability as cPB
from PySide6.QtWidgets import QApplication, QMainWindow
from main_gui import Ui_MainWindow

# After not touching python in awhile, What better way to 
# get back into it by going back to the basics? A very
# overly-complicated program rock-paper-scissor's game!
# (well..its not complicated, rather, added useless code
# to get back into python.)

# -> Look into coinProbability.probability()
# Obviously this coudlve been shortened with random.choice()
# But hey, thats not the purpose!


def botH():
    bH = cPB.probability()
    return bH
def botT():
    bT = cPB.probability()
    return bT


class MyWindow(QMainWindow):
       def __init__(self):
              super().__init__()
              self.ui = Ui_MainWindow()
              self.ui.setupUi(self)
              self.ui.headsButton.clicked.connect(self.heads_button_was_clicked)
              self.ui.tailsButton.clicked.connect(self.tails_button_was_clicked)
              self.usrPoint = 0
              self.botPoint = 0
              self.countRound = 0


       def heads_button_was_clicked(self):
              botTails = botT()
              userHead = cPB.probability()
              if userHead > botTails:
                     self.usrPoint += 1
                     self.ui.usrScore.display(self.usrPoint)
              elif userHead < botTails:
                     self.botPoint +=1
                     self.ui.botScore.display(self.botPoint)

       def tails_button_was_clicked(self):
              botHeads = botH()
              userTails = cPB.probability()

              if userTails > botHeads:
                     self.usrPoint += 1
                     self.ui.usrScore.display(self.usrPoint)
              elif userTails < botHeads:
                     self.botPoint +=1
                     self.ui.botScore.display(self.botPoint)

if __name__ == "__main__":
       app = QApplication(sys.argv)
       app.setStyle('Fusion')
       window = MyWindow()
       window.show()
       sys.exit(app.exec())
