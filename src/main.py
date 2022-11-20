import sys
from models import Model
from controllers import MainController

try:
    from PyQt6.QtWidgets import QApplication
    pyqt_version = "pyqt6"

except:
    from PyQt5.QtWidgets import QApplication
    pyqt_version = "pyqt5"


if pyqt_version == "pyqt6":
    from views.pyqt6 import ViewController


    class App(QApplication):
        def __init__(self, sys_argv):
            super(App, self).__init__(sys_argv)
            self.model = Model()
            self.main_ctrl = MainController(self.model)
            self.main_view = ViewController(self.model, self.main_ctrl)
            self.main_view.show()


    if __name__ == '__main__':
        app = App(sys.argv)
        sys.exit(app.exec())

elif pyqt_version == "pyqt5":
    from views.pyqt5 import ViewController
    print("under development")

    class App(QApplication):
        def __init__(self, sys_argv):
            """
            The __init__ method lets the class initialize the object's attributes
            Args:
                sys_argv
            """
            super(App, self).__init__(sys_argv)
            self.model = Model()
            self.main_ctrl = MainController(self.model)
            self.main_view = ViewController(self.model, self.main_ctrl)
            self.main_view.show()

    if __name__ == "__main__":
        app = App(sys.argv)
        sys.exit(app.exec_())



