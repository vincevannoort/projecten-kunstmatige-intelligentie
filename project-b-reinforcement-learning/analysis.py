# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    answerDiscount = 0.9
    answerNoise = 0
    return answerDiscount, answerNoise

def question3a():
    # Prefer the close exit (+1), risking the cliff (-10)
    # Discount high, so takes the risks since other path is too long
    # Noise low, so the risk of the cliff path is none
    # LivingReward low, so it takes the shortest terminal state
    answerDiscount = 0.2
    answerNoise = 0
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3b():
    # Prefer the close exit(+1), but avoiding the cliff(-10)
    # Discount high, so it prefers shortest terminal state
    # Noise medium, so it does not prefer the cliff path
    # LivingReward low, so it takes the shortest terminal state
    answerDiscount = 0.3
    answerNoise = 0.3
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3c():
    # Prefer the distant exit(+10), risking the cliff(-10)
    # Discount medium, so it prefers the distant terminal state with the highest reward
    # Noise low, so there is no risk at the cliff
    # LivingReward low, can't be higher than the terminal state 
    answerDiscount = 0.5    
    answerNoise = 0
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3d():
    # Prefer the distant exit(+10), avoiding the cliff(-10)
    # Discount low, so it prefers a longer route with higher reward
    # Noise medium, so it does not risk the cliff route
    # LivingReward low, can't be higher than the terminal state
    answerDiscount = 0.9
    answerNoise = 0.3
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3e():
    # Avoid both exits and the cliff(so an episode should never terminate)
    # Discount low, does not matter
    # Noise medium, does not matter
    # LivingReward high, so it prefers not to terminate
    answerDiscount = 0
    answerNoise = 0
    answerLivingReward = 10
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question6():
    answerEpsilon = None
    answerLearningRate = None
    return answerEpsilon, answerLearningRate
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print 'Answers to analysis questions:'
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print '  Question %s:\t%s' % (q, str(response))
