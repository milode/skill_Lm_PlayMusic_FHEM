from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class Lm_PlayMusic_FHEM(AliceSkill):
	"""
	Author: milode
	Description: Musik abspielen ueber fhem
	"""

	@IntentHandler('MyIntentName')
	def dummyIntent(self, session: DialogSession, **_kwargs):
		pass
