# **Investigating Dyslexic's Challenges in Learning Music**

This repo presents a project dedicated to dyslexic students who have difficulties reading music notes.
our work is separated into two parts, one regarding doing an analysis process on a paper that discussed the same topic, and the other is inspired by the analysis insights to make an A_-powered application to help ease the discussed challenge. 


| No. | Topic	                        							|
|-----|------------                       							|
| 01  | [Dyslexia and Music Notes Paper Data Analysis](#Dyslexia-and-Music-Notes-Paper-Data-Analysis)                             |
| 01  | [AI-Powered Music Learning Platform for Dyslexic Students](#AI-Powered-Music-Learning-Platform-for-Dyslexic-Students)    	|

---

# **Dyslexia and Music Notes Paper Data Analysis**

you may find all files related to this section in `paper-analysis` folder located in this repo [here](/paper-analysis)
This section contains all materials and files used in the data analysis process on paper 
[Effects of the design of written music on the readability for children with dyslexia](https://journals.sagepub.com/doi/10.1177/0255761414546245)
to find meaningful insights concerning dyslexic people having difficulties reading traditional music notes.

## Section Contents
| No. | Topic	                        							|
|-----|------------                       						|
| 01  | [Ovevrview](#overview)     									|
| 01  | [Paper Summery](#paper-summery)     						|
| 02  | [Findings](#findings)     									|
| 03  | [BI Report](#BI-report)     								|

---

## Overview
Dyslexia is a learning disorder that affects approximately 5-10% of children worldwide. 
It is characterized by difficulties with reading fluency and phonological processing, which can significantly impact academic and social development. 
Music interventions have been proposed as a potential treatment for dyslexia, 
as they can target some of the same cognitive processes that are impaired in dyslexia, such as phonological awareness and auditory memory.

---

## Paper Summary
David Gómez Oropeza et al.'s (2021) paper focuses on the effects of different music notation designs on the readability 
of music for children with dyslexia. They compare the traditional music notation system to a newly designed notation system 
that is based on the Gestalt laws of perception. They find that the newly designed notation system is more readable for children with dyslexia.


This paper investigates the relationship between the design of written music and the number of mistakes dyslexic and non-dyslexic 
children make in reading music. The study used a public dataset of musical notation examples and a group of children with and without 
dyslexia to evaluate the readability of different music notation designs.

---

## Findings
The study found that children with dyslexia made significantly more mistakes than non-dyslexic children when reading music with traditional notation. 
However, children with dyslexia made fewer mistakes when reading music with a newly designed notation system that was based on the Gestalt laws of perception.

The authors of the paper conclude that the design of written music can have a significant impact on the readability of music for children with dyslexia. 
They suggest that music notation systems should be designed to be more intuitive and easier to learn for all children, including those with dyslexia.

  - Children with dyslexia found a newly designed music notation system to be more readable than traditional music notation.
  - The newly designed notation system was based on the Gestalt principles of perception.
  - The Gestalt principles of perception include principles of proximity, similarity, and closure.
  - The newly designed notation system used larger note sizes, more note spacing, and a different font type than traditional music notation.

---

## BI Report
<figure>
    <img src="https://github.com/xShaimaa/dyslexia-and-music-notes-paper/blob/master/dyslexia%20and%20music%20notes%20paper%20dataset%20analysis/03-dashboard/img/stats.png">
    <figcaption>Paper Dataset Stats<figcaption>
<figure>

---

<figure>
    <img src="https://github.com/xShaimaa/dyslexia-and-music-notes-paper/blob/master/dyslexia%20and%20music%20notes%20paper%20dataset%20analysis/03-dashboard/img/test.png">
    <figcaption>Paper test results<figcaption>
<figure>

---

<figure>
    <img src="https://github.com/xShaimaa/dyslexia-and-music-notes-paper/blob/master/dyslexia%20and%20music%20notes%20paper%20dataset%20analysis/03-dashboard/img/preference.png">
    <figcaption>sample groups preferences<figcaption>
<figure>

---

# **AI Powered Music Learning Platform for Dyslexic Students.**
This Python application, "Music Learning for Dyslexia," is designed to help individuals with dyslexia learn music in a more accessible way. The app provides various features related to music transcription, generation, and visualization. This README provides an overview of the app's features and how to use them.

## Section Contents
| No. | Topic	                        							|
|-----|------------                       						|
| 01  | [Features](#Features)     									|
| 01  | [Pipeline](#pipeline)     						|
| 02  | [](#)     									|
| 03  | [](#)     								|

---

## Features
1. Visualizing Music Sheets in a Colorful Way
This feature allows you to upload an image of a music sheet, and the app will visualize it in a colorful way. It uses a clustering algorithm to represent the music sheet with different colors for improved accessibility.
![Image](https://github.com/rania-hossam/AI_Powered_APP/raw/main/videosofproject/ezgif.com-video-to-gif.gif)

https://github.com/rania-hossam/AI_Powered_APP/blob/main/videosofproject/gif2.gif
To use this feature:

Select "VISUALIZING MUSIC SHEETS IN A COLORFUL WAY" from the sidebar.
Upload an image of a music sheet.
Click the "Show Music Sheet Visualization" button to view the colorful music sheet.
2. Show Information About Music Notes
This feature is focused on transcribing audio files into MIDI format and extracting information about music notes from them.

To use this feature:

Select "SHOW INFORMATION ABOUT MUSIC NOTES" from the sidebar.
Upload an audio file in WAV, MP3, or OGG format.
The app will transcribe the audio to MIDI and display information about the music notes in a DataFrame.
![Image](https://github.com/rania-hossam/AI_Powered_APP/blob/main/videosofproject/gif2.gif)
![Image](https://github.com/rania-hossam/AI_Powered_APP/blob/main/videosofproject/gif3.gif)


3. Music Generation
The Music Generation feature allows you to generate music based on a text description. It uses the Meta Audiocraft library and the Music Gen Small model.

To use this feature:

Select "MUSIC GENERATION" from the sidebar.
Enter your music description in the text area.
Adjust the time duration using the slider.
The app will generate music based on your description and play it back for you to listen to.
4. Show Music Sheets from Your Audio
This feature is designed to generate music sheets from your audio files. It converts MIDI files to PNG images.
![Image](https://github.com/rania-hossam/AI_Powered_APP/blob/main/videosofproject/GIF5.gif)

To use this feature:

Select "SHOW MUSIC SHEETS FROM YOUR AUDIO" from the sidebar.
Click the "Generate Music Sheet" button to convert a specific MIDI file to a PNG image.
The generated music sheet will be displayed.
Installation and Setup
To set up and run this application, follow these steps:

Clone the repository to your local machine.
bash
Copy code
git clone <[repository_url](https://github.com/rania-hossam/AI_Powered_APP)>
Navigate to the project directory.
bash
Copy code
cd <project_directory>
Install the required Python packages using pip.
bash
Copy code
pip install -r requirements.txt
Ensure that you have the necessary external dependencies such as MuseScore installed for music sheet generation.

Run the application by executing the server.py script.

bash
Copy code
python server.py
Access the app in your web browser by opening the provided URL (usually http://localhost:8501).
Customization
You can customize the app's appearance, text, and functionality by modifying the Python code. The app uses Streamlit for the user interface, making it easy to adapt to your specific requirements.

Acknowledgments
This app makes use of various libraries and tools, including Streamlit, Meta Audiocraft, and MuseScore, to provide its features. Make sure to check their respective documentation for more information on how they work.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
This app was developed by [Rania Hossam].

Feel free to contribute to this project or contact the author for any questions or suggestions.
