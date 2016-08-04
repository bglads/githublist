Django App to display the recent opened issues from a github repo

Enter the 'github-user-name/repository-name'

####Example:
To list open issues of *github.com/django/django* url enter 
>django/django

Json response from backend:

```json
[
   {
      "data":[ ... ],
      "length":0,
      "type":"day"
   },
   {
      "data":[ ...  ],
      "length":3,
      "type":"week"
   }
]
```


Hosted on https://githublist.herokuapp.com/
