# id 867200102 (Abrup Basin : Temporary Hunting Camp), field 867200102
sm.lockInGameUI(True, False)
sm.removeAdditionalEffect()
sm.forcedAction(29, 50000)
sm.sendDelay(1000)
sm.setSpeakerType(3)
sm.setParam(57)
sm.setColor(1)
sm.sendNext("#b(This place is a lot cozier after clearing it out a bit.)")
sm.playSound("Sound/PL_MONAD.img/EP1/ACT1/wind", 128)
sm.sendSay("#b(Once I make it down off this mountain, I can start exploring the valley.)")
sm.sendSay("#b(What could be happening in Abrup?)")
sm.sendSay("#b(First order of business is to meet the lady who sent the letter.)")
sm.startQuest(64012)
sm.sendDelay(1000)
sm.sendNext("#b(Boy... this fire sure is cozy...)")
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.sendDelay(500)
sm.forcedAction(25, 50000)
sm.blind(True, 255, 0, 0, 0, 0)
sm.sendDelay(100)
sm.blind(False, 0, 0, 0, 0, 250)
sm.sendDelay(300)
sm.sendNext("#b(Should be okay to doze off for a bit, yeah?)")
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.sendDelay(1000)
sm.blind(True, 255, 0, 0, 0, 0)
sm.sendDelay(100)
sm.blind(False, 0, 0, 0, 0, 250)
sm.sendDelay(300)
sm.playSound("Sound/PL_MONAD.img/EP1/ACT1/wind", 128)
sm.sendNext("#b(Just a little bit.)")
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.sendDelay(2000)
sm.lockInGameUI(False, True)
sm.warp(867200111)
