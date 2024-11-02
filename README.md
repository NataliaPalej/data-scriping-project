# data-scripting-project
Project for Data Visualization Year 4

**Part 1: Data Collection through Web Scraping**

**Overview:**
This initial phase of the project involves extracting data from the Pokémon Database (pokemondb.net), 
focusing on the collection of Pokémon statistics and corresponding images.

**Objective:**
The primary goal is to scrape Pokémon data, including statistics and images, from the specified website. 
This will serve as the foundational dataset for further exploration and visualization tasks in subsequent phases of the project.

Step-by-Step Instructions:
1. Preparation and Compliance
2. Scraping Etiquette
3. Using Tools
4. Data Extraction
5. Individual Page Scraping
6. Data Structuring

**Deliverables:**
- A script or a set of scripts capable of scraping and parsing the required data from the Pokémon Database.
- The data collected should be saved in the JSON format, adhering to the specified guidelines.

Remember, this project is designed to introduce you to real-world data collection and parsing. 
Take this opportunity to familiarize yourself with handling web data, respecting webmaster guidelines, and structuring data effectively for future use.


**Part 2: Data Loading and Preprocessing**
**Objective:**
To load the previously collected Pokémon data into a structured format and perform necessary preprocessing steps to facilitate analysis.

**Detailed Instructions:**
1. Initialization
2. Dataframe Transposition
3. Data Storage
4. Data Type Conversion Simple
5. Data Type Conversion
6. Column Splitting - Types
7. Generation Identification
8. Column Splitting - Abilities
9. Data Cleansing
10. Evaluation

**Deliverables:**
- A Python script or notebook that processes the loaded JSON data into a cleaned and structured Pandas DataFrame.
- A pickle file containing the cleaned and preprocessed DataFrame for use in subsequent data analysis tasks.

**Considerations:**
- Maintain data tidiness principles throughout the preprocessing to facilitate smooth analysis in the following stages.
- Double-check that all modifications preserve the original meaning and integrity of the data.


**Part 3: Analysis of Pokémon Distribution by Primary Type**
**Objective:**
Familiarize yourself with the functionality of Plotly's Graph Object methods.

**Procedure:**
1. Data Aggregation 
2. Color Scheme Mapping 
3. Bar Chart Visualization 
4. Bar Chart Configuration


**Part 4: Comparative Analysis of Pokémon Distribution by Primary Type and Generation**
**Learning Outcome:** Familiarize yourself with the functionality of Plotly's Graph Object methods with complex nested controls. 
**Task:** Create a grouped bar chart that compares the count of Pokémon by **`primary_type`** across various generations, 
similar to the sample chart shown. Note that the sample's figure size is incorrect; make certain that in your implementation, 
the chart's figure size is correctly configured.

**Procedure:**
1. Data Organization
2. Grouped Bar Chart Creation
3. Removal of Duplicated Legends
4. Synchronizing Interactive Controls with LegendGroup
5. Grouped Bar Chart Enhancement
6. Stacked Bar Chart Creation
7. Stacked Bar → Matrix Bar Chart Base Alignment
8. Constraints of Matrix Bar Plots and Utilizing the Negative Y-Axis for Additional Data Representation 


**Part 5: Visualizations with Built-in Statistical Features** 
**Learning Outcome:** Familiarize yourself with the functionality of Plotly's Graph Object 
methods with built-in statistic features like histogram, barplot, KDE, … 
**Task:** Create a ridgeline plot that compares the 6 basic stats (**`HP`**, **`Attack`**, … **`Speed`**) 
of Pokémon across different generations.

**Instructions**
1. Data Grouping
2. Create Subplot
3. Main Loop for Violin subplots
4. Correct and Enhance the visualisation
5. Visualizations with Built-in Statistical Features 

**Part 6: Visualizations with Built-in Statistical Features**
Create a Chart like below
- Violin Chart: Total Stat Value Over Primary Types 
- Pie Chart: okémon Distributions Over Primary Type
- Scatter Chart: Base Exp Requirements vs Pokémon Strength
- Scatter Chart: Pokémon Height vs Pokémon Weight
- Heatmap Chart: Pokémon Primary Type - Base Exp Requirements Distribution

You will be based on this subplot structure:
# Define a 5x5 subplot layout
specs = [
    [{'rowspan': 3, 'colspan': 3},  None, None, None,               {'rowspan': 3, 'colspan': 3}, None,                           None],
    [None,                          None, None, None,               None,                         None,                           None],
    [None,                          None, None, None,               None,                         None,                           None],
    [None,                          None, None, {'type':'domain'},  None,                         None,                           None],
    [{'rowspan': 3, 'colspan': 3},  None, None, None,               {'rowspan': 3, 'colspan': 3}, None,                           None],
    [None,                          None, None, None,               None,                         None,                           None],
    [None,                          None, None, None,               None,                         None,                           None],
]

# Initialize subplots
fig = make_subplots(rows=7, cols=7, specs=specs, 
                    subplot_titles=['Pokémon Total Stat Value over Primary Types', 
                                    'Base Exp Requirements vs Pokémon Strength',
                                    'Pokémon Distributions <br> over Primary Type<br><br> ',
                                    'Pokémon Height vs Pokémon Weight',
                                    'Pokémon Primary Type - Base Exp Requirements Distribution',])