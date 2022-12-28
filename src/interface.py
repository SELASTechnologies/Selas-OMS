"""
MIT License
Copyright (c) 2020 SELASTechnologies
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/
"""

import sys

from PyQt6.QtWidgets import QApplication, QLabel, QWidget

from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
)

app = QApplication([])
window = QWidget()

layout = QHBoxLayout()
layout.addWidget(QPushButton("Jake"))
layout.addWidget(QPushButton("Nyameaama"))
window.setLayout(layout)

window.setWindowTitle("SELAS-OMS")
window.setGeometry(100, 100, 280, 80)
width = 500
height = 400

# setting  the fixed size of window
window.setFixedSize(width, height)

helloMsg = QLabel("<h1>SELAS</h1>", parent=window)
helloMsg.move(60, 15)

def start():
    window.show()
    sys.exit(app.exec())