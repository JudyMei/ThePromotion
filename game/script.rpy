#bg Images
image livingroom = "images/backgrounds/livingroom.jpg"
image bedroom = "images/backgrounds/bedroom wood.png"
image kitchen regular = "images/backgrounds/kitchen regular.jpg"
image office = "images/backgrounds/office.jpg"
image outside office = "images/backgrounds/outside office.jpg"
image office common = "images/backgrounds/office common.jpg"
image night town = "images/backgrounds/night town.jpg"
image night park = "images/backgrounds/night park.jpg"
image dinner = "images/backgrounds/restaurant.jpg"
image dinner seated = "images/backgrounds/restaurant2.jpg"
image kitchen new = "images/backgrounds/kitchen new.jpg"
image home hallway = "images/backgrounds/home hallway.jpg"

#Character Images
image mother work happy = "mother_work_happy.png"
image mother work sad = "mother_work_sad.png"
image mother work smile = "mother_work_smile.png"
image mother work annoyed = "mother_work_annoyed.png"
image mother work = "mother_work.png"
image dad home smile= "dad_home_smile.png"
image dad home= "dad_home.png"
image dad work= "dad_work.png"

image jess = "girl2.png"
image brother = "brother.png"

#Characters
define pov = Character ("[povname]", color="ffc0cb")
define d = Character ("Jim", color="0000ff")
define d_phone = Character ("On the Phone: Jim", color = "0000ff")
define j = Character ("Jess", color = "58a843")
define jon = Character ("Jonathon", color = "bf1d1d")
define c_phone = Character ("On the Phone: Charlie", color = "0000ff")

default povname = "Kate"

#Game starts here
init:
    $ confidence_points = 0
    $ negative_points = 0
