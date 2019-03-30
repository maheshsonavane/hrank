## Objective 
In this challenge, we're going to learn about the difference between a class and an instance; because this is an Object Oriented concept, it's only enabled in certain languages.

## Task 
Write a Person class with an instance variable, <i>age</i>, and a constructor that takes an integer,<i>initialAge</i>, as a parameter. The constructor must assign <i>initialAge</i> to <i>age</i> after confirming the argument passed as  is not negative; if a negative argument is passed as , the constructor should set <i>age</i> to 0 and print Age is not valid, setting age to 0.. 

In addition, you must write the following instance methods:

1. yearPasses() should increase the <i>age</i> instance variable by 1.
2. amIOld() should perform the following conditional actions:
    * If <i>age</i> < 13, print You are young..
    * If <i>age</i> >= 13 and <i>age</i> < 18 and , print You are a teenager..
    * Otherwise, print You are old..