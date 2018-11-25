import urwid
from summnews import SummNews

class SummNewsTui:
    def __init__(self):
        self.palette = [
            ("title", "black, bold", "white"),
            ("body", "black", "white"),
            ("bar", "black", "white"),
            ("content_box", "black", "white"),
            ("bg", "black", "white")]

        self.summed_articles = SummNews(5).get_summed_news()
        #[{"title": "Test Num: " + str(x), "body": "This is just a test, number " + str(x) + "."} for x in range(60)]

        pre_div = urwid.Divider()
        self.div = urwid.AttrMap(pre_div, "bar")

        self.start_up()

    def title_menu(self):
        title_list = [self.div]
        for article in self.summed_articles:
            pre_title_btn = urwid.Button(article["title"])
            urwid.connect_signal(pre_title_btn, "click", self.display_article, article)
            title_btn = urwid.AttrMap(pre_title_btn, "body", focus_map="reversed")

            title_list.extend([title_btn])

        scene = urwid.Pile(title_list)
        return urwid.Filler(scene)

    def re_title_menu(self, button):
        self.contents.original_widget = self.title_menu()

    def display_article(self, button, article):
        title = urwid.Text(("title", article["title"]), align="center")
        body = urwid.Text(("body", article["body"]), align="left")

        pre_close_btn = urwid.Button("Close")
        urwid.connect_signal(pre_close_btn, "click", self.re_title_menu)
        close_btn = urwid.AttrMap(pre_close_btn, "body", focus_map="reversed")

        scene = urwid.Pile([title, self.div, body, self.div, close_btn])
        self.contents.original_widget = urwid.Filler(scene)

    def display_all_articles(self):
        interface_articles = []
        for article in self.summed_articles:
            title = urwid.Text(("title", article["title"]), align="center")
            div = urwid.Divider()
            div_mapped = urwid.AttrMap(div, "bar")
            body = urwid.Text(("body", article["body"]), align="left")

            interface_articles.extend([title, body, div_mapped])

        return urwid.Pile(interface_articles)

    def read_key(self, key):
        if key in ("q", "Q"):
            raise urwid.ExitMainLoop()

    def start_up(self):
        pre_contents = self.title_menu()
        self.contents = urwid.AttrMap(pre_contents, "content_box")

        pre_frame = urwid.Padding(self.contents, "center", left=2, right=2)
        self.frame = urwid.AttrMap(pre_frame, "bar")

        self.overlay = urwid.Overlay(self.frame, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
                                align="center", width=("relative", 60),
                                valign="middle", height=("relative", 60))

        urwid.MainLoop(self.overlay, self.palette, unhandled_input=self.read_key).run()

#SummNewsTui()