label start:
# Day 1: 
    play music "airtone.mp3"
    show text "Day 1: \nMonday" at truecenter
    with dissolve 
    pause 1.5
    hide text 
    with dissolve
    $ povname = renpy.input("What is your name?")
    $ povname = povname.strip()
    
    if not povname: 
        $povname = "Kate"
    scene bedroom
    pov "zzzz... zzzzzz..." 
    pov "zzzzzzzzzzzz..."
    show dad home
    d "[povname], wake up!"
    "Jim nudges me awake"
    hide dad home
    menu:
        "Errrr... What time is it?":
            jump givetime
        "5 more minutes.":
            jump fivemin
        "[povname] can't come to the phone right now. Please leave a message after the beep...":
            jump phone
    show dad home
    label givetime:
        d "It's late, you gotta get ready for work."
        d "It's Day 1 of training for your new position at the bank! Exciting stuff, so lets get moving!"
        jump after_choices
    label fivemin:
        d "You gotta get going!" 
        d "You have training for your new position at the bank!"
        jump after_choices
    label phone:
        pov "..."
        pov "Beeeeeeeppp..."
        d "Haha, I was wondering if [povname] plans on getting up for work any time soon? She's gonna be late."
        pov "..."
        d "Come on! It's your first day training for your new position at the bank!"
        pov "[povname] will be up in 2 minutes."
        d "Haha okay, I'll be downstairs."
        jump after_choices
    label after_choices:
        hide dad home
    "I manage to drag myself out of bed and shuffle my way to the bathroom."
    pov "Jim! I'll meet you downstairs in a bit!"
    "I scramble to get ready."
    scene kitchen regular
    "As I head towards the kitchen I like what I smell..."
    show mother work happy at right
    pov "Good Morninggggg! What's cookin?"
    show dad home smile at left
    d "Well, someone's finally ready for the day!"
    d "Do you want an omelette?"
    hide mother work happy
    hide dad home smile
    menu:
        "Yes Please!":
            $ islate = True
            $ breakfast = True
            jump willbelate
        "Eh, I probably shouldn't":
            $ islate = False
            $ breakfast = True
            jump ontime
        "To Go?":
            $ islate = False
            $ breakfast = True
            jump togo
    label willbelate:
        "Jim places an omelette on the counter"
        show mother work sad
        pov "I'll probably be late for work today..."
        pov "Ugh, not good!"
        "I quickly shovel the food in my mouth"
        pov "I'm leaving! Love You!"
        jump work
    label ontime:
        show dad home
        d "Smart choice. You'll probably be late if you hang around any longer."
        "I head for the door."
        hide dad home
        show mother work
        pov "See you tonight, I'm heading out."
        jump work
    label togo:
        d "Yeah I'll pack you some breakfast. You should proabably get going soon."
        "Jim hands me some food in a container. I grab it and head for the door."
        show mother work smile
        pov "Thanks for the food! I'll see you tonight! Love You!"
        jump work
    label work:
        d "Love You! Have a great day at Training!"
        pov "Oh wait! You're taking the kids to school right?"
        d "Yup! I've got it under control. Don't worry!"
        pov "Remember 8am!"
        d "Yes I'll get them there by 8am haha"
        pov "Pick up is a 3pm!"
        d "I'll handle it, don't worry so much!"
        hide mother work
        show outside office
    if islate:
        "I pull up to work and I realize I'm late."
    else:
        "I arrive at work on time and head inside"
    show office
    "As I walk towards my office I see my boss heading my way."
    show mother work smile at right
    menu:
        "Sorry I'm late, won't happen again" if islate == True:
            jump atwork
        "Hey Charlie! I'm excited to get started!":
            jump atwork
        "Charlie! I was just gonna come looking for you!":
            jump atwork
    label atwork:
        if islate:
            "Charlie was not too happy that I was late for my first day of Training. I ensure them it won't happen again and they fill me in on today's schedule."
        else:
            "My boss fills me in on the day's training schedule"
    hide mother work smile
    scene night town 
    "7pm: After work..."
    "I head into town and call Jim"
    play sound "phone_call.mp3"
    "..."
    stop sound
    d_phone "Hey what's up?"
    pov "I just left work. It's a little late for me to cook dinner do you want me to pick us up some dinner instead?"
    d_phone "Yup thats fine."
    "I pick up some dinner and head home"
    scene livingroom
    show dad home smile at left
    show mother work sad at right
    d "Hey! How was work!"
    pov "Ugh I'm EXAUSTED. My boss threw so much information at me today that I don't even think I comprehended it all"
    d "At least a week from now we can call you 'Branch Manager' of Sunnyside Bank!" 
    pov "Haha that's not certain yet" 
    d "Ah, you'll get it!"
    pov "We'll have to see."
    hide dad home smile
    hide mother work sad
    scene kitchen regular
    "Jim and the kids head to the kitchen and chow down on some grub."
    show mother work annoyed
    pov "Ugh I still need to clean this kitchen tonight before I go to bed or its never gonna get done"
    "I clean up the kitchen after dinner while Jim puts the kids to sleep"
    stop music
