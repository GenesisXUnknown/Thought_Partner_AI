"""Plugin Customization Interface
Allows injection of user-defined logic or data at runtime.
"""

class PluginInterface:
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, function):
        self.plugins[name] = function

    def execute_plugin(self, name, *args, **kwargs):
        if name in self.plugins:
            return self.plugins[name](*args, **kwargs)
        return None
