import wx
import random
import time

# Rodrigo Alonso Pastor

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    __tablero__ = None
    __Juego__ = False
    __lleno__ = False
    startPos = None
    movRaton = None
    tema = "Por defecto"
    velocidad = 1

    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((859, 724))
        self.SetTitle("Deslizator")
        self.SetIcon(wx.Icon("icon.png"))

        self.dialogo = MyDialog(self)
        self.dialogVel = DialogVelocidad(self)
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
       # self.panel_1.SetBackgroundColour(wx.Colour(255, 255, 255))
        #self.panel_1.SetForegroundColour(wx.Colour(255, 255, 255))

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(sizer_2, 1, wx.ALL | wx.EXPAND, 10)

        self.sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.sizer_3, 1, wx.EXPAND, 0)

        self.label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "")
        sizer_2.Add(self.label_1, 0, 0, 0)

        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_3.Add(sizer_4, 0, wx.EXPAND, 0)

        self.button_1 = wx.Button(self.panel_1, wx.ID_ANY, "Abrir fichero")
        self.button_1.SetBitmap(wx.Bitmap("file open 1.png", wx.BITMAP_TYPE_ANY))
        self.button_1.SetBitmapCurrent(wx.Bitmap("file open 2.png", wx.BITMAP_TYPE_ANY))
        sizer_4.Add(self.button_1, 0, 0, 0)

        grid_sizer_botones = wx.GridSizer(2, 2, 0, 0)
        sizer_4.Add(grid_sizer_botones, 0, wx.CENTER, 0)

        self.button_2 = wx.BitmapButton(self.panel_1, wx.ID_ANY)
        grid_sizer_botones.Add(self.button_2, 0, 0, 0)
        self.button_2.SetBitmap(wx.Bitmap("new file 1.png", wx.BITMAP_TYPE_ANY))
        self.button_2.SetBitmapCurrent(wx.Bitmap("new file 2.png", wx.BITMAP_TYPE_ANY))


        self.button_3 = wx.BitmapButton(self.panel_1, wx.ID_ANY)
        grid_sizer_botones.Add(self.button_3, 0, 0, 0)
        self.button_3.SetBitmap(wx.Bitmap("n filas 1.png", wx.BITMAP_TYPE_ANY))
        self.button_3.SetBitmapCurrent(wx.Bitmap("n filas 2.png", wx.BITMAP_TYPE_ANY))


        self.button_4 = wx.BitmapButton(self.panel_1, wx.ID_ANY)
        grid_sizer_botones.Add(self.button_4, 0, 0, 0)
        self.button_4.SetBitmap(wx.Bitmap("temas 1.png", wx.BITMAP_TYPE_ANY))
        self.button_4.SetBitmapCurrent(wx.Bitmap("temas 2.png", wx.BITMAP_TYPE_ANY))


        self.button_5 = wx.BitmapButton(self.panel_1, wx.ID_ANY)
        grid_sizer_botones.Add(self.button_5, 0, 0, 0)
        self.button_5.SetBitmap(wx.Bitmap("speed 1.png", wx.BITMAP_TYPE_ANY))
        self.button_5.SetBitmapCurrent(wx.Bitmap("speed 2.png", wx.BITMAP_TYPE_ANY))


        #self.button_1.SetBitmap(wx.Bitmap("D:\\Downloads\\resources p2\\n filas 1.png", wx.BITMAP_TYPE_ANY))
        #self.button_1.SetBitmapCurrent(wx.Bitmap("D:\\Downloads\\resources p2\\n filas 2.png", wx.BITMAP_TYPE_ANY))


        self.list_box_1 = wx.ListBox(self.panel_1, wx.ID_ANY, choices=[])
        sizer_4.Add(self.list_box_1, 1, wx.CENTER, 0)

        #self.panel_espacio = wx.Panel(self.panel_1, wx.ID_ANY)
        #sizer_4.Add(self.panel_espacio, 1,0,0)

        self.label_3 = wx.StaticText(self.panel_1, wx.ID_ANY, "Puntos = 0")
        self.label_3.SetFont(wx.Font(8, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_SLANT, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_4.Add(self.label_3, 0, wx.CENTER, 0)

        self.panel_2 = wx.Panel(self.panel_1, wx.ID_ANY)
        self.panel_2.SetBackgroundColour(wx.Colour(255, 0, 0))
        self.panel_2.SetForegroundColour(wx.Colour(255, 0, 0))
        self.sizer_3.Add(self.panel_2, 1, wx.ALL | wx.EXPAND, 15)

        self.sizer_5 = wx.BoxSizer(wx.HORIZONTAL)


        self.p= wx.Panel(self.panel_2, wx.ID_ANY)
        self.p.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.p.SetForegroundColour(wx.Colour(255, 255, 255))
        self.sizer_5.Add(self.p, 1, wx.ALL | wx.EXPAND, 5)

        self.gs= wx.GridBagSizer(0,0)
        self.gs.SetCols(10)
        self.gs.SetRows(27)

        for i in range(27):
            self.gs.AddGrowableRow(i)

        for i in range(10):
            self.gs.AddGrowableCol(i)

        #
        # panel_prueba = wx.Panel(self.p, wx.ID_ANY)
        # panel_prueba.SetBackgroundColour(wx.Colour(255, 0, 0))
        # panel_prueba.SetForegroundColour(wx.Colour(255, 0, 2))
        # self.gs.Add(panel_prueba, wx.GBPosition(2, 1), flag=wx.EXPAND)


        panel_prueba = wx.Panel(self.p, wx.ID_ANY, size = wx.Size(0,0))
        self.gs.Add(panel_prueba, wx.GBPosition(11, 10), flag=wx.EXPAND)

        #self.gs.SetFlexibleDirection(wx.BOTH)
        self.panel_2.SetSizer(self.sizer_5)

        self.panel_1.SetSizer(sizer_1)
        self.p.SetSizer(self.gs)

        self.Bind(wx.EVT_BUTTON, self.OpenFile, self.button_1)
        self.p.Bind(wx.EVT_LEFT_DOWN, self.initMvm)
        self.Bind(wx.EVT_LEFT_UP, self.endMvm)

        self.Bind(wx.EVT_BUTTON, self.PartidaNueva, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.Filas, self.button_3)
        self.Bind(wx.EVT_BUTTON, self.menuTema, self.button_4)
        self.Bind(wx.EVT_BUTTON, self.SetVelocidad, self.button_5)
        # end wxGlade


    def menuTema(self, event):
        choices = ["Por defecto", "Oscuro", "Invertido", "Aleatorio"]
        eleccion = wx.SingleChoiceDialog(self, "Selecciona un tema para el programa", "Elegir tema", choices)
        eleccion.ShowModal()
        if eleccion.GetStringSelection() != "":
            self.tema = eleccion.GetStringSelection()
            if eleccion.GetStringSelection() == "Oscuro":
                self.p.SetBackgroundColour(wx.Colour(0,0,0))
                self.list_box_1.SetBackgroundColour(wx.Colour(0, 0, 0))
                self.list_box_1.SetForegroundColour(wx.Colour(255, 255, 255))
                self.button_1.SetBackgroundColour(wx.Colour(50,50,50))
                self.button_1.SetForegroundColour(wx.Colour(255,255,255))
                self.button_2.SetBackgroundColour(wx.Colour(50,50,50))
                self.button_2.SetForegroundColour(wx.Colour(255,255,255))
                self.button_3.SetBackgroundColour(wx.Colour(50,50,50))
                self.button_3.SetForegroundColour(wx.Colour(255,255,255))
                self.button_4.SetBackgroundColour(wx.Colour(50,50,50))
                self.button_4.SetForegroundColour(wx.Colour(255,255,255))
                self.button_5.SetBackgroundColour(wx.Colour(50, 50, 50))
                self.button_5.SetForegroundColour(wx.Colour(255, 255, 255))
                self.label_1.SetForegroundColour(wx.Colour(255, 255, 255))
                self.label_3.SetForegroundColour(wx.Colour(255, 255, 255))
                self.SetBackgroundColour(wx.Colour(0,0,0))
                self.Refresh()
            else:
                self.p.SetBackgroundColour(wx.Colour(255,255,255))
                self.list_box_1.SetBackgroundColour(wx.Colour(255, 255, 255))
                self.list_box_1.SetForegroundColour(wx.Colour(0, 0, 0))
                self.button_1.SetBackgroundColour(wx.NullColour)
                self.button_1.SetForegroundColour(wx.Colour(0,0,0))
                self.button_2.SetBackgroundColour(wx.NullColour)
                self.button_2.SetForegroundColour(wx.Colour(0,0,0))
                self.button_3.SetBackgroundColour(wx.NullColour)
                self.button_3.SetForegroundColour(wx.Colour(0,0,0))
                self.button_4.SetBackgroundColour(wx.NullColour)
                self.button_4.SetForegroundColour(wx.Colour(0,0,0))
                self.button_5.SetBackgroundColour(wx.NullColour)
                self.button_5.SetForegroundColour(wx.Colour(0, 0, 0))
                self.label_1.SetForegroundColour(wx.Colour(0,0,0))
                self.label_3.SetForegroundColour(wx.Colour(0, 0, 0))
                self.SetBackgroundColour(wx.NullColour)
                self.Refresh()
            if self.__Juego__:
                self.InicJuego()
    def initMvm(self, event):  # wxGlade: MyFrame.<event_handler>
        bloque_pulsado = event.GetEventObject()
        if self.p == bloque_pulsado:
            self.movRaton = "---"
            self.InputJugada(event)
            return
        pos = self.gs.GetItemPosition(bloque_pulsado)
        coord_x = pos[0] + 65
        coord_y = pos[1]
        self.movRaton = chr(coord_x) + str(coord_y)



        pos = wx.GetMousePosition()
        self.CaptureMouse()
        self.startPos = pos


    def endMvm(self, event):  # wxGlade: MyFrame.<event_handler>
        pos = wx.GetMousePosition()
        self.ReleaseMouse()
        if pos[0] - self.startPos[0] > 0:
            self.movRaton = self.movRaton + ">"
        else:
            self.movRaton = self.movRaton + "<"

        self.InputJugada(event)

    def OpenFile(self, event):  # wxGlade: MyFrame.<event_handler>
        openFileDialog = wx.FileDialog(self, "Open", "", "","Documentos de texto (*.txt)|*.txt",wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        openFileDialog.ShowModal()
        # iniciar juego
        if openFileDialog.GetPath() != "":
            MyFrame.__Juego__ = True
            self.path = openFileDialog.GetPath()
            MyFrame.InicJuego(self)
        openFileDialog.Destroy()
    def PartidaNueva(self, event):  # wxGlade: MyFrame.<event_handler>
        if not MyFrame.__Juego__:
            wx.MessageBox("Se necesita abrir un fichero primero", "Error de fichero")
        else:
            MyFrame.InicJuego(self)
    def InicJuego(self):
        self.list_box_1.Clear()
        self.clearTablero()
        self.__lleno__ = False
        self.__tablero__ = Tablero(self.path, self.dialogo.slider_1.GetValue(), self)
        self.__tablero__.ins_fila()
        self.label_1.SetLabel("Arrastra sobre el bloque que quieres mover")


    def Filas(self, event):  # wxGlade: MyFrame.<event_handler>
        if not MyFrame.__Juego__:
            wx.MessageBox("Se necesita abrir un fichero primero", "Error de fichero")
        else:
            self.dialogo.ShowModal()
            for x in range(27):
                for y in range(11):
                    item = self.gs.FindItemAtPosition(wx.GBPosition(x,y))
                    if item:
                        w = item.GetWindow()
                        self.gs.Detach(item.GetWindow())
                        w.Destroy()
            panel_prueba = wx.Panel(self.p, wx.ID_ANY, size = wx.Size(0,0))
            self.gs.Add(panel_prueba, wx.GBPosition(self.dialogo.slider_1.GetValue() - 1, 10), flag=wx.EXPAND)

            self.InicJuego()


    def SetVelocidad(self, event):  # wxGlade: MyFrame.<event_handler>
        self.dialogVel.ShowModal()
        self.velocidad = self.dialogVel.slider_1.GetValue()


    def InputJugada(self, event):  # wxGlade: MyFrame.<event_handler>       if not MyFrame.__Juego__:
        if not self.__Juego__:
            wx.MessageBox("Se necesita abrir un fichero primero", "Error de fichero")

        elif self.__lleno__:
            self.label_1.SetLabel(":(")
            wx.MessageBox("Has conseguido " + str(self.__tablero__.ptos) + " puntos" , "Fin del juego" )
        else:
            jug = self.movRaton
            if jug == "FIN":
                return
            res = self.__tablero__.jugada(jug)

            if res == -3:
                self.label_1.SetLabel("Error de sintaxis en jugada")
            elif res == -2:
                self.label_1.SetLabel("El bloque no puede moverse en esa dirección")
            elif res == -1:
                self.label_1.SetLabel("No hay ningún bloque en esa celda")
            else:
                self.list_box_1.Append(jug)
                self.label_1.SetLabel("Moviendo")
                ptosOld = self.__tablero__.ptos
                # Caída de bloques y borrado de filas
                seguir = True
                while seguir:
                    self.__tablero__.caida()
                    lis = self.__tablero__.eliminacion()
                    seguir = len(lis) > 0
                self.__lleno__ = self.__tablero__.lleno()
                if self.__tablero__.ptos > ptosOld:
                    self.PointsAnim()
                if not self.__lleno__:
                    self.__tablero__.ins_fila()
                    self.label_1.SetLabel("Arrastra sobre el bloque que quieres mover")

# end of class MyFrame

    def clearTablero(self):
        for x in range(self.dialogo.slider_1.GetValue()):
            for y in range(10):
                item = self.gs.FindItemAtPosition(wx.GBPosition(x,y))
                if item:
                    w = item.GetWindow()
                    self.gs.Detach(item.GetWindow())
                    w.Destroy()

    def PointsAnim(self):
        for i in range(self.__tablero__.ptos - 10, self.__tablero__.ptos + 1):
            time.sleep(0.001)
            self.label_3.SetLabel("Puntos = " + str(i))
        return

    def mvmBloque(self, bloque_ini, bloque_fin):
        # bloque_ini[0] fil
        # bloque_ini[1] col0
        # bloque_ini[2] col1
        # bloque_ini[3] color

        # Movimiento con animación

        for y in range(bloque_ini[0],bloque_fin[0]):
            time.sleep(0.001 * (2**self.velocidad))
            self.borrarBloque((y,bloque_ini[1], bloque_ini[2], bloque_ini[3]),animar=False)
            self.colocarBloque((y + 1, bloque_ini[1], bloque_ini[2], bloque_ini[3]),animar=False)

        dir = 1 if bloque_ini[1] < bloque_fin[1] else -1

        for x in range(bloque_ini[1], bloque_fin[1], dir):
            time.sleep(0.008 * (2**self.velocidad))
            self.borrarBloque((bloque_fin[0], x,  x + (bloque_ini[2] - bloque_ini[1]), bloque_ini[3]), animar=False)
            self.colocarBloque((bloque_fin[0], x + dir, x + dir + (bloque_ini[2] - bloque_ini[1]), bloque_ini[3] ), animar=False)

        # self.borrarBloque((bloque_fin[0], bloque_ini[1], bloque_ini[2], bloque_ini[3]) ,animar=True)
        # self.colocarBloque((bloque_fin[0], bloque_fin[1], bloque_fin[2], bloque_fin[3]), animar=True)

    def borrarBloque(self, bloque, animar):
        # bloque[0] fil
        # bloque[1] col0
        # bloque[2] col1
        # bloque[3] color
        if animar:
            time.sleep(0.001 * (2**self.velocidad))
        item = self.gs.FindItemAtPosition(wx.GBPosition(bloque[0], bloque[1]))
        if item:
            w = item.GetWindow()
            self.gs.Detach(item.GetWindow())
            w.Destroy()

    def colocarBloque(self, bloque, animar):
        # bloque[0] fil
        # bloque[1] col0
        # bloque[2] col1
        # bloque[3] color
        if animar:
            time.sleep(0.001 * (2**self.velocidad))
        panel_prueba = wx.Panel(self.p, wx.ID_ANY, style=wx.SUNKEN_BORDER)

        if self.tema == "Por defecto":
            if bloque[3] == 0:
                panel_prueba.SetBackgroundColour(wx.Colour(255, 0, 0))
            elif bloque[3] == 1:
                panel_prueba.SetBackgroundColour(wx.Colour(0, 255, 0))
            else:
                panel_prueba.SetBackgroundColour(wx.Colour(252, 139, 11))

        elif self.tema == "Oscuro":
            if bloque[3] == 0:
                panel_prueba.SetBackgroundColour(wx.Colour(230, 50, 50))
            elif bloque[3] == 1:
                panel_prueba.SetBackgroundColour(wx.Colour(100, 238, 100))
            else:
                panel_prueba.SetBackgroundColour((wx.Colour(230,130,10)))

        elif self.tema == "Invertido":
            if bloque[3] == 0:
                panel_prueba.SetBackgroundColour(wx.Colour(0,0,255))
            elif bloque[3] == 1:
                panel_prueba.SetBackgroundColour(wx.Colour(255,255,0))
            else:
                panel_prueba.SetBackgroundColour(wx.Colour(255,150,40))
        elif self.tema == "Aleatorio":
            panel_prueba.SetBackgroundColour(
                wx.Colour(random.randint(5, 255), random.randint(5, 255), random.randint(5, 255)))

        self.gs.Add(panel_prueba, wx.GBPosition(bloque[0], bloque[1]),
                    wx.GBSpan(1, bloque[2] - bloque[1] + 1), flag=wx.EXPAND, border=5)
        panel_prueba.Bind(wx.EVT_LEFT_DOWN, self.initMvm)
        self.p.Layout()


class DialogVelocidad(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle("Cambiar filas")

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 10)

        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        sizer_3.Add(self.panel_1, 1, wx.EXPAND, 0)


        label_1 = wx.StaticText(self, wx.ID_ANY, "Desliza para ajustar la velocidad del juego")
        sizer_3.Add(label_1, 0, 0, 10)

        self.slider_1 = wx.Slider(self, wx.ID_ANY, 1, 0, 10)
        sizer_3.Add(self.slider_1, 0, wx.EXPAND, 0)

        self.panel_2 = wx.Panel(self, wx.ID_ANY)
        sizer_3.Add(self.panel_2, 1, wx.EXPAND, 0)

        self.label_2 = wx.StaticText(self, wx.ID_ANY, "Valor actual: " + str(self.slider_1.GetValue()))
        sizer_3.Add(self.label_2, 0, 0, 0)


        sizer_2 = wx.StdDialogButtonSizer()
        sizer_1.Add(sizer_2, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

        self.button_OK = wx.Button(self, wx.ID_OK, "")
        self.button_OK.SetDefault()
        sizer_2.AddButton(self.button_OK)

        self.button_CANCEL = wx.Button(self, wx.ID_CANCEL, "")
        sizer_2.AddButton(self.button_CANCEL)

        sizer_2.Realize()

        self.SetSizer(sizer_1)
        sizer_1.Fit(self)

        self.SetAffirmativeId(self.button_OK.GetId())
        self.SetEscapeId(self.button_CANCEL.GetId())
        self.Layout()
        self.Bind(wx.EVT_SLIDER, self.CambiarValor, self.slider_1)
        # end wxGlade

    def CambiarValor(self, event):  # wxGlade: MyDialog.<event_handler>
        self.label_2.SetLabel("Valor actual: " + str(self.slider_1.GetValue()))



class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle("Cambiar filas")

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)

        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        sizer_3.Add(self.panel_1, 1, wx.EXPAND, 0)


        label_1 = wx.StaticText(self, wx.ID_ANY, "Desliza para ajustar las filas del juego")
        sizer_3.Add(label_1, 0, 0, 0)

        self.slider_1 = wx.Slider(self, wx.ID_ANY, 12, 1, 26)
        sizer_3.Add(self.slider_1, 0, wx.EXPAND, 0)

        self.panel_2 = wx.Panel(self, wx.ID_ANY)
        sizer_3.Add(self.panel_2, 1, wx.EXPAND, 0)

        self.label_2 = wx.StaticText(self, wx.ID_ANY, "Valor actual: " + str(self.slider_1.GetValue()))
        sizer_3.Add(self.label_2, 0, 0, 0)


        sizer_2 = wx.StdDialogButtonSizer()
        sizer_1.Add(sizer_2, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

        self.button_OK = wx.Button(self, wx.ID_OK, "")
        self.button_OK.SetDefault()
        sizer_2.AddButton(self.button_OK)

        self.button_CANCEL = wx.Button(self, wx.ID_CANCEL, "")
        sizer_2.AddButton(self.button_CANCEL)

        sizer_2.Realize()

        self.SetSizer(sizer_1)
        sizer_1.Fit(self)

        self.SetAffirmativeId(self.button_OK.GetId())
        self.SetEscapeId(self.button_CANCEL.GetId())
        self.Layout()
        self.Bind(wx.EVT_SLIDER, self.CambiarValor, self.slider_1)
        # end wxGlade

    def CambiarValor(self, event):  # wxGlade: MyDialog.<event_handler>
        self.label_2.SetLabel("Valor actual: " + str(self.slider_1.GetValue()))


# end of class MyDialog

class MyApp(wx.App):
    def OnInit(self):
        #
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

# ************** CONSTANTES ********************
CH_PANT = ord('#')  # Inicio secuencia caracteres pantalla
CH_FICH = ord('A')  # Inicio secuencia caracteres fichero (mayúsculas)
CH_FIL = ord('A')  # Inicio secuencia caracteres que representan filas
CH_COL = ord('0')  # Inicio secuencia caracteres que representan columnas


# Ejemplo de corutina/generador: Devuelve de forma cíclica los elementos
# de la lista que se pasa por parámetro (nunca termina)
# Ver https://docs.python.org/3/tutorial/classes.html#generators
def ciclo(lis):
    while True:
        for elem in lis:
            yield elem


class Bloque(object):
    """ Representa un bloque. Propiedades: fila, columna inicial, final y valor (color) """

    def __init__(self, fil, col0, col1, val, frame):
        self.fil = fil
        self.col0 = col0
        self.col1 = col1
        self.val = val  # Es un entero positivo (0, 1, ...)
        self.n = col1 - col0 + 1  # Tamaño del bloque
        self.frame = frame
        self.frame.colocarBloque((self.fil, self.col0, self.col1, self.val), animar=True)

    # Desplazamiento de un bloque
    def desplazar(self, dx, dy):

        bl_ant = (self.fil, self.col0, self.col1, self.val)

        self.fil += dy
        self.col0 += dx
        self.col1 += dx

        self.frame.mvmBloque(bl_ant, (self.fil, self.col0, self.col1, self.val))

    def eliminar(self):
        self.frame.borrarBloque((self.fil,self.col0,self.col1, self.val), animar=True)

    # Para depuración
    def __repr__(self):
        return f"{self.col0}-{self.col1},{self.fil}:{self.val}"

    # Ver https://docs.python.org/3/reference/datamodel.html#object.__str__
    def __str__(self):
        return chr(self.val + CH_PANT) * (4 * self.n - 1)


class Tablero(object):
    """ Representa el estado del Tablero en un momento dado """

    # Se pasa como parámetros el nombre de ficheros de filas entrantes
    # y el número de filas del tablero (las columnas son siempre 10)
    def __init__(self, nomfich, numfil, frame):
        # Lectura de fichero de filas entrantes
        with open(nomfich) as fich:
            self.entrada = ciclo(fich.read().splitlines())
        # Propiedades/Atributos: Tamaño del tablero y puntuación
        self.nfil = numfil
        self.ncol = 10
        self.ptos = 0
        self.frame = frame
        # El tablero se representa como una lista de filas,
        # cada fila es una lista de Bloques. Usamos compresión de listas
        # Ver https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
        self.dat = [[] for _ in range(numfil)]



    # ************** OPERACIONES PRINCIPALES ********************

    # Comprueba si hay bloques en la primera fila (fin de partida)
    def lleno(self):
        return len(self.dat[0]) > 0

    # Asigna una nueva fila de bloques en la parte superior del tablero
    def ins_fila(self):
        # Nueva linea de texto (formato fichero) que indica los bloques
        # Ver https://docs.python.org/3/library/functions.html#next
        # Ver https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
        linea = next(self.entrada)
        # Ver https://docs.python.org/3/tutorial/datastructures.html sección 5.1.3
        self.dat[0] = [Bloque(0, c0, c1, val, self.frame) for (c0, c1, val) in self.bloques_en_linea(linea)]


    # Traduce jugada (string) y la efectúa si es correcta. Valores devueltos:
    # -3 -> Sintaxis errónea
    # -2 -> El bloque no puede desplazarse
    # -1 -> No hay bloque en esa posición
    #  0 -> Jugada válida
    def jugada(self, jug):
        if len(jug) != 3:
            return -3
        # No hace movimiento
        if jug == '---':
            return 0
        # Obtener fila y columna
        fil = ord(jug[0]) - CH_FIL
        col = ord(jug[1]) - CH_COL
        # Fuera de rango
        if fil < 0 or fil >= self.nfil or col <  0 or col >= self.ncol:
            return -3
        # Indice del bloque en esa columna
        i = self.index_bloque(self.dat[fil], col)
        # No es una posición de bloque
        if i < 0:
            return -1
        b = self.dat[fil][i]
        # Comprobar si se puede desplazar
        if jug[2] == '<':
            if i == 0:
                # Caso de bloque situado más a la izquierda
                if b.col0 == 0:  # Pegado a borde
                    return -2
                # Lo movemos al borde
                b.desplazar(-b.col0, 0)
            else:
                ba = self.dat[fil][i - 1]  # Bloque anterior
                db = b.col0 - ba.col1 - 1  # Espacio entre bloques
                if db == 0:  # Pegado a nuestro bloque
                    return -2
                # Lo movemos de forma que se "pegue" al bloque anterior
                b.desplazar(-db, 0)
        elif jug[2] == '>':
            if i == len(self.dat[fil]) - 1:
                # Caso de bloque situado más a la derecha
                if b.col1 == self.ncol - 1:  # Pegado a borde
                    return -2
                # Lo movemos al borde
                b.desplazar(self.ncol - b.col1 - 1, 0)
            else:
                bs = self.dat[fil][i + 1]  # Bloque siguiente
                db = bs.col0 - b.col1 - 1  # Espacio entre bloques
                if db == 0:  # Pegado a nuestro bloque
                    return -2
                # Lo movemos de forma que se "pegue" al bloque siguiente
                b.desplazar(db, 0)
        else:
            return -3
        return 0

    # Se hacen caer los bloques recorriendo las filas desde la penúltima
    # a la primera (de "abajo" a "arriba")
    def caida(self):
        for fil_ori in range(self.nfil - 2, -1, -1):
            # Se recorren los bloques de la fila
            # Cuidado: Como es posible que durante el bucle modifiquemos la composición
            # de la fila, el bucle trabaja sobre una copia de la fila ([:])
            for b in self.dat[fil_ori][:]:
                # Se comprueban huecos en filas inferiores
                fil_des = pos_hueco = -1
                for i in range(fil_ori + 1, self.nfil):
                    ph = self.pos_ins_bloque(self.dat[i], b)
                    if ph == -1:
                        break
                    pos_hueco = ph
                    fil_des = i
                # Si hay descenso, mover el bloque
                if fil_des > -1:
                    self.dat[fil_ori].remove(b)
                    self.dat[fil_des].insert(pos_hueco, b)
                    b.desplazar(0, fil_des - fil_ori)

    # Elimina las filas completas, detectando si se produce una "reacción en cadena"
    # Devuelve la lista de bloques borrados
    def eliminacion(self):
        lis = []
        reaccion_cadena = False
        inc_ptos = 0
        for fil in range(self.nfil):
            if self.fila_completa(self.dat[fil], self.ncol):
                if self.fila_mismo_color(self.dat[fil]):
                    reaccion_cadena = True
                    break
                lis += self.borra_fila(fil)
                hay_borrado = True
                inc_ptos += self.ncol
        if reaccion_cadena:
            for fil in range(self.nfil):
                # Suma de las longitudes de todos los bloques de la fila,
                # usando una enumeración mediante la sintaxis (.. for .. in ..)
                # Ver https://docs.python.org/3/tutorial/classes.html#generator-expressions
                inc_ptos += sum((b.n for b in self.dat[fil]))
                lis += self.borra_fila(fil)
        self.ptos += inc_ptos
        return lis

    # Ver https://docs.python.org/3/reference/datamodel.html#basic-customization
    def __str__(self):
        return self.tab2txt()

    def __repr__(self):
        return self.tab2txt()

    # ************** OPERACIONES AUXILIARES ********************

    # Se define como método aparte para que pueda sobrescribirse en clases derivadas
    # Devuelve la lista de bloques borrados
    def borra_fila(self, fil):
        lis = self.dat[fil]
        self.dat[fil] = []
        list(map(Bloque.eliminar, lis))
        return lis

    # Iterador sobre todos los bloques del tablero, implementado mediante corutina/generador
    def iter_bloques(self):
        for fila in self.dat:
            for b in fila:
                yield b

    # Devuelve una tupla (columna inicial, final y valor/color) por cada bloque que
    # aparece en la línea de texto (formato fichero). Implementado mediante corutina/generador
    # Ver https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
    @staticmethod
    def bloques_en_linea(lin):
        i, n, c_ant = 0, 0, ' '
        for c in lin:
            if c != c_ant:
                if c_ant != ' ':
                    yield (i - n, i - 1, ord(c_ant.upper()) - CH_FICH)
                c_ant = c
                n = 1
            else:
                n += 1
            i += 1
        if c_ant != ' ':
            yield (i - n, i - 1, ord(c_ant.upper()) - CH_FICH)

    # Busca en la lista el bloque que contiene esa columna
    # Devuelve su índice en la lista o -1 si no existe
    @staticmethod
    def index_bloque(lis, col):
        i = 0
        for b in lis:
            if b.col0 <= col <= b.col1:
                return i
            i += 1
        return -1

    # Devuelve la posición donde se debería insertar un bloque
    # si existe un hueco para él (o -1 si no se puede insertar)
    @staticmethod
    def pos_ins_bloque(lis, blo):
        # Búsqueda del primer bloque totalmente posterior al nuestro
        i = 0
        for b in lis:
            if b.col0 > blo.col1:
                break
            i += 1
        # Si existe colisión, es con el bloque anterior al posterior
        return i if i == 0 or lis[i - 1].col1 < blo.col0 else -1

    # Comprueba si una fila está completa
    @staticmethod
    def fila_completa(fila, numcol):
        if len(fila) == 0:
            return False
        # Comprobación de que los bloques inicial y final cubren los extremos
        if fila[0].col0 != 0 or fila[-1].col1 != numcol - 1:
            return False
        # Comprobación de que todos los bloques están "pegados"
        # Ver https://docs.python.org/3/library/functions.html#zip
        for (b1, b2) in zip(fila, fila[1:]):
            if b1.col1 + 1 != b2.col0:
                return False
        return True

    # Comprueba si en una fila completa todos los bloques son del mismo color
    # Ver https://docs.python.org/3/library/functions.html#all
    # Ver https://docs.python.org/3/library/functions.html#map
    # Ver https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
    @staticmethod
    def fila_mismo_color(fila):
        return all(map(lambda b: b.val == fila[0].val, fila[1:]))

    # Traducción de fila a texto
    def fil2txt(self, letra, fila):
        ca = 0
        lin = letra + ' '
        for b in fila:
            lin += '|   ' * (b.col0 - ca) + '|' + str(b)
            ca = b.col1 + 1
        lin += '|   ' * (self.ncol - ca) + '|\n'
        return lin

    # Traducción de tablero a texto
    # Ver https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    # Ver https://docs.python.org/3/library/functions.html#zip
    # Ver https://docs.python.org/3/library/stdtypes.html?highlight=join#str.join
    def tab2txt(self):
        sep = '  ' + '---'.join(['+'] * (self.ncol + 1)) + '\n'
        ejey = [chr(i + CH_FIL) for i in range(self.nfil)]
        ejex = '    ' + '   '.join([chr(i + CH_COL) for i in range(self.ncol)]) + '\n'
        return sep + sep.join([self.fil2txt(*p) for p in zip(ejey, self.dat)]) + sep + ejex


def main():
    print("*** PRACTICA DE PARADIGMAS 2020-21 ***\n")
    nomfich = input("Fichero de filas iniciales: ")
    tab = Tablero(nomfich, 12)
    while not tab.lleno():
        # Insertar fila
        tab.ins_fila()
        print("1. INSERCIÓN FILA")
        print(tab)
        print(f"Puntuación: {tab.ptos}\n")
        # Obtener y realizar jugada
        error = True
        while error:
            jug = input("Introduzca jugada o --- o FIN: ")
            if jug == "FIN":
                return
            res = tab.jugada(jug)
            if res == -3:
                print("Error de sintaxis en jugada")
            elif res == -2:
                print("El bloque no puede moverse en esa dirección")
            elif res == -1:
                print("No hay ningún bloque en esa celda")
            else:
                error = False
        print("2. MOVIMIENTO")
        print(tab)
        # Caída de bloques y borrado de filas
        seguir = True
        while seguir:
            tab.caida()
            print("3. CAÍDA")
            print(tab)
            lis = tab.eliminacion()
            seguir = len(lis) > 0
            if seguir:
                print("4. ELIMINACIÓN")
                print(tab)





if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()