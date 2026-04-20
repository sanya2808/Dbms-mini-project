import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import threading
import time
from datetime import datetime

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="Perfume_shop"
)

cur = con.cursor()


# ============================================================================
# PERFUME SHOP MANAGEMENT SYSTEM - Premium Modern Tkinter GUI
# ============================================================================

class PerfumeShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Perfume Shop Management System")
        self.root.geometry("1000x650")
        self.root.resizable(False, False)
        self.root.config(bg="#1a1a2e")

        # Premium Color Scheme
        self.PRIMARY_COLOR = "#1a1a2e"      # Dark navy
        self.SECONDARY_COLOR = "#16213e"    # Darker navy
        self.ACCENT_COLOR = "#d4af37"       # Gold
        self.TEXT_PRIMARY = "#ffffff"       # White
        self.TEXT_SECONDARY = "#e0e0e0"     # Light gray
        self.BUTTON_HOVER = "#2d2d4a"       # Light navy
        self.ROSE_GOLD = "#f0a9a9"          # Rose gold
        self.PANEL_COLOR = "#0f3460"        # Deep navy
        self.SHADOW_COLOR = "#0a0a14"       # Very dark navy
        self.LIGHT_ACCENT = "#e8d5b7"       # Light gold

        self.button_widgets = []  # Track buttons for hover effects
        self.clock_label = None  # For updating clock
        self.is_running = True   # Control thread

        self.create_ui()
        self.start_clock()

    def create_ui(self):
        """Create the main UI layout"""
        # Main container
        main_container = tk.Frame(self.root, bg=self.PRIMARY_COLOR)
        main_container.pack(fill=tk.BOTH, expand=True)

        # ==================== HEADER ====================
        self.create_header(main_container)

        # ==================== BODY CONTAINER ====================
        body_container = tk.Frame(main_container, bg=self.PRIMARY_COLOR)
        body_container.pack(fill=tk.BOTH, expand=True)

        # Left Navigation Panel
        self.create_left_panel(body_container)

        # Main Content Area
        self.create_main_content(body_container)

        # ==================== FOOTER ====================
        self.create_footer(main_container)

    def create_header(self, parent):
        """Create the elegant header section with clock"""
        header_frame = tk.Frame(parent, bg=self.ACCENT_COLOR, height=100)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        header_frame.pack_propagate(False)

        # Inner frame for better styling
        inner_header = tk.Frame(header_frame, bg=self.ACCENT_COLOR)
        inner_header.pack(fill=tk.BOTH, expand=True, padx=20, pady=8)

        # Left side: Perfume bottle logo + Title
        left_side = tk.Frame(inner_header, bg=self.ACCENT_COLOR)
        left_side.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Title with perfume bottle emoji
        title_label = tk.Label(
            left_side,
            text=" PERFUME SHOP MANAGEMENT SYSTEM",
            font=("Poppins", 18, "bold"),
            bg=self.ACCENT_COLOR,
            fg=self.PRIMARY_COLOR
        )
        title_label.pack(pady=6)

        # Subtitle
        subtitle_label = tk.Label(
            left_side,
            text=" Luxury Inventory & Billing Dashboard",
            font=("Segoe UI", 10, "italic"),
            bg=self.ACCENT_COLOR,
            fg=self.PRIMARY_COLOR
        )
        subtitle_label.pack()

        # Right side: Clock
        self.clock_label = tk.Label(
            inner_header,
            text="⏰ --:--:--",
            font=("Poppins", 14, "bold"),
            bg=self.ACCENT_COLOR,
            fg=self.PRIMARY_COLOR,
            padx=15
        )
        self.clock_label.pack(side=tk.RIGHT, fill=tk.Y)

    def create_left_panel(self, parent):
        """Create the left navigation panel"""
        left_panel = tk.Frame(parent, bg=self.SECONDARY_COLOR, width=220)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, padx=0, pady=10)
        left_panel.pack_propagate(False)

        # Panel Title
        panel_title = tk.Label(
            left_panel,
            text="🎯 MENU",
            font=("Segoe UI", 12, "bold"),
            bg=self.SECONDARY_COLOR,
            fg=self.ACCENT_COLOR
        )
        panel_title.pack(pady=15)

        # Separator line
        separator = tk.Frame(left_panel, bg=self.ACCENT_COLOR, height=2)
        separator.pack(fill=tk.X, padx=15, pady=5)

        # Menu buttons data
        menu_items = [
            ("👤 Add Vendor", self.on_add_vendor),
            ("📦 Add Product", self.on_add_product),
            ("💳 Billing", self.on_billing),
            ("📊 View Inventory", self.on_view_inventory),
            ("📈 View Sales", self.on_view_sales),
        ]

        # Create menu buttons with hover effects
        for text, command in menu_items:
            self.create_nav_button(left_panel, text, command)

        # Separator before exit
        separator2 = tk.Frame(left_panel, bg=self.ACCENT_COLOR, height=1)
        separator2.pack(fill=tk.X, padx=15, pady=10)

        # Exit button
        exit_btn = self.create_nav_button(left_panel, "🚪 Exit", self.on_exit)

    def create_nav_button(self, parent, text, command):
        """Create a navigation button with hover effects and modern styling"""
        # Container frame for button with shadow effect
        button_container = tk.Frame(parent, bg=self.SECONDARY_COLOR)
        button_container.pack(fill=tk.X, padx=8, pady=6)

        # Shadow frame
        shadow_frame = tk.Frame(
            button_container, bg=self.SHADOW_COLOR, height=1)
        shadow_frame.pack(fill=tk.X, side=tk.BOTTOM)

        # Actual button frame (creates rounded effect with padding)
        button_frame = tk.Frame(
            button_container, bg=self.PANEL_COLOR, relief=tk.RAISED, bd=1)
        button_frame.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)

        button = tk.Button(
            button_frame,
            text=text,
            command=command,
            font=("Poppins", 11, "bold"),
            bg=self.PANEL_COLOR,
            fg=self.ACCENT_COLOR,
            activebackground=self.BUTTON_HOVER,
            activeforeground=self.ROSE_GOLD,
            bd=0,
            pady=12,
            padx=15,
            cursor="hand2",
            relief=tk.FLAT,
            highlightthickness=0
        )
        button.pack(fill=tk.BOTH, expand=True)

        # Add hover effects with animation
        button.bind("<Enter>", lambda e: self.on_button_enter(
            button, button_frame))
        button.bind("<Leave>", lambda e: self.on_button_leave(
            button, button_frame))

        self.button_widgets.append(button)
        return button

    def on_button_enter(self, button, button_frame):
        """Hover effect - button enter with animation"""
        button.config(bg=self.BUTTON_HOVER, fg=self.ROSE_GOLD)
        button_frame.config(bg=self.BUTTON_HOVER, relief=tk.RAISED, bd=2)

    def on_button_leave(self, button, button_frame):
        """Hover effect - button leave with animation"""
        button.config(bg=self.PANEL_COLOR, fg=self.ACCENT_COLOR)
        button_frame.config(bg=self.PANEL_COLOR, relief=tk.RAISED, bd=1)

    def create_main_content(self, parent):
        """Create the main content area"""
        content_frame = tk.Frame(parent, bg=self.PRIMARY_COLOR)
        content_frame.pack(side=tk.RIGHT, fill=tk.BOTH,
                           expand=True, padx=15, pady=10)

        # Welcome card (main section)
        self.create_welcome_card(content_frame)

        # Info cards section
        self.create_info_cards(content_frame)

    def create_welcome_card(self, parent):
        """Create the main welcome card with premium styling"""
        # Outer shadow frame
        shadow_outer = tk.Frame(parent, bg=self.SHADOW_COLOR)
        shadow_outer.pack(fill=tk.X, pady=10, padx=5)

        # Border frame (gold accent)
        border_frame = tk.Frame(shadow_outer, bg=self.ACCENT_COLOR)
        border_frame.pack(fill=tk.X, padx=0, pady=0)

        # Main card frame
        card_frame = tk.Frame(border_frame, bg=self.PANEL_COLOR)
        card_frame.pack(fill=tk.X, padx=3, pady=3)

        # Welcome icon and text
        welcome_icon = tk.Label(
            card_frame,
            text="🍾✨",
            font=("Arial", 36),
            bg=self.PANEL_COLOR
        )
        welcome_icon.pack(pady=12)

        welcome_text = tk.Label(
            card_frame,
            text="Welcome to Perfume Shop Dashboard",
            font=("Poppins", 16, "bold"),
            bg=self.PANEL_COLOR,
            fg=self.ACCENT_COLOR
        )
        welcome_text.pack(pady=5)

        welcome_desc = tk.Label(
            card_frame,
            text="Manage your luxury perfume inventory, vendors, and sales efficiently",
            font=("Segoe UI", 9),
            bg=self.PANEL_COLOR,
            fg=self.TEXT_SECONDARY
        )
        welcome_desc.pack(pady=5, padx=20)

        welcome_footer = tk.Label(
            card_frame,
            text="Select an option from the menu to get started",
            font=("Poppins", 8, "italic"),
            bg=self.PANEL_COLOR,
            fg=self.LIGHT_ACCENT
        )
        welcome_footer.pack(pady=10, padx=20)

    def create_info_cards(self, parent):
        """Create clickable information cards section"""

        cards_container = tk.Frame(parent, bg=self.PRIMARY_COLOR)
        cards_container.pack(fill=tk.BOTH, expand=True, pady=10)

        cards = [
            ("📦", "Inventory", "Manage products & stock", self.on_view_inventory),
            ("💰", "Billing", "Process transactions", self.on_billing),
            ("👥", "Vendors", "Manage suppliers", self.on_add_vendor)
        ]

        for icon, title, description, command in cards:
            self.create_info_card(
                cards_container,
                icon,
                title,
                description,
                command
            )

    def create_info_card(self, parent, icon, title, description, command):
        """Create a single info card with premium styling"""
        # Shadow container
        shadow_container = tk.Frame(parent, bg=self.SHADOW_COLOR)
        shadow_container.pack(side=tk.LEFT, fill=tk.BOTH,
                              expand=True, padx=5, pady=5)

        # Gold border frame
        border_frame = tk.Frame(shadow_container, bg=self.ACCENT_COLOR)
        border_frame.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)

        # Main card frame
        card_inner = tk.Frame(border_frame, bg=self.PANEL_COLOR)
        card_inner.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)

        # Icon
        icon_label = tk.Label(
            card_inner,
            text=icon,
            font=("Arial", 28),
            bg=self.PANEL_COLOR
        )
        icon_label.pack(pady=10)

        # Title
        title_label = tk.Label(
            card_inner,
            text=title,
            font=("Poppins", 11, "bold"),
            bg=self.PANEL_COLOR,
            fg=self.ACCENT_COLOR
        )
        title_label.pack()

        # Description
        desc_label = tk.Label(
            card_inner,
            text=description,
            font=("Segoe UI", 8),
            bg=self.PANEL_COLOR,
            fg=self.TEXT_SECONDARY,
            wraplength=100,
            justify=tk.CENTER
        )
        card_inner.bind("<Button-1>", lambda e: command())
        card_inner.config(cursor="hand2")
        icon_label.bind("<Button-1>", lambda e: command())
        title_label.bind("<Button-1>", lambda e: command())
        desc_label.bind("<Button-1>", lambda e: command())
        desc_label.pack(pady=8, padx=8)

    def create_footer(self, parent):
        """Create the footer section with premium styling"""
        # Separator line
        separator = tk.Frame(parent, bg=self.ACCENT_COLOR, height=2)
        separator.pack(fill=tk.X, padx=0, pady=0)

        footer_frame = tk.Frame(parent, bg=self.SECONDARY_COLOR, height=40)
        footer_frame.pack(fill=tk.X, padx=0, pady=0)
        footer_frame.pack_propagate(False)

        footer_label = tk.Label(
            footer_frame,
            text=" System Ready | Python + Tkinter | Premium Edition ",
            font=("Poppins", 9),
            bg=self.SECONDARY_COLOR,
            fg=self.ACCENT_COLOR
        )
        footer_label.pack(pady=10)

    # ==================== UTILITY METHODS ====================

    def start_clock(self):
        """Start the real-time clock update"""
        def update_clock():
            while self.is_running:
                try:
                    current_time = datetime.now().strftime("%H:%M:%S")
                    if self.clock_label:
                        self.clock_label.config(text=f"⏰ {current_time}")
                    time.sleep(1)
                except:
                    pass

        clock_thread = threading.Thread(target=update_clock, daemon=True)
        clock_thread.start()

    # ==================== BUTTON CALLBACKS ====================

    def on_add_vendor(self):
        win = tk.Toplevel(self.root)
        win.title("Add Vendor")
        win.geometry("500x500")
        win.config(bg=self.PRIMARY_COLOR)

        tk.Label(
            win,
            text="👤 Add Vendor",
            font=("Arial", 16, "bold"),
            bg=self.PRIMARY_COLOR,
            fg=self.ACCENT_COLOR
        ).pack(pady=15)

        tk.Label(win, text="Vendor Name",
                 bg=self.PRIMARY_COLOR, fg="white").pack()
        vname = tk.Entry(win, width=30)
        vname.pack(pady=5)

        tk.Label(win, text="Phone", bg=self.PRIMARY_COLOR, fg="white").pack()
        phone = tk.Entry(win, width=30)
        phone.pack(pady=5)

        tk.Label(win, text="City", bg=self.PRIMARY_COLOR, fg="white").pack()
        city = tk.Entry(win, width=30)
        city.pack(pady=5)

        tk.Label(win, text="Material Supplied",
                 bg=self.PRIMARY_COLOR, fg="white").pack()
        material = tk.Entry(win, width=30)
        material.pack(pady=5)

        def save_vendor():
            try:
                sql = """
                INSERT INTO vendors(vendor_name, phone, city, material_supplied)
                VALUES(%s,%s,%s,%s)
                """

                val = (
                    vname.get(),
                    phone.get(),
                    city.get(),
                    material.get()
                )

                cur.execute(sql, val)
                con.commit()

                messagebox.showinfo("Success", "Vendor Added Successfully")

                vname.delete(0, tk.END)
                phone.delete(0, tk.END)
                city.delete(0, tk.END)
                material.delete(0, tk.END)

            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(
            win,
            text="Save Vendor",
            command=save_vendor,
            bg=self.ACCENT_COLOR,
            fg="black",
            width=20
        ).pack(pady=20)

    def on_add_product(self):
        win = tk.Toplevel(self.root)
        win.title("Add Product")
        win.geometry("500x500")
        win.config(bg=self.PRIMARY_COLOR)

        title = tk.Label(
            win,
            text="📦 Add New Perfume Product",
            font=("Poppins", 16, "bold"),
            bg=self.PRIMARY_COLOR,
            fg=self.ACCENT_COLOR
        )
        title.pack(pady=15)

        # Labels + Entries
        tk.Label(win, text="Perfume Name", bg=self.PRIMARY_COLOR,
                 fg="white").pack()
        name = tk.Entry(win, width=30, font=("Segoe UI", 11))
        name.pack(pady=5)

        # Brand container
        brand_frame = tk.Frame(win, bg=self.PRIMARY_COLOR)
        brand_frame.pack(pady=5)

        tk.Label(
            brand_frame,
            text="Brand",
            bg=self.PRIMARY_COLOR,
            fg="white"
        ).pack()

        brand_entry = tk.Entry(
            brand_frame,
            width=30,
            font=("Segoe UI", 11)
        )
        brand_entry.pack(pady=5)

        listbox = tk.Listbox(
            brand_frame,
            width=30,
            height=4,
            font=("Segoe UI", 10)
        )

        # Fetch brands
        cur.execute("SELECT DISTINCT brand FROM inventory")
        brands = [row[0] for row in cur.fetchall()]

        def update_list(event):
            typed = brand_entry.get().lower()

            if typed == "":
                listbox.pack_forget()
                return

            data = [b for b in brands if typed in b.lower()]

            if data:
                listbox.delete(0, tk.END)

                for item in data:
                    listbox.insert(tk.END, item)

                listbox.pack()
            else:
                listbox.pack_forget()

        def select_item(event):
            if listbox.curselection():
                selected = listbox.get(listbox.curselection())

                brand_entry.delete(0, tk.END)
                brand_entry.insert(0, selected)

                listbox.pack_forget()

        brand_entry.bind("<KeyRelease>", update_list)
        listbox.bind("<<ListboxSelect>>", select_item)

        tk.Label(win, text="Price", bg=self.PRIMARY_COLOR,
                 fg="white").pack()
        price = tk.Entry(win, width=30, font=("Segoe UI", 11))
        price.pack(pady=5)

        tk.Label(win, text="Quantity", bg=self.PRIMARY_COLOR,
                 fg="white").pack()
        qty = tk.Entry(win, width=30, font=("Segoe UI", 11))
        qty.pack(pady=5)

        def save_product():
            try:
                sql = """
            INSERT INTO inventory(perfume_name, brand, price, quantity)
            VALUES (%s,%s,%s,%s)
            """

                val = (
                    name.get(),
                    brand_entry.get(),
                    int(price.get()),
                    int(qty.get())
                )

                cur.execute(sql, val)
                con.commit()

                messagebox.showinfo("Success", "Product Added Successfully")

                name.delete(0, tk.END)
                brand_entry.delete(0, tk.END)
                price.delete(0, tk.END)
                qty.delete(0, tk.END)

            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(
            win,
            text="💾 Save Product",
            command=save_product,
            bg=self.ACCENT_COLOR,
            fg="black",
            font=("Poppins", 11, "bold"),
            width=20
        ).pack(pady=20)

    def on_billing(self):
        win = tk.Toplevel(self.root)
        win.title("Billing")
        win.geometry("500x550")
        win.config(bg=self.PRIMARY_COLOR)

        tk.Label(
            win,
            text="💳 Generate Bill",
            font=("Arial", 16, "bold"),
            bg=self.PRIMARY_COLOR,
            fg=self.ACCENT_COLOR
        ).pack(pady=15)

        tk.Label(win, text="Customer Name",
                 bg=self.PRIMARY_COLOR, fg="white").pack()
        cname = tk.Entry(win, width=30)
        cname.pack(pady=5)

        tk.Label(
            win,
            text="Product Name",
            bg=self.PRIMARY_COLOR,
            fg="white"
        ).pack()
        # Fetch products from inventory
        cur.execute("SELECT perfume_name FROM inventory")
        products = [row[0] for row in cur.fetchall()]

        pname = ttk.Combobox(
            win,
            values=products,
            width=27,
            state="readonly"
        )
        pname.pack(pady=5)

        tk.Label(win, text="Quantity", bg=self.PRIMARY_COLOR, fg="white").pack()
        qty = tk.Entry(win, width=30)
        qty.pack(pady=5)

        def generate_bill():
            try:
                product = pname.get()
                quantity = int(qty.get())

                cur.execute(
                    "SELECT price, quantity FROM inventory WHERE perfume_name=%s",
                    (product,)
                )

                row = cur.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Product not found")
                    return

                price = row[0]
                stock = row[1]

                if quantity > stock:
                    messagebox.showerror("Error", "Insufficient Stock")
                    return

                total = price * quantity

                cur.execute("""
                    INSERT INTO sales(customer_name, product_name, qty, price, total)
                    VALUES(%s,%s,%s,%s,%s)
                """, (cname.get(), product, quantity, price, total))

                cur.execute("""
                    UPDATE inventory
                    SET quantity = quantity - %s
                    WHERE perfume_name=%s
                    """, (quantity, product))

                con.commit()

                bill_win = tk.Toplevel(self.root)
                bill_win.title("Invoice")
                bill_win.geometry("350x400")
                bill_win.config(bg="white")
                bill_text = f"""
                        PERFUME SHOP
                --------------------------------
                Customer : {cname.get()}
                Product  : {product}
                Quantity : {quantity}
                Price    : ₹{price}
                --------------------------------
                TOTAL    : ₹{total}
                --------------------------------
                Date     : {datetime.now().strftime("%d-%m-%Y")}
                --------------------------------
                Thank You!
                """
                tk.Label(
                    bill_win,
                    text=bill_text,
                    justify="left",
                    font=("Courier", 11),
                    bg="white",
                    fg="black"
                ).pack(pady=20)

            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(
            win,
            text="Generate Bill",
            command=generate_bill,
            bg=self.ACCENT_COLOR,
            fg="black",
            width=20
        ).pack(pady=20)

        tk.Button(
            bill_win,
            text="Print (Demo)",
            bg="#d4af37"
        ).pack(pady=10)

    def on_view_inventory(self):
        win = tk.Toplevel(self.root)
        win.title("Inventory Dashboard")
        win.geometry("950x580")
        win.config(bg="#1a1a2e")

        # ---------------- TITLE ----------------
        tk.Label(
            win,
            text="📊 Perfume Inventory",
            font=("Poppins", 16, "bold"),
            bg="#1a1a2e",
            fg="#d4af37"
        ).pack(pady=10)

        # ---------------- SEARCH BAR ----------------
        search_frame = tk.Frame(win, bg="#1a1a2e")
        search_frame.pack(pady=5)

        tk.Label(
            search_frame,
            text="Search:",
            bg="#1a1a2e",
            fg="white",
            font=("Arial", 11, "bold")
        ).pack(side=tk.LEFT, padx=5)

        search_entry = tk.Entry(search_frame, width=25)
        search_entry.pack(side=tk.LEFT, padx=5)

        # ---------------- TABLE ----------------
        tree = ttk.Treeview(
            win,
            columns=("ID", "Name", "Brand", "Price", "Qty"),
            show="headings",
            height=20
        )

        tree.heading("ID", text="ID")
        tree.heading("Name", text="Perfume Name")
        tree.heading("Brand", text="Brand")
        tree.heading("Price", text="Price")
        tree.heading("Qty", text="Quantity")

        tree.column("ID", width=60)
        tree.column("Name", width=260)
        tree.column("Brand", width=180)
        tree.column("Price", width=120)
        tree.column("Qty", width=120)

        tree.pack(pady=10)

        # Low stock style
        tree.tag_configure("low", background="red", foreground="white")

        # ---------------- FUNCTIONS ----------------
        def load_data(rows):
            tree.delete(*tree.get_children())

            for row in rows:
                if row[4] < 5:
                    tree.insert("", tk.END, values=row, tags=("low",))
                else:
                    tree.insert("", tk.END, values=row)

        def show_all():
            cur.execute("SELECT * FROM inventory")
            rows = cur.fetchall()
            load_data(rows)

        def search_product():
            text = search_entry.get()

            cur.execute("""
                SELECT * FROM inventory
                WHERE perfume_name LIKE %s
                OR brand LIKE %s
            """, ('%' + text + '%', '%' + text + '%'))

            rows = cur.fetchall()
            load_data(rows)

        def delete_product():
            selected = tree.selection()

            if not selected:
                messagebox.showwarning(
                    "Warning",
                    "Please select a product to delete"
                )
                return

            item = tree.item(selected[0])
            values = item["values"]
            product_id = values[0]

            confirm = messagebox.askyesno(
                "Confirm Delete",
                "Are you sure you want to delete this product?"
            )

            if confirm:
                cur.execute(
                    "DELETE FROM inventory WHERE product_id=%s",
                    (product_id,)
                )
                con.commit()

                messagebox.showinfo(
                    "Deleted",
                    "Product deleted successfully"
                )

                show_all()

        def update_product():
            selected = tree.selection()

            if not selected:
                messagebox.showwarning(
                    "Warning",
                    "Please select a product"
                )
                return

            item = tree.item(selected[0])
            values = item["values"]
            product_id = values[0]

            # ---------- Edit Window ----------
            edit = tk.Toplevel(win)
            edit.title("Update Product")
            edit.geometry("420x430")
            edit.config(bg="#1a1a2e")

            tk.Label(
                edit,
                text="✏ Update Product",
                font=("Arial", 16, "bold"),
                bg="#1a1a2e",
                fg="#d4af37"
            ).pack(pady=10)

            tk.Label(edit, text="Perfume Name",
                     bg="#1a1a2e", fg="white").pack()
            name = tk.Entry(edit, width=30)
            name.pack(pady=5)
            name.insert(0, values[1])

            tk.Label(edit, text="Brand",
                     bg="#1a1a2e", fg="white").pack()
            brand = tk.Entry(edit, width=30)
            brand.pack(pady=5)
            brand.insert(0, values[2])

            tk.Label(edit, text="Price",
                     bg="#1a1a2e", fg="white").pack()
            price = tk.Entry(edit, width=30)
            price.pack(pady=5)
            price.insert(0, values[3])

            tk.Label(edit, text="Quantity",
                     bg="#1a1a2e", fg="white").pack()
            qty = tk.Entry(edit, width=30)
            qty.pack(pady=5)
            qty.insert(0, values[4])

            def save_changes():
                cur.execute("""
                    UPDATE inventory
                    SET perfume_name=%s,
                        brand=%s,
                        price=%s,
                        quantity=%s
                    WHERE product_id=%s
                """, (
                    name.get(),
                    brand.get(),
                    price.get(),
                    qty.get(),
                    product_id
                ))

                con.commit()

                messagebox.showinfo(
                    "Success",
                    "Product updated successfully"
                )

                edit.destroy()
                win.destroy()
                self.on_view_inventory()

            tk.Button(
                edit,
                text="💾 Save Changes",
                command=save_changes,
                bg="#d4af37",
                fg="black",
                width=18
            ).pack(pady=20)

        # ---------------- BUTTONS ----------------
        tk.Button(
            search_frame,
            text="Search",
            command=search_product,
            bg="#d4af37",
            fg="black",
            width=10
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            search_frame,
            text="Show All",
            command=show_all,
            bg="white",
            fg="black",
            width=10
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            search_frame,
            text="Delete Selected",
            command=delete_product,
            bg="red",
            fg="white",
            width=15
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            search_frame,
            text="Update Selected",
            command=update_product,
            bg="blue",
            fg="white",
            width=15
        ).pack(side=tk.LEFT, padx=5)

        # Load data first time
        show_all()

    def on_view_sales(self):
        win = tk.Toplevel(self.root)
        win.title("Sales Report")
        win.geometry("950x500")
        win.config(bg=self.PRIMARY_COLOR)

        tk.Label(
            win,
            text="📈 Sales Report",
            font=("Arial", 16, "bold"),
            bg=self.PRIMARY_COLOR,
            fg=self.ACCENT_COLOR
        ).pack(pady=10)

        tree = ttk.Treeview(
            win,
            columns=("ID", "Customer", "Product",
                     "Qty", "Price", "Total", "Date"),
            show="headings",
            height=18
        )

        tree.heading("ID", text="Bill ID")
        tree.heading("Customer", text="Customer Name")
        tree.heading("Product", text="Product Name")
        tree.heading("Qty", text="Qty")
        tree.heading("Price", text="Price")
        tree.heading("Total", text="Total")
        tree.heading("Date", text="Bill Date")

        tree.column("ID", width=70)
        tree.column("Customer", width=150)
        tree.column("Product", width=180)
        tree.column("Qty", width=70)
        tree.column("Price", width=100)
        tree.column("Total", width=100)
        tree.column("Date", width=180)

        tree.pack(pady=15)

        cur.execute("select * from sales")
        rows = cur.fetchall()

        for row in rows:
            tree.insert("", tk.END, values=row)

    def on_exit(self):
        """Handle Exit button click"""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.is_running = False
            self.root.destroy()


