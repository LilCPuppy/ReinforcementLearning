# Chapter Two

## Introduction

Test this formula.
<p align="center"><img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/980caffcc884d89bb3dc24e04b8d678a.svg?invert_in_darkmode" align=middle width=113.49264465pt height=32.990165999999995pt/></p>

The most important feature about reinforcement learning from other types of the learning si that it uses training data to *evaluate* actions rather than
*instructing* the agent on what to do with correct actions.
This creates the need for exploration, since "purely evaluative feedback indicates only how good the action is, but not whether it's the best or worst action
available".  Another key distinction between evaluative vs. instructive feedback is as follows:
  * Evaluative feedback depends entirely on the action taken, whereas
  * Instructive feedback is *independent* of the action taken (think making an arbitrary chess move, then being told which was actually the *right* one).  In a
  sense, this is hardly feedback at all...
 
## The N-Armed Bandit

A motivating example used by Sutton and Barto is the n-armed bandit.  Suppose you are faced with a set of n different actions or choices
<div align=center>{a<sub>1</sub>,...,a<sub>n</sub>},</div>
and when picking an action, you recieve a reward signal chosen from a stationary probability distribution associated with that action,
<div align=center>{P<sub>a<sub>1</sub></sub>, ..., P<sub>a<sub>n</sub></sub>}.</div>

**Goal**: Maximize the reward signal over some discrete time.

An analogy to the n-armed bandit would be an n-armed slot machine, where each lever has some stationary probability distribution giving you some reward.  You want
to play the game to an extend where you can determine which are the **good** levers (i.e. associated with a probability distribution with a high expected value),
and play exclusively on these levers.

As we just mentioned, each lever (or arm/action) has an associated probability distribution, which has it's own expected value and variance.  This motivates a
definition.

**Definition**: The *value* of an action, a<sub>k</sub> (k = 1, ..., n), is the *expected value of P<sub>a<sub>k</sub></sub>*, denoted
Q<sup>&sext;</sup>(a<sub>k</sub>), i.e.
<div align=center>Q<sup>&sext;</sup>(a<sub>k</sub>) = &Eopf;(P<sub>a<sub>k</sub></sub>).</div>

Obviously, if we knew the expected values of all the distributions beforehand, there would be no issue, because we would pick the action with the highest value.
However, since we don't, we can only attain *estimates* of the values based on a historical record or picking an action.  Hence, we have a tradeoff: do we exploit
the levers we know?  Or do we explore and improve teh estimate of the levers that we don't?  Over a period of time, attaining the maximum reward may require a
combination of these.

This motivates the question, how should we estimate Q<sup>&sext;</sup>(a<sub>k</sub>)?  If at time t we have chosen an action a<sub>k</sub> m<sub>k</sub> time,
then it's intuitive to estimate Q<sup>&sext;</sup>(a<sub>k</sub>) as:
<div align=center>Q<sub>t</sub>(a<sub>k</sub>) = (<sup>1</sup> &#8260; <sub>m<sub>k</sub></sub>) (r<sub>1</sub> + ... + r<sub>m<sub>k</sub></sub>).</div>

We define Q<sub>0</sub>(a<sub>t</sub>) := 0 (or some other default value).
