from abc import abstractmethod, ABC


class StrategyProcesser(ABC):
    """ 文件处理策略接口 """

    @abstractmethod
    def read_data(self, file_path: str):
        pass
