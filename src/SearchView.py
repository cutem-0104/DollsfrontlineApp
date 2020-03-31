import ui
from src.ResultView import ResultView


class SearchView(object):
    def __init__(self):
        self.v = ui.load_view()
        self.v['search'].action = self.show_result

    def show_result(self, sender):
        hour = sender.superview['hour']
        index = hour.selected_index

        minute1 = sender.superview['minute1']
        index1 = minute1.selected_index
        minute2 = sender.superview['minute2']
        index2 = minute2.selected_index
        minute = str(
            int(minute1.segments[index1]) + int(minute2.segments[index2]))

        type = sender.superview['type']
        index3 = type.selected_index

        star = sender.superview['star']
        index4 = star.selected_index

        gun_type = sender.superview['gun_type']
        index5 = gun_type.selected_index

        d = ResultView(hour.segments[index], minute, type.segments[index3],\
                    star.segments[index4], gun_type.segments[index5])
        sender.superview.navigation_view.push_view(d.v)
