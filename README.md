# Jujutsu
<h2>This is the Third version of the app</h2>
<p>Added all the kyu grades and the first dan grade. Implemented screens for all the grades and for the home screen. Changed the Modules.py from just list to classes for every grade. Have tried to eliminate as many bugs and ways for the app to crash as possible.</p>

<h1>What is this program?</h1> 
A program to choose, at random, technics in jujustu Kai system for 1 dan.
It is build in Python and the latest Kivymodules. You need to have Kivy installed. 

<h1>How to use the app</h1>
<p>On the first screen click on the top menu. <br>
Choose your grade according to its color in the jujutsu Kai system<br>
the app will then change the screen<br>
Next, click on the top menu to choose your prefered technique family from Kihon. <br>
Click on the <i>New technique</i> the app will at random show you a technique from Kihon from that grade. i.e If you choose Atemi Wasa the app will only give you all the Atemi Wasa from that grade.<br>
Continue to Click on the <i>New technique</i> button util you are done. <br>
When the are no techniques left the app will ask you to choose a new technique family of Kihon. </p>

<h2>Plan for this project is:</h2>
Crossed out text means that goal has been reached and is moved to the Done section.

<ol>
  <li>Make the dropdown in spinner the same color as the main spinner. </li>
  <li>Have a countdown on the amount of technics that are left in a family. </li>
  <li><s>Have a progressbar that visually shows how much you have left in a family. </s></li>
  <li>Make it possible to choose if the user wants the technics in order or at random.</li>
  <li><s>Make it possible to change kyu-grade and only get that kyu-grade Kihon.</s></li> 
  <li><s>Include Classes in the code that is not a part of Kivy.</s></li>
  <li><s>Have multiple screens</s></li> 
</ol>

<h4>Stretchgoals:</h4>
<ul>
   <li>Include the Jigo wasa for all kyu and up to 3dan</li>
   <li>include the Renraku Wasa for all kyu and up to 3dan</li>
   <li>Make a counter that count how many times a User have completed a technocfamily</li>
   <ul>
      <li>Kihon completed = +1 on all sub Kihon groups.</li>
   </ul>
   <li>Have different users that indivudally can track the above</li>
   <li>Present the data in a cool fashion</li>
   <li>Develop a webapp? </li>
   <li>Release the app to android market? </li>

</ul>
  

<h4>DONE:</h4>
<ul>
  <li> Make a GUI</li>
  <li>Have a progressbar that visually shows how much you have left in a family.</li>
</ul>




<h2>How to use</h2>
In the head of the screen press the button and choose your technic family. 
Press "New Technic" button and the label in the middle of the screen show a random technic. 
Press "New Technic" again and the laven shows a new random technic.

When you have pressed the "New technic" button enough times the label tells you that you are done with that technicfamily. 

Choose a new technic family or press "Reset" and restart. 
