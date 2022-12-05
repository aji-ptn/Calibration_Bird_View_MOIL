import sys
from model.main_model import MainModel
from controller.ui_main_controller import Controller
from PyQt5.QtWidgets import QApplication
from view import main_ui_2


class App(QApplication):
    def __init__(self, sys_argv):
        """
        The __init__ method lets the class initialize the object's attributes
        Args:
            sys_argv
        """
        super(App, self).__init__(sys_argv)
        self.main_ctrl = MainModel()
        self.main_view = Controller(self.main_ctrl)
        self.main_view.show()


if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec_())
