Date: 2011-07-19 02:07
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Measuring cell fluorescence using ImageJ
Slug: measuring-cell-fluorescence-using-imagej
Tags: cell,fluorochrome,immunofluorescence,fluorescence,microscopy,imagej,imaging

Determining the level of cellular fluorescence from fluorescence microscopy images in ImageJ


![method/37/pser-imagej-setup.png](/images/method/37/pser-imagej-setup.png)








Open ImageJ. Note: ImageJ may be freely downloaded from [here](http://rsbweb.nih.gov/ij/download.html)



Select the cell of interest using any of the drawing/selection tools (i.e. rectangle, circle, polygon or freeform)

![step/246/pser-imagej-setup.png](/images/step/246/pser-imagej-setup.png)



From the Analyze menu select “set measurements”. Make sure you have **area integrated intensity** and **mean grey value** selected (the rest can be ignored).



Now select “Measure” from the analyze menu. You should now see a popup box with a stack of values for that first cell.



Now go and select a region next to your cell that has no fluroence, this will be your background.

Repeat this step for the other cells in the field of view that you want to measure.

NB: Size is not important. If you want to be super accurate here take 3+ selections from around the cell. 

![step/249/background-selection.png](/images/step/249/background-selection.png)



Once you have finished, select all the data in the Results window and copy and paste into a new spreadsheet (or similar program)



Use this formula to calculate the corrected total cell fluorescence (CTCF).

CTCF = Integrated Density – (Area of selected cell  X Mean fluorescence of background readings)





Make a graph and your done. 

Notice that rounded up mitotic cells appear to have a much higher level of staining due to its smaller size concentrating the staining in a smaller space. If you used the raw integrated density you would have data suggesting that the flattened cell has less staining then the rounded up one, when in reality they have a similar level of fluorescence.

![step/252/psercdkexcel.png](/images/step/252/psercdkexcel.png)







>This method is based, with permission, on an original protocol available [here](http://sciencetechblog.com/2011/05/24/measuring-cell-fluorescence-using-imagej/).

