## **My email recruitment process: paliwodam.s.m@gmail.com**

Web api providing login, name, bio summary of languages used in all public repositories with number of bytes written in corresponding language for github users.


## How to run the application?
1. First clone this project on your computer.

    ```
    $ git clone https://github.com/paliwodam/allegro-summer-experience-2022.git
    ```
1. Go to the location of the cloned project.

    ```
    $ cd allegro-summer-experience-2022
    ```
1. Install all required libraries from a file "requirements.txt".

    ```
    $ pip install -r requirements.txt
    ```

1. _(Optional)_ If you want to increase github rate limit:

    1. Create [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token). (without any additional scope).
    
    1. Copy `.env.example` to `.env`.

        ```
        $ cp .env.example .env
        ```

        or if you are on Windows

        ```
        $ copy .env.example .env
        ```
    
    1. Set your username as `GITHUB_USER_NAME` and token as `GITHUB_ACCESS_TOKEN`.


1. Run the development server.

    ```
    $ python3 scripts/run_development_server.py
    ```
    or if you are on Windows
    ```
    $ python scripts/run_development_server.py
    ```

## Available endpoints

### `GET /api/user/<username>/info`

Will return: 

  * login
  * name
  * bio
  * summary of languages used in all public repositories with number of bytes written in corresponding language

Sample response:

```json
{
  "bio": "Student of Computer Science at AGH University of Science and Technology", 
  "languages": {
    "CSS": 824, 
    "HTML": 6500, 
    "Java": 83904, 
    "JavaScript": 2911, 
    "Jupyter Notebook": 20993, 
    "Python": 82380
  }, 
  "login": "paliwodam", 
  "name": "Martyna Paliwoda"
}
```


### `GET /api/user/<username>/repositories`

Will return: 

  * list of repositories with summary of used languages with number of bytes written in each language


Sample response:

```json
[
  {
    "languages": {
      "Python": 68743
    }, 
    "name": "Algorithms-and-Data-Structures"
  }, 
  {
    "languages": {
      "HTML": 581, 
      "Java": 65936, 
      "JavaScript": 602
    }, 
    "name": "Bomberman"
  }, 
  {
    "languages": {
      "CSS": 824, 
      "HTML": 5919, 
      "JavaScript": 2309
    }, 
    "name": "code-lab-demo"
  }, 
  {
    "languages": {
      "Jupyter Notebook": 20993, 
      "Python": 1862
    }, 
    "name": "DifferentialEquations"
  }, 
  {
    "languages": {
      "Python": 10384
    }, 
    "name": "DoublePushout"
  }, 
  {
    "languages": {
      "Python": 1391
    }, 
    "name": "Studia-2.0"
  }, 
  {
    "languages": {
      "Java": 17968
    }, 
    "name": "VirtusLab"
  }
]
```



## How to run tests?
1. Go to the location of the cloned project.

    ```
    $ cd allegro-summer-experience-2022
    ```
1. Install all required libraries from a file "requirements-tests.txt".

    ```
    $ pip install -r requirements.txt
    ```

1. Run tests with command:

    ```
    $ python -m pytest
    ```
