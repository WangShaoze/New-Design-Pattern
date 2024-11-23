from abc import ABC
import time


class Window(ABC):
    def start(self):  # 原子操作
        pass

    def stop(self):  # 原子操作
        pass

    def repaint(self):  # 原子操作
        pass

    def run(self):
        self.start()
        while True:
            try:

                self.repaint()
                time.sleep(0.1)
            except KeyboardInterrupt:
                break
        self.stop()


class MyWindow(Window):
    def start(self):
        print("窗口开始运行...")

    def repaint(self):
        print("画面绘制中.... ============{}============".format("A"))

    def stop(self):
        print("窗口运行结束...")


if __name__ == '__main__':
    myWindow = MyWindow()
    myWindow.run()
