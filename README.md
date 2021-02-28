# Apply2Masters
## Read Me

Fillout form here: https://www.figma.com/proto/EJwZEklHKzWmhVfnhnZygf/Landing-Page?node-id=603%3A8&scaling=min-zoom

After the user fills out the typeform on our frontend, our backend checks their preferences against a list of universities and generates a university list that they are eligible for and they prefer. This is stored is `Results.csv`. Afterwards, this file is used to generate a pdf that is emailed to the user with more details about the university of their choice.

# Example
For user who answered the following questions on our website,

In which country are you a citizen? USA<br>
Will you have a bachelor's degree by the time you start the program? YES<br>
What’s your highest degree earned? BACHELOR'S<br>
In what language did you earn your highest degree? ENGLISH<br>
Have you taken the GMAT exam? YES<br>
What score did you receive? 600<br>
What GPA did you graduate with? 3.2<br>
How many years of full-time work experience do you have? 1-3<br>
What subjects are you interested in studying? MANAGEMENT<br>
Which countries would you most like to study in? ITALY (ONLY)<br>
What is the ideal city size you would like to study in? 1-2 MM<br>
How much can you afford to pay for tuition? $20,000<br>

A report is generated, which we e-mail to the user. This report is called `report.pdf` and is present in this repository