#Day 2: 
    play music "airtone.mp3"
    scene black with dissolve
    show text "Day 2:\nTuesday" with Pause(1.5)
    scene black with dissolve
    scene livingroom
    show mother work at right 
    show dad home at left
    pov "Jim, I'm leaving!"
    d "Okay! Love you!"
    hide mother work 
    show mother work sad at right
    pov "Oh wait! Ummm..."
    pov "Can you pretty please take care of dinner tonight..."
    pov "After working all day the last thing I want to think about is what's for dinner. Cause then I have go into town and thats gonna be an extra hour to my commute."
    d "Of course, yeah don't even worry about it. I'll take care of dinner."
    hide mother work sad
    show mother work happy at right
    pov "OMG I love you! Thanks for being so flexible..."
    pov "Tell the kids I say goodbye when they wake up!"
    "Jim kisses me goodbye and I head out the door."
    hide dad home
    hide mother work happy
    scene outside office
    "Today at work I'm scheduled to be on the floor with all the Bank Tellers. This is the part of Training where I should be supervising... Let's see how this goes..."
    scene office common
    "Upon entering the Tellers Floor, I bump into one of the Tellers I used to work with."
    show mother work at left
    pov "Hey Jess, How's it going?"
    show jess at right
    j "Hi, It's going well! You're the person training for the Branch Manager Position right?"
    pov "Yup!"
    j "How'd you manage to get the offer? They don't usually hire women for positions like that"
    menu:
        "What do you mean?":
            $ confidence_points += 1
            hide mother work
            show mother work annoyed at left
            j "Oh, was that rude? I'm sorry..."
            j "What I meant to say was that we don't get many female Branch Managers around here. It's nice to see some change!"
            hide mother work annoyed
            show mother work smile at left
            pov "Haha... Yeah. Don't worry, I'll be one of the cool ones."
            hide mother work smile 
            show mother work at left
            jump after_jess
        "Errr... I don't know...":
            $ negative_points += 1
            pov "I showed interest in the position and when the opportunity came up, they offered me to try it out."
            j "Wow, props to you for being able to handle everything!" 
            jump after_jess
        "No better time to change the past then now!":
            $ confidence_points += 2
            j "Haha that's right! It's nice to see some change around here!"
            jump after_jess
    label after_jess:
        hide jess
        "Jess works her way to her desk."
        "That was such a weird question to ask your supervisor..."
    "I continue my rounds of the Tellers Floor. It feels weird to be on this side for once. I started out as a teller and now I'm the one supervising them." 
    show office
    "The day goes on as usual. I had a couple meetings in the morning and a couple after lunch. "
    "I've been noticing some glances at those meetings though. Not sure if that's because they've never seen me before or if they've seen me as a Teller and are confused why I'm here..."
    scene night park
    "After work:"
    "Jim noticed how hard of a day I had at work and decided to come meet me for a walk in the park."
    show dad home smile at left
    d "Hey!"
    hide mother work
    show mother work at right
    pov "OMG, you don't know how much I needed this walk. Thanks so much for coming!"
    pov "Are the kids with the nanny?" 
    d "No, I took them to your sister's."
    d "What are your thoughts? I can see those gears turning."
    hide mother work
    show mother work sad at right
    pov "Ah, I don't know..."
    d "You don't know what?"
    pov "If I can do this job..." 
    hide dad home smile 
    hide dad home
    show dad home at left
    d "Don't get all negative like that! You've been talking about this for the longest time! What happened?"
    pov "I don't know. Everyone at work acts all weird about it. I bumped into Jess today and she acted all wierd about me possibly getting the promotion."
    d "What'd she say?"
    pov "She was just saying how women usually don't get hired... blah blah blah."
    pov "And then at my meetings, I could feel the awkwardness and the glances from everyone."
    d "Aw come on. They're just not used to seeing you in this position. You used to work with Jess so just give her some time to adjust."
    d "And at the meetings, you're a new face, so once they start to get to know you it will be less awkward."
    d "Trust me, it will get better! You started this position a day ago so don't jump to conclusions so quickly okay?"
    pov "I guess you're right. I should hold off until the end of the week at least to make my decision."
    d "Yeah, lets see how it goes at the end of the week, and then we'll talk about it then. It's not gonna be an easy start, but it'll get better!" 
    hide mother work sad
    show mother work at right 
    "Jim and I take a stroll around the park and enjoy the night."
    pov "Ready to go pick up the kids? I feel like I haven't seen them in forever. I went from droping them off at school and picking them up every day to not doing any of it."
    d "Yup! Lets go get you your babies!" 
    stop music
