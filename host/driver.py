import nxt.locator as nl

class TurretDriver:
	SET_YAW    = 1
	SET_PITCH  = 2

	SET_RYAW   = 3
	SET_RPITCH = 4

	ZERO_YAW   = 5

	SHOOT      = 6
	INTIMIDATE = 7

	ENABLE_YAW = 8
	ENABLE_PCH = 9
	ENABLE_TRG = 10

	def __init__(self, mailbox=0, host=None, name=None):
		self.mailbox = mailbox
		self.brick = nl.find_one_brick(host=host, name=name)

	def _set_yaw_msg(self, yaw):
		if yaw == None:
			return ""

	def zero_yaw(self):
		pass
		# self.brick.message_write(self.mailbox, "zero_yaw")

	def set_pos(self, yaw=None, pitch=None):
		pass

		# self.brick.message_write(self.mailbox, "set_pos:%3d,%3d" % (yaw, pitch))

	def set_rpos(self, yaw=None, pitch=None):
		pass
		

b = nl.find_one_brick()

b.message_write(0, "\0A")

print 'Test succeeded!'