from PyQt5.QtWidgets import QWidget
from ux import action_buttons

class ActionButtons(QWidget, action_buttons.Ui_Form):
    def __init__(self, view=False, check=False, edit=False, delete=False, print=False):
        super(ActionButtons, self).__init__()
        self.setupUi(self)
        self.btn_delete.setVisible(delete)
        self.btn_edit.setVisible(edit)
        self.btn_done.setVisible(check)
        self.btn_print.setVisible(print)
        self.btn_view.setVisible(view)
