# Импорт всех классов
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
import datetime; from datetime import timedelta
tema = True
vibor3_5 = False
# Глобальные настройки
Window.size = (350, 750)
Window.clearcolor = (237/255, 238/255, 240/255, 1)
#Window.clearcolor = (20/255, 20/255, 20/255, 1)
Window.title = "расчет круток"
dt_now = datetime.date.today()
dt_help = timedelta(days=1)
dni = 0
strimhelp = 0
bezdna = 0
magaz = 0
strimy = 0
# from kivy.animation import Animation
# from kivy.clock import Clock
# from kivy.config import Config
# from kivy.uix.image import Image
# from kivy.core import audio
# from kivy.core.audio import SoundLoader

# import socket
# sock = socket.socket()
# sock.bind(('', 9090))
# sock.listen(1)


class MainApp(App):
    def build(self):
        # here I add the main and second screens to the manager, this class does nothing else
        sm.add_widget(MainScreen())
        sm.add_widget(SecondScreen1())
        sm.add_widget(SecondScreen2())
        #sm.add_widget(SecondScreen3())
        #sm.add_widget(SecondScreen4())
        sm.add_widget(thirdScreen())
        sm.add_widget(ErrorScreen())
        return sm  # I return the manager to work with him later
    def DarkTheme(self, instance):
        global tema
        if tema == True:
            tema=False 
            Window.clearcolor=(20/255, 20/255, 20/255, 1)
            self.label.color = (237/255, 238/255, 240/255, 1)
            self.inf.color = (237/255, 238/255, 240/255, 1)
        else:
            self.label.color = (0/255, 0/255, 0/255, 1)
            self.inf.color = (0/255, 0/255, 0/255, 1)
            Window.clearcolor = (237/255, 238/255, 240/255, 1)
            tema = True


class MainScreen(Screen):
    def __init__(self):
        super().__init__()

        self.name = '1'  # setting the screen name value for the screen manager
        # (it's more convenient to call by name rather than by class)

        main_layout = GridLayout(cols = 2, rows =7, padding = [0, 10, 0 ,0], spacing = 0)  # creating an empty layout that's not bound to the screen
        self.add_widget(main_layout)  # adding main_layout on screen
        #self.label = Label(text='расчет круток',size_hint=(1, None), size=(350, 70),color = (0/255, 0/255, 0/255, 1), top = 1.0)
        tema = Button(text = 'темная тема', size_hint=(1, None), size = (90, 70))
        self.label = Label(text='расчет круток',size_hint=(1, None), size=(350, 70),color = (0/255, 0/255, 0/255, 1), top = 1.0)
        self.inf = Label(text='выбор обновы',size_hint=(1, None), size=(350, 70), color = (0/255, 0/255, 0/255, 1))
        
        btn1 = Button(text='обновление 3.5', size_hint=(1, None), size=(20, 70))
        btn2 = Button(text='обновление 3.6', size_hint=(1, None), size=(20, 70))
        btn3 = Button(text='обновление 3.7', size_hint=(1, None), size=(20, 70))
        btn4 = Button(text='обновление 3.8', size_hint=(1, None), size=(20, 70))
          # setting up a button to perform an action when clicked
        main_layout.add_widget(self.label)
        main_layout.add_widget(tema)
        main_layout.add_widget(self.inf)
        main_layout.add_widget(Label(text='    ', size_hint=(1, None), size = (20, 70)))
        for i in range(1):
            main_layout.add_widget(Label(text='    '))
        main_layout.add_widget(Button(text = 'ручной ввод ДД.ММ.ГГГГ', size_hint=(1, None), size = (10, 70), font_size=14))
        main_layout.add_widget(btn1)
        main_layout.add_widget(btn2)
        main_layout.add_widget(btn3)
        main_layout.add_widget(btn4)  # adding button on layout
        btn1.bind(on_press=self.to_second1_scrn)
        btn2.bind(on_press=self.to_second2_scrn)
        tema.bind(on_press=self.DarkTheme)
    def to_second1_scrn(self, *args):
        self.manager.current = '2.1'  # selecting the screen by name (in this case by name "Second")
        return 0  # this line is optional
    def to_second2_scrn(self, *args):
        self.manager.current = '2.2'
        return 0
    def DarkTheme(self, instance):
        global tema
        global text_color
        if tema == True:
            tema=False 
            Window.clearcolor=(20/255, 20/255, 20/255, 1)
            self.label.color = (237/255, 238/255, 240/255, 1)
            self.inf.color = (237/255, 238/255, 240/255, 1)
        else:
            self.label.color = (0/255, 0/255, 0/255, 1)
            self.inf.color = (0/255, 0/255, 0/255, 1)
            Window.clearcolor = (237/255, 238/255, 240/255, 1)
            tema = True
