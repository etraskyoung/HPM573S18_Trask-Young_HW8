import Classes as Cls
import scr.FormatFunctions as Format
import scr.StatisticalClasses as Stat

# Present to the gambler's change in their reward if they use an unfair coin for which the probability of head is 45%.


#settings for steady state
fair_prob = 0.5
unfair_prob = 0.45
n_sim_cohort = 1000
n_games_in_a_set = 10
alpha = 0.05

#create game for when probability = .5

FairMultipleGameSets = Cls.MultipleGameSets(ids=range(n_sim_cohort), prob_head=fair_prob, n_games_in_a_set=n_games_in_a_set)
FairMultipleGameSets.simulation()

#create game for when probability = .45

UnfairMultipleGameSets = Cls.MultipleGameSets(ids=range(n_sim_cohort, 2*n_sim_cohort), prob_head=unfair_prob, n_games_in_a_set = n_games_in_a_set)
UnfairMultipleGameSets.simulation()


#Find comparative outcome
def get_compare(sim_output_fair, sim_output_unfair):
    increase = Stat.DifferenceStatIndp(
        name='Increase in Reward',
        x=sim_output_fair.get_mean_total_reward(),
        y_ref=sim_output_unfair.get_mean_total_reward()
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_PI(alpha=alpha),
        deci=1
    )
    print("Expected increase in reward ($) and {:.{prec}%} prediction interval:".format(1 - alpha, prec=0),
          estimate_CI)
# print outcomes of each cohort
print("Estimated expected reward for a set of games with fair flips:", FairMultipleGameSets.get_mean_total_reward())
print("The 95% PI of expected reward of a set of fair flip games:", FairMultipleGameSets.get_PI_total_reward(alpha))
print("Estimated expected reward for a set of unfair flip games (probability of heads is 0.45):", UnfairMultipleGameSets.get_mean_total_reward())
print("The 95% PI of expected reward of a set of unfair flips (probability of heads is 0.45):", UnfairMultipleGameSets.get_PI_total_reward(alpha))

# print comparative outcomes
print(get_compare(FairMultipleGameSets,UnfairMultipleGameSets))
#i'm getting errors tracing back to the support library code, but i'm not sure why
