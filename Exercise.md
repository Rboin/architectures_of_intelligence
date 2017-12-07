#Unit Exercise: Alpha-Arithmetic

The following data were obtained by N. J. Zbrodoff on judging alphabetic arithmetic problems. Participants were presented with an equation like A + 2 = C and had to respond yes or no whether the equation was correct based on counting in the alphabet – the preceding equation is correct, but B + 3 = F is not.

She manipulated whether the addend was 2, 3, or 4 and whether the problem was true or false. She had 2 versions of each of the 6 kinds of problems (3 addends x 2 responses) each with a different letter (a through f). She then manipulated the frequency with which problems were studied in sets of 24 trials:

* In the Control condition, each of the 2, 3, and 4 addend problems occurred twice.
* In the Standard condition, the 2 addend problems occurred three times, the 3 addend problems twice, and the 4 addend problems once.
* In the Reverse condition, the 2 addend problems occurred once, the 3 addend problems twice, and the 4 addend problems three times.

Each participant saw problems based on one of the three conditions. There were 8 repetitions of a set of 24 problems in a block (192 problems), and there were 3 blocks for 576 problems in all. The data presented below are in seconds to judge the problems true or false based on the block and the addend. They are aggregated over both true and false responses:

```
Control Group (all problems equally frequently)

          Two     Three   Four
Block 1   1.840   2.460   2.820
Block 2   1.210   1.450   1.420
Block 3   1.140   1.210   1.170

Standard Group (smaller problems more frequent)

          Two     Three   Four
Block 1   1.840   2.650   3.550
Block 2   1.060   1.450   1.920
Block 3   0.910   1.080   1.480

Reverse Group (larger problems more frequent)

          Two     Three   Four
Block 1   2.250   2.530   2.440
Block 2   1.470   1.460   1.100
Block 3   1.240   1.120   0.870
```

The interesting phenomenon concerns the interaction between the effect of the addend and amount of practice. Presumably, the addend effect originally occurs because subjects have to engage in counting, but latter they come to rely mostly on retrieval of answers they have stored from previous computations.

The task for this unit is to develop a model of the control group data. Functions to run the experiment and most of a model that can perform the task are provided in the model called **zbrodoff**. The model as given does the task by counting through the alphabet and numbers “in its head” (using the subvocalize action of the speech module to produce reasonable timing data) to arrive at an answer which it compares to the initial equation to determine how to respond. Here is the performance of this model on the task:

```
> (zbrodoff 1)
CORRELATION:  0.289
MEAN DEVIATION:  1.309
              2 (64)      3 (64)      4 (64)
Block  1  2.301 (64)  2.806 (64)  3.287 (64)
Block  2  2.290 (64)  2.804 (64)  3.301 (64)
Block  3  2.286 (64)  2.797 (64)  3.290 (64)
```

It is always correct (64 out of 64 for each cell) but does not get any faster from block to block because it always uses the counting strategy. Your first task is to extend the model so that it attempts to remember previous instances of the trials. If it can remember the answer it does not have to resort to the counting strategy and can respond much faster.
The model encodes each trail in a chunk which has the result of its counting for the trial. A completed problem for a trial where the stimulus was “A+2 = C” would look like this:

```
CHUNK0-0
   RESULT  "c"
   ARG1  "a"
   ARG2  "2"
```

The result slot contains the result of counting 2 letters from A. An important thing to note is that the actual target letter for the trial is stored in the goal buffer for comparison after the model has finished counting to a result. The model only encodes the result of the counting in the chunk that represents a trial in the imaginal buffer. Thus the same chunk will result from a trial where the stimulus presented is “A+2 = D” because it only counts A plus 2. The assumption is that the person is actually learning the letter counting facts and not just memorizing the stimulus-response pairings for the task. 

The model will learn one chunk for each of the additions which it encounters, which will be a total of six after it completes a set of trials.

