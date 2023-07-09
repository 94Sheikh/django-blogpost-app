from datetime import date
from django.http import Http404
from django.shortcuts import render

# Create your views here.

posts = [

    {
        "slug": "mountain-hiking",
        "img": "mountains.jpg",
        "author": "Zulfiqar",
        "date": date(2023, 7, 9),
        "title": "Mountain Hiking",
        "excerpt": """Lorem ipsum dolor sit, amet consectetur adipisicing elit.
                    Libero vero odio id quisquam consequatur aut error, 
                    officiis repellendus incidunt assumenda.""",
        "content": """
                    Lorem ipsum dolor sit amet consectetur adipisicing elit.
                     Unde commodi consequatur magni repudiandae expedita ipsam quas sapiente tempore dolore,
                     molestias voluptates dolorem, recusandae maxime. Repellat optio ratione omnis nesciunt nostrum?

                     Lorem ipsum dolor sit amet consectetur adipisicing elit.
                     Unde commodi consequatur magni repudiandae expedita ipsam quas sapiente tempore dolore,
                     molestias voluptates dolorem, recusandae maxime. Repellat optio ratione omnis nesciunt nostrum?
                     
                     Lorem ipsum dolor sit amet consectetur adipisicing elit.
                     Unde commodi consequatur magni repudiandae expedita ipsam quas sapiente tempore dolore,
                     molestias voluptates dolorem, recusandae maxime. Repellat optio ratione omnis nesciunt nostrum?
                """
    },

     {
        "slug": "wood-importance",
        "img": "woods.jpg",
        "author": "Rehmat Zulfiqar",
        "date": date(2023, 5, 13),
        "title": "Woods Important",
        "excerpt": """Lorem ipsum dolor sit, amet consectetur adipisicing elit.
                    Libero vero odio id quisquam consequatur aut error, 
                    officiis repellendus incidunt assumenda.""",
        "content": """
                    Lorem ipsum dolor sit amet consectetur adipisicing elit.
                     Unde commodi consequatur magni repudiandae expedita ipsam quas sapiente tempore dolore,
                     molestias voluptates dolorem, recusandae maxime. Repellat optio ratione omnis nesciunt nostrum?

                     Lorem ipsum dolor sit amet consectetur adipisicing elit.
                     Unde commodi consequatur magni repudiandae expedita ipsam quas sapiente tempore dolore,
                     molestias voluptates dolorem, recusandae maxime. Repellat optio ratione omnis nesciunt nostrum?
                     
                     Lorem ipsum dolor sit amet consectetur adipisicing elit.
                     Unde commodi consequatur magni repudiandae expedita ipsam quas sapiente tempore dolore,
                     molestias voluptates dolorem, recusandae maxime. Repellat optio ratione omnis nesciunt nostrum?
                """
    },

     {
        "slug": "coding-manners",
        "img": "coding.jpg",
        "author": "Faiza Kanwel",
        "date": date(2023, 6, 11),
        "title": "Coding Atheks",
        "excerpt": """Lorem ipsum dolor sit, amet consectetur adipisicing elit.
                    Libero vero odio id quisquam consequatur aut error, 
                    officiis repellendus incidunt assumenda.""",
        "content": """
                    Lorem ipsum dolor sit amet consectetur adipisicing elit.
                     Unde commodi consequatur magni repudiandae expedita ipsam quas sapiente tempore dolore,
                     molestias voluptates dolorem, recusandae maxime. Repellat optio ratione omnis nesciunt nostrum?

                     Lorem ipsum dolor sit amet consectetur adipisicing elit.
                     Unde commodi consequatur magni repudiandae expedita ipsam quas sapiente tempore dolore,
                     molestias voluptates dolorem, recusandae maxime. Repellat optio ratione omnis nesciunt nostrum?
                     
                     Lorem ipsum dolor sit amet consectetur adipisicing elit.
                     Unde commodi consequatur magni repudiandae expedita ipsam quas sapiente tempore dolore,
                     molestias voluptates dolorem, recusandae maxime. Repellat optio ratione omnis nesciunt nostrum?
                """
    }
]

def get_date(post):
    return post['date']


def homepage(request):
    sorted_post = sorted(posts, key = get_date, reverse = True)
    latest_post = sorted_post[:3]
    context = {
        'posts' : latest_post
    }
    return render(request, "blogApp/home.html", context)


def allblogposts(request):
      context = {
           'posts' : posts
           }
      return render(request, "blogApp/all-posts.html", context )



def detailpost(request, slug):
    try:
        identified_post = next(post for post in posts if post['slug'] == slug)
        context = {
            'identified_post': identified_post
        }
        return render(request, "blogApp/detail-post.html", context)
    except StopIteration:
        raise Http404


# def detailpost(request, slug):
#     identified_post =next(post for post in posts if post['slug'] == slug)
#     context ={
#          'identified_post': identified_post
#     }
#     return render(request, "blogApp/detail-post.html", context)