class SecondScreen1(Screen):
    def __init__(self):
        super().__init__()
    # on this screen, I do everything the same as on the main screen to be able to switch back and forth
        self.name = '2.1'
        main_layout = GridLayout(cols = 2, rows =7, padding = [0, 10, 0 ,0], spacing = 0)  # creating an empty layout that's not bound to the screen
        self.add_widget(main_layout)  # adding main_layout on screen
        self.label = Label(text='расчет круток',size_hint=(1, None), size=(350, 70),color = (0/255, 0/255, 0/255, 1), top = 1.0)
        tema = Button(text = 'темная тема', size_hint=(1, None), size = (90, 70))
        self.inf = Label(text='выбор половины 3.5',size_hint=(1, None), size=(350, 70), color = (0/255, 0/255, 0/255, 1))
        btn1 = Button(text='начало первой', size_hint=(1, None), size=(20, 70))
        btn2 = Button(text='начало второй', size_hint=(1, None), size=(20, 70))
        btn3 = Button(text='конец обновления', size_hint=(1, None), size=(20, 70))
        btn4 = Button(text='назад', size_hint=(1, None), size=(20, 70))
        tema.bind(on_press=self.DarkTheme)
        btn1.bind(on_press=self.to_date1_scrn)
        btn2.bind(on_press=self.to_date2_scrn)
        btn3.bind(on_press=self.to_date3_scrn)
        btn4.bind(on_press=self.to_main_scrn)
        main_layout.add_widget(self.label)
        main_layout.add_widget(tema)
        main_layout.add_widget(self.inf)
        main_layout.add_widget(Label(text='    ', size_hint=(1, None), size = (20, 70)))
        for i in range(2):
            main_layout.add_widget(Label(text = '    '))
        main_layout.add_widget(btn1)
        main_layout.add_widget(btn2)
        main_layout.add_widget(btn3)
        main_layout.add_widget(btn4)
    def to_date1_scrn(self, *args):
        self.manager.current = 'error'
    def to_main_scrn(self, *args):  # together with the click of the button, it transmits info about itself.
        # In order not to pop up an error, I add *args to the function
        self.manager.current = '1'
        return 0
    def to_date2_scrn(self, *args):
        global dt_now, dt_help, strimhelp, strimy, dni, b, bezdna
        dt_future = datetime.date(2023, 3, 21); testovie =2
        dt_now1 = dt_now
        m_now = dt_now.month
        m_future = dt_future.month
        magaz = m_future - m_now
        dt_3_5 = datetime.date(2023, 3, 1)
        while dt_3_5 > dt_now1: 
            dt_now1 = dt_now1 + dt_help
            strimhelp +=1
        if strimhelp >= 12: strimy +=1
        while dt_future > dt_now:
            b = dt_now.day
            dt_now = dt_now + dt_help
            dni +=1
        if b == 1 or b == 16: bezdna+=1
        print(dni, "дней осталось")
        self.manager.current = '3'
        return 0
    def to_date3_scrn(self, *args):
        global dt_now, dt_help, strimhelp, strimy, dni, b, bezdna
        dt_future = datetime.date(2023, 4, 11); strimy =1; testovie =2
        dt_now1 = dt_now
        m_now = dt_now.month
        m_future = dt_future.month
        magaz = m_future - m_now
        dt_3_5 = datetime.date(2023, 3, 1)
        while dt_3_5 > dt_now1: 
            dt_now1 = dt_now1 + dt_help
            strimhelp +=1
        if strimhelp >= 12: strimy +=1
        while dt_future > dt_now:
            b = dt_now.day
            dt_now = dt_now + dt_help
            dni +=1
        if b == 1 or b == 16: bezdna+=1
        print(dni, "дней осталось")
        self.manager.current = '3'
        return 0
    def DarkTheme(self, instance):
        global tema
        if tema == True:
            tema=False 
            Window.clearcolor=(20/255, 20/255, 20/255, 1)
            self.label.color = (237/255, 238/255, 240/255, 1)
            self.inf.color = (237/255, 238/255, 240/255, 1)
        else:
            self.label.color = (0/255, 0/255, 0/255, 1)
            self.inf.color = (0/255, 0/255, 0/255, 1)
            Window.clearcolor = (237/255, 238/255, 240/255, 1)
            tema = True
