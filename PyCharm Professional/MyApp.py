from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.picker import MDDatePicker


class MyLayout(BoxLayout):
    customer_id = ObjectProperty()
    date = ObjectProperty()
    size = ObjectProperty()
    item_id = ObjectProperty()

    def validate_fields(self):
        if not self.customer_id.text.isdigit():
            self.customer_id.error = True
        if not self.date.text:
            self.date.error = True
        elif not self.is_valid_date(self.date.text):
            self.date.error = True
            dialog = MDDialog(title="Error", text="Please enter a valid date (YYYY-MM-DD).", size_hint=(0.8, 0.3),
                              buttons=[MDFlatButton(text="OK", on_release=lambda *args: dialog.dismiss())])
            dialog.open()
        if not self.size.text.isdigit():
            self.size.error = True
        if not self.item_id.text.isdigit():
            self.item_id.error = True

    def is_valid_date(self, date_text):
        try:
            TextInput().input_filter(date_text, 'int')
            date_format = "%Y-%m-%d"
            datetime.datetime.strptime(date_text, date_format)
            return True
        except ValueError:
            return False

    def clear_fields(self):
        self.customer_id.text = ""
        self.date.text = ""
        self.size.text = ""
        self.item_id.text = ""

    def open_date_picker(self):
        date_dialog = MDDatePicker(callback=self.set_date)
        date_dialog.open()

    def set_date(self, date_obj):
        self.date.text = date_obj.strftime("%Y-%m-%d")

    def submit_data(self):
        self.validate_fields()
        if not any(field.error for field in [self.customer_id, self.date, self.size, self.item_id]):
            # perform submit action here
            self.clear_fields()
        else:
            dialog = MDDialog(title="Error", text="Please fill in all required fields.", size_hint=(0.8, 0.3),
                              buttons=[MDFlatButton(text="OK", on_release=lambda *args: dialog.dismiss())])
            dialog.open()


class MyMainApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    MyMainApp().run()

Builder.load_string("""
<MyLayout>:
    orientation: 'vertical'
    customer_id: customer_id
    date: date
    size: size
    item_id: item_id
    
    MDToolbar:
        title: 'My App'
    
    MDTextField:
        id: customer_id
        hint_text: "Customer ID"
        icon_left: "account"
        input_filter: "int"
        required: True
        helper_text: "Required"
        helper_text_mode: "on_error"
        
    MDTextField:
        id: date
        hint_text: "Date"
        icon_left: "calendar"
        on_focus: if self.focus: app.root.open_date_picker()
        required: True
        helper_text: "Required"
        helper_text_mode: "on_error"
        
    MDTextField:
        id: item
        hint_text: "Item"
        icon_left: "package-variant-closed"
        required: False
        
    MDTextField:
        id: size
        hint_text: "Size"
        icon_left: "ruler"
        input_filter: "int"
        required: True
        helper_text: "Required"
        helper_text_mode: "on_error"
        
    MDTextField:
        id: item_id
        hint_text: "Item ID"
        icon_left: "barcode-scan"
        input_filter: "int"
        required: True
        helper_text: "Required"
        helper_text_mode: "on_error"
    
    MDBoxLayout:
        padding: 10
        spacing: 10
        size_hint_y: None
        height: self.minimum_height
        
        MDFlatButton:
            text: 'Clear'
            on_release: app.root.clear_fields()
        
        MDFlatButton:
            text: 'Submit'
            on_release: app.root.submit_data()
"""
