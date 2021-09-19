.v:
	python3 -m venv .v
	./.v/bin/pip -r requirements.txt

format:
	./.v/bin/black *.py
	./.v/bin/isort *.py