class ErrorScreen(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'error'
        main_layout = BoxLayout(orientation='vertical', padding = [0, 10, 0 ,0], spacing = 0)  # creating an empty layout that's not bound to the screen
        self.add_widget(main_layout)
        self.label = Label(text ='начало первой половины 3.5', color = (0/255, 0/255, 0/255, 1), size_hint=(1, None), size = (40, 50))
        self.label1 = Label(text ='уже в прошлом и неактуально', color = (0/255, 0/255, 0/255, 1), size_hint=(1, None), size = (40, 50))
        main_layout.add_widget(self.label)
        main_layout.add_widget(self.label1)
        main_layout.add_widget(Label(text ='    '))
        tema = Button(text = 'темная тема', size_hint=(1, None), size = (40, 100))
        main_layout.add_widget(tema)
        tema.bind(on_press=self.DarkTheme)
        return_back = Button(text = 'обратно', size_hint=(1, None), size = (40, 100))
        main_layout.add_widget(return_back)
        return_back.bind(on_press=self.back)
    def back(self, *args):
        self.manager.current = '2.1'
        return 0
    def DarkTheme(self, instance):
        global tema
        if tema == True:
            tema=False 
            Window.clearcolor=(20/255, 20/255, 20/255, 1)
            self.label.color = (237/255, 238/255, 240/255, 1)
            self.label1.color = (237/255, 238/255, 240/255, 1)
        else:
            self.label.color = (0/255, 0/255, 0/255, 1)
            self.label1.color = (0/255, 0/255, 0/255, 1)
            Window.clearcolor = (237/255, 238/255, 240/255, 1)
            tema = True
class thirdScreen(Screen):
    def __init__(self):
        super().__init__()
    # on this screen, I do everything the same as on the main screen to be able to switch back and forth
        self.name = '3'
        main_layout = BoxLayout(orientation= 'vertical', padding = [0, 10, 0 ,0], spacing = 0)  # creating an empty layout that's not bound to the screen
        self.add_widget(main_layout)  # adding main_layout on screen
        self.label = Label(text='расчет круток',size_hint=(1, None), size=(350, 70),color = (0/255, 0/255, 0/255, 1), top = 1.0)
        tema = Button(text = 'темная тема', size_hint=(1, None), size = (90, 70))
        self.inf = Label(text='выбор обновы',size_hint=(1, None), size=(350, 70), color = (0/255, 0/255, 0/255, 1))
        dniluny = TextInput(hint_text="сколько дней луны осталось", multiline=False)
        krutki = TextInput(hint_text="текущее количество круток", multiline=False)
        otkrucheno = TextInput(hint_text="сколько сделано", multiline=False)
        etaz = TextInput(hint_text="этажей бездны проходишь", multiline=False)
        drugieistochniki = TextInput(hint_text="другие источники круток", multiline=False)
        itog = TextInput(hint_text="количество купленных лун", multiline=False)
        btn1 = Button(text='далее', size_hint=(1, None), size=(20, 70))
        btn2= Button(text='на главную', size_hint=(1, None), size=(20, 70))
        btn2.bind(on_press=self.to_main_scrn)
        tema.bind(on_press=self.DarkTheme)
        #main_layout.add_widget(self.label)
        main_layout.add_widget(tema)
        main_layout.add_widget(dniluny)
        main_layout.add_widget(krutki)
        main_layout.add_widget(otkrucheno)
        main_layout.add_widget(etaz)
        main_layout.add_widget(drugieistochniki)
        main_layout.add_widget(itog)
        main_layout.add_widget(btn1)
        main_layout.add_widget(btn2)

    def to_main_scrn(self, *args):  # together with the click of the button, it transmits info about itself.
        # In order not to pop up an error, I add *args to the function
        self.manager.current = '1'
        return 0
    def DarkTheme(self, instance):
        global tema
        if tema == True:
            tema=False 
            Window.clearcolor=(20/255, 20/255, 20/255, 1)
            self.label.color = (237/255, 238/255, 240/255, 1)
            self.inf.color = (237/255, 238/255, 240/255, 1)
        else:
            self.label.color = (0/255, 0/255, 0/255, 1)
            self.inf.color = (0/255, 0/255, 0/255, 1)
            Window.clearcolor = (237/255, 238/255, 240/255, 1)
            tema = True
class FourthScreen(Screen):
    def __init__(self):
        super().__init__()
        self.name = '4'
        main_layout = GridLayout(cols = 2, rows =7, padding = [0, 10, 0 ,0], spacing = 0)
        self.add_widget(main_layout)
class SecondScreen2(Screen):
    def __init__(self):
        super().__init__()
    # on this screen, I do everything the same as on the main screen to be able to switch back and forth
        self.name = '2.2'
        main_layout = GridLayout(cols = 2, rows =7, padding = [0, 10, 0 ,0], spacing = 0)  # creating an empty layout that's not bound to the screen
        self.add_widget(main_layout)  # adding main_layout on screen
        self.label = Label(text='расчет круток',size_hint=(1, None), size=(350, 70),color = (0/255, 0/255, 0/255, 1), top = 1.0)
        tema = Button(text = 'темная тема', size_hint=(1, None), size = (90, 70))
        self.inf = Label(text='выбор половины 3.6',size_hint=(1, None), size=(350, 70), color = (0/255, 0/255, 0/255, 1))
        btn1 = Button(text='начало первой', size_hint=(1, None), size=(20, 70))
        btn2 = Button(text='начало второй', size_hint=(1, None), size=(20, 70))
        btn3 = Button(text='конец обновления', size_hint=(1, None), size=(20, 70))
        btn4 = Button(text='назад', size_hint=(1, None), size=(20, 70))
        btn4.bind(on_press=self.to_main_scrn)
        tema.bind(on_press=self.DarkTheme)
        btn2.bind(on_press=self.to_date1_scrn)
        main_layout.add_widget(self.label)
        main_layout.add_widget(tema)
        main_layout.add_widget(self.inf)
        main_layout.add_widget(Label(text='    ', size_hint=(1, None), size = (20, 70)))
        for i in range(2):
            main_layout.add_widget(Label(text = '    '))
        main_layout.add_widget(btn1)
        main_layout.add_widget(btn2)
        main_layout.add_widget(btn3)
        main_layout.add_widget(btn4)
    def to_main_scrn(self, *args):  # together with the click of the button, it transmits info about itself.
        # In order not to pop up an error, I add *args to the function
        self.manager.current = '1'
        return 0
    def to_date1_scrn(self, *args):
        self.manager.current = '3'
        return 0
    def DarkTheme(self, instance):
        global tema
        if tema == True:
            tema=False 
            Window.clearcolor=(20/255, 20/255, 20/255, 1)
            self.label.color = (237/255, 238/255, 240/255, 1)
            self.inf.color = (237/255, 238/255, 240/255, 1)
        else:
            self.label.color = (0/255, 0/255, 0/255, 1)
            self.inf.color = (0/255, 0/255, 0/255, 1)
            Window.clearcolor = (237/255, 238/255, 240/255, 1)
            tema = True
sm = ScreenManager()  # it's necessary to create a manager variable that will collect screens and manage them


if __name__ == '__main__':
    MainApp().run()