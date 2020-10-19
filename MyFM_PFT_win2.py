#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Dependencies:
# for Debian, Ubuntu
# sudo apt install python3-tk python3-magic python3-pil python3-pil.imagetk
# for OpenSuse:
# sudo zypper install python3-tk python3-magic python3-Pillow python3-Pillow-tk

import os
import time
from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox
import subprocess
from PIL import Image, ImageTk
# import imghdr
import magic
import sys

w = 710
h = 470
w_tab_image = 20
w_tab_ext = 79
w_tab_size = 79
w_tab_mtime = 150
w_tab_atime = 150
w_tab_name = w-(w_tab_image+w_tab_ext+w_tab_size+w_tab_mtime+w_tab_atime)-33
date_time = '%Y.%m.%d %H:%M:%S'
key_sort_by = 'name'
key_sort_invers = 0
key_hide_files_hidden = 1
str_folder_up = '. . .'
start_switch = '#'

background_dirs = '#cccccc'
background_txt = '#ccffff'
background_with = '#ffffff'
background_media = '#ccccff'
background_image = '#ffccff'

# file_config = '.myfm_pft_config.txt'
# if os.path.exists('/home/divik/1_MyPO'):
#     file_config = os.path.join('/home/divik/1_MyPO', file_config)


def PrintMyName():
    print('My details:')
    print('divik')
    print('diviks2008@yandex.ru')


def CenteredWindow(root):
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = int((sw - w) / 2)
    y = int((sh - h) / 2)
    return w, h, x, y


