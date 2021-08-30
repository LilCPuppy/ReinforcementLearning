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
Q^*(a_k)<img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/518e156ac12070b671260a54b4071da3.svg?invert_in_darkmode" align=middle width=29.75569574999999pt height=21.68300969999999pt/><img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/40366d2e4e6730ae3512b2f0ef1035f7.svg?invert_in_darkmode" align=middle width=132.72481365pt height=24.65753399999998pt/><img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/733ad4f44db3c437cdbc4d9c95dc0cd6.svg?invert_in_darkmode" align=middle width=700.2747246pt height=282.55708469999996pt/>Q^*(a_k)<img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/021f445291a88eb86263c1de625608d4.svg?invert_in_darkmode" align=middle width=248.1538158pt height=22.831056599999986pt/>a_k<img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/65fd351951c3b7990cba6b13152c6483.svg?invert_in_darkmode" align=middle width=60.23236559999998pt height=22.831056599999986pt/>m_k<img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/58ccb712b68533f94c56dfc23b3b7124.svg?invert_in_darkmode" align=middle width=247.46941064999993pt height=24.7161288pt/>Q^*(a_k)<img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/46b3be68e89f85e71a2e9e68ff86a138.svg?invert_in_darkmode" align=middle width=25.526955299999994pt height=14.15524440000002pt/><img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/f85ea34f244e5dda5e29ff1ee6ed12c7.svg?invert_in_darkmode" align=middle width=224.8934094pt height=57.53473439999999pt/><img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/7eef423f5a34f70e858abcde4cb76803.svg?invert_in_darkmode" align=middle width=54.794651999999985pt height=39.45205439999997pt/>Q_0(a_t):=0$ (or some other default value).
