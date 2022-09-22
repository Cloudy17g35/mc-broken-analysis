
# McDonalds US - broken ice creames machines

  

  

## I. Problem Overview

  

Problem: There are ice creames machines in McDonalds restaurants in whole US. Some of them are working, some of them are not.

  

If they re not working it's logic that client who wanted to buy an ice cream won't do it so company is losing money.

  

  

Goal: find out how much money McDonalds might be losing due to broken ice cream machines in the US

  

  

*What will be needed?*

  

  

* How many McDonalds are in US

  

* Average revenue/per minute made on ice creams sold in every restaurant in US McDonalds

  

* Percentage value for broken ice creams machines in current minute

  

  

*Assumptions:*

  

  

* There's only one ice cream machine per restaurant

  

* The demand for ice cream might be bigger in summer and lower in winter so i'm going to assume that **4 people** wants to buy ice cream in every **single minute** in every single restaurant in US

* One ice cream costs on average **1$**

  

* Every McDonald in US is open **24 hours per week**

  

* Based on this [article](https://www.scrapehero.com/location-reports/McDonalds-USA/) - there is **13,337** McDonalds restaurants in US

  
  

## II. Solution

With all assumptions and data listed in problem overview we can solve this problem.

  

**Potential revenue** - revenue when all ice creames machines are working, which might be calculated like this:

  

(cost of one ice cream * amount of people buying it) * number of restaurants in us

  

Thats potential revenue, but we know that some percentage of all machines are broken, so amount of **lost revenue** might be calculated like that :

  

(potential revenue * percentage of not working machines) / 100

  

of course both calculations shall be calculated **per minute** .

  

## III. Coding

  

There are **two python scripts:**

  

* **extract.py** - responsible for scraping percentage of currently broken ice cream machines from this [site](https://mcbroken.com/), calculating lost revenue, and storing calculated results in **.json format**.

* **app.py** - responsible for calculating lost revenue for particular date and displaying result (using [streamlit](https://streamlit.io/) framework)

  
  
  

## IV. How to run locally?

  
Python version: **3.9.12**

**extract.py** is using [selenium](https://www.selenium.dev/documentation/), which needs [gekodriver](https://github.com/mozilla/geckodriver) , on **MacOS** it can be easily installed using **brew**:

    brew install geckodriver

When gekodriver is installed open terminal, **cd** to this repo and use command:

    pip install -r requirements.txt
   
   Now you should be able to run two python scripts, for extracting by command:
   

    python extract.py

and app.py (in different terminal) using streamlit freamwork:

    streamlit run app.py

App should work on **http://localhost:8501/**.
