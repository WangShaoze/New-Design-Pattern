from .general_file_processer import StrategyProcesser


class JSONProcesser(StrategyProcesser):
    """ 处理 专门的 JSON 文件的类 """

    def read_data(self, file_path: str):
        print("正在解析: JSON 文件")
