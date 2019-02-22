import repo
infraction_points = repo.Calc_Points()

speed = input('How many times did the driver speed: \n')
swerve = input('How many times did the driver swerve outside their lane: \n')
rolling = input('How many times did the driver perform a rolling stop: \n')
tail_gating = input(
    'How many times did the driver follow too closely to the driver in front: \n')

speed_points = infraction_points.speeding(speed)
swerve_points = infraction_points.swerving(swerve)
rolling_points = infraction_points.rolling_stop(rolling)
tg_points = infraction_points.tail_gate(tail_gating)
points = infraction_points.total_points(
    repo.base_points, swerve_points, rolling_points, speed_points, tg_points)

if points <= 150:
    print('The premium cost is $115 month.')
elif points > 150 or points <= 175:
    print('The premium cost is $130 per month.')
elif points > 175 or points <= 200:
    print('The premium cost is $150 per month.')
elif points > 200:
    print('The premium cost is $175 per month.')
