from tkinter import*
from tkinter import messagebox
import math, random, os
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #========All Variables===========
        # Here we define all the variables either they are integere or strings
        #========Cosmetics================= 
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gel = IntVar()
        self.lotion = IntVar()

        #========Grocery==================
        self.rice = IntVar()
        self.sugar = IntVar()
        self.flour = IntVar()
        self.salt = IntVar()
        self.tea = IntVar()
        self.c_oil = IntVar()

        #========ColdDrinks================
        self.b_app = IntVar()
        self.stings = IntVar()
        self.sprite = IntVar()
        self.coca = IntVar()
        self.fanta = IntVar()
        self.pepsi = IntVar()

        #========Total Product Price======
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        #========Tax Variable======
        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        #========Customer==========
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()


        #========Customer Details==============
        F1 = LabelFrame(self.root, text="Customer Details", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname_label = Label(F1, text="Customer Name", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15,textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=5)

        cphn_label = Label(F1, text="Phone No.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=5)

        c_bill_label = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, padx=10, pady=5)

        bill_btn = Button(F1, text="Search", command = self.find_bill, width=10, bd=7, font="arial 12 bold").grid(row=0, column=6, padx=10, pady=10)
 

        #========Cosmetics Frame==============
        F2 = LabelFrame(self.root, text="Cosmetics", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F2.place(x=5, y=180, width=325, height=380)

        b1_label = Label(F2, text="Bath Soap", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        b1_text = Entry(F2, width=10, textvariable=self.soap, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        b2_label = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        b2_text = Entry(F2, width=10, textvariable=self.face_cream, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        b3_label = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        b3_text = Entry(F2, width=10, textvariable=self.face_wash, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        b4_label = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        b4_text = Entry(F2, width=10, textvariable=self.spray, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        b5_label = Label(F2, text="Hair Gel", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        b5_text = Entry(F2, width=10, textvariable=self.gel, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=0, pady=10)

        b6_label = Label(F2, text="Body Lotion", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        b6_text = Entry(F2, width=10, textvariable=self.lotion, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        #========Grocery Frame==============
        F3 = LabelFrame(self.root, text="Grocery", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        g1_label = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        g1_text = Entry(F3, width=10, textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        g2_label = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_text = Entry(F3, width=10, textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        g3_label = Label(F3, text="Flour", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_text = Entry(F3, width=10, textvariable=self.flour, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        g4_label = Label(F3, text="Salt", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4_text = Entry(F3, width=10, textvariable=self.salt, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        g5_label = Label(F3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g5_text = Entry(F3, width=10, textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=0, pady=10)

        g6_label = Label(F3, text="Cooking Oil", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6_text = Entry(F3, width=10, textvariable=self.c_oil, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)


        #========Cold Drinks Frame==============
        F4 = LabelFrame(self.root, text="Cold Drinks", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F4.place(x=675, y=180, width=325, height=380)

        cd1_label = Label(F4, text="Big Apple", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        cd1_text = Entry(F4, width=10, textvariable=self.b_app, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        cd2_label = Label(F4, text="Stings", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        cd2_text = Entry(F4, width=10, textvariable=self.stings, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        cd3_label = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        cd3_text = Entry(F4, width=10, textvariable=self.sprite, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        cd4_label = Label(F4, text="Coca Cola", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        cd4_text = Entry(F4, width=10, textvariable=self.coca, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        cd5_label = Label(F4, text="Fanta", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        cd5_text = Entry(F4, width=10, textvariable=self.fanta, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=0, pady=10)

        cd6_label = Label(F4, text="Pepsi", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        cd6_text = Entry(F4, width=10, textvariable=self.pepsi, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        #===================Bill Area=====================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)
        bill_title = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        #===================Button Frame=====================
        F6 = LabelFrame(self.root, text="Bill Menu", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1 = Label(F6, text="Total Cosmetics Price", font=("times new roman", 14, "bold"), bg=bg_color, fg="white").grid(row=0, column=0, padx=20, pady=1, sticky="w")
        m1_text = Entry(F6, width=18, textvariable=self.cosmetic_price, font="arial 10 bold", bd=7, relief=GROOVE).grid(row=0, column=1, padx=10, pady=1)

        m2 = Label(F6, text="Total Grocery Price", font=("times new roman", 14, "bold"), bg=bg_color, fg="white").grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_text = Entry(F6, width=18, textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=GROOVE).grid(row=1, column=1, padx=10, pady=1)

        m3 = Label(F6, text="Total Cold Drinks Price", font=("times new roman", 14, "bold"), bg=bg_color, fg="white").grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_text = Entry(F6, width=18, textvariable=self.cold_drink_price, font="arial 10 bold", bd=7, relief=GROOVE).grid(row=2, column=1, padx=10, pady=1)

        c1 = Label(F6, text="Cosmetics Tax", font=("times new roman", 14, "bold"), bg=bg_color, fg="white").grid(row=0, column=2, padx=20, pady=1, sticky="w")
        c1_text = Entry(F6, width=18, textvariable=self.cosmetic_tax, font="arial 10 bold", bd=7, relief=GROOVE).grid(row=0, column=3, padx=10, pady=1)

        c2 = Label(F6, text="Grocery Tax", font=("times new roman", 14, "bold"), bg=bg_color, fg="white").grid(row=1, column=2, padx=20, pady=1, sticky="w")
        c2_text = Entry(F6, width=18, textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=GROOVE).grid(row=1, column=3, padx=10, pady=1)

        c3 = Label(F6, text="Cold Drinks Tax", font=("times new roman", 14, "bold"), bg=bg_color, fg="white").grid(row=2, column=2, padx=20, pady=1, sticky="w")
        c3_text = Entry(F6, width=18, textvariable=self.cold_drink_tax, font="arial 10 bold", bd=7, relief=GROOVE).grid(row=2, column=3, padx=10, pady=1)

        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=750, width=580, height=105)

        total = Button(btn_f, command=self.total, text="Total", bd = 2, bg="cadetblue", fg="white", pady=15, width=9, font="arial 14 bold").grid(row=0, column=0, padx=5, pady=5)
        gbill = Button(btn_f, text="Generate Bill", command = self.bill_area, bd = 2, bg="cadetblue", fg="white", pady=15, width=11, font="arial 14 bold").grid(row=0, column=1, padx=5, pady=5)
        clear = Button(btn_f, text="Clear",command=self.clear_data, bd = 2, bg="cadetblue", fg="white", pady=15, width=9, font="arial 14 bold").grid(row=0, column=2, padx=5, pady=5)
        exit = Button(btn_f, command = self.Exit_app, text="Exit", bd = 2, bg="cadetblue", fg="white", pady=15, width=9, font="arial 14 bold").grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

    def total(self):

        self.c_s_p = self.soap.get() * 40
        self.c_fc_p = self.face_cream.get() * 120
        self.c_fw_p = self.face_wash.get() * 60
        self.c_hs_p = self.spray.get() * 180
        self.c_hg_p = self.gel.get() * 140
        self.c_bl_p = self.lotion.get() * 180

        self.total_cosmetic_price = float(
                                            self.c_s_p +
                                            self.c_fc_p +
                                            self.c_fw_p +
                                            self.c_hs_p +
                                            self.c_hg_p +
                                            self.c_bl_p
                                            )
        self.cosmetic_price.set("Rs. " + str(self.total_cosmetic_price))
        self.c_tax = round((self.total_cosmetic_price * 0.05), 2)
        self.cosmetic_tax.set("Rs. " + str(self.c_tax))


        self.g_r_p = self.rice.get() * 380
        self.g_s_p = self.sugar.get() * 100
        self.g_f_p = self.flour.get() * 200
        self.g_sl_p = self.salt.get() * 60
        self.g_t_p = self.tea.get() * 500
        self.g_o_p = self.c_oil.get() * 550

        self.total_grocery_price = float(
                                            self.g_r_p +
                                            self.g_s_p +
                                            self.g_f_p +
                                            self.g_sl_p +
                                            self.g_t_p +
                                            self.g_o_p
                                            )
        
        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price * 0.1), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        
        self.d_ba_p = self.b_app.get() * 90
        self.d_st_p = self.stings.get() * 100
        self.d_co_p = self.coca.get() * 60
        self.d_sp_p = self.sprite.get() * 60
        self.d_f_p = self.fanta.get() * 60
        self.d_p_p = self.pepsi.get() * 60
        
        self.total_cold_drink_price = float(
                                            self.d_ba_p +
                                            self.d_st_p +
                                            self.d_co_p +
                                            self.d_sp_p +
                                            self.d_f_p +
                                            self.d_p_p
                                            )
        self.cold_drink_price.set("Rs. " + str(self.total_cold_drink_price))
        self.d_tax = round((self.total_cold_drink_price * 0.05), 2)
        self.cold_drink_tax.set("Rs. " + str(self.d_tax))
        
        self.Total_bill = float(
            self.total_cosmetic_price +
            self.total_grocery_price +
            self.total_cold_drink_price +
            self.c_tax +
            self.g_tax +
            self.d_tax
            )
    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome DIK Enterprises")
        self.txtarea.insert(END, f"\n Bill Number: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number: {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n======================================")
        self.txtarea.insert(END, f"\nProducts\t\tQTY\t\tPrice")
        self.txtarea.insert(END, f"\n======================================")

    def bill_area(self):
        if self.c_name.get() == " " and self.c_phone.get() == " ":
            messagebox.showerror("Error", "Customer Details Are Must")
        elif self.cosmetic_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drink_price.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
            #===cosmetics===
            if self.soap.get() != 0:
                self.txtarea.insert(END, f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get() != 0:
                self.txtarea.insert(END, f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get() != 0:
                self.txtarea.insert(END, f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.spray.get() != 0:
                self.txtarea.insert(END, f"\n Hair Spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")
            if self.gel.get() != 0:
                self.txtarea.insert(END, f"\n Hair Gel\t\t{self.gel.get()}\t\t{self.c_hg_p}")
            if self.lotion.get() != 0:
                self.txtarea.insert(END, f"\n Body Lotion\t\t{self.lotion.get()}\t\t{self.c_bl_p}")

            #===Grocery===
            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.flour.get() != 0:
                self.txtarea.insert(END, f"\n Flour\t\t{self.flour.get()}\t\t{self.g_f_p}")
            if self.salt.get() != 0:
                self.txtarea.insert(END, f"\n Salt\t\t{self.salt.get()}\t\t{self.g_sl_p}")
            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")
            if self.c_oil.get() != 0:
                self.txtarea.insert(END, f"\n Oil\t\t{self.c_oil.get()}\t\t{self.g_o_p}")

            #===Cold Drinks===
            if self.b_app.get() != 0:
                self.txtarea.insert(END, f"\n Badam\t\t{self.b_app.get()}\t\t{self.d_ba_p}")
            if self.stings.get() != 0:
                self.txtarea.insert(END, f"\n Stings\t\t{self.stings.get()}\t\t{self.d_st_p}")
            if self.coca.get() != 0:
                self.txtarea.insert(END, f"\n Cocacola\t\t{self.coca.get()}\t\t{self.d_co_p}")
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_sp_p}")
            if self.fanta.get() != 0:
                self.txtarea.insert(END, f"\n Fanta\t\t{self.fanta.get()}\t\t{self.d_f_p}")
            if self.pepsi.get() != 0:
                self.txtarea.insert(END, f"\n Pepsi\t\t{self.pepsi.get()}\t\t{self.d_p_p}")


            self.txtarea.insert(END, f"\n--------------------------------------")
            if self.cosmetic_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Cosmetic Tax\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Grocery Tax\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Cold Drink Tax\t\t{self.cold_drink_tax.get()}")

            self.txtarea.insert(END, f"\n Total Bill\t\tRs. {str(self.Total_bill)}")
            self.txtarea.insert(END, f"\n--------------------------------------")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/" + str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no. : {self.bill_no.get()} Saved Successfully")
        else:
            return
        
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete("1.0", END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            #===Cosmetics===
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gel.set(0)
            self.lotion.set(0)

            #===Grocery===
            self.rice.set(0)
            self.sugar.set(0)
            self.flour.set(0)
            self.salt.set(0)
            self.tea.set(0)
            self.c_oil.set(0)

            #===ColdDrinks===
            self.b_app.set(0)
            self.stings.set(0)
            self.sprite.set(0)
            self.coca.set(0)
            self.fanta.set(0)
            self.pepsi.set(0)

           #========Total Product Price======
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            #========Tax Variable======
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            #========Customer==========
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to Exit?")
        if op > 0:
            self.root.destroy()

root = Tk()
obj = Bill_App(root)
root.mainloop()