class LoginPage:

    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("500x420")
        self.root.config(bg="#1a1a2e")

        tk.Label(
            root,
            text="🔐 Perfume Shop Login",
            font=("Poppins", 18, "bold"),
            bg="#1a1a2e",
            fg="#d4af37"
        ).pack(pady=30)

        tk.Label(
            root,
            text="Username",
            bg="#1a1a2e",
            fg="white"
        ).pack()

        self.username = tk.Entry(root, width=30)
        self.username.pack(pady=10)

        tk.Label(
            root,
            text="Password",
            bg="#1a1a2e",
            fg="white"
        ).pack()

        self.password = tk.Entry(root, width=30, show="*")
        self.password.pack(pady=10)

        tk.Button(
            root,
            text="Login",
            command=self.check_login,
            bg="#d4af37",
            fg="black",
            width=18,
            font=("Poppins", 11, "bold")
        ).pack(pady=25)

    def check_login(self):

        user = self.username.get()
        pwd = self.password.get()

        if user == "admin" and pwd == "1234":

            for widget in self.root.winfo_children():
                widget.destroy()

            PerfumeShopApp(self.root)

        else:
            messagebox.showerror(
                "Login Failed",
                "Invalid Username or Password"
            )
# ============================================================================
# MAIN APPLICATION
# ============================================================================


if __name__ == "__main__":
    root = tk.Tk()
    LoginPage(root)
    root.mainloop()
