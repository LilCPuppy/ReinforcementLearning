# Chapter One

## Overview

**Definition (Informal)**: *Reinforcement Learning* defines a process of how to map situations to actions such that a numerical reward signal is maximized.

One often thinks of supervised learning when considering ML, and reinforcement learning differs in a distinct way: RL problems are interactive.  The environment can change around the agent, and the agent could possibly change the environment.

There are two distinguishing characteristics associated with reinforcement learning problems:
- Trial and error search, and,
- delayed reward

What makes these distinguishing?  The *trial and error* ensures that the agent (or the learner) will try new things.  As a result, we mitigate the possibility of the agent finding some local maximum w.r.t the reward signal, and will continue to explore the state space.  The *delayed reward* means that the agent must think about the future, and the possible long term effects of the current action.

Another facet of machine learning is the trade-off between exploration and exploitation?  Should the agent take advantage of moves/states that it already knows?  Or should it consider exploring a new state?
This is a dilemma that does not even arise in conventional supervised learning, and has been studied extensively by mathematicians for decades.

Now, RL problems are *goal oriented*.  There is always a very explicit goal in mind in well posed RL problems, and Sutton and Barto provide some examples here:
  - A master chess player deciding a move (goal: win the game)
  - An adaptive controller changing parameters of a business' machines in real-time (goal: optimize ouput)
  - A gazelle struggling to walk after being born to running 20 minutes later (goal: locomotion)
  - Mobile robot deciding to clean a new room or head back to it's charging station to refuel (goal: minimize cleaning time)

There are several key characteristics that are worth noting in the above examples and RL problems in general:
  - There is always interaction between the agent and the environment in which the agent tries to achieve some goal despite uncertainty (the chess player cannot possibly account for all the possible outcomes of their move)
  - The agent is able to *change* the state of the environment (the chess player quite literally changes the board)
  - Correct choices often require foresight to account for delayed consequence of actions (for example, the chess player must account for the next possible chain of moves)

## Elements of RL

**The policy**: defines how the agent behaves in a given state or time

**The reward function**: defines the *goal* of the RL problem to the agent, and maps each state of the environment to a single number/reward.  *It cannot be altered by the agent, but it can alter the agent's policy*.

**The value function**: specifies the *long-term value* of an action/state.  The value of the state is the total amount of reward the agent can expect to accumulate over the future, starting from that state.

We might consider rewards to be a more *fundamental* than value, because without reward, there is no value.  However, in RL algorithms (and the users, us) focus much more on value.  In fact, according to Sutton and Barto, the most important component of RL problems is how value is defined and computed.  It is a much more difficult factor to derive/compute, because it must be estimated and re-estimated based on the everchanging experience of the agent.

Some problems don't focus on value at all, and instead focus on exploring the *space of policies*.  These algorithms are called *evolutionary methods* and can be effective on certain classes of problems.

## Example: Tic-Tac-Toe

We now discuss how a RL solution might look for an agent who wants to win tic-tac-toe.  The goal here is very clear:

**Goal**: Win the game.

The *policy* would be the rule that tells the agent/player what move to make next in every state of the game.

The first thing we want to do is have a table of scalars, bijectively associated with every state of the game.  This scalar will represent the probability that we will win the game given that state.  Hence, this is our **value function** that will be learned, since we will update it over time.  To initialize this function, any states with three x's in a row is assigned 1.0 (since we already won), any state with three o's in a row is assigned 0.0 (since we already lost), and we give everything else 0.5, a coin-tosses chance.

So how will we update the value function?  It's intuitive that as we play the game against the opponent and accumulate sequences of boards, we want the *values of the earlier states to become closer to the values of the later states*.

Let E denote the set of possible states/board configurations (so |E| = 19683 if we ignore impossible boards w.r.t to the rules).  Then let,
<div align=center>V:E &rarr; &Kfr;</div>.
Then for a sequence of of boards *in which it was the agents turn to play* for a single game, namely
<div align=center> {S<sub>1</sub>, ..., S<sub>N</sub>} </div>
and
<div align=center> V(S<sub>k</sub>) = V(S<sub>k</sub>) + &alpha;[ V(S<sub>k+1</sub>)-V(S<sub>k</sub>) ]</div>.

Colloquially, we move the value of the board an &alpha; amount in the value of the next board's direction.  We call &alpha; the step size, and this can be tuned by the programmer.  Note that k < N and this recursive definition is well-defined, since we have already accounted for the values of the boards at the termination of the game.
