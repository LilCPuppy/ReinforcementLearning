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

### Softmax Action Selection

The last segment detailed a method for our agent to choose an *action*.  Another way to pick an action is to assign each choice a probability.  For example, say we pick
action <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/44bc9d542a92714cac84e01cbbb7fd61.svg?invert_in_darkmode" align=middle width=8.68915409999999pt height=14.15524440000002pt/> with probability
<p align="center"><img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/725c686ee859eb0f6b9779685bf7249d.svg?invert_in_darkmode" align=middle width=139.36113015pt height=42.21837675pt/></p>
where <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/4bdc8d9bcfb35e1c9bfb51fc69687dfc.svg?invert_in_darkmode" align=middle width=7.054796099999991pt height=22.831056599999986pt/> iterates over all the possible actions, and <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/0fe1677705e987cac4f589ed600aa6b3.svg?invert_in_darkmode" align=middle width=9.046852649999991pt height=14.15524440000002pt/> corresponds to the temperature.  High temperatures cause actions to become close to equiprobable, and low temperatures cause a greater difference in selection probability.  In fact, as <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/b1469e5a5fe09bce59fa71176d5367b0.svg?invert_in_darkmode" align=middle width=42.83664329999999pt height=21.18721440000001pt/>, the softmax action selection becomes the same as greedy action selection.

It's unclear whether <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/7ccca27b5ccc533a2dd72dc6fa28ed84.svg?invert_in_darkmode" align=middle width=6.672392099999992pt height=14.15524440000002pt/>-greedy action selection or softmax action selection is more effective.
The <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/7ccca27b5ccc533a2dd72dc6fa28ed84.svg?invert_in_darkmode" align=middle width=6.672392099999992pt height=14.15524440000002pt/> methods are easier to tune and dynamically change, whereas the softmax selection means picking <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/0fe1677705e987cac4f589ed600aa6b3.svg?invert_in_darkmode" align=middle width=9.046852649999991pt height=14.15524440000002pt/>, hence needing to know how likely action values and powers of <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/8cd34385ed61aca950a6b06d09fb50ac.svg?invert_in_darkmode" align=middle width=7.654137149999991pt height=14.15524440000002pt/>.

## Evaluation vs. Instruction

The n-armed bandit problem gives us an example of purely evaluative feedback.
In reinforcement learning, the "feedback" is independent of the action.  So it's not "real" feedback.  Supervised learning algorithms try to configure/shape themselves to their environment - but they cannot learn to control or influence their environments.

### Example

Let's dig into these differences by emphasizing an example given by Sutton and Barto.  Consider the n-armed bandit problem with 2 arms (i.e. <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/556c0111ccb62a5da0f266e044f76810.svg?invert_in_darkmode" align=middle width=48.222926399999984pt height=21.18721440000001pt/>).  Each action has two rewards, success and failure (binary actions).
In a supervised learning setting we might infer an action was "correct" if you got success, and if you got failure, you may assume the *other* action was "success".
Then as you play, you can tally how many times an action was inferred to be correct, and you pick the action based on the tallys (more tallys = higher chance of winning).

Suppose the actions we're deterministic (i.e. they're assigned be either completely success or completely failure), then this algorithm would never be wrong.  After a single choice, we would know exactly what action we would fix on.  But if the actions were stochastic (each action has a *probability* of success), then this is certainly not the case.

In this case, the supervised learning approach would work *only* if the probabilities fulfill the assumption that one action is bad (failure) and the other is good (success).  Hence, we need one action will probability of success greater than <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/47d54de4e337a06266c0e1d22c9b417b.svg?invert_in_darkmode" align=middle width=6.552545999999997pt height=27.77565449999998pt/>, with the other having a probability of success less than <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/47d54de4e337a06266c0e1d22c9b417b.svg?invert_in_darkmode" align=middle width=6.552545999999997pt height=27.77565449999998pt/>.  Then, the algorithm would fixate on the better choice, and we would win.

But if *both* were good (probability of success over <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/47d54de4e337a06266c0e1d22c9b417b.svg?invert_in_darkmode" align=middle width=6.552545999999997pt height=27.77565449999998pt/>), or *both* were bad (probability of success less than <img src="https://github.com/LilCPuppy/ReinforcementLearning/blob/main/sutton_and_barto/chapter_two/svgs/47d54de4e337a06266c0e1d22c9b417b.svg?invert_in_darkmode" align=middle width=6.552545999999997pt height=27.77565449999998pt/>), than the supervised learning methods how no way of determining which choice is *better* (or *worse*).  In the *both bad* case, the algorithm would likely pick a failing action, and always assume the other action is better.  When it picks the other option (and *also* gets failure), it would flip back to the first choice.  This cycles, and we get an oscillating algorithm that cannot truly find the better choice of the two.  In the *both good* case, we would quickly fixate on a single action (since it usually wins, the other must usually lose, right?), typically, the first action picked.

So what does a reinforcement learning approach look like?