---
title: How to keep up Good Habits Without Burning Out 
sub_title: Using Psychology and Machine Learning
author: Nathan Laundry
options:
  end_slide_shorthand: true
  incremental_lists: true
---

# Disclaimer
> This is not an Applied ML Workshop

You'll find this interesting IF:
- You're curious about how a CS degree is used in Research
- Examples of topics you can do research in
- The Psychology of behaviour change

---
# Who Am I?

- First year PhD student at UofT in Human Computer Interaction 
- Huge Vim and Plain text nerd (this presentation is written in markdown and presented from the terminal)
- Writer/Blogger about Psychologically backed strategies for improving well-being and philosophy of ethics i.e. what is well-being and living a good life?

> https://alittlebetter.org

> https://nathanlaundry.com 

> https://medium.com/@nathan.laundry

> Or add me on Linkedin (my linkedin sucks tho)

---

# Why I do my Research

- Myself and many of my loved ones have struggled with mental health
- Mental Health treatments are mostly: 
    - building a set of healthy habits 
    - tearing down bad ones
- Building and Breaking Habits is hard 

> Goal: How can we help people build Good Habits without the constant Exhaustion caused by relying on Discipline?
- 
---
# Story Time
## Lockdown Screen-time go up


- **Pre-Lockdown Phone Use**
  - Gradual increase unnoticed
  - Time taken from other activities (friends, studying, coding, cooking)

- **2022 Stats Revelation**
  - Reached 4 hours/day on phone
  - Work emails, but mostly social media (Reddit, Instagram)
  - I was **doom-scrolling**

---

# Story Time
## Screen-time sucks and I couldn't stop myself

- **Need for Change**
  - Research links high phone use to:
    - Negative mental health outcomes
    - Poor academic performance
    - Decreased well-being

- **Struggle to Reduce Use**
  - Initial efforts to cut down failed
  - Temporary success followed by relapse

---

# Story Time
## One-Sec - The First Strategy

- **Discovery of One Sec App**
  - Intervenes when accessing blocked apps
  - Simple prompt: "Do you really wanna do this?" with a 5-second delay
  - Significant reduction in screen time (down by 1 hour)

- **Effective Small Interventions**
  - Realized small changes can have a big impact
  - Screen-time reduced sustainably

--- 
# Story Time
## Stacking Strategies

- **Stacking Additional Strategies**
  - Inspired by "Atomic Habits"
  - Strategies included:
    - Black and white screen
    - Turning off notifications
    - Uninstalling apps
  - Screen-time reduced to 30 minutes/day (mostly Spotify, texting, work emails)

---
# Story Time
## Choice Architecture, Nudges, and Interventions


- **Academic Curiosity**
  - One-Sec was a Research Prototype
  - Built on the concept of Choice Architecture and Self-Nudging

- **Today's Topic**
  - Psychology of Nudges
  - Application of machine learning (adaptive A/B Testing) by FAANG companies to identify and select successful self-nudging strategies

---

# Topic Overview

## Background

- Why Willpower and Motivation aren't sustainable as the ONLY driver of self-improvement
- How Choice Architecture and Nudges make it easier to make "Good Choices" and less likely you'll make "Bad Choices"
- The Benefits of stacking Self-Nudges

## My Research
- Building Applications to support self-directed Choice Environment Architecture
    - How you can Stack Nudges (building an ecosystem of nudges that help you)
- How Machine Learning can help you identify which Nudges work and which don't
    - Adaptive A/B Testing with Contextual Multi-Armed Bandits

---
# Topic Overview

> Goal: Help people create sustainable positive behaviours to support their well-being

- Problem: Willpower is limited
    - SOLUTION: Nudges don't require willpower
- Problem: Sometimes one nudge isn't enough to consistently change your behaviour
    - SOLUTION: Stack self-nudges
- Problem: Which Nudges Do we Choose and How do we know they're effective?
    - SOLUTION: A/B Testing

---
# PROBLEM #1: Willpower runs low when we're tired

## What is Willpower?


> Willpower: our ability to exercise self-control. 

Why do we have to control ourselves?

---
# Problem #1: Willpower runs low when we're tired
## Two thinking systems: System 1 and 2 

- **System 1**
  - Fast, automatic, and intuitive
  - Operates unconsciously
  - Handles everyday decisions and routine tasks
  - Brings in biases and heuristics that were adaptive in evolutionary history but not always helpful now
  - Examples of System 1 biases:
    - **Hyperbolic Discounting**: Preferring smaller, immediate rewards over larger, future rewards
    - **Preference for High-Calorie Foods**: Craving fatty, sugary foods that were scarce and vital for survival in ancient times

- **System 2**
  - Slow, deliberate, and analytical
  - Requires conscious effort and attention
  - Handles complex decisions and problem-solving
  - Examples: solving math problems, planning a trip

---
# Problem #1: Willpower runs low
## Systems in Conflict

- **Willpower as System 2 to Override System 1**
    - set long term goal: succeed on exam so I can graduate
  - Recognize impulsive desires - play league cause it's more fun than studying
  - Pause and engage System 2 to evaluate long-term goals and consequences
  - Apply deliberate effort to make a choice aligned with those goals

