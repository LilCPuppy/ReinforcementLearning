# Chapter Two

## Introduction

The most important feature about reinforcement learning from other types of the learning si that it uses training data to *evaluate* actions rather than
*instructing* the agent on what to do with correct actions.
This creates the need for exploration, since "purely evaluative feedback indicates only how good the action is, but not whether it's the best or worst action
available".  Another key distinction between evaluative vs. instructive feedback is as follows:
  * Evaluative feedback depends entirely on the action taken, whereas
  * Instructive feedback is *independent* of the action taken (think making an arbitrary chess move, then being told which was actually the *right* one).  In a
  sense, this is hardly feedback at all...
 
## The N-Armed Bandit

A motivating example used by Sutton and Barto is the n-armed bandit.  Suppose you are faced with a set of n different actions or choices
<p align="center"><img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/c1143b0f8370f09ab2aa5f2eedc889be.svg?invert_in_darkmode" align=middle width=92.1479988pt height=29.58934275pt/></p>
and when picking an action, you recieve a reward signal chosen from a stationary probability distribution associated with that action,
<p align="center"><img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/e0d7c3decbc0846360538ecad8822751.svg?invert_in_darkmode" align=middle width=109.9361505pt height=29.58934275pt/></p>

**Goal**: Maximize the reward signal over some discrete time.

An analogy to the n-armed bandit would be an n-armed slot machine, where each lever has some stationary probability distribution giving you some reward.  You want
to play the game to an extend where you can determine which are the **good** levers (i.e. associated with a probability distribution with a high expected value),
and play exclusively on these levers.

As we just mentioned, each lever (or arm/action) has an associated probability distribution, which has it's own expected value and variance.  This motivates a
definition.

**Definition**: The *value* of an action, <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/74aca3669751ef853fc79fc195d7f108.svg?invert_in_darkmode" align=middle width=111.51778934999997pt height=22.831056599999986pt/>, is the *expected value of <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/3d02cfa2ebf67fc3d749503f621bd042.svg?invert_in_darkmode" align=middle width=24.048253349999992pt height=22.465723500000017pt/>*, denoted
<img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/5e33cd267d54d410646631613bdeca0b.svg?invert_in_darkmode" align=middle width=50.11504574999999pt height=24.65753399999998pt/>, i.e.
<p align="center"><img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/7fadd6b229faf3d9ae19d63452350edd.svg?invert_in_darkmode" align=middle width=132.72481365pt height=16.5387882pt/></p>

Obviously, if we knew the expected values of all the distributions beforehand, there would be no issue, because we would pick the action with the highest value.
However, since we don't, we can only attain *estimates* of the values based on a historical record or picking an action.  Hence, we have a tradeoff: do we exploit
the levers we know?  Or do we explore and improve teh estimate of the levers that we don't?  Over a period of time, attaining the maximum reward may require a
combination of these.

This motivates the question, how should we estimate <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/5e33cd267d54d410646631613bdeca0b.svg?invert_in_darkmode" align=middle width=50.11504574999999pt height=24.65753399999998pt/>?  If at time t we have chosen an action <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/888b6c2a06fc366952ac84a80c43f5f7.svg?invert_in_darkmode" align=middle width=15.95518319999999pt height=14.15524440000002pt/> a total of <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/8249cb78ba370605835603be00f4a356.svg?invert_in_darkmode" align=middle width=21.69913019999999pt height=14.15524440000002pt/> times,
then it's intuitive to estimate <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/5e33cd267d54d410646631613bdeca0b.svg?invert_in_darkmode" align=middle width=50.11504574999999pt height=24.65753399999998pt/> as:
<p align="center"><img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/0e4cbc6dbbde624ac44da7fb05a204ce.svg?invert_in_darkmode" align=middle width=228.56347139999997pt height=49.315569599999996pt/></p>

We define <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/7a17495e38fc50657d106e6a214cbb56.svg?invert_in_darkmode" align=middle width=82.33522439999999pt height=24.65753399999998pt/> (or some other default value).  We note that this estimate has some measure of "goodness" when observing that
<p align="center"><img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/d8ef0b340ffcf48ce9a6c967ac635d93.svg?invert_in_darkmode" align=middle width=172.7453046pt height=23.93607315pt/></p>

Clearly we don't want to play greedily, i.e. always pick an action <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/ea2934ecd8e8b0b206942ed2ba41c097.svg?invert_in_darkmode" align=middle width=15.424348499999988pt height=22.63846199999998pt/> such that,
<p align="center"><img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/85a1c0115cda1449036ffd1fb4fe5a82.svg?invert_in_darkmode" align=middle width=149.88989565pt height=16.438356pt/></p>
since we would never explore (beyond some action set we already know).

A way to promote this exploration is to have an <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/7ccca27b5ccc533a2dd72dc6fa28ed84.svg?invert_in_darkmode" align=middle width=6.672392099999992pt height=14.15524440000002pt/> chance to explore, and pick <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/307382c45247c31fca5424cd58742439.svg?invert_in_darkmode" align=middle width=149.88989565pt height=24.65753399999998pt/> the rest of the time.  These methods are call <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/7ccca27b5ccc533a2dd72dc6fa28ed84.svg?invert_in_darkmode" align=middle width=6.672392099999992pt height=14.15524440000002pt/>-greedy methods.  In the asymptotic case, we see that we will have to eventually pick every action an infinite number of times (weird to think about, huh?), and hence we maintain that
<p align="center"><img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/09e5a77d5ac6f19c1d2d0f03e119da5f.svg?invert_in_darkmode" align=middle width=99.7350288pt height=22.0041624pt/></p>

