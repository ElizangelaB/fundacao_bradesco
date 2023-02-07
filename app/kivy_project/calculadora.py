from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.operators= ["/","*","+","-"]
        self.last_was_operator= None
        self.last_button= None
        main_layout= BoxLayout(orientation="vertical")
        self.solution= TextInput(
            multiline=False, readonly=True, halign="right" font_size=55         
        )
        main_layout.add_widget(self.solution)
        buttons= [
            ["7","8","9","/"],
            ["4","5","6","*"],
            ["1","2","3","-"],
            [".","0","C","+"],
        ]
        for row in buttons:
            h_layout= BoxLayout()
            for label in row:
                button= Button(
                text=label, 
                pos_hint={"center_x":0.5, "center_y":0,5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        equals_button.bind(on_press=self.on_solution) #botão de igual adicionado ao evento main
        main_layout.add_widget(equals_button)
        retunr main_layout        
                
 #criando manipulador de evento on_button_press()
    def  on_button_press(self, instance):
        current= self.solution.text
        button_text= instance.text 
        
        if button_text== "C": #o usuario precionando o c limparar o arquivo solution
            self.solution.text=""
        else:
            if current and (
                self.last_was_operator and button_text in self.operators):  
                #evita de colocar dois operadores 1*/
                return
            elif current== "" and button_text in self.operators:
                #verifica se o primeiro caractere é um operador se for nao sera atualizado.
                return
            else:
                new_text= current+ button_text #se nenhuma causa for atendida atualiza o solution
                self.solution.text= new_text
        self.last_button= button_text # define o ultimo botao pressionado
        self.last_was_operator= self.last_button in self.operators # define True or False dependendo de ser ou nao um caractere de operador
        
    def on_solution(self, instance):
        
        text= self.solution.text
        if text:
            solution= str(eval(self.solution.text))
            self.solution.text= solution                
                
                    
            
        
                     
            