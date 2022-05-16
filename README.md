# Python-queue-simultaion
Goal of this simulation is to test different window arrangement.
Introduction:
1. we have 3 different types of tasks:<br>
1.1 Type A,B and C
1.2 Each task is build like [task type, execution time(random number)].<br>
2. we have 4 different window types:<br>
2.1 Window A which handles tasks of type A.<br>
2.2 Window B which handles tasks of type B.<br>
2.3 Window C which handles tasks of type C.<br>
2.4 Window E which handles tasks of all types (express window).<br>
3. For compleating each task we earn as much as the execution time:<br>
3.1 Example: for [A,25] we earn 25 units.<br>
4. Each window has its operational cost per time unit:<br>
4.1 Cost is a number in the range (0,1)<br>
4.2 Example: If operational cost of window A is 0.5, from task [A,25] we earn 12.5 units.<br>
5. As output we get 4 bar plots:<br>
5.1 Number of satisfied clients.<br>
5.2 Cost of operating windows.<br>
5.3 Earning from compleating tasks.<br>
5.4 Profit.<br>
