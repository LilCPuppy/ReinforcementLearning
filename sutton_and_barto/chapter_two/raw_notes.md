# Chapter Two

## Introduction

The most important feature about reinforcement learning from other types of the learning is that it uses training data to *evaluate* actions rather than
*instructing* the agent on what to do with correct actions.
This creates the need for exploration, since "purely evaluative feedback indicates only how good the action is, but not whether it's the best or worst action
available".  Another key distinction between evaluative vs. instructive feedback is as follows:
  * Evaluative feedback depends entirely on the action taken, whereas
  * Instructive feedback is *independent* of the action taken (think making an arbitrary chess move, then being told which was actually the *right* one).  In a
  sense, this is hardly feedback at all...
 
## The N-Armed Bandit

A motivating example used by Sutton and Barto is the n-armed bandit.  Suppose you are faced with a set of n different actions or choices
$$
\Big\{a_1, \dots, a_n\Big\}
$$
and when picking an action, you recieve a reward signal chosen from a stationary probability distribution associated with that action,
$$
\Big\{P_{a_1}, \dots, P_{a_n}\Big\}
$$

**Goal**: Maximize the reward signal over some discrete time.

An analogy to the n-armed bandit would be an n-armed slot machine, where each lever has some stationary probability distribution giving you some reward.  You want
to play the game to an extend where you can determine which are the **good** levers (i.e. associated with a probability distribution with a high expected value),
and play exclusively on these levers.

As we just mentioned, each lever (or arm/action) has an associated probability distribution, which has it's own expected value and variance.  This motivates a
definition.

**Definition**: The *value* of an action, $a_k\;\;, k=1, \dots n$, is the *expected value of $P_{a_k}$*, denoted
$Q^*(a_k)$, i.e.
$$
Q^*(a_k):=E(P_{a_k}).
$$

Obviously, if we knew the expected values of all the distributions beforehand, there would be no issue, because we would pick the action with the highest value.
However, since we don't, we can only attain *estimates* of the values based on a historical record or picking an action.  Hence, we have a tradeoff: do we exploit
the levers we know?  Or do we explore and improve teh estimate of the levers that we don't?  Over a period of time, attaining the maximum reward may require a
combination of these.

This motivates the question, how should we estimate $Q^*(a_k)$?  If at time t we have chosen an action $a_k$ a total of $m_k$ times,
then it's intuitive to estimate $Q^*(a_k)$ as:
$$
Q_t(a_k) = \frac{1}{m_k}\;\Bigg(r_1+\dots+r_{m_k}\Bigg)
$$

We define $Q_0(a_t):=0$ (or some other default value).  We note that this estimate has some measure of "goodness" when observing that
$$
\lim_{m_k\to\infty} Q_t(a_k) = Q^*(a_k).
$$

Clearly we don't want to play greedily, i.e. always pick an action $a^*$ such that,
$$
a^* = \text{arg max}_a \;Q_{t}(a)
$$
since we would never explore (beyond some action set we already know).

A way to promote this exploration is to have an $\epsilon$ chance to explore, and pick $a^* = \text{arg max}_a \; Q_t(a)$ the rest of the time.  These methods are call $\epsilon$-greedy methods.  In the asymptotic case, we see that we will have to eventually pick every action an infinite number of times (weird to think about, huh?), and hence we maintain that
$$
\lim_{t\to\infty} Q_t = Q^*.
$$

### Softmax Action Selection

The last segment detailed a method for our agent to choose an *action*.  Another way to pick an action is to assign each choice a probability.  For example, say we pick
action $a$ with probability
$$
P(a) = \frac{e^{Q_t(a)/\tau}}{\sum_b e^{Q_t(b)/\tau}}
$$
where $b$ iterates over all the possible actions, and $\tau$ corresponds to the temperature.  High temperatures cause actions to become close to equiprobable, and low temperatures cause a greater difference in selection probability.  In fact, as $\tau \to 0$, the softmax action selection becomes the same as greedy action selection.

It's unclear whether $\epsilon$-greedy action selection or softmax action selection is more effective.
The $\epsilon$ methods are easier to tune and dynamically change, whereas the softmax selection means picking $\tau$, hence needing to know how likely action values and powers of $e$.

## Evaluation vs. Instruction

The n-armed bandit problem gives us an example of purely evaluative feedback.
In reinforcement learning, the "feedback" is independent of the action.  So it's not "real" feedback.  Supervised learning algorithms try to configure/shape themselves to their environment - but they cannot learn to control or influence their environments.

### Example

Let's dig into these differences by emphasizing an example given by Sutton and Barto.  Consider the n-armed bandit problem with 2 arms (i.e. $n=10$).  Each action has two rewards, success and failure (binary actions).
In a supervised learning setting we might infer an action was "correct" if you got success, and if you got failure, you may assume the *other* action was "success".
Then as you play, you can tally how many times an action was inferred to be correct, and you pick the action based on the tallys (more tallys = higher chance of winning).

Suppose the actions we're deterministic (i.e. they're assigned be either completely success or completely failure), then this algorithm would never be wrong.  After a single choice, we would know exactly what action we would fix on.  But if the actions were stochastic (each action has a *probability* of success), then this is certainly not the case.

In this case, the supervised learning approach would work *only* if the probabilities fulfill the assumption that one action is bad (failure) and the other is good (success).  Hence, we need one action will probability of success greater than $\frac{1}{2}$, with the other having a probability of success less than $\frac{1}{2}$.  Then, the algorithm would fixate on the better choice, and we would win.

But if *both* were good (probability of success over $\frac{1}{2}$), or *both* were bad (probability of success less than $\frac{1}{2}$), than the supervised learning methods how no way of determining which choice is *better* (or *worse*).  In the *both bad* case, the algorithm would likely pick a failing action, and always assume the other action is better.  When it picks the other option (and *also* gets failure), it would flip back to the first choice.  This cycles, and we get an oscillating algorithm that cannot truly find the better choice of the two.  In the *both good* case, we would quickly fixate on a single action (since it usually wins, the other must usually lose, right?), typically, the first action picked.

So what does a reinforcement learning approach look like?  Let
$$
\pi_t(x) = \text{"The probability of selecting action }x\text{ at time}t\text{."}
$$
We then define the *next* timestep as
$$
\pi_{t+1}(x) = \pi_t(d_t) + \alpha\Big[1 - \pi_t(d_t)\Big].
$$
If the action inferred to be correct on play $t$ was $d_t$, then we update $\pi_t(d_t)$ an $\alpha$ amount from it's current value toward $1$  We then inversely adjust the other probabilities so they sum to one.  We call this algorithms the $L_{R-P}$ (linear, reward-penalty) algorithm.  If we do nothing on a failure, we call this the $L_{R-I}$ algorithm (linear, reward-inaction).