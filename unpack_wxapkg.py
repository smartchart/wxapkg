# -*- coding: utf-8 -*-
import os

class wxapkg:
    wxapkg_path = ""
    out_path = ""

    def __init__(self, wxapkg_path):
        self.wxapkg_path = wxapkg_path
        if wxapkg_path.endswith('.wxapkg'):
            self.out_path = wxapkg_path[:wxapkg_path.rfind('.wxapkg')]
        else:
            self.out_path = wxapkg_path + '_decode'

    def open_wxapkg(self):
        fd = open(self.wxapkg_path, "rb")
        if not self.is_wxapkg():
            fd.close()
            return
        # header
        self.get_header(fd)
        # get file name
        file_num = self.get_file_num(fd)
        # file resource
        for i in range(0, file_num):
            self.get_file(fd)

    def close_wxapkg(self):
        self.close()

    def is_wxapkg(self):
        fd = open(self.wxapkg_path, "rb")
        key = fd.read(1)
        if ord(key) == 0xbe:
            # print(" right format")
            return True
        else:
            print("not wxapkg format")
            return False

    @staticmethod
    def bytesToInt(byte_array):
        num = (byte_array[0] << 24) + (byte_array[1] << 16) + (byte_array[2] << 8) + byte_array[3]
        return num

    @staticmethod
    def get_int(fd, length):
        num = 0
        for i in range(0, length):
            num = (num << 8) + (ord(fd.read(1)))
        return num

    @staticmethod
    def create_path(path):
        if path.find(os.sep):
            dir_path = path[:path.rfind(os.sep)]
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

    # read wxapkg
    @staticmethod
    def get_header(fd):
        header = fd.read(0x10)

    def get_file_num(self, fd):
        file_num = self.get_int(fd, 2)
        return file_num

    # read file
    def get_file(self, fd):
        file_name_length = self.get_int(fd, 4)
        file_name = fd.read(file_name_length).decode().replace('/', os.sep, )
        file_path = self.out_path + file_name
        file_start = self.get_int(fd, 4)
        file_length = self.get_int(fd, 4)
        tmp_seek = fd.tell()
        fd.seek(file_start, os.SEEK_SET)
        file_content = fd.read(file_length)
        print("[start] %4x [length] %4x [file_name] %s" % (file_start, file_length, file_name))
        self.create_path(file_path)
        open(file_path, "wb").write(file_content)
        fd.seek(tmp_seek, os.SEEK_SET)
