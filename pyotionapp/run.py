from settings.settings import settingsApp


# App version

config = settingsApp()
version = config.version()

if __name__ == '__main__':

	print('ok')