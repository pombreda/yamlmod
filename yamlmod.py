import os
import imp
import sys
import yaml

class YamlImportHook:
	def find_module(self, fullname, path=None):
		name = fullname.split('.')[-1]

		for folder in path or sys.path:
			if os.path.exists(os.path.join(folder, '%s.yml' % name)):
				return self

		return None

	def load_module(self, fullname):
		if fullname in sys.modules:
			return sys.modules[fullname]

		sys.modules[fullname] = mod = imp.new_module(fullname)

		if '.' in fullname:
			pkg, name = fullname.rsplit('.', 1)
			path = sys.modules[pkg].__path__
		else:
			pkg, name = '', fullname
			path = sys.path

		for folder in path:
			if os.path.exists(os.path.join(folder, '%s.yml' % name)):
				mod.__file__ = os.path.join(folder, '%s.yml' % name)
				mod.__package__ = pkg
				mod.__loader__ = self

				mod.__dict__.update(yaml.load(open(mod.__file__)) or {})

				return mod

		# somehow not found, delete from sys.modules
		del sys.modules[fullname]

sys.meta_path.append(YamlImportHook())
