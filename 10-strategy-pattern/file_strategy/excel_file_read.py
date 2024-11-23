from .file_processer_interface import StrategyProcesser


class XLSXExcelProcesser(StrategyProcesser):
    """ 处理 专门的XLSX 文件的类 """

    def read_data(self, file_path: str):
        print("正在解析:xlsx 的Excel文件")


class XLSExcelProcesser(StrategyProcesser):
    """ 处理 专门的XLS 文件的类 """

    def read_data(self, file_path: str):
        print("正在解析:xls 的Excel文件")