A strong recommendation for adding the retrieval strategy to the model is to continue to use the existing encoding productions before the retrieval, the existing response productions (**final-answer-yes** and **final-answer-no**) after a successful retrieval, and the given counting productions if it fails to retrieve. It may be necessary to modify productions at the end of the encoding process and/or the beginning of the counting process to add the retrieval process into the model, but the response productions should not be modified in any way. Using the given response productions is important because they already handle the important steps necessary for the model to repeatedly perform this task successfully: they create a new goal chunk which will make sure the model is ready for the next trial, they make the correct response based on the comparison of the value read from the screen and the correct value of the sum which has been encoded in the imaginal buffer, and that imaginal buffer chunk is cleared so that it can enter declarative memory and strengthen the knowledge for that fact.

After your model is able to utilize a retrieval strategy along with the counting strategy given, your next step is to adjust the parameters so that the model’s performance better fits the experimental data. The results should look something like this after you have the retrieval strategy working with the parameters as set in the starting model:

```
CORRELATION:  0.929
MEAN DEVIATION:  0.656
              2 (64)      3 (64)      4 (64)
Block  1  1.265 (64)  1.444 (64)  1.338 (64)
Block  2  1.094 (64)  1.077 (64)  1.093 (64)
Block  3  1.043 (64)  1.047 (64)  1.039 (64)
```

The model is still always responding correctly on all trials, the correlation is good, but the deviation is quite high because the model is too fast overall. The model’s performance will depend on the same four parameters as the paired associate model: latency factor, activation noise, base-level decay rate, and retrieval threshold. In the model you are given, the first three are set to the same values as in the paired associate model and represent reasonable values for this task. The retrieval threshold (the :rt parameter) is set to its default value of 0. This is the parameter you should manipulate first to improve the fit to the data. Here is our fit to the data adjusting only the retrieval threshold:

```
> (zbrodoff 20)
CORRELATION:  0.987
MEAN DEVIATION:  0.174
              2 (64)      3 (64)      4 (64)
Block  1  1.870 (64)  2.179 (64)  2.558 (64)
Block  2  1.376 (64)  1.520 (64)  1.632 (64)
Block  3  1.215 (64)  1.282 (64)  1.359 (64)
```

If you would like to try to fit the data even better then you could also adjust the latency factor and activation noise parameters as well. The base-level decay rate parameter should be left at the value .5 (that is a recommended value which should not be adjusted in most models). Here is our best fit with adjusting all three parameters:

```
> (zbrodoff 300)
CORRELATION:  0.991
MEAN DEVIATION:  0.082
              2 (64)      3 (64)      4 (64)
Block  1  1.994 (64)  2.375 (64)  2.755 (64)
Block  2  1.267 (64)  1.361 (64)  1.448 (64)
Block  3  1.092 (64)  1.110 (64)  1.132 (64)
```

This experiment is more complicated than the ones that you have seen previously. It runs continuously for many trials and the learning that occurs across trials is important. Thus the model cannot treat each trial as an independent event and be reset before each one as has been done for the previous units. While writing your model and testing the fit to the data you will probably want to test it on smaller runs than the whole task. There are four functions you can use to run parts of the experiment.

The **zbrodoff-trial** function can be used to run a single trial. It takes four parameters which are all single character strings and an optional fifth parameter. The first three are the elements of the equation to present i.e. "a" "2" "c" to present a + 2 = c. The fourth is the correct key which should be pressed for the trial, "K" for a true probe and "D" for a false probe. The optional parameter indicates whether or not to show the task display. If the optional parameter is not provided then the window will not be shown (a virtual window will be used) and if it is the value t then it will show the task window. This call would present the a + 2 = c problem to the model with a window that is visible:

```
(zbrodoff-trial "a" "2" "c" "k" t)
```

Here are the twelve different problems which are used in this experiment along with the correct response for each:

```
("a" "2" "c" "k")("d" "2" "f" "k")
("b" "3" "e" "k")("e" "3" "h" "k")
("c" "4" "g" "k")("f" "4" "j" "k")
("a" "2" "d" "d")("d" "2" "g" "d")
("b" "3" "f" "d")("e" "3" "i" "d")
("c" "4" "h" "d")("f" "4" "k" "d")
```

