# ICPFP

#### Iranian car price forecasting project

![img1](https://raw.githubusercontent.com/mimseyedi/ICPFP/master/docs/iranian_cars_poster.jpg)

The idea of this project started by listening to the `Radio Geek podcast`.
It became interesting for me to write a script that collects the information of Iranian cars from `bama.ir` and then make a model to `predict the price` of these cars.

I must add that this was my first project in this field. And to be honest, I don't know much about cars :)
But I tried to do this project as much as possible according to the limited knowledge I have, and I would be grateful if you could share your ideas with me and criticize my method.

In the following, I will tell the different parts of the project along with the work process and the necessary explanations.


### First step:
First, I wrote a web scraper called `icdc.py` (Iranian cars data collector) to collect information about Iranian cars. The first attempts were not very interesting and soon I realized that I had to separate the information of the cars according to the name and model of the car and then collect them.
I collected the information of `11 models of famous Iranian cars` and worked only on them.

`Note: Due to the severe inflation in Iran, car prices are constantly changing. Therefore, I must mention that this information was collected on 1401/11/21 Jalali, Feb 11 2023 and may not have any validity in the future.`

<br />

| Row | Cars | Models|
|-----|---|---|
| 1   |Dena|Normal, Plus, Turbo Plus|
| 2   |Peugeot 206|Style 2, Style 3 Panorama, Style 5|
| 3   |Peugeot 207|Normal, MC, Panorama, TU5, TU5 Panorama|
| 4   |Peugeot 405|GLX, GLX 2Fuel, SLX|
| 5   |Peugeot Pars|ELX, LX, XU7, XU7P|
| 6   |Pride|SE-111, SE-131, SE-151, Hatchback|
| 7   |Quick|Normal|
| 8   |Saina|EX, S|
| 9   |Samand|EF7-LX, EF7-LX 2Fuel, XU7-LX|
| 10  |Tiba|EX Hatchback, SX Hatchback|
|  11 |Tondar90|Normal, Plus, E2|


In the end, I collected the information of `2399 cars`, which unfortunately took several hours due to the weak and unstable Internet in Iran, and some of the information was not recorded, which made the information of all the cars not equal!

Also, I could only get limited models of these 11 types of cars.

`This information is stored separately in csv format files in the dataset directory.`

### Second step:
At this stage, I started `pre-processing` and `cleaning the data` on each car individually, which was a bit annoying due to the lack of proper compatibility of operating systems in Farsi :)

I made a special model of each car. This is exactly where I don't know much about, and more than anything I was worried about being caught by the dimensional curse. That's why I decided to make a regression model for each type of car.

Some information was not useful and I had to delete it. For this reason, specifications such as car models and colors were limited.

Finally, on average, the models that have been built have `9 million tomans` of error in the worst case, which is an acceptable model made by the comparison I made with Iranian car price prediction sites.

All information related to this section is stored in the `models` directory.

### Third step:
At this stage, I wrote a very basic program called `ptpoic.py` (Predicting the price of Iranian cars), through which you can give the information of the car and it will be loaded according to the information of the desired model, and it will make the prediction according to the information and show the result.

`In the future, I plan to write a better and graphical program for this.`

Here I will show the comparison of the model I made with the model of the famous website https://www.hamrah-mechanic.com using the information of my car.

In[1]
```
python3 ptpoic.py
```

Out[1]:
```
[Predicting the price of Iranian cars]

 1-Dena
 2-Peugeot 206
 3-Peugeot 207
 4-Peugeot 405
 5-Peugeot Pars
 6-Pride
 7-Quick
 8-Saina
 9-Samand
10-Tiba
11-Tondar90

[STEP 1] Please Select a car (1/11): 
```

In[2]:
```
10
```

Out[2]:
```
[Predicting the price of Iranian cars]

[STEP 2] Enter year of car production: 
```

In[3]:
```
1398
```

Out[3]:
```
[Predicting the price of Iranian cars]

[STEP 3] Enter the amount the car has moved in kilometers: 
```

In[4]:
```
69000
```

Out[4]:
```
[Predicting the price of Iranian cars]

[STEP 4] In order and separated by a space.
         Enter 1 if correct, otherwise 0.

EX Hatchback | SX Hatchback | Manual | White
>>> 
```

In[5]:
```
1 0 1 1
```

Out[5]:
```
273,515,228 T
```

#### Price prediction by https://www.hamrah-mechanic.com model:
![img1](https://raw.githubusercontent.com/mimseyedi/ICPFP/master/docs/tiba_price_in_hamrah_mechanic.png)

#### `Difference: 273,515,228 - 272,000,000 = 1,515,228 T`

### Last word:
Definitely, important issues have not been observed in this project and it is because I am not a professional in this field. But I am very interested and I like to challenge myself. So please share with me if you have any ideas, tips or interesting thoughts in mind so that this project can progress and I will also learn from you.

Thankful.