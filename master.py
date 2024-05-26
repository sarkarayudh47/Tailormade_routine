from GeneticAlgo import run_genetic_algo
from peak_conc import RunPeak_conc
from routine import generate_timetable
# solution=run_genetic_algo(8,6)
# solution=solution[0]
maxIncreaseRate=0.9
n=1
for i in range (n):
    print(f"iteration number {i}")
    RunPeak_conc(maxIncreaseRate)
    maxIncreaseRate-=0.1

