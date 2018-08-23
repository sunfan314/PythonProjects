class Settings():
	#store game settings
	def __init__(self):
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (230,230,230)
		#ship config
		self.ship_speed_factor = 0.5
		self.ship_limit = 3
		#bullet config
		self.bullet_speed_factor = 0.5
		self.bullet_width = 2
		self.bullet_height = 10
		self.bullet_color = (60,80,60)
		self.bullets_allowed = 10

		#alien config
		self.alien_speed_factor = 0.2
		self.fleet_drop_speed = 10
		#alien fleet move direction
		self.fleet_direction = 1
		
