import Classes as Cls
import scr.FormatFunctions as Format
import scr.StatisticalClasses as Stat

# Present to the casino’s owner the change in their reward if they use an unfair coin for which the
# probability of head is 45%.


#settings for steady state
fair_prob = 0.5
unfair_prob = 0.45
n_games = 1000
alpha = 0.05


#create game for when probability = .5

FairSetOfGames = Cls.SetOfGames(id=1, prob_head=fair_prob, n_games=n_games)
FairOutcomes = FairSetOfGames.simulation()

#create game for when probability = .45

UnfairSetOfGames = Cls.SetOfGames(id=2, prob_head=unfair_prob, n_games=n_games)
UnfairOutcomes = UnfairSetOfGames.simulation()


#Find comparative outcome
def get_compare(sim_output_fair, sim_output_unfair):
    increase = Stat.DifferenceStatIndp(
        name='Increase in Reward',
        x=sim_output_fair.get_rewards(),
        y_ref=sim_output_unfair.get_rewards()
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_t_CI(alpha=alpha),
        deci=1
    )
    print("Average increase in reward ($) and {:.{prec}%} confidence interval:".format(1 - alpha, prec=0),
          estimate_CI)

# print outcomes of each cohort
print("Estimated expected reward for a fair flip:", FairOutcomes.get_ave_reward())
print("The 95% CI of expected reward of a fair flip:", FairOutcomes.get_CI_reward(alpha))
print("Estimated expected reward for an unfair flip (probability of heads is 0.45):", UnfairOutcomes.get_ave_reward())
print("The 95% CI of expected reward of an unfair flip (probability of heads is 0.45):", UnfairOutcomes.get_CI_reward(alpha))

# print comparative outcomes
print(get_compare(FairOutcomes,UnfairOutcomes))
