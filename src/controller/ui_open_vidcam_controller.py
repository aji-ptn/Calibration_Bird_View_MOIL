from src.view.select_source_video import Ui_OpenVideo_OpenCam
from .view_additional_function import select_file


class OpenVideoCamera(Ui_OpenVideo_OpenCam):
    def __init__(self, RecentWindow, parent):
        """
        Create class controller open video or streaming camera
        Args:
            RecentWindow: current active user interface
        """
        super(OpenVideoCamera, self).__init__()
        self.recent = RecentWindow
        self.video_controller = parent
        self.setupUi(self.recent)
        self.open_mode = "file"
        self.line_edit = [self.lineEdit_source_1, self.lineEdit_source_2, self.lineEdit_source_3,
                          self.lineEdit_source_4, self.lineEdit_source_5, self.lineEdit_source_6]
        self.total_camera_used()
        self.select_open_mode()
        self.connect_event()

    def connect_event(self):
        self.radioButton.clicked.connect(self.select_open_mode)
        self.radioButton_2.clicked.connect(self.select_open_mode)
        self.button_source_stream_1.clicked.connect(lambda: self.onclick_select_source_file(0))
        self.button_source_stream_2.clicked.connect(lambda: self.onclick_select_source_file(1))
        self.button_source_stream_3.clicked.connect(lambda: self.onclick_select_source_file(2))
        self.button_source_stream_4.clicked.connect(lambda: self.onclick_select_source_file(3))
        self.button_source_stream_5.clicked.connect(lambda: self.onclick_select_source_file(4))
        self.button_source_stream_6.clicked.connect(lambda: self.onclick_select_source_file(5))
        self.buttonBox.accepted.connect(self.onclick_button_oke)
        self.buttonBox.rejected.connect(self.onclick_button_cancel)

    def select_open_mode(self):
        if self.radioButton.isChecked():
            self.open_mode = "file"
            self.lineEdit_source_1.setText("select file")
            self.lineEdit_source_2.setText("select file")
            self.lineEdit_source_3.setText("select file")
            self.lineEdit_source_4.setText("select file")
            self.lineEdit_source_5.setText("select file")
            self.lineEdit_source_6.setText("select file")
            self.enable_button()

        elif self.radioButton_2.isChecked():
            self.open_mode = "streaming"
            self.lineEdit_source_1.setText("input cam")
            self.lineEdit_source_2.setText("input cam")
            self.lineEdit_source_3.setText("input cam")
            self.lineEdit_source_4.setText("input cam")
            self.lineEdit_source_5.setText("input cam")
            self.lineEdit_source_6.setText("input cam")
            self.disable_button()

    def total_camera_used(self):
        total_cam = self.video_controller.view_controller.model.total_camera_used
        camera_placement = self.video_controller.view_controller.model.camera_placement
        if total_cam == 6:
            self.enable_ui()
            if camera_placement == "center":
                self.set_text_label_6cam_center()
            else:
                self.set_text_label_6cam_corner()
        else:
            self.disable_ui()
            if camera_placement == "center":
                self.set_text_label_4cam_center()
            else:
                self.set_text_label_4cam_corner()

    def onclick_select_source_file(self, num):
        source = select_file(self.recent, "Select video", "../", "video (*.avi *.mp4)")
        if source is not None:
            self.line_edit[num].setText(source)

    def disable_ui(self):
        self.label_5.setDisabled(True)
        self.lineEdit_source_5.setDisabled(True)
        self.button_source_stream_5.setDisabled(True)
        self.label_6.setDisabled(True)
        self.lineEdit_source_6.setDisabled(True)
        self.button_source_stream_6.setDisabled(True)

    def enable_ui(self):
        self.label_5.setDisabled(False)
        self.lineEdit_source_5.setDisabled(False)
        self.button_source_stream_5.setDisabled(False)
        self.label_6.setDisabled(False)
        self.lineEdit_source_6.setDisabled(False)
        self.button_source_stream_6.setDisabled(False)

    def disable_button(self):
        self.button_source_stream_1.setDisabled(True)
        self.button_source_stream_2.setDisabled(True)
        self.button_source_stream_3.setDisabled(True)
        self.button_source_stream_4.setDisabled(True)
        self.button_source_stream_5.setDisabled(True)
        self.button_source_stream_6.setDisabled(True)

    def enable_button(self):
        self.button_source_stream_1.setDisabled(False)
        self.button_source_stream_2.setDisabled(False)
        self.button_source_stream_3.setDisabled(False)
        self.button_source_stream_4.setDisabled(False)
        self.button_source_stream_5.setDisabled(False)
        self.button_source_stream_6.setDisabled(False)
        self.total_camera_used()

    def onclick_button_oke(self):
        # video_path = [self.lineEdit_source_1.text(), self.lineEdit_source_2.text(), self.lineEdit_source_3.text(),
        #               self.lineEdit_source_4.text()]
        video_path = [
            "/home/aji/Documents/MyGithub/calibration-bird-view/images/07112022_data parking front edu/Videos/edu to electronic/video_3.avi",
            "/home/aji/Documents/MyGithub/calibration-bird-view/images/07112022_data parking front edu/Videos/edu to electronic/video_2.avi",
            "/home/aji/Documents/MyGithub/calibration-bird-view/images/07112022_data parking front edu/Videos/edu to electronic/video_1.avi",
            "/home/aji/Documents/MyGithub/calibration-bird-view/images/07112022_data parking front edu/Videos/edu to electronic/video_4.avi"]
        if self.video_controller.view_controller.model.total_camera_used == 6:
            video_path.append(self.lineEdit_source_5.text())
            video_path.append(self.lineEdit_source_6.text())
        self.video_controller.select_source_video(video_path)
        self.recent.close()

    def onclick_button_cancel(self):
        self.recent.close()

    def set_text_label_4cam_center(self):
        self.label.setText("front")
        self.label_2.setText("left")
        self.label_3.setText("right")
        self.label_4.setText("rear")
        self.label_5.setText("-")
        self.label_6.setText("-")

    def set_text_label_4cam_corner(self):
        self.label.setText("front left")
        self.label_2.setText("front right")
        self.label_3.setText("rear left")
        self.label_4.setText("rear right")
        self.label_5.setText("-")
        self.label_6.setText("-")

    def set_text_label_6cam_corner(self):
        self.label.setText("front left")
        self.label_2.setText("front right")
        self.label_3.setText("right")
        self.label_4.setText("left")
        self.label_5.setText("rear left")
        self.label_6.setText("rear right")

    def set_text_label_6cam_center(self):
        self.label.setText("front")
        self.label_2.setText("left 1")
        self.label_3.setText("right 2")
        self.label_4.setText("left 1")
        self.label_5.setText("left")
        self.label_6.setText("rear right")