#Day 3: 
    play music "airtone.mp3"
    scene black with dissolve
    show text "Day 3:\nWednesday" with Pause(1.5)
    scene black with dissolve
    scene kitchen regular
    show dad home at left 
    show mother work smile at right
    pov "Remember we have dinner with my brother tonight after work. Dress up a little!"
    pov "I haven't seen my brother in a while. We've been so busy so it'll be nice to catch up."
    d "Oh yeah, that was tonight! I'll drop the kids off at my mother's when I pick them up from school."
    pov "Sounds good! Please don't be late. We're meeting Jonathon at 8pm in the Diner Downtown."
    d "I won't!"
    pov "You're late to EVERYTHING!" 
    d "I won't be late tonight. Promise!"
    pov "Alright if you say so. See you tonight I gotta get going. Don't want to be late!"
    scene dinner
    "Later that night..."
    show dad work at left 
    show mother work at right
    "Jim and I arrive at dinner and wait for Jonathon to show up."
    d "Told you I would be on time."
    pov "You did tell me so. I really didn't believe you, haha"
    d "Oh! There's Jonathon!"
    show brother
    jon "Hey! How ya'll doing? Long time no see!"
    pov "We're doing good! Tired, for sure, but good."
    jon "Let's have a seat and chat!"
    scene dinner seated
    show brother
    show dad work at left
    show mother work at right
    jon "So... I hear you have a new job! How's it going?"
    pov "It's going well. I'm still training this week so my job really starts next week."
    jon "And Jim, what are you doing?"
    d "Just taking care of the kids, working from home, the usual."
    jon "Oh? Working from home?"
    d "Yeah, I'm doing freelance work from home. With [povname]'s new job, the hours are too long for us to both have 9-5 jobs."
    jon "Oh so you take the kids to school and pick them up while [povname] is at work?"
    d "Yeah, we had to make some switches to the daily routine to make everthing work."
    jon "[povname], you're fine with all this? I thought you liked your old job."
    hide brother
    hide dad work
    hide mother work
    menu:
        "Yeah I did, but this new position pays a lot better.":
            show brother
            show dad work at left
            show mother work at right
            jon "Oh, I see that. With two kids that pay raise must feel nice."
            d "Ohhh Yeah! Haha"
            pov "It's AMAZING!"
            jump dinner
        "Ehhh, not really. I didn't want to be a teller much longer":
           show brother
           show dad work at left
           show mother work at right
           jon "What? Really? I always thought you liked being a Teller."
           pov "I liked the Bank, not the position."
           d "She'd come home complaining everyday about the people she had to deal with."
           jump dinner
        "Yeah, but I wanted to try something new. Thought it was time for some change.":
          show brother
          show dad work at left
          show mother work at right
          jon "You're always itching for some change."
          pov "Yup! That's never changed."
          d "[povname] get's bored if she does the same thing over and over again."
          pov "Exactly, this job is much more interesting."
          jump dinner
    label dinner:
    jon "Props to you sis! All this change is definitely not for me" 
    jon "Props to you too Jim! If I were you i'd be itching to get out of the house. I would never be able to let my wife do all the work."
    d "What do you mean, 'Do all the work'?"
    jon "I mean, you're at home taking care of the kids and [povname] is out making the bucks!"
    jon "In typical families, the wife is usually taking care of the kids and you're the one going out and working."
    hide brother
    hide dad work
    hide mother work
    menu:
        "Yeah, we do things a little differently than most families, but we make it work and that's all that matters.":
            $ confidence_points += 1
            show mother work at right
            pov "I don't think we need to stick exactly to what other families do. A great opportunity came up for us and we took it!"
            jump after_dinner
        "Yeah I guess you're right...":
            $ negative_points += 1
            show mother work at right
            pov "At least this gives the kids more time to hang with Jim while I'm at work."
            show dad work at left
            d "Haha yeah!"
            jump after_dinner
        "Who cares what 'typical' families do? We do what works for us.":
            $ confidence_points += 2
            show mother work at right
            pov "That's right. I wanted the job and we could use the money, so I took the job."
            show dad work at left
            d "We make it work and that's all that really matters"
            jump after_dinner
    label after_dinner:
        show brother
        jon "You know, if one family can make it work its y'all. I couldn't name a stronger family."
        jon "Not my cup of tea, but i'm glad y'all make it work."
    show dad work at left
    pov "We should get going it's late. We still have to pick up the kids and I have work tomorrow morning."
    d "Oh gosh! How is it already 10pm!"
    jon "Time flies when you're with family!"
    hide brother
    hide mother work
    hide dad work
    "We pick up the kids and head home for the night"
    show livingroom
    show mother work at right
    show dad work at left
    pov "That was nice to catch up with Jonathon, but I knew he was gonna be skeptical about me taking this new job"
    d "Like I said yesterday, people just aren't used to it. Let them ease into it and i'm sure they'll be fine with it eventually."
    stop music
