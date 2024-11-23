from file_strategy import *

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
