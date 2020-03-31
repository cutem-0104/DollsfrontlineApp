import ui
from src.SearchView import SearchView

a = SearchView()
nv = ui.NavigationView(a.v)
nv.height = 500
nv.width = 500
nv.name = 'SearchPage'

nv.present('sheet')
