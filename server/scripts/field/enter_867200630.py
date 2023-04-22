# id 867200630 (Abrup Basin : Open Snowfield), field 867200630
sm.lockInGameUI(True, False)
sm.removeAdditionalEffect()
sm.spawnNpc(9400667, 520, 330)
sm.showNpcSpecialActionByTemplateId(9400667, "summon", 0)
sm.spawnNpc(9400617, 790, 300)
sm.showNpcSpecialActionByTemplateId(9400617, "summon", 0)
sm.spawnNpc(9400618, 740, 300)
sm.showNpcSpecialActionByTemplateId(9400618, "summon", 0)
sm.spawnNpc(9400619, 640, 300)
sm.showNpcSpecialActionByTemplateId(9400619, "summon", 0)
sm.spawnNpc(9400617, 540, 300)
sm.showNpcSpecialActionByTemplateId(9400617, "summon", 0)
sm.spawnNpc(9400619, 590, 300)
sm.showNpcSpecialActionByTemplateId(9400619, "summon", 0)
sm.spawnNpc(9400618, 690, 300)
sm.showNpcSpecialActionByTemplateId(9400618, "summon", 0)
sm.showNpcSpecialActionByTemplateId(9400667, "ear", 0)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(9400596) # Snowfield Archer
sm.sendNext("M-monster! There's a monster!")
sm.moveNpcByTemplateId(9400617, True, 2000, 210)
sm.moveNpcByTemplateId(9400618, True, 2000, 300)
sm.moveNpcByTemplateId(9400619, True, 2000, 270)
sm.moveNpcByTemplateId(9400617, True, 2000, 230)
sm.moveNpcByTemplateId(9400619, True, 2000, 200)
sm.moveNpcByTemplateId(9400618, True, 2000, 250)
sm.showNpcSpecialActionByTemplateId(9400667, "jumpattack", 0)
sm.setInnerOverrideSpeakerTemplateID(9400619) # Resident
sm.sendSay("Aaaaaaagh!")
sm.showNpcSpecialActionByTemplateId(9400667, "howl", 0)
sm.zoomCamera(2000, 2000, 3000, 520, 330)
sm.sendDelay(2000)
sm.sendDelay(2000)
sm.createFieldTextEffect("#r#fnﾳﾪﾴﾮﾰ￭ﾵ￱ ExtraBold##fs26#??????#k", 100, 4000, 4, 80, 200, 1, 4, 0, 0, 0)
sm.createFieldTextEffect("#fnﾳﾪﾴﾮﾰ￭ﾵ￱ ExtraBold##fs16#It's the monster that brought the snowstorm.", 100, 1500, 4, 80, 250, 1, 4, 0, 0, 0)
sm.sendDelay(6000)
sm.moveCamera(True, 0, 0, 0)
sm.sendDelay(500)
sm.lockInGameUI(False, True)
sm.warp(867200720)
