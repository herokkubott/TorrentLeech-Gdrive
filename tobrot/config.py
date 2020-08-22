from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
	TG_BOT_TOKEN= "1221269735:AAHMbG34oCUml4sRplaXIl9eJS4Ylp8SaWM"
	APP_ID = 1682719
	API_HASH ="2edcaea55a3738985d979c3bf72b2e0d"
	OWNER_ID = "1042281429" #ID of bot owner
	AUTH_CHANNEL = [-1001227823555]
	DESTINATION_FOLDER = "Colab Drive" #Name of your folder read readme
	RCLONE_CONFIG = """type = drive
scope = drive
root_folder_id = 1Id7U2EhLH7jZ5lUQzVfZPzTrtQ7Fqcp7
token = {"access_token":"ya29.a0AfH6SMD0Ls_GTmTUJqGwStnlrqslENsrS24-ycdJ4DhHuQP5v51mIs2E75KGPYLgbcHr0qHubDzt9iw0xrOLsW9cu__cnaKE2eHPSV8WuuxoC4Usp2yEWRc-Pqd5qmxPhqGLloCIpZmbTbBAV3tiSSM1KMGXuxyZQ88","token_type":"Bearer","refresh_token":"1//0gsTfePPhgts5CgYIARAAGBASNwF-L9Ir2fUBzQKc9UblcWooJ6LpY4tKiD7Yq0hi13LLftps2ZUJW-nbcD7C9NMZRrUKMjz8MBo","expiry":"2020-08-18T10:04:16.242408105Z"}
team_drive = 0AH6MHzqge7IuUk9PVA"""
	#fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
