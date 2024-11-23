from abc import ABC, abstractmethod


class StrategyProcesser(ABC):
    """ 文件处理策略接口 """

    @abstractmethod
    def read_data(self, file_path: str):
        pass


class XLSXExcelProcesser(StrategyProcesser):
    """ 处理 专门的XLSX 文件的类 """

    def read_data(self, file_path: str):
        print("正在解析:xlsx 的Excel文件")


class XLSExcelProcesser(StrategyProcesser):
    """ 处理 专门的XLS 文件的类 """

    def read_data(self, file_path: str):
        print("正在解析:xls 的Excel文件")


class TXTProcesser(StrategyProcesser):
    """ 处理 专门的TXT 文件的类 """

    def read_data(self, file_path: str):
        print("正在解析: TXT 文件")


class CSVProcesser(StrategyProcesser):
    """ 处理 专门的CSV 文件的类 """

    def read_data(self, file_path: str):
        print("正在解析: CSV 文件")


class JSONProcesser(StrategyProcesser):
    """ 处理 专门的 JSON 文件的类 """

    def read_data(self, file_path: str):
        print("正在解析: JSON 文件")


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
