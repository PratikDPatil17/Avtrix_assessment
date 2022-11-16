1. Start server and send request to access application - http://127.0.0.1:8000/ 

    1) We can perform CRUD through Django application as well 
        a. add order - http://127.0.0.1:8000/create/

        b. Details - http://127.0.0.1:8000/detail/1  = <pass pk>

        c. Update - http://127.0.0.1:8000/update/1

        d. Delete - http://127.0.0.1:8000/delete/1

2. To get orders details in API - 
    1) send request to - http://127.0.0.1:8000/api/

                         http://127.0.0.1:8000/api/results
        
        (we can perform CRUD on records through REST Api as well)

    2) Search based on product use search query - ?search=<Product name>

        http://127.0.0.1:8000/api/results/?search=Carrot
    