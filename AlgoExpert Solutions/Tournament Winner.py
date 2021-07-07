def tournamentWinner(competitions, results):
    # Write your code here.
	score = {}
	teamWinVar = ""
	for i in range(len(competitions)):
		if results[i] == 0:
			teamWinVar = competitions[i][1]
		else:
			teamWinVar = competitions[i][0]
			
		if score.get(teamWinVar):
			score[teamWinVar] += 3
		else:
			score[teamWinVar] = 3
		
    return (max(score, key=score.get))

