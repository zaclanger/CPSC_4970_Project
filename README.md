# Final Project - CPSC 4970: Python

### Background

When I saw that one of our options for our final project was creating a Django app, I jumped at the opportunity. The truth is, I've been wanting to start learning Django for a while to try my hand at implementing a few ideas I have kicking around -- and just because Python is a fun language to develop in. In some ways, this project is the first step towards one of those ideas.

Before I made the leap into the world of IT, I worked in ministry at a small church for five years. There are many challenges that come with that sort of work, but one of the things I'd never considered is how much of a challenge is presented by the lack of technologies, resources, and applications targeted directly towards those sorts of churches. We had about 100 people, with the average age being about 70 (at the youngest), and even the younger people didn't have the time or background to do things like manage a website or membership database, which meant those tasks fell to me. 

It turns out, there *are* options out there ... almost all of which are inaccessibly expensive for a church on a limited budget. They're sleek and powerful, and they feel very much like something a modern, with-the-times sort of church would use, but the cost was a burden that proved untenable. Beyond that, they were packed full of features that would be great for a church with thousands of attendees, but not for our little one with attendance in the double digits. As I realized there weren't any options out there to do what I had in mind, I started imagining what something like this would look like.

This project is not what I had in mind. This project is a tiny step in the direction of what I imagined, which has a congregational database as one of the core elements. Knowing that I may someday like to try my hand at creating the real thing, this seemed like a great opportunity to dip my toes in the water of Django and see whether it may be a good framework to continue learning.

(The answer is yes, by the way. I really enjoyed this project!)

### The Project

Organization Manager is a very basic CRUD app with three levels: Person, Household, and Organization. A person can belong to a household, and a household can belong to organizations.

There are base lists of each level accessible through the NavBar at the top of the screen that show all entities of each type. From those pages you can add a new entity, delete an existing entity, or go to a page where you can edit an individual entity. There is also a search bar at the top of the screen where you can limit the visible rows based on their parent: you can limit person results to a certain household, and household results to a certain organization.

Though the most basic functionality is there, there are some issues that still persist:
1. The table overflows the right boundary of its container on most pages.
2. On pages where you're editing individual entities that hold lists of others (e.g. the members field of Household), the selection box is ugly.
3. The new entry form for households and organizations is *very* ugly.

With that said, as a simple project and starting point for future projects, I'm satisfied with how this came together. I'm also impressed by how *easily* (relatively) it was to create!

### Behind the scenes

I made use of a few additional libraries for this project, all of which can be found listed in the requirements.txt file. They can simply be installed with the following command in the top-level FinalProject directory:

    pip install -r requirements.txt

These libraries include Bootstrap5 and Crispy-Forms, because this is not a web development class and I didn't want to spend a huge amount of time tweaking formatting. The other libraries are included with Django.