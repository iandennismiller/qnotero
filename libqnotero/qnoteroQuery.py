"""
This file is part of qnotero.

qnotero is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

qnotero is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with qnotero.  If not, see <http://www.gnu.org/licenses/>.
"""

from PyQt4.QtGui import QLineEdit
from PyQt4.QtCore import Qt, QTimer, QEvent
from libqnotero.config import getConfig

class QnoteroQuery(QLineEdit):

	"""The search input box"""

	def __init__(self, qnotero):

		"""
		Constructor

		Arguments:
		qnotero -- a Qnotero instance
		"""

		#QLineEdit.__init__(self, qnotero)
		super(QnoteroQuery, self).__init__(qnotero)
		self.qnotero = qnotero
		self.timer = QTimer(self)
		self.needUpdate = True
		self.textChanged.connect(self._textChanged)
		print "init"

	def event(self, event):
		if (event.type()==QEvent.KeyPress) and (event.key()==Qt.Key_Tab):
			self.emit(SIGNAL("tabPressed"))
			print "tab"
			return True
		else:
			print event

		return QLineEdit.event(self, event)

	def showEvent(self, e):
		print "ok"
		self.setFocus()

	"""def keyPressEvent(self, e):

		""
		Handle key presses

		Arguments:
		e -- a QKeyEvent
		""

		#print "%s" % e.key()
		print "hi"
		super(QnoteroQuery, self).keyPressEvent(e)
		#return

		if e.key() == Qt.Key_Return:
			print self.text()
			self.qnotero.search(setFocus=False)
		elif e.key() == Qt.Key_Down:
			if self.needUpdate:
				self.qnotero.search(setFocus=True)
			elif self.qnotero.ui.listWidgetResults.count() > 0:
				self.qnotero.ui.listWidgetResults.setFocus()
			self.qnotero.ui.listWidgetResults.setCurrentItem( \
				self.qnotero.ui.listWidgetResults.item(0))
		else:
			self.timer.stop()
			self.timer = QTimer(self)
			self.timer.setSingleShot(True)
			self.timer.setInterval(getConfig("autoFire"))
			self.timer.timeout.connect(self.search)
			self.timer.start()

			#QLineEdit.keyPressEvent(self, e)
			#super(QnoteroQuery, self).keyPressEvent(e)
	"""

	def search(self):

		"""Perform a search without losing focus"""

		self.qnotero.search(setFocus=False)

	def _textChanged(self):

		"""Set the needUpdate flag"""

		self.needUpdate = True