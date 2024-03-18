import pymysql
from tkinter import *
from tkinter import ttk

class StudentDetails:
    def __init__(self,root):
        self.root = root
        self.root.title('NTH')
        self.root.geometry('1340x680')
        title1 = Label(self.root, text='Welcome to Narayana Tech House',
                       font=('monotype corsiva', 30, 'bold'),
                       bd=5, bg='green',fg='white',
                       relief=GROOVE)
        title1.pack(fill='x')

        self.roll_no_var = StringVar()
        self.first_name_var = StringVar()
        self.last_name_var = StringVar()
        self.email_var = StringVar()
        self.course_var = StringVar()
        self.mobile_var = StringVar()
        self.location_var = StringVar()

#Creating Frames
        dataEntryFrame = Frame(self.root, bg='green')
        dataEntryFrame.place(x=10, y=70, width=400, height=600)

        dataDisplayFrame = Frame(self.root, bg='green')
        dataDisplayFrame.place(x=420, y=70, width=910, height=600)

#Working with dataEntryFrame
        title2 = Label(dataEntryFrame, text='Students Data Entry Here...', font=('monotype corsiva', 20, 'bold'), bg='green', fg='yellow', bd=2, relief=RAISED)
        title2.grid(row=0, columnspan=2,padx=50, pady=10)

#Roll NO
        lbl_roll_no = Label(dataEntryFrame, text='Roll No:',font=('Microsoft Sans Serif', 17, 'bold'), bg='green', fg='white')
        lbl_roll_no.grid(row=1, column=0, sticky='W')

        txt_roll_no = Entry(dataEntryFrame,textvariable = self.roll_no_var,font=('Microsoft Sans Serif', 15, 'bold'))
        txt_roll_no.grid(row=1, column=1,sticky='E',padx=10)

#First Name
        lbl_first_name = Label(dataEntryFrame, text='First Name:',font=('Microsoft Sans Serif', 17, 'bold'), bg='green', fg='white')
        lbl_first_name.grid(row=2, column=0)

        txt_first_name = Entry(dataEntryFrame,textvariable = self.first_name_var, font=('Microsoft Sans Serif', 15, 'bold'))
        txt_first_name.grid(row=2, column=1,sticky='E',padx=10, pady=15)

#Last Name
        lbl_last_name = Label(dataEntryFrame, text='Last Name:',font=('Microsoft Sans Serif', 17, 'bold'), bg='green', fg='white')
        lbl_last_name.grid(row=3, column=0)

        txt_last_name = Entry(dataEntryFrame,textvariable = self.last_name_var, font=('Microsoft Sans Serif', 15, 'bold'))
        txt_last_name.grid(row=3, column=1,sticky='E',padx=10)

#Email
        lbl_email = Label(dataEntryFrame, text='Email ID:',font=('Microsoft Sans Serif', 17, 'bold'), bg='green', fg='white')
        lbl_email.grid(row=4, column=0,sticky='W')

        txt_email = Entry(dataEntryFrame,textvariable = self.email_var, font=('Microsoft Sans Serif', 15, 'bold'))
        txt_email.grid(row=4, column=1,sticky='E',padx=10, pady=15)

#Course
        lbl_course = Label(dataEntryFrame, text='Course:',font=('Microsoft Sans Serif', 17, 'bold'), bg='green', fg='white')
        lbl_course.grid(row=5, column=0,sticky='W')

        txt_course = Entry(dataEntryFrame,textvariable = self.course_var, font=('Microsoft Sans Serif', 15, 'bold'))
        txt_course.grid(row=5, column=1,sticky='E',padx=10)

#Mobile
        lbl_mobile = Label(dataEntryFrame, text='Mobile:',font=('Microsoft Sans Serif', 17, 'bold'), bg='green', fg='white')
        lbl_mobile.grid(row=6, column=0,sticky='W')

        txt_mobile = Entry(dataEntryFrame,textvariable = self.mobile_var, font=('Microsoft Sans Serif', 15, 'bold'))
        txt_mobile.grid(row=6, column=1,sticky='E',padx=10,pady=15)

