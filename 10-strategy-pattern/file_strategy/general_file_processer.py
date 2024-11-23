from .excel_file_read import *
from .txt_file_read import *
from .csv_file_read import *
from .json_file_read import *


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
            XLSXExcelProcesser().read_data(self.file_path)
        if self.file_type == "xls":
            XLSExcelProcesser().read_data(self.file_path)

        if self.file_type == "txt":
            TXTProcesser().read_data(self.file_path)

        if self.file_type == "csv":
            CSVProcesser().read_data(self.file_path)

        if self.file_type == "json":
            JSONProcesser().read_data(self.file_path)


if __name__ == "__main__":
    pass
