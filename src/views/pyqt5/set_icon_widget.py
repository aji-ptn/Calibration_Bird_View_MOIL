from PyQt5 import QtGui, QtCore


class SetIconUserInterface(object):
    def __init__(self, main_ui):
        """

        Args:
            main_ui:
        """
        self.__main_ui = main_ui
        self.icon = QtGui.QIcon()
        self.icon_hide_show_config()
        self.icon_hide_show_adjust_level()
        self.icon_zoom_in_zoom_out()
        self.icon_toolbox()
        self.icon_open_image()
        self.icon_load_save_config()
        self.set_icon_video_controller()
        self.set_icon_video_play_pause()
        self.set_icon_media_source()
        self.set_icon_change_mode_view_video()
        self.set_icon_zoom_anypoint()
        self.set_icon_video_frame()
        # self.set_icon_mode_view()

    def set_icon_mode_view(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/adas_front.png"),
                       QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)

        self.__main_ui.button_mode_view_forward.setIcon(icon)
        self.__main_ui.button_mode_view_forward.setIconSize(QtCore.QSize(25, 25))

        self.__main_ui.button_front_wide_view.setIcon(icon)
        self.__main_ui.button_front_wide_view.setIconSize(QtCore.QSize(25, 25))

    def set_icon_video_frame(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/recording.png"),
                       QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.__main_ui.button_record_video.setIcon(icon)
        self.__main_ui.button_record_video.setIconSize(QtCore.QSize(40, 40))

        icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/screnshoot.png"),
                       QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.__main_ui.button_save_frame.setIcon(icon)
        self.__main_ui.button_save_frame.setIconSize(QtCore.QSize(30, 30))

    def set_icon_zoom_anypoint(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/minus.png"),
                       QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.__main_ui.button_minus_zoom_anypoint.setIcon(icon)
        self.__main_ui.button_minus_zoom_anypoint.setIconSize(QtCore.QSize(20, 20))

        icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/plus.png"),
                       QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.__main_ui.button_plus_zoom_anypoint.setIcon(icon)
        self.__main_ui.button_plus_zoom_anypoint.setIconSize(QtCore.QSize(20, 20))

    def set_icon_change_mode_view_video(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/default.png"),
                       QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)

        self.__main_ui.button_change_mode_view.setIcon(icon)
        self.__main_ui.button_change_mode_view.setIconSize(QtCore.QSize(30, 30))

    def set_icon_media_source(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/select_video_file.png"),
                       QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.__main_ui.button_open_file_video.setIcon(icon)
        self.__main_ui.button_open_file_video.setIconSize(QtCore.QSize(30, 30))

        # icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/open_camera.png"),
        #                QtGui.QIcon.Mode.Normal,
        #                QtGui.QIcon.State.Off)
        # self.__main_ui.button_streaming_camera.setIcon(icon)
        # self.__main_ui.button_streaming_camera.setIconSize(QtCore.QSize(30, 30))

        icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/updates.png"),
                       QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.__main_ui.button_update_properties.setIcon(icon)
        self.__main_ui.button_update_properties.setIconSize(QtCore.QSize(30, 30))

    def set_icon_video_controller(self):
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/rewind.png"),
                            QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
        self.__main_ui.btn_prev_video.setIcon(self.icon)
        self.__main_ui.btn_prev_video.setIconSize(QtCore.QSize(30, 30))

        self.icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/stop.png"),
                            QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
        self.__main_ui.btn_stop_video.setIcon(self.icon)
        self.__main_ui.btn_stop_video.setIconSize(QtCore.QSize(30, 30))

        self.icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/fast_forward.png"),
                            QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
        self.__main_ui.btn_skip_video.setIcon(self.icon)
        self.__main_ui.btn_skip_video.setIconSize(QtCore.QSize(30, 30))

    def set_icon_video_play_pause(self, status="begin"):
        self.icon = QtGui.QIcon()
        if status == "begin":
            self.icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/play.png"),
                                QtGui.QIcon.Mode.Normal,
                                QtGui.QIcon.State.Off)
        elif status == "play":
            self.icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/pause.png"),
                                QtGui.QIcon.Mode.Normal,
                                QtGui.QIcon.State.Off)
        elif status == "pause":
            self.icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/resume.png"),
                                QtGui.QIcon.Mode.Normal,
                                QtGui.QIcon.State.Off)
        self.__main_ui.btn_play_pause.setIcon(self.icon)
        self.__main_ui.btn_play_pause.setIconSize(QtCore.QSize(30, 30))

    def icon_open_image(self):
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/opened_folder.png"),
                            QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
        self.__main_ui.button_open_image.setIcon(self.icon)
        self.__main_ui.button_open_image.setIconSize(QtCore.QSize(30, 30))

        self.icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/open_video.png"),
                            QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)

        self.__main_ui.button_run_video.setIcon(self.icon)
        self.__main_ui.button_run_video.setIconSize(QtCore.QSize(30, 30))

    def icon_load_save_config(self):
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/save_file_config.png"),
                            QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
        self.__main_ui.button_save_config.setIcon(self.icon)
        self.__main_ui.button_save_config.setIconSize(QtCore.QSize(20, 20))

        self.icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/open_file_config.png"),
                            QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
        self.__main_ui.button_load_config.setIcon(self.icon)
        self.__main_ui.button_load_config.setIconSize(QtCore.QSize(20, 20))

    def icon_zoom_in_zoom_out(self):
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/zoom_in.png"),
                            QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
        self.__main_ui.button_zoom_in_overlay.setIcon(self.icon)
        self.__main_ui.button_zoom_in_overlay.setIconSize(QtCore.QSize(25, 25))

        self.icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/zoom_out.png"),
                            QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
        self.__main_ui.button_zoom_out_overlay.setIcon(self.icon)
        self.__main_ui.button_zoom_out_overlay.setIconSize(QtCore.QSize(25, 25))

        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/zoom_in.png"),
                            QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
        self.__main_ui.button_zoom_in_birds_view.setIcon(self.icon)
        self.__main_ui.button_zoom_in_birds_view.setIconSize(QtCore.QSize(25, 25))

        self.icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/zoom_out.png"),
                            QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
        self.__main_ui.button_zoom_out_birds_view.setIcon(self.icon)
        self.__main_ui.button_zoom_out_birds_view.setIconSize(QtCore.QSize(25, 25))

        self.icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/zoom_in.png"),
                            QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
        self.__main_ui.button_zoom_in_video.setIcon(self.icon)
        self.__main_ui.button_zoom_in_video.setIconSize(QtCore.QSize(30, 30))

        self.icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/zoom_out.png"),
                            QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
        self.__main_ui.button_zoom_out_video.setIcon(self.icon)
        self.__main_ui.button_zoom_out_video.setIconSize(QtCore.QSize(30, 30))

    def icon_hide_show_config(self, status=True):
        self.icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/right_box.png"),
                            QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
        if status:
            self.icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/left.png"),
                                QtGui.QIcon.Mode.Normal,
                                QtGui.QIcon.State.Off)
        self.__main_ui.button_show_hide_config.setIcon(self.icon)
        self.__main_ui.button_show_hide_config.setIconSize(QtCore.QSize(40, 40))

    def icon_hide_show_adjust_level(self, status=True):
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/left.png"),
                            QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)
        if status:
            self.icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/right_box.png"),
                                QtGui.QIcon.Mode.Normal,
                                QtGui.QIcon.State.Off)
        self.__main_ui.button_show_hide_rebalance.setIcon(self.icon)
        self.__main_ui.button_show_hide_rebalance.setIconSize(QtCore.QSize(40, 40))

    def icon_toolbox(self, activated=0):
        self.icon = QtGui.QIcon()
        for i in range(6):
            self.icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/down.png"),
                                QtGui.QIcon.Mode.Normal,
                                QtGui.QIcon.State.Off)
            if i == activated:
                self.icon.addPixmap(QtGui.QPixmap("views/ui_design/icon/right.png"),
                                    QtGui.QIcon.Mode.Normal,
                                    QtGui.QIcon.State.Off)
            self.__main_ui.toolbox_configuration.setItemIcon(i, self.icon)
