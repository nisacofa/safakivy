import aplicacion
import kivymd
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.uix.button import Button
from kivymd.uix.button import *
from kivymd.uix.gridlayout import GridLayout
from volcado_datos import *
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

def mostrar_etiqueta(panel):
    boton1 = Button(text="Hola")
    panel.add_widget(boton1)

def desaparecer(panel):
    panel.clear_widgets()

class Aplicacion(MDApp):
    def build(self):
        ventana = Screen(name="Zapatos APP")
        panel_principal = GridLayout(cols=1, rows=2)
        panel = GridLayout(cols=4,rows=3,row_force_default=True, row_default_height=40)
        panel_tabla = MDBoxLayout()

        boton1 = Button(text="Cargar")
        boton1.bind(on_press= lambda a: insertar_datos() )
        boton2 = Button(text="Buscar" )
        boton3 = Button(text="Mostrar" )
        boton3.bind(on_press=lambda a: mostrar_etiqueta(panel))
        boton4 = Button(text="Desaparecer" )
        boton4.bind(on_press=lambda a: desaparecer(panel))

        panel.add_widget(boton1)
        panel.add_widget(boton2)
        panel.add_widget(boton3)
        panel.add_widget(boton4)


        tabla = MDDataTable(
            column_data=[
                ("marca", dp(30)),
                ("modelo", dp(30)),
                ("precio", dp(30)),
                ("genero", dp(30)),
            ],
        )

        panel_tabla.add_widget(tabla)
        panel_principal.add_widget(panel)
        panel_principal.add_widget(panel_tabla)

        ventana.add_widget(panel_principal)

        return ventana

Aplicacion().run()