The Research shows us this:
1. It's harder to exercise self-control when you're already tired
2. It's tiresome to exercise self-control

What this means:
> You will burn yourself out if you rely ONLY on willpower all day long

---


# The Power of Choice Architecture and Nudges

> Choice architecture: the way options are presented to influence decision-making by taking advantage of biases in human thinking

> Nudge: subtle changes in how choices are presented to encourage specific choices without restricting others.

---
# The Power of Choice Architecture and Nudges
### Example Biases to Create Effective Nudges


In general: more obvious, less effort, less thought

1. **Default Bias**
   - **Description**: Tendency to go with pre-set options because they require less effort.
   - **Nudge**: Make healthy choices the default option.
   - **Example**: Placing the fruit at eye level and subtly hiding the chips in the school cafeteria.

2. **Reducing Friction**
   - **Description**: Making desirable behaviors easier to perform by removing obstacles.
   - **Nudge**: Provide timely reminders and easy access to resources.
   - **Example**: Providing a weekly reminder text to students with a link to the studying materials.

3. **Automaticity**
   - **Description**: Making behaviors automatic to reduce the need for active decision-making.
   - **Nudge**: Set up systems that automatically promote good habits.
   - **Example**: Your company automatically invests 10% of each paycheck into your retirement fund.



--- 
# Self-Nudging

> Self-Nudging: selecting and applying nudges to yourself. Architecting your Choice Environment on your own to achieve certain behavioural changes.

## Paternalistic Nudges 
1. Food Choice (salience): Placing the fruit at eye level and subtly hiding the chips in the school cafeteria
2. Studying Choices (reducing friction): Providing a weekly reminder text to students with a link to the studying materials
3. Financial Choices (automaticity): Your company automatically invests 10% on each paycheck into your retirement fund

## Self-Nudge Alternatives
1. Food Choice (salience): Placing the fruit at eye level and subtly hiding the chips in your home kitchen
2. Studying Choices (reducing friction): Leaving your textbook open on your desk so that you don't have to go get it out
3. Financial Choices (automaticity): Setting up automatic investments on your investment app


--- 
# Stacking Self-Nudges


### Stacked Self-Nudge Routine

1. **Set a Default Study Time**: Schedule a daily study session from 6 PM to 7 PM.
2. **Prepare Your Study Environment**: Organize all materials and create a dedicated study space.
3. **Reward Yourself**: Plan a small reward after each study session, such as a favorite snack.
4. **Join a Study Group**: Study with peers or a buddy to stay motivated.
5. **Visualize Losses**: Think about the negative consequences of not studying, such as failing the exam.
6. **Start Small** (Anchoring bias): Begin with a 10-minute review session and gradually increase the duration.

By combining these nudges, you create a supportive environment and system that makes it more likely you'll stick to your study routine, leading to consistent study habits and better preparation for your exam.

---

# A/B Testing Self-Nudges

Maybe some of these don't work for you

1. **Join a Study Group**: Study with peers or a buddy to stay motivated.
2. **Visualize Losses**: Think about the negative consequences of not studying, such as failing the exam.

Maybe you don't know what will and what won't work for you
That's where A/B Testing comes into play

---

# Nudges Recap

1. Willpower is limited and the more tired we are, the harder it is to exert it
2. Nudges help us make "Better Choices" without engaging willpower BUT DO NOT make the "bad choice" impossible
    - Nudges work by:
        - making the good choice stand out (putting the fruit at eye level)
        - subtly hiding the bad choice (putting the chips at the back of the pantry)
        - making the good choice automatic (automatic investing)
    - Nudges have limitations: applied by someone else
3. Self-Nudges 
    - Give us control
    - We decide what our goals are and our strategies
4. Stacking Nudges 
   - sometimes one nudge isn't enough
   - we can combine a series of nudges to greater effect
   - But which nuges do we choose?

---
# Introduction to A/B Testing

## How does A/B Testing work?
>  A/B Testing: comparing two versions of something, webpage, app, or two nudges to see which one performs better.


- **How It Works**
  - **Create Variations**: 
      - Nudge A - reminder message when you've been on an app for over 5 minutes
      - Nudge B - total app lockout
  - **Divide the Group**: Randomly split your audience into two groups, each experiencing one nudge.
  - **Run the Experiment**: Track phone usage during study times
  - **Find the Winner**: See which nudge resulted in less phone usage.
   
---
# Introduction to A/B Testing
## Use Cases
- **Where You Can Use It**
  - **Cutting Phone Use**: Test nudges to keep phones away while studying.
  - **Healthier Habits**: Compare nudges to encourage exercise or better eating.
  - **Productivity Boosts**: Evaluate nudges to improve focus at work.

---
# Introduction to A/B Testing
## Limitations of Traditional A/B Testing

- **Challenges**
  - **Needs Enough People**: Requires a good number of participants for solid results.
  - **Takes Time**: Needs time to plan, run, and analyze the tests.
  - **50/50 Allocation:** Shift from 50/50 to 100/0 
