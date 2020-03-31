import ui
import console
from src.service.dolls_service import DollsSearchService, DollsYamlRepository
import webbrowser
import datetime

class ResultView(object):
	def __init__(self, hour, minute, type, star, gun_type):
		self.v = ui.load_view()
		ds = DollsSearchService(DollsYamlRepository())
		self.dolls = ds.search(hour, minute, star, gun_type)
		scroll = ui.ScrollView()
		for index, doll in enumerate(self.dolls):
			scroll.add_subview(self.create_doll_view(doll, index))
		self.type = type
		scroll.frame = (0, 50, self.v.width, self.v.height)
		scroll.content_size = (500, 120 + len(self.dolls) * 220)
		self.v.add_subview(scroll)

	def create_doll_view(self, doll, index):
		view = ui.View()
		view.frame = (10, 10 + index * 220, self.v.width-20, 220)
		#view.background_color = ('midnightblue')
		view.add_subview(self.create_webview(doll))
		view.add_subview(self.create_name_label(doll))
		view.add_subview(self.create_button(doll, index))
		view.add_subview(self.create_type_label(doll))
		view.add_subview(self.create_time_label(doll))
		view.add_subview(self.create_get_label(doll))
		return view

	def create_webview(self, doll):
		web = ui.ImageView()
		web.frame = (10, 10, 140, 200)
		print(doll.image_url)
		web.load_from_url(doll.image_url)
		return web

	def create_name_label(self, doll):
		label = ui.Label()
		label.frame = (160, 10, self.v.width-190, 30)
		label.text = doll.name
		label.background_color = (0, 0, 0, 0.5)
		label.tint_color = ('white')
		label.alignment = ui.ALIGN_CENTER
		return label

	def create_button(self, doll, index):
		button = ui.Button()
		button.frame = (160, 50, self.v.width-190, 30)
		button.title = 'link'
		button.name = str(index)
		button.action = self.tap_new_button
		button.background_color = (0, 0, 0, 0.5)
		button.tint_color = ('white')
		return button

	def create_type_label(self, doll):
		label = ui.Label()
		label.frame = (160, 90, self.v.width-190, 30)
		label.text = doll.type
		label.background_color = (0, 0, 0, 0.5)
		label.tint_color = ('white')
		label.alignment = ui.ALIGN_CENTER
		return label

	def create_time_label(self, doll):
		label = ui.Label()
		label.frame = (160, 130, self.v.width-190, 30)
		label.text = str(doll.time.strftime('%H:%M:%S'))
		label.background_color = (0, 0, 0, 0.5)
		label.tint_color = ('white')
		label.alignment = ui.ALIGN_CENTER
		return label

	def create_get_label(self, doll):
		label = ui.TextView()
		label.frame = (160, 170, self.v.width-190, 40)
		label.text = doll.how_to_get
		label.background_color = (0, 0, 0, 0.5)
		label.tint_color = ('white')
		label.alignment = ui.ALIGN_CENTER
		return label

	def tap_new_button(self, sender):
		browse = webbrowser.get('safari')
		browse.open(self.dolls[int(sender.name)].link_url)
	
		
