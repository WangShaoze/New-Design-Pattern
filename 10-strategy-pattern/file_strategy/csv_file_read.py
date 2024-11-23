from .general_file_processer import StrategyProcesser


class CSVProcesser(StrategyProcesser):
    """ 处理 专门的CSV 文件的类 """

    def read_data(self, file_path: str):
        print("正在解析: CSV 文件 ")
