dependencies:
	pip install -r requirements.txt

dev:
	WIFIPOS_SETTINGS=dev-settings.py python main.py

production:
	WIFIPOS_SETTINGS=production-settings.py python main.py
