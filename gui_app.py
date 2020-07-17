from tkinter import *

app = Tk()
# spider list
spider_label = Label(app, text='Choose a spider')
spider_label.grid(row=0, column=0, stick=W, pady=10, padx=10)

spider_text = StringVar(app)
spider_text.set('Choose a spider')
spiders = ['spider 1', 'spider 2']
spiders_dropdown = OptionMenu(app, spider_text, *spiders)
spiders_dropdown.grid(row=0, column=1, stick=W, columnspan = 2)
# Feed type
feed_label = Label(app, text='Choose a feed')
feed_label.grid(row=1, column=0, stick=W, pady=10, padx=10)

feed_text = StringVar(app)
feed_text.set('Choose a feed')
feeds = ['JSON', 'CSV']
feeds_dropdown = OptionMenu(app, feed_text, *feeds)
feeds_dropdown.grid(row=1, column=1, stick=W, columnspan = 2)

# Path Entry
folder_path_text = StringVar(app)
folder_path_entry = Entry(app, textvariable=folder_path_text)
folder_path_entry.grid(row=2, column=0, stick=W, pady=10, padx=10)

# Path Entry
dataset_text = StringVar(app)
dataset_entry = Entry(app, textvariable=dataset_text,width=10)
dataset_entry.grid(row=2, column=1)

# Button
browse_btn = Button(app, text='Browse')
browse_btn.grid(row=2,column=2)

execute_btn = Button(app, text='Execute')
execute_btn.grid(row=3,column=0,columnspan=3)

app.title('Spider Execute')
app.geometry('300x200')
app.resizable(False, False)
app.mainloop()
