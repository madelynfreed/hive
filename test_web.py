#HTML TEST
import unittest
import webbrowser
import tempfile
import time
import webhive


class TestHive(unittest.TestCase):
	def test_draw_html(self):
		with tempfile.NamedTemporaryFile(suffix='.html') as f:
			f.write(webhive.build_string())  
			f.flush()
			print f.name
			webbrowser.open_new_tab('file://'+f.name)
			time.sleep(1)	

if __name__ == '__main__':
	unittest.main()
