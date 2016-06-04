from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.app import App
from kivy.lang import Builder
import csv


class Main(App):
    status_text = StringProperty()
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        #loads datalines from the load items function
        self.data_lines = self.load_items()

    def build(self):
        #loads the kivy code onto the program
        self.status_text = "Choose action from the left menu, then select items on the right"
        self.title = "Equipment Hire"
        # load file
        self.root = Builder.load_file('hireGUI.kv')

        #loads data_lines and creates button
        data_lines = self.load_items()
        self.create_buttons(data_lines)
        # testing code
        print('build')

        return self.root

    #function from first assignment. loads items from the csv file into data_lines
    def load_items(self):
        return_array = []
        #Open, read and transfer the lines in data to the memory variable
        data_file = open("items2.csv")

        self.count = 0
        for line in data_file:
            values = line.split(",")
            return_array.append([values[0], values[1], values[2], values[3]])
            self.count = self.count + 1


        print('loaditems')
        print(return_array)
        #stores the data in returnarray and returned the array.
        return return_array

    #creates the buttons for kivy
    def create_buttons(self, data_lines):
        for line in data_lines:
            # creates a button for each line in datalines (csv)
            # Labels the text of the button accordingly.
            new_button = Button(text=line[0])
            new_button.bind(on_release=self.entry)
            self.root.ids.entryBox.add_widget(new_button)
            print(line)

    def entry(self, instance):
        #for when the button is clicked the price will show up
        name = instance.text
        for line in self.data_lines:
            if line[0] == instance.text:
                tempprice = line[2]

        self.status_text = "{} ${}".format(name, tempprice)

    def add_items(self):
        #when the add items menu is clicked a popup opens where the user can type a new entry
        self.status_text = "Enter details for a new hire item"
        self.root.ids.addItems.open()

        #saves the new entry into the csv file.
    def save(self, name_field, price_field, description_field):
        self.data_lines.append([name_field, description_field, price_field, 'in \n'])
        print(self.data_lines)

        #saves the new item in the csv file and rearranges the format so the program can read it.
        for line in self.data_lines:
            newitems = '{} {} {} {}'.format(line[0], line[1], line[2], line[3])
        with open ('items2.csv', 'wb') as f:
            writer = csv.writer(f, delimiter = ",", lineterminator ='')
            writer.writerows(self.data_lines)

        #testing code
        print(newitems)


        self.root.ids.entryBox.cols = 5 // 5 + 1
        new_button = Button(text=name_field.text)
        new_button.bind(on_release=self.entry)
        self.root.ids.entryBox.add_widget(new_button)
        self.root.ids.addItems.dismiss()
        self.clear_text()

    #clears text from the fields in the new item pop up
    def clear_text(self):
        self.root.ids.name_field.text = ""
        self.root.ids.price_field.text = ""
        self.root.ids.description_field.text = ""

    #when the user presses cancel the popup is dismissed and clear text is called with clears all the text from the fields
    def cancel(self):
        self.root.ids.addItems.dismiss()
        self.clear_text()
        self.status_text = ""

    #my attempt at making the hire function work..
    def hire(self):
        data_lines = self.load_items()

        for line in data_lines:
            # create a button for each entry
            if 'in' in line[3]:
                self.new_button = Button(text=line[0])
                self.new_button.bind(on_release=self.entry)
                self.new_button.background_color=[0,3,6,22]
                self.root.ids.entryBox.add_widget(self.new_button)
                print('testrun')


            #new_button.bind(on_release=self.changecolor(data_lines))


        self.status_text = "Choose the items you would like to hire, then press confirm."






Main().run()
