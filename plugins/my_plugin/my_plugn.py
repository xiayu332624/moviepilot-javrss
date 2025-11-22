from app.plugins import _PluginBase

class MyPlugin(_PluginBase):
    plugin_name = "我的插件"
    plugin_desc = "这是一个示例插件"
    plugin_version = "1.0"
    plugin_author = "你的名字"
    plugin_level = 1

    def init_plugin(self, config=None):
        self.logger.info("插件初始化成功！")

    def get_state(self):
        return False  # 默认不启用
