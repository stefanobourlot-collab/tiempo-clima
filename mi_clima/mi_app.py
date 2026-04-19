import flet as ft
import requests
from datetime import datetime

def main(page: ft.Page):
    page.title = "Clima - Concepción del Uruguay"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.Colors.BLUE_900
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO
    
    def actualizar_datos(e=None):
        try:
            latitud = -32.48
            longitud = -58.23
            
            url_clima = f"https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&current_weather=true"
            respuesta = requests.get(url_clima)
            datos = respuesta.json()
            
            temperatura = datos['current_weather']['temperature']
            viento = datos['current_weather']['windspeed']
            
            if temperatura > 30:
                icono = "🥵"
            elif temperatura > 20:
                icono = "🌞"
            elif temperatura > 10:
                icono = "🍂"
            else:
                icono = "❄️"
            
            clima_temp.value = f"{icono} {temperatura}°C"
            clima_viento.value = f"💨 Viento: {viento} km/h"
            
            altura_rio = 2.00
            rio_valor.value = f"🌊 {altura_rio} m"
            rio_tendencia.value = "⬆️ Crece (+0.02m en 12hs)"
            
            ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            actualizacion.value = f"🔄 Actualizado: {ahora}"
            
            page.update()
            
        except Exception as error:
            clima_temp.value = "⚠️ Error"
            clima_viento.value = f"No se pudo cargar: {error}"
            page.update()
    
    titulo = ft.Text("🌊 Concepción del Uruguay", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    autor = ft.Text("👨‍💻 Stefano Bourlot | GitHub: StefanoBourlot", size=14, color=ft.Colors.CYAN_300, italic=True)
    
    clima_temp = ft.Text("---", size=50, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    clima_viento = ft.Text("---", size=16, color=ft.Colors.WHITE_70)
    
    rio_titulo = ft.Text("Río Uruguay", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.CYAN_300)
    rio_valor = ft.Text("---", size=35, weight=ft.FontWeight.BOLD, color=ft.Colors.CYAN_200)
    rio_tendencia = ft.Text("---", size=14, color=ft.Colors.GREEN_300)
    
    actualizacion = ft.Text("---", size=12, color=ft.Colors.WHITE_54)
    boton = ft.ElevatedButton("🔄 Actualizar", on_click=actualizar_datos, bgcolor=ft.Colors.CYAN_700, color=ft.Colors.WHITE)
    
    page.add(
        titulo, autor,
        ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
        clima_temp, clima_viento,
        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
        rio_titulo, rio_valor, rio_tendencia,
        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
        actualizacion,
        ft.Divider(height=15, color=ft.Colors.TRANSPARENT),
        boton
    )
    
    actualizar_datos()

if __name__ == "__main__":
    ft.app.run(target=main, view=ft.AppView.WEB_BROWSER)