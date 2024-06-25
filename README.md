# Django-API's
## SET UP
1. Create a Virtual Environment
    - `pip install virtualenv`
    - Acitvate it
2. Install Django `pip install django`
3. Create Your project folder `django-admin startproject ProjectName .` subsequent files are created directly in this folder
4. Create Your application folder `python manage.py startapp appname`
5. Create a Templates folder at the **root** level
6. Configure Your Settings.py file
    - Append Your Application name in INSTALLED_APPS list
    - Add Your templates folder name in TEMPLATES inside the list of **DIRS** key
7. If you have styles, images, assets files all these should be under Static folder which is in **root** level

## API's
The Application Consist of Three API's
1) An API with get method which takes a string name and displays a pop-up for greeting
    - Uses a sweeralert pop-up
    - Uses regex validator that matches for alphabets and space pattern. For invalid data error messages are shown besides the respective fields.
    - Uses Ajax for form submissions
2) An API with post method which takes name, age and salary and displays a pop-up containing these variables
    - Uses a sweetalert pop-up
    - Uses Regex, MaxValue, MinValue and Decimal Validators to validate data before submitting the form. For invalid data error messages are shown besides the respective fields.
    - Uses Ajax for form submissions
3) An API with post method that accesses a third-part API and displays the data in list format in HTML
   - To access this third party API you have to create an account [API Ninjas](https://api-ninjas.com/) Free Tier Available
   - To Integrate the API programming language specific codes are available
   - Embed your API Key in your code
   - An external library should be installed `pip install requests`
   - Since this application uses free tier account a list of one item is displayed but the code works to access multiple items
   - Uses Ajax for form submissions
