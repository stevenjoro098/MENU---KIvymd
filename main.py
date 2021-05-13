import requests
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivymd.uix.card import MDCard
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import AsyncImage
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton

Window.size = (320, 600)

url = 'http://127.0.0.1:8000'

class MenuGrid(MDScreen):
    def create_widgets(self,title, image_source,price):
        item_card = MDCard(
            size=(300, 240),
            border_radius=20,
            radius=[20,],
            elevation=10)
        #item_card.md_bg_color = [1, 0.54, 0, .3]
        card_layout = RelativeLayout()
        image = AsyncImage(source = image_source,
                        size_hint = (.5, .5),
                        pos_hint={"center_x":.3,"center_y": .5})
        item_title = MDLabel(text=title,
                        halign="center",
                        theme_text_color="ContrastParentBackground",
                        font_style="H5",
                        pos_hint={"center_x": .7,"center_y":.7})

        item_price = MDLabel(text=price,
                        halign="center",
                        theme_text_color="Secondary",
                        pos_hint={"center_x": .7, "center_y": .6})
        order = MDRaisedButton(
                        text="Order",
                        size_hint=(.5, None),
                        pos_hint={"center_x": .68, "center_y": .15})
        card_layout.add_widget(image)
        card_layout.add_widget(item_title)
        card_layout.add_widget(item_price)
        card_layout.add_widget(order)
        item_card.add_widget(card_layout)
        self.list_menu.add_widget(item_card)

    def fetch_api(self):#fetch api and update home page
        try:
            url_ = url
            content = requests.get(url_).json()
            print(content)
            for items in content:
                name = items['name']
                price = items['price']
                image = items['image']
                self.create_widgets(name,image,price)
        except:
            toast("Failed")

class MenuApp(MDApp):

    def build(self):
        #self.theme_cls.primary_color = 'Red'
        return MenuGrid()


if __name__ == "__main__":
    MenuApp().run()
