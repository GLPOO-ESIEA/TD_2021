from PySide6.QtWidgets import QWidget,  QVBoxLayout, QFormLayout, QLineEdit, QCheckBox


class UserQtView(QWidget):
    def __init__(self):
        super().__init__()

        self.setup()

    def setup(self):
        # Create an outer layout
        outerLayout = QVBoxLayout()
        # Create a form layout for the label and line edit
        topLayout = QFormLayout()
        # Add a label and a line edit to the form layout
        topLayout.addRow("Some Text:", QLineEdit())
        # Create a layout for the checkboxes
        optionsLayout = QVBoxLayout()
        # Add some checkboxes to the layout
        optionsLayout.addWidget(QCheckBox("Option one"))
        optionsLayout.addWidget(QCheckBox("Option two"))
        optionsLayout.addWidget(QCheckBox("Option three"))
        # Nest the inner layouts into the outer layout
        outerLayout.addLayout(topLayout)
        outerLayout.addLayout(optionsLayout)
        # Set the window's main layout
        self.setLayout(outerLayout)