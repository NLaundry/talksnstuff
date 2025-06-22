What is this talk about?

- A/B Testing Self-Nudges


Do I want to start with a personal story like me-search?

Do I want to start with an example?

Example






















---

https://docs.google.com/presentation/d/1FpNMFXVu6aK3CaPEF6SaP4MdS8qAlx4iKtig4qg2WxA/edit#slide=id.g25199db24cc_0_403

What do I want to talk about?

- How adaptive AB testing is used in industry (META)
    - How this is great for industry and could help research but needs to be adapted
    - Over-exploitation (we get a handful of good data points, it starts over assigning, we don't get a lot of data for the other points, and that makes it hard to draw inference)
    - There's the problem: In science we have to be able to make deeply trust-worthy influences, the costs of over-stating are high. In business, you don't really need to know WHY or if it's 100% TRUE, you're optimizing for profits.
- I need to talk about the ML and personalization aspect
- methods of deployment
- How I'm applying it to my research



Slide topics: 

Start with an application:
- Problem: different people respond differently to different kinds of treatment - this can be influenced by cultural background and values, gender, socio-economic status, but also less "stable" factors like, mood, energy levels for the day, and more.
- Imagine we could use explainable machine learning algorithms to personalize scalable treatments based on those contextual factors .
- That's what we do at the Intelligent Adaptive Interventions lab run by my supervisor Joseph Jay Williams.

EXAMPLE:
- One way we're applying this is in text (SMS) based CBT interventions. 
- What we do is consult experts in Cognitive behavioural therapy to recommend a variety of strategies and prompts that might help a person struggling with mild depression or anxiety. 
- Three examples might be:
    - 1. a gratitude reflection prompt: "take 5 minute to list 3 things you're grateful for today and the positive impact it had on you todatake 5 minute to list 3 things you're grateful for today and the positive impact it had on you today."
    - 2. a social prompt: "schedule a 10 minute call with a loved one today"
    - 3. Cognitive Restructuring: "You've mentioned in the past you feel as though you 'fail at everything you try to do', can you think of 3 times you actually succeeded at something you tried, no matter how trivial or small that thing seems?"

Here we have 3 common CBT techniques that we can prompt someone to try over SMS. Now, let's say we also take into account a self-report about their mood (1 being terrible, 5 being elated, extremely happy.) energy 1-5 Exhausted to Bursting with energy. We may form some hypotheses like "people are more likely to be willing to try a social activity like a call on days when their energy is higher." OR "people benefit from gratitude reflection prompts more when they report low moods. It shows them they do have things to be grateful for." OR we may even hypothesize that cognitive restructuring can be harmful when it's unguided and someone is already experiencing low mood, because it may cause them to further reinforce a harmful belief if say they can't think of something they've succeeded at.

Adaptive ABTesting with contextual factors like mood, energy levels, and other factors can give us a way to make sure, over time, we provide people with the interventions (that's what we call these sorts of targetted attempts at adjusting mindset or behaviour) that are most likely to have the best impact on them at any given time, and phase out interventions that are unhelpful.

#Pause for Questions.

# Machine Learning - ABTesting and Contextual Multi-Armed Bandits

So now, if you're keen, you're asking the question: HOW?
What kinds of machine learning do we do? How do we test our hypotheses?

1. What is ABTesting + Randomized Control Trials
2. Where the ML comes in: What is adaptive ABTesting?
3. How is it used in industry - AX at Meta: Goes faster than a traditional RCT but not "scientifically valid" which is fine for products but not fine if you're testing psychological theories and treatments.
4. Finding the middle ground: Inference and Speed + certainty and deployment

#TODO: Get this from the SIPS presentation
# Choice Architecture, Nudges, and Interventions - tools for behaviour change


# Merging Interventions and ML via Digital Deployment


# My Research - Systematic ABTesting of self-nudges

I'm interested in creating applications that help people figure out over time what they want to change about their behaviour, and what ecosystem of nudges and interventions is going to work best for them given different factors like their mood, energy levels, their values, the type of goal they're setting, and so on.

I've been testing this on myself for years! 