#Day 4: 
    play music "airtone.mp3"
    scene black with dissolve
    show text "Day 4:\nThursday" with Pause(1.5)
    scene black with dissolve
    scene livingroom
    show dad home at left
    show mother work at right
    d "Tomorrow's D-day! How you feeling about that?"
    hide dad home 
    hide mother work
    menu:
        "Great! I can't wait for this week to be over!":
            $ confidence_points += 1
            show mother work at right
            show dad home at left
            pov "I HATE training weeks. They throw all this information at you and then you never ever have to use it again."
            d "Yeah that's the typical job training for you"
            jump dday
        "Not sure still...":
            $ negative_points += 1
            show dad home at left
            show mother work at right
            d "Ah, you have today to still think about it. Just know that you're doing great!"
            pov "Thanks."
            jump dday
        "Surprisingly, quite good. I've been doing a lot of thinking about it.":
            $ confidence_points += 1
            show dad home at left
            d "That's good! I'm glad that you're feeling less tense about the situation."
            jump dday
    label dday:
        hide dad home 
        show mother work smile
        pov "I have a pretty light day at work today. I have a phone meeting with Charlie and some paperwork I need to finish but other than that, I'm pretty much done with training!"
    d "Wow! It really is coming to an end. I'm so excited for you!"
    scene outside office
    pov "Last day of training... Wow, FINALLY!"
    hide mother work smile
    scene office 
    play sound "phone_call.mp3"
    "..."
    stop sound
    show mother work at right
    c_phone "Hello? Hey [povname], how's it going?"
    pov "It's going well! Just finishing up the last of my paperwork"
    c_phone "That's great! Training is coming to an end, do you think you're ready to make a decision tomorrow?"
    pov "I'm gonna go home tonight and talk it out with my husband and we're gonna decide together"
    c_phone "Okay, perfect. I just wanted to set up a call with you to see how you were doing and if you had any questions for me."
    pov "I think I'm good for now, you've been pretty informative throughout the week."
    c_phone "Alright then, it was nice to talk with you and I look forward to hearing from you tomorrow!"
    "The meeting with Charlie ends and I finish up my paperwork for the day."
    scene outside office
    "I get off work early and head home for the day!"
    scene livingroom
    show mother work at right
    show dad home at left
    pov "I'm home!"
    d "Wow! You're home early!?"
    pov "Yeah, there wasn't much for me to do at work so I finished my paperwork and headed home."
    d "Did you want to talk about what you wanted to do?"
    pov "Yeah we should probably talk that out."
    d "Well what are you thoughts, positive, negative?"
    hide mother work
    hide dad home
    menu:
        "I think I want to go through with the position.":
            show mother work smile at right
            show dad home smile at left
            d "You do? That's great!"
            pov "Yeah I've been thinking hard about it, and its a great position, I enjoy what I do, and it could really help us out."
            pov "We'll need to make some more adjustments to our schedules but I'm sure we can make it work right?"
            d "Of course we can, we've already been so flexible this week with your new schedule, I'm sure we can make it work in the long run."
            jump accept
        "Eh, I don't know... It's all happening so fast.": 
            d "What do you mean."
            pov "It's a lot of change and things are moving really quickly. Maybe I stick to being a teller a little longer and later down the road if another opportunity comes along we can consider."
            pov "But right now, I just want to spend more time with the kids and not have too work so much."
            d "If that's how you feel, then that's what you should do. Whatever makes you happy."
            jump reject
    label accept:
        stop music
        play music "airtone.mp3"
        scene black with dissolve
        show text "1 Month Later" with Pause(1.5)
        scene black with dissolve
        scene home hallway
        show mother work happy at right
        show dad home smile at left
        pov "Wow! Look at this place! IT'S HUGE!"
        d "Isn't it!? I could've never imagined living in a place like this!"
        hide mother work happy at right
        pov "Look at this kitchen! Oh my gosh!"
        hide dad home smile at left
        scene kitchen new
        show mother work happy at right
        show dad home smile at left
        d "Oh wow, it's really amazing!"
        d "All your hard work paid off [povname]! This is all possible beacuse of you and your hard work."
        pov "Aw stop, it's a team effort, we work amazingly together and we were able to get to this point together"
        "Jim and I embrace and soak in the moment in our new home."
        jump end
    label reject:
        stop music
        play music "airtone.mp3"
        scene black with dissolve
        show text "1 Month Later" with Pause(1.5)
        scene black with dissolve
        scene livingroom
        show mother work at right
        show dad work at left
        "Jim heads off to work. I drop off the kids at school and also make my way to work. I have resumed my job as a Teller at the bank and Jim has resumed his 9-5 job as well."
        jump end
    label end:
        scene black with dissolve
        show text "Thank You for Playing!\nPlease take a look at the attached Works Cited page!" with Pause(3)
        scene black with dissolve
    return