The zbrodoff-trial function should be used until you are certain that your model is able to successfully use a retrieval strategy along with counting. To do that you will want to present the model with the same trial again and again and make sure that at some point it can retrieve the correct fact and respond correctly. You will also want to test it with both true and false facts to make sure it can retrieve the right information and respond correctly in both cases. You will also want to check the model’s declarative memory to make sure that it is only creating the correct facts – it should not be learning chunks which represent the wrong addition.

Once you are confident that your model is learning the correct chunks and can use both retrieval and counting to respond correctly you can use the **zbrodoff-set** and **zbrodoff-block** functions to run the model over multiple trials. Each takes one optional parameter, like **zbrodoff-trial**, to control whether the task display is shown, and if it is not provided they will not show the display. The **zbrodoff-set** function runs the model through 24 trials of the task presenting each problem twice in a randomly generated order. The **zbrodoff-block** function runs through 192 trials, which is 8 repetitions of the 24 trial set. The data which is being modeled is the result of three blocks of trials.

After making sure the model can successfully complete a set and block of trials then you will want to use the **zbrodoff** function to run it through the experiment multiple times and compare its performance to the data. The **zbrodoff** function takes one parameter indicating the number of times to run the full experiment. That function will average the results of running the full experiment that many times and report the correlation and deviation to the experimental data. It may take a while to run, especially if you request a lot of trials.

An important thing to note is that the only one of those functions which calls **reset** is **zbrodoff**. So if you are using the other functions while testing the model keep in mind that unless you call the **reset** function, press the “Reset” button on the Control Panel, or reload the model, then the model will still have all the chunks which it has learned since the last time it was reset (or loaded) in its declarative memory.

As you look at the starting model you will see one additional setting at the end of the model definition which you have not seen before:

```
(set-all-base-levels 100000 -1000)
```

This sets the base-level activation of all the chunks in declarative memory that exist when it is called (which are the sequence chunks provided) to very large values by setting the parameters **n** and **L** of the optimized base-level equation for each one. The first parameter, 100000, specifies n and the second parameter, -1000, specifies the creation time of the chunk. This ensures that the initial chunks which encode the sequencing of numbers and letters maintain a very high base-level activation and do not fall below the retrieval threshold over the course of the task. The assumption is that counting and the order of the alphabet are very well learned tasks for the model and the human participants and the use of that knowledge does not lead to any significant learning for those things during the course of the experiment.

Finally, because this experiment involves a lot of trials and you need to run several experiments to get the average results of the model there are some additional things that can be done to improve the performance of the software simulation itself i.e. the real time it takes to run the model through the experiment not the simulated time the model reports for doing the task. Probably the most important will be to turn off the model’s trace by setting the :v parameter to **nil**. The starting model has that setting, but while you are testing and debugging your addition of a retrieval process you will probably want to turn it back on by setting it to **t** so that you can see what is happening in your model. Something else which you will want to do when running the whole experiment is to close any open inspector tools in the ACT-R Environment because they update with every change to ACT-R and thus will slow down the running of the system. One final thing which can be done is to compile the model file to improve the performance of the Lisp code which performs the task itself. Some Lisp systems do this automatically (Clozure Common Lisp for example does) but many do not. Doing so in a Lisp which does not automatically compile may result in a further reduction in the time it takes to run the experiment. Some details on how to compile a model file and potential problems to be careful of when doing so can be found in the experiment document for this unit.

##References

Anderson, J.R. (1981). Interference: The relationship between response latency and response accuracy. *Journal of Experimental Psychology: Human Learning and Memory, 7*, 326-343.

Zbrodoff, N. J. (1995). Why is 9 + 7 harder than 2 + 3? Strength and interference as explanations of the problem-size effect. *Memory & Cognition, 23* (6), 689-700.