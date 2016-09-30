lint:
	pep8 audio_recorder
	pep8 setup.py
	pep8 test_project/test_project
	pep8 test_project/audio_files --exclude migrations

test:
	py.test test_project/audio_files/tests.py

serve:
	python test_project/manage.py runserver