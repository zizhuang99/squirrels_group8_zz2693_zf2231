# squirrels_group8_zz2693_zf2231
## 1.Introduction
We biult an application to track of all the known squirrels at Central Park. Users can view, add, update and see some general statistics on the web.  
[Try it!](https://zz2693-project-for-tools.appspot.com/)  

## 2. Import and export squirrels data.
Users can import and export data via command line.The file path should be specified at the command line after the name of the management command.  
Note: Here we already prepared squirrel dataset in home directory for users to import. The name of the dataset is 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv  

    #import data  
    $ python manage.py import_squirrel_data /path/to/file.csv  
    #export data  
    $ python manage.py export_squirrel_data /path/to/file.csv  
 
 ## 3. Map and sightings.
 #### 3.1 Map
 [This map displays the location of the squirrel sightings](https://ibb.co/3fyHFB2).   
 Note: We can only plot 100 unique coordinates.
 
 #### 3.2 Sighingts
After entering the sightings page (/sightings), you will first see a link called ‘add new data’ on the top of the page, after clicking which, you will be directed to a page where you can add a new sighting.   

Then you will see a link called ‘See some stats!’. This will link you to a statistic page where you can see the number of sightings in the database that we just imported, the number of squirrels that runs away from people, the number of squirrels that climbs on the tree , the number of squirrels that are black, and the number of squirrels that are chasing when sighted.  

Below is a list of Squirrel ID, each of which is linked to a page where you can update specific attributes of this sighting.  

## 4. Group Information
Group name and section: Project Group 8, Section 2  
A list of UNI for each member on the team: [zz2693,zf2231]  
A link to the server running our application: https://zz2693-project-for-tools.appspot.com/  
