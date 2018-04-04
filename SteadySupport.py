
import Classes as Cls
import scr.FormatFunctions as Format
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat
import P1 as P1

alpha = P1.alpha



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
        interval=increase.get_t_CI(alpha=P1.alpha),
        deci=1
    )
    print("Average increase in survival time (years) and {:.{prec}%} confidence interval:".format(1 - P1.alpha, prec=0),
          estimate_CI)
