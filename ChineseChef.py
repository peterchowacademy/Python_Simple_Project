# inheritance of class - add other existing class to your new class
from chef import Chef


class ChineseChef(Chef):
    def make_special_dish(self):
        print("The chef makes orange chichek")

    def make_fried_rice(self):
        print("The chef makes fried rice")