class App():
    def __init__(self, master):
        self.master = master
        self.folder_rab = os.getcwd()
        self.key_hide_files_hidden = key_hide_files_hidden
        self.key_sort_by = key_sort_by
        self.key_sort_invers = key_sort_invers

        frame01 = Frame(master)
        frame01.pack(side=LEFT, fill=Y, expand=1)
        self.text = Text(master)
        self.text.pack(side=LEFT, fill=BOTH, expand=1)

        frame1 = LabelFrame(frame01, height=17)  # , bg='Yellow')#, text='path to file')
        frame1.pack(padx=5, pady=5, side=TOP, fill=X)
        frame2 = LabelFrame(frame01)  # , bg='Blue')
        frame2.pack(padx=5, side=TOP, fill=BOTH, expand=1)  # , anchor=NW)
        frame3 = Frame(frame01, height=17)  # , bg='Green')
        frame3.pack(padx=5, pady=5, side=TOP, fill=X)

        # self.get_default_setup()
        self.frame2 = frame2

        l_frame1 = Label(frame1, text='Folder:')
        l_frame1.pack(padx=5, side=LEFT)

        self.e_frame1 = Entry(frame1)
        self.e_frame1.pack(padx=5, side=LEFT, fill=X, expand=1)
        self.e_frame1.insert(END, self.folder_rab)

        self.b_frame1 = Button(frame1, text='UP', command=self.folder_up)
        self.b_frame1.pack(padx=5, side=LEFT)

        # self.lb_frame2 = Listbox(frame2)
        # self.lb_frame2.pack(side=LEFT, fill=BOTH, expand=1)

        self.l_frame3 = Label(frame3)
        self.l_frame3.pack(padx=5, side=LEFT, fill=X, expand=1, anchor=W)
        self.l_frame4 = Label(frame3)
        self.l_frame4.pack(padx=5, side=LEFT, fill=X, expand=1, anchor=W)

        self.tree = ttk.Treeview(frame2, selectmode=BROWSE)
        # self.tree = ttk.Treeview(frame2)
        self.style = ttk.Style()
        self.style.map('Treeview', foreground=self.fixed_map('foreground'),
                       background=self.fixed_map('background'), tagname=self.fixed_map('tagname'))

        vsb_y = ttk.Scrollbar(frame2, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb_y.set)
        vsb_x = ttk.Scrollbar(frame2, orient=HORIZONTAL, command=self.tree.xview)
        self.tree.configure(xscrollcommand=vsb_x.set)

        vsb_x.pack(side=BOTTOM, fill=X)
        vsb_y.pack(side=RIGHT, fill=Y)
        self.tree.pack(side=LEFT, fill=BOTH, expand=1)

        self.tree['columns'] = ('Name', 'Ext', 'Size', 'mtime', 'atime')
        self.tree.column('#0', width=w_tab_image, minwidth=w_tab_image)
        self.tree.column('Name', width=w_tab_name, minwidth=w_tab_name)  # , stretch=NO)
        self.tree.column('Ext', width=w_tab_ext, minwidth=w_tab_ext)
        self.tree.column('Size', width=w_tab_size, minwidth=w_tab_size)
        self.tree.column('mtime', width=w_tab_mtime, minwidth=w_tab_mtime)
        self.tree.column('atime', width=w_tab_atime, minwidth=w_tab_atime)
        # self.tree.heading('#0', text='', anchor='center', command=self.sort_column_by_image)
        self.tree.heading('Name', text='Name', anchor='center', command=self.sort_column_by_name)
        self.tree.heading('Ext', text='Ext', anchor='center', command=self.sort_column_by_ext)
        self.tree.heading('Size', text='Size', anchor='center', command=self.sort_column_by_size)
        self.tree.heading('mtime', text='Date modified', anchor='center', command=self.sort_column_by_mtime)
        self.tree.heading('atime', text='Date access', anchor='center', command=self.sort_column_by_atime)

        self.insert_in_tree()

    def fixed_map(self, option):
        # Fix for setting text colour for Tkinter 8.6.9
        # From: https://core.tcl.tk/tk/info/509cafafae
        #
        # Returns the style map for 'option' with any styles starting with
        # ('!disabled', '!selected', ...) filtered out.

        # style.map() returns an empty list for missing options, so this
        # should be future-safe.
        return [elm for elm in self.style.map('Treeview', query_opt=option) if elm[:2] != ('!disabled', '!selected')]

    def insert_in_tree(self):
        self.menu_close_com()
        dic_dirs, dic_files = self.get_dic_in_folder()
        self.dic_dirs = dic_dirs
        self.dic_files = dic_files
        dirs_list = list(dic_dirs.keys())
        files_list = list(dic_files.keys())
        dirs_list = self.sort_list_files(dirs_list)
        files_list = self.sort_list_files(files_list)
        collapsed_icon = PhotoImage(data='R0lGODlhDwANAKIAAAAAAMDAwICAgP//////ADAwMAAAAAAA'
                                         'ACH5BAEAAAEALAAAAAAPAA0AAAMyGCHM+lAMMoeAT9Jtm5NDKI4Wo'
                                         'FXcJphhipanq7Kvu8b1dLc5tcuom2foAQQAyKRSmQAAOw==')
        label = Label(image=collapsed_icon)
        label.image = collapsed_icon

        if self.key_sort_invers:
            dirs_list.reverse()
            files_list.reverse()
            self.key_sort_invers = 0
        else:
            self.key_sort_invers = 1

        self.clear_e_frame1()
        self.tree.insert('', 'end', values=[str_folder_up])

        for dir_path in dirs_list:
            if os.path.basename(dir_path).startswith('.') and self.key_hide_files_hidden:
                continue
            tab_mtime, tab_atime = self.get_mtime_file(dir_path)
            if dic_dirs[dir_path][1] == 'denied':
                tab_values = ['    ' + dic_dirs[dir_path][0], '', dic_dirs[dir_path][1], tab_mtime, tab_atime]
            else:
                tab_values = ['    ' + dic_dirs[dir_path][0], '{}/{}'.format(dic_dirs[dir_path][2], dic_dirs[dir_path][3]), dic_dirs[dir_path][1], tab_mtime, tab_atime]
            self.tree.insert('', 'end', image=label.image, values=tab_values, tags=('dirs',))
            # self.tree.tag_configure(tagname='dirs', background=background_dirs)
        for file_path in files_list:
            if os.path.basename(file_path).startswith('.') and self.key_hide_files_hidden:
                continue
            # file_size = self.converter_number_to_gb(os.path.getsize(file_path))
            # tab_size = '{:9}{:3}'.format(file_size.split(' ')[0], file_size.split(' ')[1])
            tab_size = self.converter_number_to_gb(os.path.getsize(file_path))
            tab_mtime, tab_atime = self.get_mtime_file(file_path)
            tab_values = [dic_files[file_path][0], os.path.splitext(dic_files[file_path][0])[1], tab_size, tab_mtime, tab_atime]
            m = magic.Magic(mime=True)
            try:
                if m.from_file(file_path).startswith('text'):
                    self.tree.insert('', 'end', values=tab_values, tags=('txt',))
                    self.tree.tag_configure(tagname='txt', background=background_txt)
                elif m.from_file(file_path).startswith('video') or m.from_file(file_path).startswith('audio'):
                    self.tree.insert('', 'end', values=tab_values, tags=('media',))
                    self.tree.tag_configure(tagname='media', background=background_media)
                elif m.from_file(file_path).startswith('image'):
                    self.tree.insert('', 'end', values=tab_values, tags=('image',))
                    self.tree.tag_configure(tagname='image', background=background_image)
                else:
                    self.tree.insert('', 'end', values=tab_values, tags=('w',))
                    self.tree.tag_configure(tagname='w', background=background_with)
            except:
                self.tree.insert('', 'end', values=tab_values, tags=('w',))
                self.tree.tag_configure(tagname='w', background=background_with)
        child_id = self.tree.get_children()[0]
        self.tree.selection_set(child_id)
        self.tree.focus(child_id)
        self.tree.selection_own()
        self.tree.focus_set()

    def get_dic_in_folder(self):
        dic_dirs = {}
        dic_files = {}
        for f in os.listdir(self.folder_rab):
            f_path = os.path.join(self.folder_rab, f)
            if os.path.isdir(f_path):
                try:
                    full_list = os.listdir(f_path)
                    d_list = [os.path.join(f_path, d) for d in full_list if os.path.isdir(os.path.join(f_path, d))]
                    f_list = [os.path.join(f_path, f) for f in full_list if os.path.isfile(os.path.join(f_path, f)) or os.path.islink(os.path.join(f_path, f))]
                    dic_dirs[f_path] = [f, len(full_list), len(d_list), len(f_list)]
                except:
                    dic_dirs[f_path] = [f, 'denied']
            else:
                try:
                    dic_files[f_path] = [f, os.path.getsize(f_path)]
                except:
                    dic_files[f_path] = [f, 'denied']
        return dic_dirs, dic_files

    def get_folder_rab_from_entry(self, event):
        folder_old = self.e_frame1.get()
        folder_new = filedialog.askdirectory(initialdir=self.folder_rab)
        if folder_new:
            if os.path.exists(folder_new):
                self.folder_rab = folder_new
            else:
                self.folder_rab = folder_old
            self.e_frame1.delete(0, END)
            self.e_frame1.insert(0, self.folder_rab)
            # self.save_setup()
            self.insert_in_tree()

    def folder_up(self):
        folder_old = self.e_frame1.get()
        if os.path.exists(folder_old):
            folder_new = os.path.dirname(folder_old)
            if os.path.exists(folder_new):
                self.folder_rab = folder_new
        else:
            self.folder_rab = os.getcwd()
        self.e_frame1.delete(0, END)
        self.e_frame1.insert(END, self.folder_rab)
        # self.save_setup()
        self.insert_in_tree()

    def converter_number_to_gb(self, size):
        KB = 1024.0
        MB = KB * KB
        GB = MB * KB
        if size >= GB:
            return '{:,.1f} Gb'.format(size / GB)
        if size >= MB:
            return '{:,.1f} Mb'.format(size / MB)
        if size >= KB:
            return '{:,.1f} Kb'.format(size / KB)
        return '{} B'.format(size)

    def sort_column_by_image(self):
        pass

    def sort_column_by_name(self):
        self.key_sort_by = 'name'
        self.insert_in_tree()

    def sort_column_by_ext(self):
        self.key_sort_by = 'ext'
        self.insert_in_tree()

    def sort_column_by_size(self):
        self.key_sort_by = 'size'
        self.insert_in_tree()

    def sort_column_by_mtime(self):
        self.key_sort_by = 'mtime'
        self.insert_in_tree()

    def sort_column_by_atime(self):
        self.key_sort_by = 'atime'
        self.insert_in_tree()

    def sort_by_name(self, f_path):
        return os.path.basename(f_path).lower()

    def sort_by_ext(self, f_path):
        if os.path.isdir(f_path):
            if self.dic_dirs[f_path][1] == 'denied':
                return 0
            return self.dic_dirs[f_path][2]
        return os.path.splitext(f_path)[1].lower()

    def sort_by_size(self, f_path):
        if os.path.isdir(f_path):
            if type(self.dic_dirs[f_path][1]) == str:
                return -1
            return self.dic_dirs[f_path][1]
        if type(self.dic_files[f_path][1]) == str:
            return -1
        return os.path.getsize(f_path)

    def sort_by_mtime(self, f_path):
        return os.path.getmtime(f_path)

    def sort_by_atime(self, f_path):
        return os.path.getatime(f_path)

    def sort_list_files(self, list_files):
        if self.key_sort_by == 'name':
            list_files.sort(key=self.sort_by_name)
        elif self.key_sort_by == 'ext':
            list_files.sort(key=self.sort_by_ext)
        elif self.key_sort_by == 'size':
            list_files.sort(key=self.sort_by_size)
        elif self.key_sort_by == 'mtime':
            list_files.sort(key=self.sort_by_mtime)
        elif self.key_sort_by == 'atime':
            list_files.sort(key=self.sort_by_atime)
        return list_files

    def clear_e_frame1(self):
        if self.folder_rab.endswith('/') and len(self.folder_rab) != 1:
            folder_rab = self.folder_rab[:-1]
        self.e_frame1.delete(0, END)
        self.e_frame1.insert(0, self.folder_rab)
        for i in self.tree.get_children():
            self.tree.delete(i)

    def hide_files_hidden(self, event):
        if self.key_hide_files_hidden:
            self.key_hide_files_hidden = 0
        else:
            self.key_hide_files_hidden = 1
        f_select = ' #'
        self.insert_in_tree()

    def print_islink(self, file_path):
        if os.path.islink(file_path):
            self.l_frame3.configure(text='link: {}'.format(file_path), anchor='w')
            self.l_frame4.configure(text='real path: {}'.format(os.readlink(file_path)), anchor='w')

    def line_clicked_double(self, event):
        folder_old = self.e_frame1.get()
        try:
            f_select = self.tree.item(self.tree.selection(), 'values')[0].strip()
        except:
            return
        if f_select == str_folder_up:
            self.folder_up()
            self.l_frame3.configure(text=os.path.basename(self.folder_rab), anchor=W)
            self.l_frame4.configure(text='')
            return
        file_path = os.path.join(self.folder_rab, f_select)

        if os.path.islink(file_path):
            self.print_islink(file_path)
            return
        try:
            if self.dic_dirs[file_path][1] == 'denied':
                self.l_frame3.configure(text=os.path.basename(file_path) + ': denied', anchor=W)
                self.l_frame4.configure(text='')
                return
        except:
            pass
        if os.path.isdir(file_path):
            self.folder_rab = file_path
            # self.save_setup()
            self.insert_in_tree()
            self.l_frame3.configure(text=os.path.basename(file_path), anchor=W)
            self.l_frame4.configure(text='')
            return
        elif os.path.isfile(file_path):
            if sys.platform == 'win32':
                os.startfile(file_path)
                return
            try:
                subprocess.run(['xdg-open', file_path])
                return
            except:
                return
        else:
            # link
            return

    def line_clicked(self, event):
        self.menu_close_com()
        self.text.delete(0.0, END)
        try:
            f_select = self.tree.item(self.tree.selection(), 'values')[0]
        except:
            return
        if f_select == str_folder_up:
            file_path = self.folder_rab
        else:
            file_path = os.path.join(self.folder_rab, f_select)

        if os.path.islink(file_path):
            self.print_islink(file_path)
            return

        self.l_frame3.configure(text=os.path.basename(file_path), anchor=W)
        try:
            if self.dic_dirs[file_path][1] == 'denied' or self.dic_files[file_path][1] == 'denied':
                self.l_frame4.configure(text='denied')
            else:
                self.l_frame4.configure(text='')
        except:
            self.l_frame4.configure(text='')

        m = magic.Magic(mime=True)
        try:
            if m.from_file(file_path).startswith('text'):
                try:
                    lines = open(file_path, 'r').readlines()
                except:
                    return
                for line in lines:
                    self.text.insert(END, line)
            elif m.from_file(file_path).startswith('image'):
                img = Image.open(file_path)
                img_data = 'size:{} format:{} mode:{}'.format(img.size, img.format, img.mode)
                self.l_frame4.configure(text=img_data)

                (x_image, y_image) = img.size
                x_win = self.text.winfo_x() - 80
                y_win = int(x_win * y_image / x_image)
                siz_win = (x_win, y_win)

                img_size = img.resize(siz_win, Image.ANTIALIAS)
                img_size = ImageTk.PhotoImage(img_size)
                self.img = Label(self.text, image=img_size)
                self.img.image = img_size
                self.img.place(x=5, y=5)
            self.text.update()
        except:
            return

    def get_mtime_file(self, file_path):
        f_mtime = os.path.getmtime(file_path)
        f_atime = os.path.getatime(file_path)
        tab_mtime = time.strftime(date_time, time.localtime(f_mtime))
        tab_atime = time.strftime(date_time, time.localtime(f_atime))
        return tab_mtime, tab_atime

    def menu_get(self, event):
        try:
            self.menu_close_com()
        except:
            pass
        self.menu = Menu(self.frame2, tearoff=0)
        # self.menu.add_command(label='Обновить папку', command=self.UpdateWin)
        # self.menu.add_command(label='Вывести все', command=self.PrintListAll)

        self.menu.add_command(label='Cancel', command=self.menu_close_com)
        self.menu.add_command(label='Show/Hide hidden files', command=self.show_or_hide_hidenfile)
        self.menu.add_command(label='----------------------------------')
        self.menu.add_command(label='Delete a file', command=self.delete_file)
        self.menu.post(event.x_root, event.y_root)
        # self.menu.configure(font=self.myFont)

    def menu_close(self, event):
        try:
            self.menu.destroy()
        except:
            pass
        try:
            self.help.destroy()
        except:
            pass
        try:
            self.img.destroy()
        except:
            pass
        self.master.clipboard_clear()

    def menu_close_com(self):
        self.menu_close(event='')

    def delete_file(self):
        # Delete folder if empty or delete file
        self.menu_close_com()
        try:
            f_name = f_select = self.tree.item(self.tree.selection(), 'values')[0]
        except:
            return
        file_path = os.path.join(self.folder_rab, f_name)
        if os.path.isdir(file_path):
            if len(os.listdir(file_path)):
                messagebox.showerror(title='Deletion Error! ', message='Deleting only empty folders is allowed!')
                return
            else:
                os.rmdir(file_path)
        else:
            if messagebox.askyesno(title='Delete File! ', message='File \n' + f_name + '\nWill be deleted. Confirm?'):
                os.remove(file_path)
        self.set_key_sort_invers()

    def set_key_sort_invers(self):
        if self.key_sort_invers:
            self.key_sort_invers = 0
        else:
            self.key_sort_invers = 1
        self.insert_in_tree()

    def show_or_hide_hidenfile(self):
        if self.key_hide_files_hidden:
            self.key_hide_files_hidden = 0
        else:
            self.key_hide_files_hidden = 1
        self.set_key_sort_invers()

    def help(self, event):
        try:
            self.menu.destroy()
        except:
            pass

        help_txt = '''Description:
MyFM_PFT_win2 - it is a File Manager with minimum functionality.
The main feature is a fast navigation over text, photo and video files.

Usage:
After the application was started, expand appeared window to a full screen.

Files list view:
- Names of text, photo and video files have different colored background, all other files have white background
- The name of selected file is shown in the bottom, if it is a line, a full real path will be shown as well.

Navigation with mouse:
1. Right panel is shown in a full screen mode shows text, image, video files previews
2. Double cline on a top address panel - opens dialog to choose a new path
3. Double click on ". . ." - goes to parent folder
4. Double click on a folder name - goes to selected folder
5. Double click on a file - opens file in a default application
6. Single click on a text, image or video file - shows preview on a right panel
7. Right click on any area - show context menu with:
  - Show/Hide hidden files and folders
  - Delete file/folder

Sorting files:
1. Single click on a column name - sort files by it property
2. For reverse sorting click on the column name again

Sorting features:
1. Column 'Ext' - sort folders by an amount of children folders
2. Column 'Size' - sort folders by an amount of total children elements in it

Keyboard navigation:
1. "Up" and "Down" arrows to navigate over files/folders list in a left panel
2. "Escape" - close context menu or "Help" window
3. "Space" - open file in a default application (no action with links)
4. "Ctrl+H" - show/hide hidden files
        '''

        # sw = self.master.winfo_screenwidth()
        # sh = self.master.winfo_screenheight()
        sw = 770
        sh = 400
        # x = int((sw - w) / 2)
        # y = int((sh - h) / 2)
        self.help = Toplevel()
        self.help.geometry('{}x{}+{}+{}'.format(sw, sh, 0, 0))
        self.help.title('Help for MyFM win2')
        text_window = Text(self.help)  # , width=width_w, height=height_w)
        text_window.pack(side=LEFT, fill=BOTH, expand=True)
        # button = Button(help, text=self.lang_dic['text_button'], command=help.destroy)
        # button.pack(side=BOTTOM)
        text_window.insert(END, help_txt)

        scrollbar1 = Scrollbar(self.help)
        scrollbar1.pack(side=RIGHT, fill=Y)
        text_window.config(yscrollcommand=scrollbar1.set)
        scrollbar1.config(command=text_window.yview)
        self.help.bind('<Escape>', self.menu_close)

    # def save_setup(self):
    #     data_dic = self.get_dic_from_file()
    #     data_dic['folder_rab'] = self.folder_rab
    #     with open(file_config, 'w') as f:
    #         for key in data_dic.keys():
    #             f.write('{} = {}'.format(key, data_dic[key]))
    #
    # def get_default_setup(self):
    #     if not os.path.exists(file_config):
    #         self.set_default_setup()
    #     data_dic = self.get_dic_from_file()
    #     self.folder_rab = data_dic['folder_rab']
    #
    # def set_default_setup(self):
    #     with open(file_config, 'w') as f:
    #         folder_rab = os.getcwd()
    #         f.write('folder_rab = {}'.format(folder_rab))
    #
    # def get_list_from_file(self):
    #     data_list = []
    #     if os.path.exists(file_config):
    #         with open(file_config, 'r') as f:
    #             f_lines = f.readlines()
    #         for f_line in f_lines:
    #             if f_line.strip().startswith(start_switch):
    #                 continue
    #             elif f_line.strip():
    #                 data_list.append(f_line.strip())
    #     else:
    #         self.set_default_setup()
    #         return self.get_list_from_file()
    #     return data_list
    #
    # def get_dic_from_file(self):
    #     data_dic = {}
    #     if os.path.exists(file_config):
    #         with open(file_config, 'r') as f:
    #             lines = f.readlines()
    #         for line in lines:
    #             if line.strip().startswith(start_switch):
    #                 continue
    #             elif line.strip():
    #                 data_dic[line.strip().split('=')[0].strip()] = line.strip().split('=')[1].strip()
    #     else:
    #         return {}
    #     return data_dic
    #
    # def get_dirs_and_files_in_folder(self, folder):
    #     full_f = [os.path.join(folder, f) for f in os.listdir(folder)]
    #     dirs = [d for d in full_f if os.path.isdir(d)]
    #     files = [f for f in full_f if os.path.isfile(f)]
    #     return dirs, files


def MyFM_PFT_v2():
    root = Tk()
    root.title('My Files Manager')
    root.geometry('{}x{}+{}+{}'.format(*CenteredWindow(root)))

    app = App(root)
    app.e_frame1.bind('<Double-ButtonRelease-1>', app.get_folder_rab_from_entry)
    root.bind('<Control-h>', app.hide_files_hidden)
    app.tree.bind('<Double-ButtonRelease-1>', app.line_clicked_double)
    app.tree.bind('<space>', app.line_clicked_double)
    app.tree.bind('<ButtonRelease-1>', app.line_clicked)
    app.tree.bind('<Button-3>', app.menu_get)
    root.bind('<Escape>', app.menu_close)
    root.bind('<Up>', app.line_clicked)
    root.bind('<Down>', app.line_clicked)
    root.bind('<F1>', app.help)

    root.mainloop()


if __name__ == '__main__':
    MyFM_PFT_v2()
