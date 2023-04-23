# id 867200859 (Abrup Basin : Abandoned Village Outskirts), field 867200859
sm.lockInGameUI(True, False)
sm.changeBGM("Bgm00.img/Silence", 0, 0)
sm.blind(True, 255, 0, 0, 0, 0)
sm.forcedFlip(True)
sm.sendDelay(1000)
sm.playSound("Sound/PL_MONAD.img/EP1/ACT2/footstep1", 128)
sm.blind(False, 0, 0, 0, 0, 1000)
sm.sendDelay(1500)
sm.spawnNpc(9400580, 1550, 170)
sm.showNpcSpecialActionByTemplateId(9400580, "summon", 0)
sm.playSound("Sound/PL_MONAD.img/EP1/ACT2/footstep2", 128)
sm.sendDelay(2000)
sm.moveNpcByTemplateId(9400580, True, 100, 80)
sm.sendDelay(500)
sm.forcedFlip(True)
sm.setSpeakerType(3)
sm.setParam(57)
sm.setColor(1)
sm.sendNext("#bWho's there? ")
sm.sendDelay(1000)
sm.moveNpcByTemplateId(9400580, True, 100, 80)
sm.sendDelay(500)
sm.playSound("Sound/PL_MONAD.img/EP1/ACT2/footstep3", 128)
sm.changeBGM("BgmPL2.img/WalkTogether", 0, 0)
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendNext("#face5#Ah... ")
sm.setParam(57)
sm.sendSay("#bAlika? ")
sm.setParam(37)
sm.sendSay("#face5##h0#...")
sm.setParam(57)
sm.sendSay("#bIt's late. What is it? ")
sm.sendDelay(500)
sm.forcedMove(False, 400)
sm.sendDelay(500)
sm.setParam(37)
sm.sendNext("#face5#Nothing. I had a nightmare, so I wanted to clear my head. I suppose I wandered too far. ")
sm.setParam(57)
sm.sendSay("#bYou should stay inside the camp. It's dangerous out here. ")
sm.setParam(37)
sm.sendSay("#face5#I know... I... Could I sit here for a bit before I go back? ")
sm.sendDelay(500)
sm.moveNpcByTemplateId(9400580, True, 90, 80)
sm.playSound("Sound/PL_MONAD.img/EP1/ACT2/footstep1", 128)
sm.sendDelay(1000)
sm.playSound("Sound/PL_MONAD.img/EP1/ACT2/footstep2", 128)
sm.forcedMove(False, 78)
sm.sendDelay(2000)
sm.showNpcSpecialActionByTemplateId(9400580, "sit", -1)
sm.sendDelay(500)
sm.forcedAction(29, 9999999)
sm.sendDelay(2000)
sm.setParam(57)
sm.sendNext("#b... ")
sm.setParam(37)
sm.sendSay("#face0#Are you well-rested? You could simply assign this task to the knights, you know. ")
sm.setParam(57)
sm.sendSay("#bI'm fine. I wanted to give the Afinas Dispatch a chance to rest. They've been going non-stop since the attack. ")
sm.setParam(37)
sm.sendSay("#face0#Indeed. They are very committed people. ")
sm.setParam(57)
sm.sendSay("#b... ")
sm.setParam(37)
sm.sendSay("#face0#Oh, I meant to ask you... Did you ever find out who sent the letter? ")
sm.setParam(57)
sm.sendSay("#bNot yet. It doesn't seem to be anyone from Kaptafel. ")
sm.setParam(37)
sm.sendSay("#face1#Well then... Since you've done so much for us, #h0#, let us help you find the sender. ")
sm.setParam(57)
sm.sendSay("#bI don't need anything in return, Alika. I'm doing this because it's the right thing to do. ")
sm.setParam(37)
sm.sendSay("#face1#I know, and that's why I want to help you. ")
sm.sendSay("#face1#You deserve our gratitude. ")
sm.setParam(57)
sm.sendSay("#b...Thanks. Little awkward, but thanks. ")
sm.setParam(37)
sm.sendSay("#face1#Hee hee.")
sm.sendDelay(3000)
sm.setParam(57)
sm.sendNext("#bSo... What was your dream about? ")
sm.setParam(37)
sm.sendSay("#face0#...Ah. ")
sm.setParam(57)
sm.sendSay("#bOh, sorry. If you don't want to talk about it, forget I asked. ")
sm.setParam(37)
sm.sendSay("#face5#Let's discuss that another time. ")
sm.sendSay("#face0#You know what's strange? I know this place is dangerous, and that we're in terrible danger. But right now, right here... this is nice. ")
sm.sendSay("#face0#Brisk wind, clear sky, beautiful aurora... ")
sm.sendDelay(500)
sm.sendDelay(7000)
sm.sendDelay(1000)
sm.sendNext("#face1#It really helps me clear my mind. ")
sm.setParam(57)
sm.sendSay("#bYou're not cold? ")
sm.setParam(37)
sm.sendSay("#face5#Oh, I am. But if anything it makes me feel more alive. ")
sm.sendSay("#face0#I used to wake up from my nightmares in an empty room, night after night. But tonight, I awoke to a tent full of people sleeping. ")
sm.sendSay("#face0#Being around all those peaceful sleepers brought me so much relief. ")
sm.sendSay("#face0#And then, when I stepped outside, there was the aurora blanketing the sky in soft light. ")
sm.sendSay("#face0#...And there was you, #h0#. ")
sm.sendSay("#face1#Don't think too much of it. I'm just... so glad you're here. ")
sm.setParam(57)
sm.sendSay("#b...It's still late. You should get some sleep while you can. ")
sm.setParam(37)
sm.sendSay("#face0#I'll do that. Tomorrow will be another tough journey, won't it? ")
sm.sendSay("#face0#I hope things go as well as they did today. ")
sm.sendDelay(1000)
sm.resetNpcSpecialActionByTemplateId(9400580)
sm.sendDelay(250)
sm.sendNext("#face1#So... I'll head back, then. See you in the morning, #h0#.")
sm.sendDelay(1000)
sm.flipNpcByTemplateId(9400580, False)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400580, False, 300, 80)
sm.sendDelay(500)
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.sendDelay(500)
sm.lockInGameUI(False, True)
sm.completeQuestNoCheck(64040)
sm.startQuest(64041)
sm.createQuestWithQRValue(64006, "WC=7;k1=0;k2=0;k3=0;speed=40;man=200;prog=0;Pt=CaravanP1_chk15;Ec=0;max=16;weather=3;food=240")
sm.createQuestWithQRValue(64006, "WC=7;k1=0;k2=0;k3=0;speed=40;man=200;prog=0;Pt=CaravanP1_chk15;Ec=0;max=0;weather=3;food=240")
sm.createQuestWithQRValue(64006, "WC=7;k1=0;k2=0;k3=0;speed=40;man=200;prog=0;Pt=CaravanP1_chk15;Ec=0;max=0;weather=3;food=320")
sm.createQuestWithQRValue(64006, "WC=7;k1=0;k2=0;k3=0;speed=40;man=200;prog=0;Pt=CaravanP1_chk15;Ec=0;max=0;weather=0;food=320")
sm.createQuestWithQRValue(64006, "WC=0;k1=0;k2=0;k3=0;speed=40;man=200;prog=0;Pt=CaravanP1_chk15;Ec=0;max=0;weather=0;food=320")
sm.createQuestWithQRValue(64007, "happy0=100;happy1=100;happy2=100;happy3=100;man0=56;man1=32;man2=38;man3=73")
sm.createQuestWithQRValue(64006, "WC=0;k1=0;k2=0;k3=0;speed=40;man=199;prog=0;Pt=CaravanP1_chk15;Ec=0;max=0;weather=0;food=320")
sm.warp(867200551)