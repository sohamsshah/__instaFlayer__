# instaFlayer

A smart Instagram-Bot made in Python.


# Introduction to InstaFlayer

InstaFlayer is a fully-featured Instagram Bot which can perform various Instagram operations automatically. It is presently
made in two variants in order for better understanding to the users. The first version is made upon the *instabot* library, 
while the latter is completely developed  using *Selenium* web-scrapping tool.

### Features of __instaFlayer__v1

1. Can fetch random meme from Reddit 
2. Can fetch random image from Unsplash 
3. Can post random image from Reddit or Unsplash automatically
4. Can post random caption on the posted image scrapped from www.saganipsum.com
5. Resets Cache and counter in order to prevent errors while posting.

### Features of __instaFlayer__v2

1. Can comment on user's photos (random comments as hardcoded)
2. Can like user's photos
3. Can like and comment based on hashtags
4. Get any user's followers and perform likes/comments/follow accordingly on them
5. Can follow users


*Note*:

1. One of the most common error that persists for posting multiple images one after
the other, it shows "*ERROR - Photo Upload failed with the following response: <Response [403]> instagram bot*".
This error can be solved by resetting cache and counter file content saved when using it. Refer the code for it.
2. Instagram is strict about the automatically operated bots and has declared illegal. So while testing and running the code
on the profile, don't perform too many actions otherwise there are chances of the profile to be blocked. 

