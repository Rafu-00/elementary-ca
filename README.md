# elementary-ca
 A basic implementation of an elementary CA

This basic program tries to simulate a basic train station queuing scenario.
Initially, a two-dimensional array is initialized wherein the first row is a set of randomized numbers represented only by 0 or 1. This is to illustrate whether a "spot" has been taken or not.
The array is then populated with zeroes according to a specified dimension. In this case, 10 x 15.

In order to simulate movement or growth, these rules were given:
1. If the first northern array position is populated, it will check for a vacant northeastern or northwestern array position ranging from one to two positions away. If any, it will occupy its position. Otherwise, it will occupy the array position behind the northern array position mentioned earlier.
2. If the first northern array position is vacant, it will occupy its position.
3. If the first northern array position is occupied as well as the northeastern and northwestern positions, it will occupy the position behind the northern array position.

For observation purposes, each iteration will printed to show how positions have changed. It was observed that outer positions (closest to min and max column length) have a few more occupied positions than that of the middle portion.
It is to be noted that while elementary CA was used for this observation, it could be said that a sandpile model could also produce a similar or even better results as it could simulate how people disperse to different queues if they see an influx of people in a certain area.