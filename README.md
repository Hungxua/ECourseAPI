# ECourseAPI
category API:

    show list categories
    method:GET
    /categories/

courseAPI:

    show list courses
    method: GET
    /courses/
    
    get lessons in course with keyword
    method: GET
    /courses/{pk}/lessons/?kw=

lessonAPI:

      add tags to lesson
      method: POST
      /lessons/{pk}/tags/
      
      add comment to lesson
      method: POST
      /lessons/{pk}/add-comment/
      
      like lesson
      method: POST
      /lessons/{pk}/like/
      
      rate lesson
      method: POST
      /lessons/{pk}/rate/
      
      increase view for lesson
      method: GET
      /lessons/{pk}/views/
      
userAPI:

    get current user
    method: GET
    /users/current-user/
    

commentAPI:

    delete comment
    method: DELETE
    /comments/{pk}/
    
    update comment
    method: PATCH
    /comments/{pk}/
    
      