--- 
# Adaptive A/B Testing at Meta

- **What is Adaptive A/B Testing?**
  - Adaptive A/B Testing is a dynamic approach to testing that adjusts the allocation of users to different versions based on real-time results.

Imagine we're A/B Testing a new login page on Facebook

- Traditional A/B Testing = 50/50
- Adaptive A/B Testing = X/100 - X

Where X is somehow proportionate to the amount of evidence we've collected SO FAR that Condition A is better than Condition B

--- 

# Adaptive A/B Testing at Meta

> Bandit Algorithm: A class of algorithms that balance Explore Exploit

- **Explore-Exploit Problem**: The dilemma of choosing between trying new options (exploration) to discover their potential benefits and sticking with known options (exploitation) to maximize immediate rewards.
- **Goal**: To find an optimal balance that maximizes overall long-term rewards.

--- 

# Adaptive A/B Testing for Mental Health Interventions

- **Explore-Exploit Problem**: Deciding whether to try new mental health interventions (exploration) to discover their effectiveness or to continue using known interventions (exploitation) that have shown some success.

### Example

1. **Scenario**:
   - You are testing two mental health interventions to reduce anxiety:
     - **Intervention A**: One-Sec's 5s before allow
     - **Intervention B**: Full App Block

2. **Initial Phase (Exploration)**:
   - You don't know which intervention is more effective.
   - Randomly assign equal numbers of users to Intervention A and Intervention B.
   - Collect data on screen-time


3. **Data Collection**:
   - Measure the reduction in screen-time.

---
# Adaptive A/B Testing for Mental Health Interventions

- **Explore-Exploit Problem**: Deciding whether to try new mental health interventions (exploration) to discover their effectiveness or to continue using known interventions (exploitation) that have shown some success.

1. **Thompson Sampling (Balancing Exploration and Exploitation)**:
   - **Sampling**: For each new user, sample a probability of success (screen-time) from the Beta distribution for both interventions.
   - **Selection**: Assign the user to the intervention with the higher sampled probability of success.
   - **Update**: After observing the user's response, update the Beta distribution for the selected intervention based on whether it succeeded or failed in reducing screen-time.

2. **Iterative Process**:
   - Over time, as more data is collected, the algorithm will:
     - Continue to explore by assigning some users to both interventions to gather more data.
     - Exploit by assigning more users to the intervention showing better results.

3. **Outcome**:
   - The algorithm adaptively learns which intervention is more effective at reducing screen-time.
   - Eventually, it will favor the better-performing intervention while still occasionally testing the other to ensure it remains optimal.

---
# Multi-Armed Bandits
But we want to A/B test a *whole stack of nudges* on *ourselves*

> Allocation Probability: A + B + C + D = 100%

1. **Set a Default Study Time**: Schedule a daily study session from 6 PM to 7 PM.
2. **Prepare Your Study Environment**: Organize all materials and create a dedicated study space.
3. **Reward Yourself**: Plan a small reward after each study session, such as a favorite snack.
4. **Join a Study Group**: Study with peers or a buddy to stay motivated.
5. **Visualize Losses**: Think about the negative consequences of not studying, such as failing the exam.
6. **Start Small** (Anchoring bias): Begin with a 10-minute review session and gradually increase the duration.


--- 

# Contextual Multi-Armed Bandits

> Contextual Variable: Mood, Energy, Motivation, etc.

With a Contextual Multi-armed Bandit we have a different set of allocation probabilities for each Context

> High Intrinsic Motivation: A + B + C + D = 100%

> Low Intrinsic Motivation: W + X + Y + Z = 100%

1. **Set a Default Study Time**: Schedule a daily study session from 6 PM to 7 PM.
2. **Prepare Your Study Environment**: Organize all materials and create a dedicated study space.
3. **Reward Yourself**: Plan a small reward after each study session, such as a favorite snack.
4. **Join a Study Group**: Study with peers or a buddy to stay motivated.
5. **Visualize Losses**: Think about the negative consequences of not studying, such as failing the exam.
6. **Start Small** (Anchoring bias): Begin with a 10-minute review session and gradually increase the duration.

--- 

# Bringing it All Together

How do we make use of Contextual Multi-Armed Bandits to help people Figure out what set of nudges help them?

1. Help people come up with a set of Nudges for a given behaviour/habit they want to improve
2. Deploy digital nudges (text prompts, app stuff, etc.) to the user
    - IF Contextual -> get the contextual variable from the user first
3. The user enters back if the nudge worked or not
4. The ML algorithm overtime learns which nudges work for you and which don't in different contexts too
5. Cut out nudges that don't work, keeping nudges that do, and introducing new nudges that might work
6. Repeat 1-5 until your environment deeply supports the habits you want to build and helps you avoid the habits you don't

---

# To Learn More

- For more about nudges and strategies for self-improvement sign up for my newsletter at: https://alittlebetter.org

> https://alittlebetter.org

> https://nathanlaundry.com 

> https://medium.com/@nathan.laundry
