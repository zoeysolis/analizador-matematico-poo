import wx

# --- LÓGICA MATEMÁTICA (Clase de Negocio) ---
class CalculadoraMatematica:
    """Clase encargada de procesar la lógica de los números."""
    
    def es_primo(self, n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def obtener_factores(self, n):
        i = 2
        factores = []
        temp_n = n
        while i * i <= temp_n:
            if temp_n % i:
                i += 1
            else:
                temp_n //= i
                factores.append(str(i))
        if temp_n > 1:
            factores.append(str(temp_n))
        return " x ".join(factores) if factores else str(n)

# --- INTERFAZ GRÁFICA (Clase de Vista) ---
class VentanaAnalizador(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Analizador de Números Primos', size=(400, 300))
        self.calculadora = CalculadoraMatematica()
        self.configurar_interfaz()
        self.Show()

    def configurar_interfaz(self):
        panel = wx.Panel(self)
        contenedor = wx.BoxSizer(wx.VERTICAL)

        # Elementos visuales
        self.instruccion = wx.StaticText(panel, label="Ingrese un número entero:")
        self.entrada = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        self.boton = wx.Button(panel, label="Analizar Número")
        self.resultado = wx.StaticText(panel, label="")
        
        # Eventos
        self.boton.Bind(wx.EVT_BUTTON, self.al_analizar)

        # Diseño (Layout)
        contenedor.Add(self.instruccion, 0, wx.ALL | wx.CENTER, 10)
        contenedor.Add(self.entrada, 0, wx.ALL | wx.EXPAND, 10)
        contenedor.Add(self.boton, 0, wx.ALL | wx.CENTER, 10)
        contenedor.Add(self.resultado, 0, wx.ALL | wx.CENTER, 10)

        panel.SetSizer(contenedor)

    def al_analizar(self, event):
        valor = self.entrada.GetValue()
        if not valor.isdigit():
            self.resultado.SetLabel("Error: Ingrese un número válido.")
            return

        n = int(valor)
        primo = "SÍ" if self.calculadora.es_primo(n) else "NO"
        factores = self.calculadora.obtener_factores(n)

        res_texto = (f"¿Es Primo?: {primo}\n\n"
                     f"Descomposición en factores:\n{factores}")
        
        self.resultado.SetLabel(res_texto)

if __name__ == '__main__':
    app = wx.App()
    VentanaAnalizador()
    app.MainLoop()