#Location
        lbl_location = Label(dataEntryFrame, text='Location:',font=('Microsoft Sans Serif', 17, 'bold'), bg='green', fg='white')
        lbl_location.grid(row=7, column=0,sticky='W')

        txt_location = Entry(dataEntryFrame,textvariable = self.location_var, font=('Microsoft Sans Serif', 15, 'bold'))
        txt_location.grid(row=7, column=1,sticky='E',padx=10)



        btnFrame = Frame(dataEntryFrame, bg='green', bd=4, relief=RAISED)
        btnFrame.place(x=25, y=400, width=350, height=110)


        btnAdd = Button(btnFrame, text='Add',command = self.adding_data, bg='red',fg='white', font=('Microsoft Sans Serif', 13, 'bold'))
        btnAdd.grid(row= 0, column=0, ipadx=10, pady=30   )

        btnUpdate = Button(btnFrame, text='Update',command=self.update_data, bg='blue',fg='white', font=('Microsoft Sans Serif', 13, 'bold'))
        btnUpdate.grid(row=0, column=1, padx=20, pady=30)

        btnDelete = Button(btnFrame, text='Delete',command=self.delete_data, bg='yellow',fg='red', font=('Microsoft Sans Serif', 13, 'bold'))
        btnDelete.grid(row=0, column=2,  pady=30)

        btnClear = Button(btnFrame, text='Clear', command = self.clear_data, font=('Microsoft Sans Serif', 13, 'bold'))
        btnClear.grid(row=0, column=3, padx=20, pady=30)

        title3 = Label(dataDisplayFrame, text='Students Data Here...', font=('monotype corsiva', 20, 'bold'), bg='green', fg='yellow', bd=2, relief=RAISED)
        title3.grid(row=0, columnspan=2,padx=300, pady=10)

        tblFrame = Frame(dataDisplayFrame, bg='green', bd=5, relief=RAISED)
        tblFrame.place(x=10, y= 60, width=885, height=450)


        self.Student_Table = ttk.Treeview(tblFrame, columns = ('roll_no', 'first_name', 'last_name', 'email', 'course', 'mobile', 'location'))

        self.Student_Table.heading('roll_no', text='Roll No')
        self.Student_Table.heading('first_name', text='First Name')
        self.Student_Table.heading('last_name', text='Last Name')
        self.Student_Table.heading('email', text='Email ID')
        self.Student_Table.heading('course', text='Course')
        self.Student_Table.heading('mobile', text='Contact')
        self.Student_Table.heading('location', text='Location')

        self.Student_Table['show'] = 'headings'

        
        self.Student_Table.column('roll_no', width=120, anchor = CENTER)
        self.Student_Table.column('first_name', width=120, anchor = CENTER)
        self.Student_Table.column('last_name', width=120, anchor = CENTER)
        self.Student_Table.column('email', width=150, anchor = CENTER)
        self.Student_Table.column('course', width=120, anchor = CENTER)
        self.Student_Table.column('mobile', width=120, anchor = CENTER)
        self.Student_Table.column('location', width=120, anchor = CENTER)

        
        self.Student_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.Student_Table.pack()
        self.fetching_data()     


    def adding_data(self):
        connection = pymysql.connect(host='localhost', user='root', password='nth@9010', db='python8pmproject', port=9010)
        c = connection.cursor()
        c.execute('insert into studentsdata values(%s, %s, %s, %s, %s, %s, %s)',
                  (self.roll_no_var.get(),
                   self.first_name_var.get(),
                   self.last_name_var.get(),
                   self.email_var.get(),
                   self.course_var.get(),
                   self.mobile_var.get(),
                   self.location_var.get()
                   ))
        connection.commit()
        self.fetching_data()
        self.clear_data()
        connection.close()
        
    def clear_data(self):
        self.roll_no_var.set('')
        self.first_name_var.set('')
        self.last_name_var.set('')
        self.email_var.set('')
        self.course_var.set('')
        self.mobile_var.set('')
        self.location_var.set('')

    def fetching_data(self):
        connection = pymysql.connect(host='localhost', user='root', password='nth@9010', db='python8pmproject', port=9010)
        c = connection.cursor()
        c.execute('select * from studentsdata')
        rows = c.fetchall()

        if len(rows) != 0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('', END, values=row)
            connection.commit()
        connection.close()

    def get_cursor(self,var):
        cursor_row = self.Student_Table.focus()
        content = self.Student_Table.item(cursor_row)
        row = content['values']
        self.roll_no_var.set(row[0])
        self.first_name_var.set(row[1])
        self.last_name_var.set(row[2])
        self.email_var.set(row[3])
        self.course_var.set(row[4])
        self.mobile_var.set(row[5])
        self.location_var.set(row[6])

    def update_data(self):
        connection = pymysql.connect(host='localhost', user='root', password='nth@9010', db='python8pmproject', port=9010)
        c = connection.cursor()
        c.execute('update studentsdata set first_name = %s, last_name=%s, email=%s, course=%s, mobile=%s, location=%s where id=%s',
                   (self.first_name_var.get(),
                  self.last_name_var.get(),
                  self.email_var.get(),
                  self.course_var.get(),
                  self.mobile_var.get(),
                  self.location_var.get(),
                   self.roll_no_var.get() 
                  ))
        connection.commit()
        self.clear_data()
        self.fetching_data()
        connection.close()

    def delete_data(self):
        connection = pymysql.connect(host='localhost', user='root', password='nth@9010', db='python8pmproject', port=9010)
        c = connection.cursor()
        c.execute('delete from studentsdata where id=%s', self.roll_no_var.get())
        connection.commit()
        self.fetching_data()
        self.clear_data()
        connection.close()
        

root = Tk()
obj = StudentDetails(root)
root.mainloop()







