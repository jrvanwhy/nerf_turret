import nxt.locator as nl

class TurretDriver:
	SET_YAW    = 1
	SET_PITCH  = 2

	SET_RYAW   = 3
	SET_RPITCH = 4

	ZERO_YAW   = 5

	SHOOT_ONCE = 6
	SHOOT_BGN  = 7
	SHOOT_END  = 8
	INTIMIDATE = 9

	ENABLE_YAW = 10
	ENABLE_PCH = 11

	QUERY_YAW  = 12
	QUERY_PCH  = 13

	ABORT      = 14

	def __init__(self, outbox=0, inbox=1, host=None, name=None):
		self.outbox = outbox
		self.brick = nl.find_one_brick(host=host, name=name)

	def _set_yaw_msg(self, yaw):
		if yaw == None:
			return ""
		# else:
			# return str(SET_YAW) + 

	def zero_yaw(self):
		pass
		# self.brick.message_write(self.outbox, "zero_yaw")

	def set_pos(self, yaw=None, pitch=None):
		pass

		# self.brick.message_write(self.outbox, "set_pos:%3d,%3d" % (yaw, pitch))

	def set_rpos(self, yaw=None, pitch=None):
		pass
		

# b = nl.find_one_brick()

# b.message_write(0, "\0A")

# print 'Test succeeded!'