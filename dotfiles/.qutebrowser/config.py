config.load_autoconfig()
c.content.proxy = "http://127.0.0.1:7890"
c.window.transparent = True
c.window.hide_decoration = True
c.tabs.show = "multiple"
c.colors.webpage.darkmode.enabled = True
c.url.default_page = "https://google.com/"
c.url.searchengines = {"DEFAULT": "https://google.com/search?q={}"}
c.url.start_pages = "about:blank"
config.bind(",h", "help")
config.bind(",y", "history")
config.bind(",d", "devtools")
config.bind(",D", "devtools-focus")
config.unbind("d")
config.bind("dd", "tab-close")
config.bind(",w", "tab-close")
config.bind(",c", "tab-close")
config.bind("X", "tab-close")
config.bind(",q", "quit")
config.bind(",m", "bookmark-list")
config.bind("J", "back")
config.bind("K", "forward")
config.bind("H", "tab-prev")
config.bind("L", "tab-next")
config.bind("<Ctrl-TAB>", "tab-next")
