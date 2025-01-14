# Hemlock-Holm

## Details and Purpose
Hemlock Holm is an app that enables users to identify plants with a breeze: through the use of image and textual prompts. The name, which is a playful botanical take on Sherlock Holmes, is a reference to two plants; Hemlock and Holm Oak which literally and culturally signify Poison and death and strength and longevity respectively. This app will be developed with a vision to encourage botanical exploration and environmental awareness through a fun and engaging experience while also aiming to be educational and as a source of reference for students and plant enthusiasts.
### APIs
**<ins>Trefle</ins>**\
The project will be built upon a stack of APIs, with the primary API being Trefle. 
[Trefle API](https://docs.trefle.io/docs/guides/getting-started) is a global plants API that provides a free and open-sourced botanical database with information about a million plant species. It is an extremely useful resource which would help in training machine learning (ML) models to identify plants accurately via computer vision (CV). It would also enable users to pinpoint a specific plants with the help of textual cues and filters such as specifying physical details or genera. More information on this can be found on my [API Proposal](https://drive.google.com/file/d/1OAPkShvCQggll5b40C4tMEdGX73-9lLI/view?usp=sharing) documentation.

**<ins>Cloud Vision</ins>**\
In order for the app to be able to use computer vision to identify plants, it would need the appropriate facilities which Trefle may not be able to provide. Google’s [Cloud Vision API](https://cloud.google.com/vision/docs) allows developers to easily integrate vision detection features within applications, including image labeling, face and landmark detection, optical character recognition (OCR), and tagging of explicit content. This would enable the app to use its features to identify the right species by observing the details of the plant image and cross referencing with the Trefle database to match and spit accurate results.

**<ins>OpenAI</ins>**\
The app will also feature an interactive LLM (Large Language Model) chatbot to assist in answering questions. This feature will be undertaken by implementing [OpenAI API](https://platform.openai.com/docs/api-reference/introduction) which provides one of the best LLM in today’s world and is also easily integrable into the application.

## App Functions and Features

Hemlock Holm is set to provide a range of novel features in order to tackle common issues faced in plant identification. These features are as follows:
- Primarily, it will enable users to capture an image of the plant in question and will return the name, species, genera, etc. of the most closely matched plants by cross referencing the image scanned by Cloud Vision with Trefle’s extensive database.
- In case the user wishes to identify a plant which may not be in view, the app would offer the option to set filters or textual prompts to help identify it. For instance, “List all plants that are under 5 inches tall and grow in the tropics” OR “List all countries having less than 10 species of plants”.
- If the user requires a summarized answer to a broad topic or an explanation to a complex question, he/she would have the option to pose the question to the in-built chatbot (which uses OpenAI API) which will return a clear appropriate response to the query. On command, it will even clarify all botanical jargon to ensure clarity and user understandability.
- Finally, taking into account the importance of raising awareness of the environment and generating interest in plant life, the app would be gamified to enhance the experience by including achievements and badges every time a new plant is scanned. This feature may be developed further in the future to introduce point scoring mechanisms which could be renewed to win gifts from app sponsors. However this would be added only on an ad hoc basis.

## Additional Project Information

This project is part of a feasibility study on the aforementioned API (i.e Trefle) and is carried out as part of the Undergraduate Research Volunteering (URV) Winter 2024 program at the University of Massachusetts Amherst. 
This project is currently owned and managed by [@Fardeen0-0](https://github.com/Fardeen0-0) (yours truly) and is open to ideas and collaboration.

