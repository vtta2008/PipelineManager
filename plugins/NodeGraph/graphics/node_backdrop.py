# -*- coding: utf-8 -*-
"""

Script Name: node_backdrops.py
Author: Do Trinh/Jimmy - 3D artist.

Description:


"""
# -------------------------------------------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals

from PyQt5.QtCore                       import QPoint, QPointF
from PyQt5.QtGui                        import QColor

from appData                            import (Z_VAL_PIPE, NODE_SEL_COLOR, NODE_SEL_BORDER_COLOR, SIZEF_CURSOR,
                                                PEN_NONE, MOUSE_LEFT, WORD_WRAP, BRUSH_NONE, INTERSECT_ITEM_SHAPE,
                                                CONTAIN_ITEM_SHAPE, left, center)
from .node_abstract                     import AbstractNodeItem
from plugins.NodeGraph.graphics.pipe   import Pipe
from plugins.NodeGraph.graphics.port   import PortItem

from devkit.Widgets                     import GraphicObject
from devkit.Gui                         import Cursor, PainterPath, Pen
from devkit.Core                        import RectF, Rect



class BackdropSizer(GraphicObject):

    key                                 = 'BackdropSizer'

    def __init__(self, parent=None, size=6.0):
        super(BackdropSizer, self).__init__(parent)
        self.setFlag(self.ItemIsSelectable, True)
        self.setFlag(self.ItemIsMovable, True)
        self.setFlag(self.ItemSendsScenePositionChanges, True)
        self.setCursor(Cursor(SIZEF_CURSOR))
        self.setToolTip('double-click auto resize')
        self._size = size

    @property
    def size(self):
        return self._size

    def set_pos(self, x, y):
        x -= self._size
        y -= self._size
        self.setPos(x, y)

    def boundingRect(self):
        return RectF(0.5, 0.5, self._size, self._size)

    def itemChange(self, change, value):
        if change == self.ItemPositionChange:
            item = self.parentItem()
            mx, my = item.minimum_size
            x = mx if value.x() < mx else value.x()
            y = my if value.y() < my else value.y()
            value = QPointF(x, y)
            item.on_sizer_pos_changed(value)
            return value
        return super(BackdropSizer, self).itemChange(change, value)

    def mouseDoubleClickEvent(self, event):
        item = self.parentItem()
        item.on_sizer_double_clicked()

    def paint(self, painter, option, widget):

        painter.save()

        rect = self.boundingRect()
        item = self.parentItem()
        if item and item.selected:
            color = QColor(*NODE_SEL_BORDER_COLOR)
        else:
            color = QColor(*item.color)
            color = color.darker(110)
        path = PainterPath()
        path.moveTo(rect.topRight())
        path.lineTo(rect.bottomRight())
        path.lineTo(rect.bottomLeft())
        painter.setBrush(color)
        painter.setPen(PEN_NONE)
        painter.fillPath(path, painter.brush())

        painter.restore()


