# **ResUpgrade - _ATS Resume Checker_**

ResUpgrade is an innovative **ATS (Applicant Tracking System) Resume Checker application** designed to help job seekers optimize their resumes for specific job descriptions. 


## **Overview**

This project aims to help students and employees review and improve their resume by utilizing the advanced capabilities of Google Deepmind's Gemini Pro model. ResUpgrade offers a user-friendly interface to compare a resume against a job description, providing valuable feedback on match percentage, missing keywords, profile summary and also provides suggestions to improve the resume.


## **Features**

- **Job Description Analysis**: Users can input a specific job title and description.
- **Resume Upload**: The app supports PDF format resume uploads for analysis.
- **Gemini Pro Integration**: Leverages Google's advanced AI model for accurate and detailed resume evaluation.
- **Feedback and Improvement Suggestions**: Provides detailed feedback including job description match percentage, missing keywords, and a profile summary.


## **Technologies Used**

**Primary Langauge** - Python

- **Streamlit**: An open-source app framework used for building the front-end of the application.
- **Gemini Pro API**: A state-of-the-art AI model used for generating content and analyzing resumes.
- **PyPDF2**: A Python library used for handling PDF file operations like reading and extracting text.
- **python-dotenv**: A Python package used for managing environment variables.


## **How it Works**

1. **Input Job Description**: You have to type the job description into the provided text area.
2. **Upload Resume**: You have to upload your resume file. ( `.pdf` file only )
3. **Analysis**: Upon clicking "`Submit`", the app analyses the resume in comparison with the job description.
4. **Feedback**: The app displays the match percentage, missing keywords, profile summary and suggestions to improve the resume.


## **Installation**

1. **Clone the repository:**

 `git clone` [https://github.com/argishh/ResUpgrade-ATS-Resume-Checker.git](https://github.com/argishh/ResUpgrade-ATS-Resume-Checker.git)

2. **Install the required libraries:**

`pip install -r requirements.txt`

3. **Set up a `.env` file with your Google API key:**

`GOOGLE_API_KEY = "Your-API-Key"`

4. **Run the Streamlit app:**

run the `run.bat` file 

_or_

type the following command in cmd terminal -

`streamlit run app.py`

## **Usage**

- `Run` the application and navigate to the provided `local URL`.
- Follow the on-screen instructions to input the job description and upload your resume.
- Click "`Submit`" to receive your personalized resume feedback.

## **Contributions**

We actively welcome your contributions! If you would like to improve the app or suggest features, please feel free to fork the repository and submit a pull request.

Follow these steps to contribute to the project:

1. Fork the repository on GitHub.
2. Create a new branch from the `main` branch.
3. Make your modifications and enhancements.
4. Test your changes, then `commit` and `push` your changes to your forked repository.
5. Submit a `pull request` to the `main` repository, describing your changes in detail.

_Please ensure your contributions adhere to the project's coding standards and guidelines._


## **Acknowledgements**

Special thanks to:
- Google Deepmind for providing the Gemini Pro AI model.
- Streamlit for their intuitive app framework, making this application possible.
- The open-source community for their ongoing support and contributions. <br>
  _p.s. I had hard time solving a particular issue in streamlit that finally got resolved after installing an older version, as mentioned in the requriements.txt file. **Big Thanks** to the community for actively helping out others!_

## **License**

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## **Contact**

For queries, suggestions, or collaborations, please contact the project maintainer at [argish.work@gmail.com](mailto:argish.work@gmail.com)

---
