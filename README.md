# <div align="center">Road Rage</div>

Road Rage is designed to simulate the traffic over a 1km distance of road in order to find the optimal speed limit for that section of road. This simulation starts with 30 cars per kilometer.

### <div align="center">Assumptions</div>

* Drivers want to go up to 120 km/hr.
* The average car is 5 meters long.
* Drivers want at least a number of meters equal to their speed in meters/second between them and the next car.
* Drivers will accelerate 2 m/s up to their desired speed as long as they have room to do so.
* If another car is too close, drivers will match that car's speed until they have room again.
* If a driver would hit another car by continuing, they stop.
* Drivers will randomly (10% chance each second) slow by 2 m/s.
* This section of road is one lane going one way.
* Cars exiting the road start again at the beginning.
* The optimal speed limit is one standard deviation above the mean speed.

## <div align="center">Instructions</div>

* The Road Rage notebook can be viewed on GitHub or downloaded to the users computer.
* Before the user can view the Road Rage notebook on their computer or run the Road Rage simulations, the user must first clone the road-rage repo onto their computer. The user must have Python 3 installed.
* To properly run the notebook, the contents of requirements.txt must be installed in the folder the notebook will be running from.
  * After navigating to the folder containing `road-rage.ipynb` and `road_rage.py`, enter `pip install -r requirements.txt` on the command-line to download the contents of requirements.txt.
* The user can then enter `ipython notebook road-rage.ipynb` on the command-line to view the notebook or run the Road Rage simulations.
