import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class JurosCompostos(App):
    def build(self):
        layout = GridLayout(cols=2)

        layout.add_widget(Label(text="Valor Inicial:"))
        self.valor_inicial = TextInput(multiline=False)
        layout.add_widget(self.valor_inicial)

        layout.add_widget(Label(text="Taxa de juros anual (%):"))
        self.taxa = TextInput(multiline=False)
        layout.add_widget(self.taxa)

        layout.add_widget(Label(text="Período de tempo (anos):"))
        self.tempo = TextInput(multiline=False)
        layout.add_widget(self.tempo)

        layout.add_widget(Label(text="Aporte mensal:"))
        self.aporte_mensal = TextInput(multiline=False)
        layout.add_widget(self.aporte_mensal)

        layout.add_widget(Label(text="Valor Investido:"))
        self.valor_investido = Label(text="")
        layout.add_widget(self.valor_investido)

        layout.add_widget(Label(text="Valor em Juros:"))
        self.valor_juros = Label(text="")
        layout.add_widget(self.valor_juros)

        layout.add_widget(Label(text="Valor Final:"))
        self.valor_final = Label(text="")
        layout.add_widget(self.valor_final)

        calcular = Button(text="Calcular", on_press=self.calcular_juros)
        layout.add_widget(calcular)

        return layout

    def calcular_juros(self, event):
        p = float(self.valor_inicial.text)
        r = float(self.taxa.text)
        t = float(self.tempo.text)
        m = float(self.aporte_mensal.text)

        # Fórmula de juros compostos com aportes mensais: Vf = P * (1 + r/n) ^ (n*t) + m * [((1 + r/n) ^ (n*t) - 1) / (r/n)]
        n = 12 # número de vezes que o juros é aplicado por ano, para este exemplo usaremos mensal
        vf = p * (1 + (r/100)/n) ** (n*t) + m * (((1 + (r/100)/n) ** (n*t) - 1) / ((r/100)/n))
        juros = vf - p - m * (t * 12)
        
        self.valor_investido.text = "R$ {:.2f}".format(p)
        self.valor_juros.text = "R$ {:.2f}".format(juros)
        self.valor_final.text = "R$ {:.2f}".format(vf)

if __name__ == '__main__':
    JurosCompostos().run()
