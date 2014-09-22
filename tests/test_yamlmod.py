import os
import sys

from nose.tools import *

try:
	from importlib import reload
except ImportError:
	try:
		from imp import reload
	except ImportError:
		pass

def setup_yamlmod():
	import yamlmod
	reload(yamlmod)

def teardown_yamlmod():
	import yamlmod

	for hook in sys.meta_path:
		if isinstance(hook, yamlmod.YamlImportHook):
			sys.meta_path.remove(hook)
			break

@with_setup(setup_yamlmod, teardown_yamlmod)
def test_import_installs_hook():
	import yamlmod

	hooks = []

	for hook in sys.meta_path:
		if isinstance(hook, yamlmod.YamlImportHook):
			hooks.append(hook)

	eq_(len(hooks), 1, 'did not find exactly one hook')

@with_setup(setup_yamlmod, teardown_yamlmod)
def test_import_fixture():
	import fixture

	eq_(fixture.debug, True)
	eq_(fixture.domain, 'example.com')
	eq_(fixture.users, ['alice', 'bob', 'cathy'])


@with_setup(setup_yamlmod, teardown_yamlmod)
def test_hidden_attributes():
	import fixture

	eq_(fixture.__name__, 'fixture')
	eq_(fixture.__file__, os.path.join(os.path.dirname(__file__), 'fixture.yml'))
