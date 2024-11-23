from .general_file_processer import StrategyProcesser


class TXTProcesser(StrategyProcesser):
    """ 处理 专门的TXT 文件的类 """

    def read_data(self, file_path: str):
        print("正在解析: TXT 文件")
