import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class NumberInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        if substring.isnumeric() or substring == "." or substring == ",":
            if substring == ",":
                substring = "."
            return super().insert_text(substring, from_undo=from_undo)

class JurosCompostos(App):
    def build(self):
        layout = GridLayout(cols=2)

        layout.add_widget(Label(text="Valor Inicial:"))
        self.valor_inicial = NumberInput(multiline=False)
        layout.add_widget(self.valor_inicial)

        layout.add_widget(Label(text="Taxa de juros anual (%):"))
        self.taxa = NumberInput(multiline=False)
        layout.add_widget(self.taxa)

        layout.add_widget(Label(text="Período de tempo (anos):"))
        self.tempo = NumberInput(multiline=False)
        layout.add_widget(self.tempo)

        layout.add_widget(Label(text="Aporte mensal:"))
        self.aporte_mensal = NumberInput(multiline=False)
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
        vf = p
        investido = p
        for i in range(int(t * n)):
            investido += m
            vf *= (1 + (r/100)/n)
            vf += m

        juros = vf - investido
        
        self.valor_investido.text = "R$ {:.2f}".format(investido)
        self.valor_juros.text = "R$ {:.2f}".format(juros)
        self.valor_final.text = "R$ {:.2f}".format(vf)

if __name__ == '__main__':
    JurosCompostos().run()
