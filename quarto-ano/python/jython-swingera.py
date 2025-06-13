from javax.swing import JFrame, JButton, JPanel, JOptionPane
from javax.swing.JOptionPane import showMessageDialog
from java.awt import Dimension, Component, GridBagLayout
from java.awt.event import ActionListener, ActionEvent

class Action(ActionListener):
    def actionPerformed(self,event):
        showMessageDialog(None, "TONTAO :)", "OU",  JOptionPane.INFORMATION_MESSAGE)

f = JFrame("TONTO")
f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
f.setSize(600,800)

p = JPanel()
p.setLayout(GridBagLayout())


b = JButton("clica aqui tontao")
b.setPreferredSize(Dimension(300, 20))
b.setAlignmentX(Component.CENTER_ALIGNMENT)
b.setAlignmentY(Component.CENTER_ALIGNMENT)

b.addActionListener(Action())

p.add(b)
f.add(p)
f.setVisible(True)