class BackdropNodeItem(AbstractNodeItem):

    def __init__(self, name='backdrop', text='', parent=None):
        super(BackdropNodeItem, self).__init__(name, parent)
        self.setZValue(Z_VAL_PIPE - 1)
        self._properties['backdrop_text'] = text
        self._min_size = 80, 80
        self._sizer = BackdropSizer(self, 20.0)
        self._sizer.set_pos(*self._min_size)
        self._nodes = [self]

    def _combined_rect(self, nodes):
        group = self.scene().createItemGroup(nodes)
        rect = group.boundingRect()
        self.scene().destroyItemGroup(group)
        return rect

    def mouseDoubleClickEvent(self, event):
        viewer = self.viewer()
        if viewer:
            viewer.node_double_clicked.emit(self.id)
        super(BackdropNodeItem, self).mouseDoubleClickEvent(event)

    def mousePressEvent(self, event):
        if event.button() == MOUSE_LEFT:
            pos = event.scenePos()
            rect = RectF(pos.x() - 5, pos.y() - 5, 10, 10)
            item = self.scene().items(rect)[0]

            if isinstance(item, (PortItem, Pipe)):
                self.setFlag(self.ItemIsMovable, False)
                return
            if self.selected:
                return

            viewer = self.viewer()
            [n.setSelected(False) for n in viewer.selected_nodes()]

            self._nodes += self.get_nodes(False)
            [n.setSelected(True) for n in self._nodes]

    def mouseReleaseEvent(self, event):
        super(BackdropNodeItem, self).mouseReleaseEvent(event)
        self.setFlag(self.ItemIsMovable, True)
        [n.setSelected(True) for n in self._nodes]
        self._nodes = [self]

    def on_sizer_pos_changed(self, pos):
        self._width = pos.x() + self._sizer.size
        self._height = pos.y() + self._sizer.size

    def on_sizer_double_clicked(self):
        self.auto_resize()

    def paint(self, painter, option, widget):
        painter.save()

        rect = self.boundingRect()
        color = (self.color[0], self.color[1], self.color[2], 50)
        painter.setBrush(QColor(*color))
        painter.setPen(PEN_NONE)
        painter.drawRect(rect)

        top_rect = RectF(0.0, 0.0, rect.width(), 20.0)
        painter.setBrush(QColor(*self.color))
        painter.setPen(PEN_NONE)
        painter.drawRect(top_rect)

        if self.backdrop_text:
            painter.setPen(QColor(*self.text_color))
            txt_rect = RectF(top_rect.x() + 5.0, top_rect.height() + 2.0, rect.width() - 5.0, rect.height())
            painter.setPen(QColor(*self.text_color))
            painter.drawText(txt_rect, left | WORD_WRAP, self.backdrop_text)

        if self.selected and NODE_SEL_COLOR:
            sel_color = [x for x in NODE_SEL_COLOR]
            sel_color[-1] = 10
            painter.setBrush(QColor(*sel_color))
            painter.setPen(PEN_NONE)
            painter.drawRect(rect)

        txt_rect = RectF(top_rect.x(), top_rect.y() + 1.2, rect.width(), top_rect.height())
        painter.setPen(QColor(*self.text_color))
        painter.drawText(txt_rect, center, self.name)

        path = PainterPath()
        path.addRect(rect)
        border_color = self.color
        if self.selected and NODE_SEL_BORDER_COLOR:
            border_color = NODE_SEL_BORDER_COLOR
        painter.setBrush(BRUSH_NONE)
        painter.setPen(Pen(QColor(*border_color), 1))
        painter.drawPath(path)

        painter.restore()

    def get_nodes(self, inc_intersects=False):
        mode = {True: INTERSECT_ITEM_SHAPE, False: CONTAIN_ITEM_SHAPE}
        nodes = []
        if self.scene():
            polygon = self.mapToScene(self.boundingRect())
            rect = polygon.boundingRect()
            items = self.scene().items(rect, mode=mode[inc_intersects])
            for item in items:
                if item == self or item == self._sizer:
                    continue
                if isinstance(item, AbstractNodeItem):
                    nodes.append(item)
        return nodes

    def auto_resize(self, nodes=None):
        nodes = nodes or self.get_nodes(True)
        if nodes:
            padding = 40
            nodes_rect = self._combined_rect(nodes)
            self.xy_pos = [nodes_rect.x() - padding, nodes_rect.y() - padding]
            self._sizer.set_pos(nodes_rect.width() + (padding * 2),
                                nodes_rect.height() + (padding * 2))
            return

        width, height = self._min_size
        self._sizer.set_pos(width, height)

    def pre_init(self, viewer, pos=None):
        nodes = viewer.selected_nodes()
        if nodes:
            padding = 40
            scene = viewer.scene()
            group = scene.createItemGroup(nodes)
            rect = group.boundingRect()
            scene.destroyItemGroup(group)
            self.xy_pos = [rect.x() - padding, rect.y() - padding]
            self._sizer.set_pos(rect.width() + (padding * 2),
                                rect.height() + (padding * 2))
        else:
            self.xy_pos = pos

    @property
    def minimum_size(self):
        return self._min_size

    @minimum_size.setter
    def minimum_size(self, size=(50, 50)):
        self._min_size = size

    @property
    def backdrop_text(self):
        return self._properties['backdrop_text']

    @backdrop_text.setter
    def backdrop_text(self, text):
        self._properties['backdrop_text'] = text
        self.update(self.boundingRect())

    @AbstractNodeItem.width.setter
    def width(self, width=0.0):
        AbstractNodeItem.width.fset(self, width)
        self._sizer.set_pos(self._width, self._height)

    @AbstractNodeItem.height.setter
    def height(self, height=0.0):
        AbstractNodeItem.height.fset(self, height)
        self._sizer.set_pos(self._width, self._height)

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 30/12/2019 - 15:15
# © 2017 - 2019 DAMGteam. All rights reserved