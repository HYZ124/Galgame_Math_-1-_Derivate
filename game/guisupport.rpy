init -100 python in gui:

    def scale(n):
        return int(n)

# NOTE: 官方模板这里的 init 100 块会在每次启动时重跑 launcher 的
# gui7 生成器（generate_gui/_gui_images），会扰动引擎模块并导致
# init 1600 (00mixers) 崩溃。游戏本体不需要它，删除。
