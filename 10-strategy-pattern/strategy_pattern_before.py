class FileProcesser:
    """  文件处理类 """

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file_name = None
        self.file_type = None
        self.__paser_file_path()

    def __paser_file_path(self):
        tmp = ""
        if "\\" in self.file_path:
            tmp = self.file_path.split("\\")[-1]
        self.file_type = tmp.split(".")[1]
        self.file_name = tmp.split(".")[0]

    def read_data(self):
        if self.file_type == "xlsx":
            print("正在解析:Excel文件{}.{}".format(self.file_name, self.file_type))

        if self.file_type == "xls":
            print("正在解析:Excel文件{}.{}".format(self.file_name, self.file_type))

        if self.file_type == "txt":
            print("正在解析:Excel文件{}.{}".format(self.file_name, self.file_type))

        if self.file_type == "csv":
            print("正在解析:Excel文件{}.{}".format(self.file_name, self.file_type))

        if self.file_type == "json":
            print("正在解析:Excel文件{}.{}".format(self.file_name, self.file_type))


if __name__ == "__main__":
    ri_zhi = FileProcesser("..\日志文件.xlsx")
    ri_zhi.read_data()

    ri_zhi = FileProcesser("..\日志文件.xls")
    ri_zhi.read_data()

    ri_zhi = FileProcesser("..\日志文件.txt")
    ri_zhi.read_data()

    ri_zhi = FileProcesser("..\日志文件.json")
    ri_zhi.read_data()

    ri_zhi = FileProcesser("..\日志文件.csv")
    ri_zhi.read_data()
